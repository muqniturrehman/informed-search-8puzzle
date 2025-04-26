import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []        # In this method, We use Heap Data structure
    
    def enqueue(self, priority, item):
        heapq.heappush(self.elements, (priority, item)) # [list of tuples] like this: [(priority, item),(),()]
    
    def dequeue(self):        
        return heapq.heappop(self.elements)[1]   # It will pop the element with low priority from heap
    
    def is_empty(self):
        return len(self.elements) == 0


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.g = parent.g + 1 if parent else 0  # Cost from start
        self.h = self.heuristic()  # Heuristic cost
        self.f = self.g + self.h  # Total cost

    def __lt__(self, other):
        return self.f < other.f  # A* sorts based on f(n)
    
    def heuristic(self):
        # Manhattan Distance Algorithm
        distance = 0
        goal_positions = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), ' ': (2, 2)
        }
        
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != ' ':  # Don't calculate for the empty space
                    goal_x, goal_y = goal_positions[value]
                    distance += abs(goal_x - i) + abs(goal_y - j)
        
        return distance
    
    def __str__(self):
        output = ""
        for row in self.state:
            output += ' '.join(str(x) if x != ' ' else ' ' for x in row) + "\n"
        return output
    
class PuzzleSolver:
    def __init__(self, start, goal):
        self.start = Node(start)
        self.goal = Node(goal)
    
    def find_space(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    return (i, j)
    
    def find_moves(self, pos):
        x, y = pos
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    
    def find_children(self, state):
        children = []
        space = self.find_space(state.state)
        moves = self.find_moves(space)
        for move in moves:
            if self.is_valid(move):
                child = self.play_move(state, move, space)
                children.append(child)
        return children

    def is_valid(self, move):
        x, y = move
        if (x < 0 or x > 2) or (y < 0 or y > 2):
            return False
        else:
            return True
    
    def play_move(self, state, move, space):
        n_state = [row[:] for row in state.state]  # Create a copy of the state (shallow copy)
        new_node = Node(n_state, state)  # Create a new node with the copied state
        x, y = move
        sx, sy = space
        # Swap the values of the empty space with the new tile
        new_node.state[x][y], new_node.state[sx][sy] = new_node.state[sx][sy], new_node.state[x][y]
        return new_node        
    
    def solve_puzzle(self):
        pq = PriorityQueue()
        pq.enqueue(self.start.h, self.start)
        explored = set()
        open_set = set()
        open_set.add(str(self.start.state))
        
        while not pq.is_empty():
            current_node = pq.dequeue()
            open_set.discard(str(current_node))
            # if goal state is reached:
            if current_node.state == self.goal.state:
                print("Goal Reached")
                self.print_solution(current_node)
                return
            explored.add(str(current_node.state))
            children = self.find_children(current_node)
            for child in children:
                child_g = child.g + 1 
                child_f = child_g + child.h
                if str(child.state) not in explored and str(child) not in open_set:
                    pq.enqueue(child.f, child)
                    open_set.add(str(child))
        print("No Solution Found")
        
    
    def print_solution(self, node):        
        solution_path = []
        current_node = node
        while current_node:
            solution_path.append(current_node)
            current_node = current_node.parent

        solution_path.reverse()      # Reverse the list to see/display from start to Goal
        # Print the solution:
        step = 0
        for node in solution_path:
            print(f"\nStep {step}:")
            print(node)
            step += 1


def main():
    start_state = [[4, 7, 8], 
                   [3, 6, 5], 
                   [1, 2, ' ']]
    goal_state = [[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, ' ']]
    ps = PuzzleSolver(start_state, goal_state)
    ps.solve_puzzle()


main()
