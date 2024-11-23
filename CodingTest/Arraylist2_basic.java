import java.util.*;

class Solution {
    public List<Integer> solution(List<Integer> input) {
        List<Integer> result = new ArrayList<>();
        for (int num : input) {
            if (num % 2 == 0) {
                result.add(num);
            }
        }
        return result;
    }
}