# 인접 리스트로 구현

# dfs 함수 정의
def dfs(v):
    print(v, end= ' ')
    # 현재 노드 방문 처리
    visited[v] = 1
    # 현재 노드와 연결된 다른 노드를 재귀 함수 호출
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


# N = 정점의 개수, M = 간선의 개수, v = 정점의 번호
N, M, V = map(int, input().split())

# graph 초기화
graph = []

# 노드가 연결된 경로를 리스트 자료형으로 입력
for i in range(N):
    graph.append(sorted(list(map(int, input().split()))))
# graph[0]을 공백으로 입력
graph.insert(0, [])

# 노드 방문 정보를 리스트 자료형으로 표현
visited = [0] * (N + 1)

# dfs 호출
dfs(V)

