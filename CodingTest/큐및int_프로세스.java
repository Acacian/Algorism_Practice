import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> queue = new LinkedList<>(); // 큐에 {우선순위, 위치} 배열 저장

        // 1. 큐 초기화
        for (int i = 0; i < priorities.length; i++) {
            queue.add(new int[] { priorities[i], i }); // {우선순위, 위치}
        }

        int order = 0; // 실행 순서

        // 2. 큐 처리
        while (!queue.isEmpty()) {
            int[] current = queue.poll(); // 현재 프로세스 {우선순위, 위치}

            // 우선순위가 더 높은 프로세스가 있는지 확인
            if (queue.stream().anyMatch(p -> p[0] > current[0])) {
                queue.add(current); // 우선순위 높은 프로세스가 있으면 다시 삽입
            } else {
                order++; // 실행 순서 증가
                if (current[1] == location) { // 목표 프로세스라면 종료
                    return order;
                }
            }
        }

        return order; // 실제로는 도달하지 않음
    }
}
