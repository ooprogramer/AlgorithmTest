# Chapter 4 실전문제3: 게임 개발
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
w, h = map(int, input().split())
row, col, direction = map(int, input().split())
map_arr = []
for _ in range(h):
    map_arr.append(list(input().split()))

map_visited = [[False]*w for _ in range(h)]
map_visited[row][col] = True
def turnLeft(d):
    if d == 0:
        return 3
    else:
        return d-1

now = [row, col]
turn_time = 0
cnt = 0
while True:
    for _ in range(4):
        direction = turnLeft(direction)
        moved = [now[0]+dx[direction], now[1]+dy[direction]]
        if map_arr[moved[0]][moved[1]] == '0' and map_visited[moved[0]][moved[1]] == False:
            now = moved
            map_visited[moved[0]][moved[1]] = True
            cnt += 1
            turn_time = 0
            break
        turn_time += 1
    if turn_time == 4:
        moved = [now[0]-dx[direction], now[1]-dy[direction]]
        if map_arr[moved[0]][moved[1]] == '1':
            break
        else:
            now = moved
        turn_time = 0

print(cnt)
    
