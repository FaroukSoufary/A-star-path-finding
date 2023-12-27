import numpy as np
import pygame


# This file contains an implementation of the A* (A-star) algorithm for path-finding applied on a cursor chaser made with PyGame


class Node():
    def __init__(self, x, y, obstacle = False, parent = None):
        self.x = x 
        self.y = y 
        self.parent = parent
        
        self.h = 0
        self.g = 0
        self.f = 0
        self.obstacle = obstacle
        
        
class Grid():
    def __init__(self, height, width, start_pos):
        self.Height = height
        self.Width = width
        self.Grid = []
        self.start_pos = start_pos
        
        
    def fill_grid(self, digits_maze):
        for i in range(self.Height):
            Row = []
            for j in range(self.Width):
                Row.append(Node(i, j, obstacle=(digits_maze[i][j]==1)))
            self.Grid.append(Row)
        self.Grid = np.array(self.Grid)
        
        
def get_best_open(open_list):
    min_f = open_list[0].f
    best_idx = 0
    for i, node in enumerate(open_list):
        if node.f < min_f:
            min_f = node.f
            best_idx = i
    return open_list[best_idx]    


def heuristic(s, target):
    return (s.x - target.x)**2 + (s.y - target.y)**2


def node_in(node, list):
    for s in list:
        if(s.x == node.x and s.y == node.y):
            return True 
    return False

def get_quivalent(node, list):
    for s in list:
        if(s.x == node.x and s.y == node.y):
            return s
    return None

def get_successors(grid, current_node):  
    H = grid.Height 
    W = grid.Width 
    successors = []
    c_x, c_y = current_node.x, current_node.y
    
    if(c_x + 1 < H and grid.Grid[c_x+1, c_y].obstacle==False):
        successors.append(Node(c_x+1, c_y))
        
    if(c_x - 1 >= 0 and grid.Grid[c_x-1, c_y].obstacle==False):
        successors.append(Node(c_x-1, c_y))

    if(c_y + 1 < W and grid.Grid[c_x, c_y+1].obstacle==False):
        successors.append(Node(c_x, c_y+1))
        
    if(c_y - 1 >= 0 and grid.Grid[c_x, c_y-1].obstacle==False):
        successors.append(Node(c_x, c_y-1))
        
    return successors
    
def A_star(grid, target_pos):
    
    start_pos = grid.start_pos
    
    if(grid.Grid[target_pos[0]][target_pos[1]].obstacle==True):
        return []
        
    start = grid.Grid[start_pos[0], start_pos[1]]
    target = grid.Grid[target_pos[0], target_pos[1]]
    
    Visited = []
    Open = [start]
    
    while len(Open) > 0:
        current_node = get_best_open(Open)
        Visited.append(current_node)
        Open.remove(current_node)
        
        successors = []
        
        if (current_node.x == target.x and current_node.y == target.y):
            # print("Reached Target !")
            break
        
        successors = get_successors(grid, current_node)
            
        for s in successors:
            s.parent = current_node
            s.g = current_node.g + 1
            s.h = heuristic(s, target)
            s.f = s.g * 0.9 + s.h * 0.1
            
            if node_in(s, Visited):
                continue
            
            elif not node_in(s, Open):
                Open.append(s)
            
            else:
                equivalent = get_quivalent(s, Open)
                if(equivalent.g > s.g):
                    s.parent = current_node
                    s.g = current_node.g + 1
                    s.f = s.g * 0.9 + s.h * 0.1
                    Open.remove(equivalent)
                    Open.append(s)
                    
    path = []
    current = current_node
    while current is not None:
        path.append((current.x, current.y))
        current = current.parent
        
    return path[::-1] 
        

        
maze = [[0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1]]

maze2 =[[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

maze2 =[[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]





pygame.init()
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Pathfinding")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


grid_object = Grid(10, 10)
grid_object.fill_grid(maze)

start_position = (0, 0)
end_position = (6, 7)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    for i in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (i, 0), (i, HEIGHT))
    for j in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, BLACK, (0, j), (WIDTH, j))
        
        
    pygame.draw.circle(screen, RED, (start_position[0] * GRID_SIZE + GRID_SIZE//2, start_position[1] * GRID_SIZE + GRID_SIZE//2), 5)

    pygame.display.flip()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    end_position = (mouse_x // GRID_SIZE, mouse_y // GRID_SIZE)

    path = A_star(grid_object, start_position, end_position)
    
    screen.fill(WHITE)
    

    for row in grid_object.Grid:
        for node in row:
            color = WHITE if not node.obstacle else BLACK
            pygame.draw.rect(screen, color, (node.x * GRID_SIZE, node.y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

    for x, y in path[1:]:
        pygame.draw.circle(screen, GREEN, (x * GRID_SIZE + GRID_SIZE // 2, y * GRID_SIZE + GRID_SIZE // 2), 5)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()


# By Farouk Soufary
# Computer Science Student specializing in Artificial Intelligence
# @ENSEIRB-MATMECA