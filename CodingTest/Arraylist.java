import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] ranges) {
        // Prefix Sum 계산
        int[] prefixSums = new int[arr.length + 1];
        for (int i = 1; i <= arr.length; i++) {
            prefixSums[i] = prefixSums[i - 1] + arr[i - 1];
        }

        // 결과 배열 생성
        int[] result = new int[ranges.length];
        for (int i = 0; i < ranges.length; i++) {
            int start = ranges[i][0];
            int end = ranges[i][1];
            // 범위가 잘못된 경우 -1 반환
            if (start < 0 || end >= arr.length || start > end) {
                result[i] = -1;
            } else {
                result[i] = prefixSums[end + 1] - prefixSums[start];
            }
        }

        return result;
    }
}
