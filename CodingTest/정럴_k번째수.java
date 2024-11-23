import java.util.*;
import java.util.stream.*;
import java.io.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        return Arrays.stream(commands) // commands를 스트림으로 변환
                     .mapToInt(command -> { // 각 command 배열 처리
                         int i = command[0] - 1; // 시작 인덱스 (0-based)
                         int j = command[1];     // 끝 인덱스
                         int k = command[2] - 1; // k번째 숫자 (0-based)
                         return Arrays.stream(array, i, j) // i부터 j까지 자름
                                      .sorted()            // 정렬
                                      .toArray()[k];       // k번째 값 반환
                     })
                     .toArray();
    }
}
