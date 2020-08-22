# graph 초기화
N = 3
graph = []

# 노드가 연결된 경로를 리스트 자료형으로 입력
for i in range(N):
    graph.append(sorted(list(map(int, input().split()))))

graph = sorted(graph, key= lambda x: x[0])
print(graph)
