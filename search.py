# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    node = (problem.getStartState(), []) #node is a node with state = problem.initial state space, and an empty list for the path.
    if (problem.isGoalState(node[0])): #If we start on a goal state, there is no need to move
        return []
    
    frontier = util.Stack()#Frontier is a LIFO Queue
    frontier.push(node)#With the node as the only element
    explored = []#Explored is an empty set
    expanded = []#Expanded is an empty set that will contain everything we have expanded.

    while (not problem.isGoalState(node[0])):#While we are not at a goal state
        if (frontier.isEmpty()):#If the frontier is empty, return failure.
            return []
        node = frontier.pop()#Node = pop frontier
        explored.append(node[0]) #Add node.state to explored
        if (problem.isGoalState(node[0])):#If we are at a goal state
            return node[1]#Return the path to that goal state
        if (node[0] not in expanded):#If we have not expanded the current node before
            expanded.append(node[0])#Add the current node to our list of expansions
            for child in problem.getSuccessors(node[0]):#For each child of our current node
                if child[0] not in explored: #If child.state is not in explored or frontier
                    newNode = (child[0], node[1] + [child[1]])#Our new node is equal to the child node and the added cost of actions from our previous node and this node.
                    frontier.push(newNode)#Add into our frontier the new node.

    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    node = (problem.getStartState(), []) #node is a node with state = problem.initial state space, and an empty list for the path.
    if (problem.isGoalState(node[0])): #If we start on a goal state, there is no need to move
        return []
    
    frontier = util.Queue()#Frontier is a FIFO Queue
    frontier.push(node)#With the node as the only element
    explored = []#Explored is an empty set
    expanded = []#Expanded is an empty set that will contain everything we have expanded.
   
    while (not problem.isGoalState(node[0])):#While we are not at a goal state
        if (frontier.isEmpty()):#If the frontier is empty, return failure.
            return []
        node = frontier.pop()#Node = pop frontier
        explored.append(node[0]) #Add node.state to explored
        if (problem.isGoalState(node[0])):#If we are at a goal state
            return node[1]#Return the path to that goal state

        if (node[0] not in expanded):#If we have not expanded the current node before
            expanded.append(node[0])#Add the current node to our list of expansions
            for child in problem.getSuccessors(node[0]):#For each child of our current node (CALLING GETSUCCESSORS COUNTS AS EXPANSION)
                if child[0] not in explored: #If child.state is not in explored or frontier
                    newNode = (child[0], node[1] + [child[1]])#Our new node is equal to the child node and the added cost of actions from our previous node and this node.
                    frontier.push(newNode)#Add into our frontier the new node.
            
    return node[1]

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    node = (problem.getStartState(), []) #node is a node with state = problem.initial state space, and an empty list for the path.
    if (problem.isGoalState(node[0])): #If we start on a goal state, there is no need to move
        return []
    
    frontier = util.PriorityQueue()#Frontier is a FIFO Queue
    frontier.push(node, problem.getCostOfActions(node[1]))#With the node as the only element
    explored = []#Explored is an empty set
    expanded = []#Expanded is an empty set that will contain everything we have expanded.

    while (not problem.isGoalState(node[0])):#While we are not at a goal state
        if (frontier.isEmpty()):#If the frontier is empty, return failure.
            return []
        node = frontier.pop()#Node = pop frontier
        explored.append(node[0]) #Add node.state to explored
        if (problem.isGoalState(node[0])):#If we are at a goal state
            return node[1]#Return the path to that goal state

        if (node[0] not in expanded):#If we have not expanded the current node before
            expanded.append(node[0])#Add the current node to our list of expansions
            for child in problem.getSuccessors(node[0]):#For each child of our current node
                if child[0] not in explored: #If child.state is not in explored or frontier
                    newNode = (child[0], node[1] + [child[1]])#Our new node is equal to the child node and the added cost of actions from our previous node and this node.
                    frontier.push(newNode, problem.getCostOfActions(newNode[1]))#Add into our frontier the new node.
                elif child[0] in frontier.heap:#Else if child.state is in frontier (with higher path cost does not matter, our priority queue handles this automatically and allows us to push multiple copies of the same thing with different priority values)
                    newNode = (child[0], node[1] + [child[1]])
                    frontier.push(newNode, problem.getCostOfActions(newNode[1]))#Again, we do not need to replace - our queue handles this for us, we only need to push the node and its cost.

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    node = (problem.getStartState(), []) #node is a node with state = problem.initial state space, and an empty list for the path.
    if (problem.isGoalState(node[0])): #If we start on a goal state, there is no need to move
        return []
    
    frontier = util.PriorityQueue()#Frontier is a FIFO Queue
    frontier.push(node, heuristic(node[0], problem))#With the node as the only element
    explored = []#Explored is an empty set
    expanded = []#Expanded is an empty set that will contain everything we have expanded.

    while (not problem.isGoalState(node[0])):#While we are not at a goal state
        if (frontier.isEmpty()):#If the frontier is empty, return failure.
            return []
        node = frontier.pop()#Node = pop frontier
        explored.append(node[0]) #Add node.state to explored
        if (problem.isGoalState(node[0])):#If we are at a goal state
            return node[1]#Return the path to that goal state

        if (node[0] not in expanded):#If we have not expanded the current node before
            expanded.append(node[0])#Add the current node to our list of expansions
            for child in problem.getSuccessors(node[0]):#For each child of our current node
                if child[0] not in explored: #If child.state is not in explored or frontier
                    newNode = (child[0], node[1] + [child[1]])#Our new node is equal to the child node and the added cost of actions from our previous node and this node.
                    frontier.push(newNode, problem.getCostOfActions(newNode[1]) + heuristic(child[0], problem))#Add into our frontier the new node.
                elif child[0] in frontier.heap:#Else if child.state is in frontier (with higher path cost does not matter, our priority queue handles this automatically and allows us to push multiple copies of the same thing with different priority values)
                    newNode = (child[0], node[1] + [child[1]])
                    frontier.push(newNode, problem.getCostOfActions(newNode[1] + heuristic(child[0], problem)))#Again, we do not need to replace - our queue handles this for us, we only need to push the node and its cost.
                
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
