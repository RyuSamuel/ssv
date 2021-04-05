import typing
import collections

#스택을 이용한 DFS 알고리즘은 다음과 같은 순서로 실행된다.

#1.탐색을 시작할 스타팅 노드를 스택에 넣는다.

#2.스택이 빈 공간이 아닐 때 까지 다음을 실행한다.

#3.스택에서 정점 하나를 꺼내 방문하지 않았으면 방문 표시를 하고 그 정점에 인접한 모든 정점을 스택에 넣는다.(방문 하지 않은 정점들만)

#4.2번으로 간다.

def DES_iterative(graph, vertex):
    discovered = []
    stack = [vertex] #stack이라는 스택을 하나 생성한다. 현재 방문 정점의 인접 정점들을 담는다. 탐색하고자 하는 시작 정점 vertex를 스택에 push한다.

    while stack: #스택이 빈 공간이 아닐 때 까지 아래 연산들을 반복한다.
        vertex = stack.pop() # 현재 탐색 하고 있는 정점을 stack에 넣는다.

        if vertex not in discovered: #만약 vertex가 탐색되지 않았으면, 탐색 완료 표시를 한다.
            discovered.append(vertex)
            for w in graph[vertex]:
                stack.append(w) # 현재 정점 vertex의 모든 인접한 정점 w를 스택에 넣는다. (w가 방문되지 않았으면)

    return discovered

graph_list = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3]
}



print(DES_iterative(graph_list, 1))