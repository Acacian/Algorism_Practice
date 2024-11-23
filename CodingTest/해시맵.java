import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();
        
        for (String player : participant) {
            map.put(player, map.getOrDefault(player, 0) + 1);
        }

        for (String player : completion) {
            map.put(player, map.getOrDefault(player, 0) - 1);
        }

        for (String key : map.keySet()) {
            if (map.getOrDefault(key,0) != 0) {
                return key; // 완주하지 못한 선수의 이름 반환
            }
        }
        
        // 예외 상황은 문제에서 보장되지 않으므로 추가적인 반환 불필요
        return "";
    }
}