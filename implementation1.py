N = int(input())
a = input().split()
x,y = 1,1

dx = [0,-1,1,0]
dy = [-1,0,0,1]
mode = ['L','U','D','R']

for tool in a: #5
    for i in range(len(mode)): #4
        if(tool == mode[i]):
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    x = nx
    y = ny
print(x,y)
