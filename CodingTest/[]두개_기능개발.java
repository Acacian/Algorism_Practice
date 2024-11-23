import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] days = IntStream.range(0, progresses.length)
                              .map(i -> (100 - progresses[i] + speeds[i] - 1) / speeds[i])
                              .toArray();

        List<Integer> result = new ArrayList<>();
        int maxDay = days[0], count = 0;

        for (int day : days) {
            if (day > maxDay) {
                result.add(count);
                count = 0;
                maxDay = day;
            }
            count++;
        }
        result.add(count);

        return result.stream().mapToInt(i -> i).toArray();
    }
}
