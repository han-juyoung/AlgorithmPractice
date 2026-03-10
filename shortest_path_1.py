import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선개수
n, m = map(int, input().split())

# 시작 노드번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]

# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)

# 최단거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split()) # a노드에서 b노드로가는 비용이 c
    graph[a].append((b, c))

# def