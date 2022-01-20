# Credits: Percy Liang & Dorsa Sadigh



import sys
import util
sys.setrecursionlimit(10000)

### Model (search problem)

class TransportationProblem(object):
    def __init__(self, N):
        # N = number of blocks
        self.N = N
    def startState(self): # start state
        return 1
    def isEnd(self, state): # goal test
        return state == self.N
    def succAndCost(self, state): # (s,a)
        # return list of (action, newState, cost) triples
        result = []
        if state+1<=self.N:
            result.append(('walk', state+1, 1))
        if state*2<=self.N:
            result.append(('tram', state*2, 2))
        return result

### Algorithms

# def printSolution(solution):
#     totalCost, history = solution
#     print('totalCost: {}'.format(totalCost))
#     for item in history:
#         print(item)

def backtrackingSearch(problem):
    # Best solution found so far (dictionary because of python scoping technicality)
    best = {
        'cost': float('+inf'),
        'history': None
    }
    def recurse(state, history, totalCost):
        # At state, having undergone history, accumulated
        # totalCost.
        # Explore the rest of the subtree under state.
        if problem.isEnd(state):
            # Update the best solution so far
            if totalCost<best['cost']:
                best['cost'] = totalCost
                best['history'] = history
                #print(totalCost, history)
            return
        # Recurse on children
        for action, newState, cost in problem.succAndCost(state):
            recurse(newState, history+[(action, newState, cost)], totalCost+cost)
    
    
    recurse(problem.startState(), history=[], totalCost=0) # initial state
    return (best['cost'], best['history'])


### Main

problem = TransportationProblem(N=6)
#print(problem.succAndCost(116))
#print(problem.succAndCost(9))
#printSolution(backtrackingSearch(problem))
backtrackingSearch(problem)

