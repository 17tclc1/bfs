# First In First Out
map = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G'],
    'D': ['H','I'],
    'E': ['J','K'],
    'F': ['L','M'],
    'G': ['N','O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': [],
}
def Breadth_First_Search(start, goal):
    frontier = [start]
    explored = set()
    print("Frontier: ")
    while(frontier):
        print(frontier)
        state = frontier.pop(0)
        if(state == goal):
            print("Found the goal")
            return True
        for neighbours in map[state]:
            if neighbours not in (frontier and explored):
                frontier.append(neighbours)
    return False
if __name__=="__main__": 
    Breadth_First_Search('A','M')