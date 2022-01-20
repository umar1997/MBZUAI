# Credits: Percy Liang & Dorsa Sadigh


import sys
import util
sys.setrecursionlimit(10000)

### Model (search problem)

class TransportationProblem(object):
    def __init__(self, N):
        # N = number of blocks
        self.N = N
    def startState(self):
        return 1
    def isEnd(self, state):
        return state == self.N
    def succAndCost(self, state):
        # return list of (action, newState, cost) triples
        result = []
        if state+1<=self.N:
            result.append(('walk', state+1, 1))
        if state*2<=self.N:
            result.append(('tram', state*2, 2))
        return result

### Algorithms

def printSolution(solution):
    totalCost, history = solution
    print('totalCost: {}'.format(totalCost))
    for item in history:
        print(item)

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
            return
        # Recurse on children
        for action, newState, cost in problem.succAndCost(state):
            recurse(newState, history+[(action, newState, cost)], totalCost+cost)
    recurse(problem.startState(), history=[], totalCost=0)
    return (best['cost'], best['history'])

def dynamicProgramming(problem):
    cache = {} # state -> futureCost(state)
    def futureCost(state):
        # Base case
        if problem.isEnd(state):
            return 0
        if state in cache: # Exponential savings Memoization
            return cache[state][0]
        
        # Actually doing work
        best_result = (float('inf'), None, None, None)

        for action, newState, cost in problem.succAndCost(state):
            fCost = cost + futureCost(newState)
            result = (fCost, action, newState, cost)
            best_result = min(best_result, result) # FutureCost(s) = min Actions(s) that are possible

        cache[state] = best_result    
        
        return best_result[0]

    state = problem.startState()
    totalCost = futureCost(state)

    history = []
    while not problem.isEnd(state):
        _, action, newState, cost = cache[state]
        history.append((action, newState, cost))
        state = newState

    return (totalCost, history)



    

def uniformCostSearch(problem):
    frontier = util.PriorityQueue()
    frontier.update(problem.startState(), 0)
    while True:
        # Move from frontier to explored
        state, pastCost = frontier.removeMin()
        if problem.isEnd(state):
            return (pastCost, [])
        # Push out on the frontier
        for action, newState, cost in problem.succAndCost(state):
            frontier.update(newState, pastCost+cost)

### Main

problem = TransportationProblem(N=10000)
# print(problem.succAndCost(3))
# print(problem.succAndCost(9))
#printSolution(backtrackingSearch(problem))
printSolution(dynamicProgramming(problem))
#printSolution(uniformCostSearch(problem))
