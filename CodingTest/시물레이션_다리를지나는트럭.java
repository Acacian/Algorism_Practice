import java.util.*;
import java.util.stream.*;
import java.io.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<int[]> queue = new LinkedList<>(); // 다리 위 트럭 관리 {무게, 진입 시간}
        int currentWeight = 0; // 다리 위 트럭의 총 무게
        int time = 0; // 시뮬레이션 시간
        int index = 0; // 대기 중인 트럭 인덱스

        while (index < truck_weights.length || !queue.isEmpty()) {
            time++; // 시간 증가

            // 1. 다리를 완전히 건넌 트럭 제거
            if (!queue.isEmpty() && time - queue.peek()[1] >= bridge_length) {
                currentWeight -= queue.poll()[0]; // 무게 감소
            }

            // 2. 새로운 트럭 추가
            if (index < truck_weights.length && currentWeight + truck_weights[index] <= weight) {
                queue.add(new int[] { truck_weights[index], time }); // {무게, 진입 시간}
                currentWeight += truck_weights[index]; // 무게 증가
                index++; // 다음 트럭으로 이동
            }
        }

        return time;
    }
}