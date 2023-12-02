import copy
import pygame
import queue
from sys import exit
start = []
end = []    
rr = [0, 0, 1, -1]
cc = [1, -1, 0, 0]
arr = ['r', 'l', 'd', 'u']

pygame.init()
screen = pygame.display.set_mode((1200,750))
pygame.display.set_caption('8 puzzle')
clock =pygame.time.Clock()
k=0



start.append(list(map(int, input().split(' '))))
start.append(list(map(int, input().split(' '))))
start.append(list(map(int, input().split(' '))))
end.append(list(map(int, input().split(' '))))
end.append(list(map(int, input().split(' '))))
end.append(list(map(int, input().split(' '))))



num =pygame.font.Font(None,300)


background = pygame.image.load('img/back.png')
sound  = pygame.mixer.Sound('Effect/aa.mp3')
win  = pygame.mixer.Sound('Effect/tt.mp3')



g=[]
#g.append( num.render('',False,'Blue').convert())
g.append(  num.render('',False,'Blue').convert())
g.append(  pygame.image.load('img/a (1).png').convert_alpha())
g.append(  pygame.image.load('img/a (2).png').convert_alpha())
g.append(  pygame.image.load('img/a (3).png').convert_alpha())
g.append(  pygame.image.load('img/a (4).png').convert_alpha())
g.append(  pygame.image.load('img/a (5).png').convert_alpha())
g.append(  pygame.image.load('img/a (6).png').convert_alpha())
g.append(  pygame.image.load('img/a (7).png').convert_alpha())
g.append(  pygame.image.load('img/a (8).png').convert_alpha())
g.append(  pygame.image.load('img/a (9).png').convert_alpha())




visit = {}
q = queue.Queue()
visit[tuple(map(tuple, start))] = 5
q.put(start)
while not q.empty():
    state = q.get()
    if state == end:
        break
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                for k in range(4):
                    ii = rr[k] + i
                    jj = cc[k] + j
                    if 0 <= ii <= 2 and 0 <= jj <= 2:
                        new_state = copy.deepcopy(state)
                        new_state[i][j], new_state[ii][jj] = new_state[ii][jj], new_state[i][j]
                        new_state_tuple = tuple(map(tuple, new_state))
                        if new_state_tuple not in visit:
                            visit[new_state_tuple] = state
                            q.put(new_state)

ans = []
while end != start:
    if end == start:
        break
    ans.append(end)
    end = list(visit[tuple(map(tuple, end))])

ans.append(start)
ans.reverse()





for i in range(3):
    for j in range(3):
        if start[i][j]==0:
            start[i][j]=g[0]
        if start[i][j]==1:
            start[i][j]=g[1]
        if start[i][j]==2:
            start[i][j]=g[2]
        if start[i][j]==3:
            start[i][j]=g[3]
        if start[i][j]==4:
            start[i][j]=g[4]
        if start[i][j]==5:
            start[i][j]=g[5]
        if start[i][j]==6:
            start[i][j]=g[6]
        if start[i][j]==7:
            start[i][j]=g[7]
        if start[i][j]==8:
            start[i][j]=g[8]
            
delay=0
uuu=0
k=0
            
clocK = pygame.time.Clock()
while True:

    screen.blit(background,(0,0))

    if delay >10:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                exit()
        
        
        
        screen.blit(start[0][0], (30 + 285,0  + 120))
        screen.blit(start[0][1], (215 + 285, 0 + 120))
        screen.blit(start[0][2], (400 + 285, 0+ 120))

        screen.blit(start[1][0], (315, 185 + 120))
        screen.blit(start[1][1], (500, 185 + 120))
        screen.blit(start[1][2], (685, 185 + 120))

        screen.blit(start[2][0], (315, 369 + 120))
        screen.blit(start[2][1], (500, 369 + 120))
        screen.blit(start[2][2], (685, 369 + 120))

        pygame.display.update()
       # clock.tick(2)
        if k==len(ans):
          if uuu == 0:win.play()
          uuu=10
          k-=1
        else:
          sound.play()
        start = ans[k]
        for i in range(3):
            for j in range(3):
                if start[i][j]==0:
                    start[i][j]=g[0]
                if start[i][j]==1:
                    start[i][j]=g[1]
                if start[i][j]==2:
                    start[i][j]=g[2]
                if start[i][j]==3:
                    start[i][j]=g[3]
                if start[i][j]==4:
                    start[i][j]=g[4]
                if start[i][j]==5:
                    start[i][j]=g[5]
                if start[i][j]==6:
                    start[i][j]=g[6]
                if start[i][j]==7:
                    start[i][j]=g[7]
                if start[i][j]==8:
                    start[i][j]=g[8]
        k+=1
    delay+=1
    clocK.tick(2)
