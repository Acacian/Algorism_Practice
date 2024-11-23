import java.util.*;
import java.util.stream.*;
import java.io.*;

class Solution {
    public int[] solution(int[] arr) {
        return IntStream.range(0, arr.length)
                        .filter(i -> i == 0 || arr[i] != arr[i - 1])
                        .map(i -> arr[i])
                        .toArray();
    }
}
