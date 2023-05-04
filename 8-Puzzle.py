from datetime import datetime
import pygame
import time

pygame.init()
screen = pygame.display.set_mode((450, 600))
background = pygame.Surface((450, 450))
menu_font = pygame.font.SysFont("Calibri", 35)
img0 = pygame.image.load("0_.png")
img1 = pygame.image.load("1_.png")
img2 = pygame.image.load("2_.png")
img3 = pygame.image.load("3_.png")
img4 = pygame.image.load("4_.png")
img5 = pygame.image.load("5_.png")
img6 = pygame.image.load("6_.png")
img7 = pygame.image.load("7_.png")
img8 = pygame.image.load("8_.png")

list_ = []
class Node:
    node_counter = 0
    node_list = {"0"}
    def __init__(self, matrix, parent, lvl, goal):
        self.answer_list = []
        self.matrix = matrix
        self.lvl = lvl
        if lvl != 0:
            self.parent = parent
        self.child = []
        self.goal = goal
        Node.node_counter += 1
        Node.node_list.add(str(matrix))
    def show_route(self):
        lv = self.lvl
        result = [""]*lv

        result[0] = self
        for i in range(1, lv):
            result[i] = result[i-1].parent
        result.reverse()
        for i in result:
            i.print_node()
        return result
    def move_list(self):
        result = []
        for i in self.matrix:
            result.append(i.copy())
        return result
    def print_node(self):
        # list = []
        # for i in self.matrix:
        #     list.append(i)
        list_.append(self.matrix)
    def comparison(self):
        return self.matrix == self.goal
    def expansion(self):
        pos = {}
        for y in range(3):
            for x in range(3):
                if self.matrix[y][x] == 0:
                    pos = {"x": x, "y": y}
        if pos["x"] == 0:
            temp = self.move_list()     #matrix
            temp[pos["y"]][pos["x"]] = self.matrix[pos["y"]][pos["x"] + 1]
            temp[pos["y"]][pos["x"] + 1] = 0
            if str(temp) not in Node.node_list:
                self.child.append(Node(temp, self, self.lvl+1, self.goal))
        elif pos["x"] == 2:
            temp = self.move_list()
            temp[pos["y"]][pos["x"]] = self.matrix[pos["y"]][pos["x"] - 1]
            temp[pos["y"]][pos["x"] - 1] = 0
            if str(temp) not in Node.node_list:
                self.child.append(Node(temp, self, self.lvl+1, self.goal))
        else:
            temp = self.move_list()
            temp[pos["y"]][pos["x"]] = self.matrix[pos["y"]][pos["x"] + 1]
            temp[pos["y"]][pos["x"] + 1] = 0
            if str(temp) not in Node.node_list:
                self.child.append(Node(temp, self, self.lvl+1, self.goal))
            temp = self.move_list()
            temp[pos["y"]][pos["x"]] = self.matrix[pos["y"]][pos["x"] - 1]
            temp[pos["y"]][pos["x"] - 1] = 0
            if str(temp) not in Node.node_list:
                self.child.append(Node(temp, self, self.lvl+1, self.goal))
        if pos["y"] == 0:
            temp = self.move_list()
            temp[pos["y"]][pos["x"]] = self.matrix[pos["y"]+1][pos["x"]]
            temp[pos["y"]+1][pos["x"]] = 0
            if str(temp) not in Node.node_list:
                self.child.append(Node(temp, self, self.lvl+1, self.goal))
        elif pos["y"] == 2:
            temp = self.move_list()
            temp[pos["y"]][pos["x"]] = self.matrix[pos["y"]-1][pos["x"]]
            temp[pos["y"]-1][pos["x"]] = 0
            if str(temp) not in Node.node_list:
                self.child.append(Node(temp, self, self.lvl+1, self.goal))

        else:
            temp = self.move_list()
            temp[pos["y"]][pos["x"]] = self.matrix[pos["y"]+1][pos["x"]]
            temp[pos["y"]+1][pos["x"]] = 0
            if str(temp) not in Node.node_list:
                self.child.append(Node(temp, self, self.lvl+1, self.goal))
            temp = self.move_list()
            temp[pos["y"]][pos["x"]] = self.matrix[pos["y"]-1][pos["x"]]
            temp[pos["y"]-1][pos["x"]] = 0
            if str(temp) not in Node.node_list:
                self.child.append(Node(temp, self, self.lvl+1, self.goal))
class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.root = ''
        self.fringe = []
        self.finish = False
    def search(self, goal):
        self.root = Node(self.matrix, "", 0, goal)
        self.fringe.append(self.root)
        while not self.finish:
            flag = False
            for i in self.fringe:
                if i.comparison():
                    i.show_route()

                    print("nodes = ", Node.node_counter)
                    print("steps = ", i.lvl)

                    self.finish = True
                    flag = True
                    break
            if not flag:
                temp = []
                for i in self.fringe:
                    i.expansion()
                    temp = temp+i.child
                self.fringe.clear()
                self.fringe = temp.copy()
                temp.clear()

def timer_():
    time = datetime.now()
    real_time = time.minute*60 + time.second
    return real_time

def show_in_display(matrix):
    background.fill((200, 200, 200))
    for k in range(len(matrix)):
        for i in range(len(matrix[k])):
            for j in range(len(matrix[k][i])):
                if matrix[k][i][j] == 1:
                    background.blit(img1, (j*150, i*150))
                if matrix[k][i][j] == 2:
                    background.blit(img2, (j*150, i*150))
                if matrix[k][i][j] == 3:
                    background.blit(img3, (j*150, i*150))
                if matrix[k][i][j] == 4:
                    background.blit(img4, (j*150, i*150))
                if matrix[k][i][j] == 5:
                    background.blit(img5, (j*150, i*150))
                if matrix[k][i][j] == 6:
                    background.blit(img6, (j*150, i*150))
                if matrix[k][i][j] == 7:
                    background.blit(img7, (j*150, i*150))
                if matrix[k][i][j] == 8:
                    background.blit(img8, (j*150, i*150))
                if matrix[k][i][j] == 0:
                    background.blit(img0, (j*150, i*150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((100, 100, 100))
        screen.blit(background, (1, 1))

        # step_disp = menu_font.render(step_show, 1, (120, 0, 0))
        time_disp = menu_font.render(time_took, 1, (120, 0, 0))
        screen.blit(time_disp, (50, 470))
        # screen.blit(step_disp, (50, 500))

        pygame.display.update()
        time.sleep(.5)
    run = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((100, 100, 100))
        screen.blit(background, (1, 1))
        # step_disp = menu_font.render(step_show, 1, (120, 0, 0))
        time_disp = menu_font.render(time_took, 1, (120, 0, 0))
        # screen.blit(step_disp, (50, 500))
        screen.blit(time_disp, (50, 470))
        pygame.display.update()
    # pygame.quit()


exa = [[8, 7, 6],
      [5, 4, 3],
      [2, 1, 0]]

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]

time1 = timer_()
x = Graph(exa)
x.search(goal)
time2 = timer_()

print("took", time2-time1, "sec")
time_took = "took " + str(time2-time1) + " sec to solve"
# step_show = "number of steps: " + str(steps)
print(list_)
show_in_display(matrix=list_)
if run is False:
    pygame.quit()
