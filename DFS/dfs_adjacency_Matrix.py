# 인접행렬로 구현
def dfs(v):
    print(v, end= ' ')
    # 방문 처리
    visited[v] = 1

    # 재귀 함수 호출
    for i in range(1, N + 1):
        if visited[i] == 0 and adj[v][i] == 1:
            dfs(i)


# N = 정점의 개수, M = 간선의 개수, v = 정점의 번호
N, M, V = map(int, input().split())

# 2차원 배열 초기화
adj = [[0] * (N + 1) for i in range(N + 1)]

# 노드 방문 정보를 리스트 자료형으로 표현
visited = [0 for j in range(N + 1)]

# 2차원 배열 입력
for i in range(M):
    x, y = map(int, input().split())
    adj[x][y] = 1
    adj[y][x] = 1

# 출력
dfs(V)
