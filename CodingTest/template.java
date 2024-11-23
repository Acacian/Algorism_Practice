import java.util.*;
import java.util.stream.*;
import java.io.*;

//기본
return Arrays.stream(arr)
                .filter(num -> num % 2 == 0) // 조건: 짝수만
                .toArray();                  // 배열로 반환

//매트릭스
int result = 0;
for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
        // 예제: 행렬의 모든 값의 합 계산
        result += matrix[i][j];
    }
}
return result;

// 리스트
List<Integer> result = new ArrayList<>();
for (int num : input) {
    // 예제: 리스트에서 홀수만 저장
    if (num % 2 != 0) {
        result.add(num);
    }
}
return result;

//키값
Map<Integer, Integer> map = new HashMap<>();
for (int num : arr) {
    map.put(num, map.getOrDefault(num, 0) + 1); // 빈도수 계산
}
return map;

//큐
Queue<Integer> queue = new LinkedList<>();
for (int num : arr) {
    queue.add(num); // 값 추가
}

while (!queue.isEmpty()) {
    int current = queue.poll(); // 값 꺼내기
    // 예제: 큐에서 값을 꺼내서 처리
}
return 0;

//스텍
Stack<Character> stack = new Stack<>();
for (char c : s.toCharArray()) {
    if (c == '(') {
        stack.push(c); // 값 추가
    } else {
        if (stack.isEmpty()) {
            return 0; // 올바르지 않은 경우
        }
        stack.pop(); // 값 제거
    }
}
return stack.isEmpty() ? 1 : 0; // 스택이 비었으면 올바른 괄호

//리스트 정렬
list.sort(Collections.reverseOrder()); // 내림차순 정렬
return list;
//배열 정렬
Arrays.sort(arr); // 오름차순 정렬
return arr;

//DFS
visited[node] = true; // 방문 처리
for (int next : graph.get(node)) {
    if (!visited[next]) {
        dfs(next, visited, graph); // 재귀 호출
    }
}
//BFS
public void bfs(int start, boolean[] visited, List<List<Integer>> graph) {
    Queue<Integer> queue = new LinkedList<>();
    queue.add(start);
    visited[start] = true;

    while (!queue.isEmpty()) {
        int node = queue.poll();
        for (int next : graph.get(node)) {
            if (!visited[next]) {
                queue.add(next);
                visited[next] = true;
            }
        }
    }

//조합
if (current.size() == nums.size()) {
    result.add(new ArrayList<>(current));
    return;
}

for (int i = 0; i < nums.size(); i++) {
    if (used[i]) continue;
    used[i] = true;
    current.add(nums.get(i));
    generatePermutations(nums, current, used, result);
    current.remove(current.size() - 1);
    used[i] = false;
}

//Prefix(누적합)
int[] prefixSum = new int[arr.length + 1];
for (int i = 1; i <= arr.length; i++) {
    prefixSum[i] = prefixSum[i - 1] + arr[i - 1];
}

int[] result = new int[queries.length];
for (int i = 0; i < queries.length; i++) {
    int start = queries[i][0], end = queries[i][1];
    result[i] = prefixSum[end + 1] - prefixSum[start];
}

return result;