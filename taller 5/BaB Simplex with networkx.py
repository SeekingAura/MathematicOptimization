# Branch And Bound
from scipy.optimize import linprog
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
# https://stackoverflow.com/questions/45873783/python-linprog-minimization-simplex-method

import networkx as nx
import matplotlib.pyplot as plt

import numpy as np

# https://networkx.github.io/documentation/stable/reference/drawing.html
# https://networkx.github.io/documentation/stable/reference/functions.html
# https://matplotlib.org/examples/color/named_colors.html
# H = nx.Graph(G)  # convert G to undirected graph
# PyGraphviz
# https://github.com/CristiFati/Prebuilt-Binaries/tree/master/Windows/PyGraphviz
# Graphviz 64 bit windows
# https://github.com/mahkoCosmo/GraphViz_x64/

def draw_graph_states(G, iteration):
	plt.figure(iteration)
	plt.title("BaBSimplex {}".format(iteration), fontsize=16)

	# set edge colors
	nx.set_edge_attributes(G, "black", "color")

	# pos with graphviz
	pos=nx.nx_agraph.pygraphviz_layout(G, prog='dot')

	edge_labels = nx.get_edge_attributes(G,'action')
	node_colors=nx.get_node_attributes(G,'color')
	edge_colors=nx.get_edge_attributes(G,'color')

	node_labels=nx.get_node_attributes(G,'label')

	nx.draw(G, pos, labels=node_labels, edge_color=edge_colors.values(), node_color=node_colors.values(),with_labels=True, font_weight='bold')

	#pos[0]=pos[0]+0.2
	nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, with_labels=True, font_weight='bold')

def printStep(stepName, varNames, res, decimals, width=50):
	print("Operation {}".format(stepName).center(width, "-"))
	print("Message {}".format(res.get("message")))
	print("Objective = {}".format(res.get('fun')))
	for varName, i in zip(varNames, res.x):
		print(varName, round(i, decimals))

def is_worst_objective(G, startNode, is_maximize):
	
	# Actions format is "xn|<=###" or "xn|>=###"
	currentNode=startNode

	# is worst if objhective function takes worst in depth 2
	for i in range(2):
		parentNode=G.nodes[currentNode]["parent"]

		if(parentNode is None):
			return False

		objectiveCurrent=G.nodes[currentNode]["objective"]
		objetiveParent=G.nodes[parentNode]["objective"]

		if(is_maximize):
			if(objectiveCurrent>=objetiveParent):
				return False
		else:
			if(objectiveCurrent<=objetiveParent):
				return False
		
		currentNode=parentNode

	# is worst
	return True

def get_actions(G, startNode, intVars):
	# Actions format is "xn|<=###" or "xn|>=###"
	actions={var:None for var in intVars}
	currentNode=startNode
	while True:
		parentNode=G.nodes[currentNode]["parent"]

		if(parentNode is None):
			break
		currentAction=G.edges[currentNode, parentNode]["action"]

		varAction, action=currentAction.split("|")
		
		# Put the last action var
		if(actions[varAction] is None):
			actions[varAction]=action
		currentNode=parentNode

	return actions



def BaBSimplex(c, A_ub, b_ub, A_eq, b_eq, intVars=["x1"], is_maximize=False, decimals=10):
	# number of variables from model
	numberVars=len(c)

	"""
	Create a list with a properly variables names (x1, x2, ... xn) n is 
	the value of numberVars
	"""
	varNames=["x"+str(x) for x in range(1, numberVars+1)]

	# Create a dict base for check integer vars
	intVarsBase={i:False for i in intVars}
	# set intVars in All int
	intVars=intVarsBase.copy()
	
	
	colorFailed="red"
	colorWorst="orange"
	colorPossibleSolution="yellow"
	colorUnsolved="blue"
	colorSolvedDecimal="gray"
	colorOptimalSolution="green"

	# List of bounds of all variables
	bounds=[(None, None)]*len(c)

	# Configure values for maximize or minize
	if(is_maximize):
		factor=-1# Factor for result for maximize with minimize process
		c *= -1 # negate the objective coefficients		
	else:
		factor=1

	# Create graph instance
	G=nx.Graph()

	# Get answers for root node
	res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
	
	# var control
	iteration=0
	
	if(not res.get("success")):
		print("can't found optimal answer from root state with message: {}".format(res.get("message")))
		printStep("{} phase root".format(iteration), varNames, res, decimals)

		G.add_nodes_from([[iteration, {"color":colorFailed, "objective":res.get("fun")*factor}]])
		return G


	G.add_nodes_from([[iteration, {"color":colorUnsolved, "parent":None, "objective":res.get("fun")*factor}]])
	printStep("{} phase root".format(iteration), varNames, res, decimals)
	draw_graph_states(G, iteration)
	iteration+=1
	
	
	
	while colorUnsolved in nx.get_node_attributes(G,'color').values():
		

		# Control for iterations, because graph change for each iteration (only add nodes)
		IterationsNodes=list(G.nodes())
		for nodeI in IterationsNodes:
			if(G.nodes[nodeI]["color"]==colorUnsolved):
				
			
				# Get actions for bound restrictions #### continuie here
				actions=get_actions(G, nodeI, intVars.keys())
				
				# Update bounds
				for varName in actions:
					if(actions.get(varName) is not None):
						# Separate xn from <= ### (xn|###)
						action=actions.get(varName)
						if(action[:2]==">="):
							# Bound index is var number -1
							bounds[int(varName[1:])-1]=(int(action[2:]), None)
						elif(action[:2]=="<="):
							bounds[int(varName[1:])-1]=(None, int(action[2:]))
					else:
						#if control is none
						bounds[int(varName[1:])-1]=(None, None)

				# Get solution with simplex
				res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)

				# Update extra actions in label node
				varInts=[i+":"+str(res.x[int(i[1:])-1]) for i in actions]
				G.nodes[nodeI]["label"]=(str(nodeI)+"\n"+str(varInts)[1:-1]+"\n"+"Objective"+str(round(res.get("fun")*factor, decimals))).replace("None", "").replace(",", "\n")

				if(not res.get("success")):
					printStep(nodeI, varNames, res, decimals)
					print("Optimal failed")
					
					G.nodes[nodeI]["color"]=colorFailed
					G.nodes[nodeI]["objective"]=round(res.get("fun")*factor, decimals)
					draw_graph_states(G, nodeI)
					continue

				# set intVars in All int
				intVars=intVarsBase.copy()

				# Check decimal vars in integer vars
				for varName, varResult in zip(varNames,res.x):
					if(varName in intVars):
						if(round(varResult, decimals).is_integer()):
							intVars[varName]=True

				
				# All vars are integers
				if(False in intVars.values()):
					#print("found optimal with integer values")
					#print("Objective = {}".format(res.get('fun')))
					printStep(nodeI, varNames, res, decimals)
					G.nodes[nodeI]["color"]=colorSolvedDecimal
					G.nodes[nodeI]["objective"]=res.get("fun")*factor
					
					#G.add_nodes_from([[iteration, {"color":colorUnsolved, "parent":nodeToSolve}]])
					#iteration+=1

					# Check if objetive worsts
					if(is_worst_objective(G,nodeI,is_maximize)):
						print("Worst objective")
						G.nodes[nodeI]["color"]=colorWorst
						G.nodes[nodeI]["objective"]=round(res.get("fun")*factor, decimals)
						draw_graph_states(G, nodeI)
						continue

					for varName in intVars:
						# Is not integer answer
						if(intVars.get(varName) is False):

							# Left part
							G.add_nodes_from([[iteration, {"color":colorUnsolved, "parent":nodeI}]])
							G.add_edges_from([[nodeI, iteration, {"action":varName+"|<="+str(int(res.x[int(varName[1:])-1]))}]])
							iteration+=1

							# Rigth Part
							G.add_nodes_from([[iteration, {"color":colorUnsolved, "parent":nodeI}]])
							G.add_edges_from([[nodeI, iteration, {"action":varName+"|>="+str(int(res.x[int(varName[1:])-1])+1)}]])
							iteration+=1
							draw_graph_states(G, nodeI)
							break
				else:
					printStep(nodeI, varNames, res, decimals)
					print("found with integer values")
					G.nodes[nodeI]["color"]=colorPossibleSolution
					G.nodes[nodeI]["objective"]=round(res.get("fun")*factor, decimals)
					draw_graph_states(G, nodeI)

					

	optimalValue=None
	for nodeI in G.nodes():
		if(G.nodes[nodeI]["color"]==colorPossibleSolution):
			if(optimalValue is None):
				optimalValue=G.nodes[nodeI]["objective"]
			else:
				if(is_maximize):
					if(G.nodes[nodeI]["objective"]>optimalValue):
						optimalValue=G.nodes[nodeI]["objective"]
				elif(not is_maximize):
					if(G.nodes[nodeI]["objective"]<optimalValue):
						optimalValue=G.nodes[nodeI]["objective"]

	
	for nodeI in G.nodes():
		if(G.nodes[nodeI]["color"]==colorPossibleSolution):
			if(G.nodes[nodeI]["objective"]==optimalValue):
				G.nodes[nodeI]["color"]=colorOptimalSolution
				break

	return G
			
			

		


	
		





	



if __name__ == "__main__":
	"""Min z=-16x1-14x2+3*480
	Ejemplo 1
	Minimize        z = 3x_1 + 2x_2

	Subject to:     x_1 - 2x_2 + x_3 = 5/2
					2x_1 + x_2 +x_4 = 3/2
					
					x_2 >=-1 # Restriction 1
					
					x_3 >=-3 # Restriction 2
					
					
					# integrality
					x_1, x_2, x_3, x_4 >= 0

					x_2 , x_3 son enteros

	with              
	"""

	# Restrictions part left of '<='
	A_ub = np.array(
		[
			# Restriction 1
			[0, -1, 0, 0], 
			
			# Restriction 2
			[0, 0, -1, 0],

			# inte

			[-1, 0, 0, 0], 
			
			[0, -1, 0, 0], 

			[0, 0, -1, 0], 

			[0, 0, 0, -1],

			# extra
			#[0, 0, 1, 0]
		]
	)

	# Resticctions part rigth of '<='
	b_ub = np.array(
		[3, 1, 0, 0, 0, 0]
	)

	A_eq = np.array(
		[
			# Restriction 1
			[1, -2, 1, 0], 

			[2, 1, 0, 1]
			
		]
	)

	b_eq = np.array(
		[5/2, 3/2]
	)

	# Multiplicators of objective function
	c = np.array(
		[3, 2, 0, 0]
	)

	# Indicates what vars are integer 
	intVars=["x1", "x3"]

	# is maximize process or not (minimize)
	is_maximize=False

	G=BaBSimplex(c, A_ub, b_ub, A_eq, b_eq, intVars, is_maximize, decimals=10)

	draw_graph_states(G, "Finished")
	
	plt.show()

	

