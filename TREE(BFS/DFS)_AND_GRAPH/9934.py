import sys
input = sys.stdin.readline

K = int(input())
nums = list(map(int, input().split())) # 방문한 순서를 담은 리스트
nums.reverse()
tree = [0 for _ in range(2 ** K)] # 빌딩 번호 완전이진트리 리스트


def make_tree(tree, nums, root): # 중위 순회 순서대로 빌딩 번호 세팅
    if root < 1 or 2 ** K <= root or tree[root] != 0: return
    make_tree(tree, nums, 2 * root) # 왼쪽 자식 노드 탐색
    tree[root] = nums.pop() # 빌딩 번호 할당
    make_tree(tree, nums, 2 * root + 1) # 오른쪽 자식 노드 탐색
    
    
make_tree(tree, nums, 1)
i = 1
while i < 2 ** K: # 출력 반복문
    for j in range(i, i * 2):
        print(tree[j], end=' ')
    print()
    i *= 2