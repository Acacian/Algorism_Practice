import java.io.*;
import java.util.*;

public class s11478 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String n = reader.readLine().trim();
        
        Set<String> uniqueSubstrings = new HashSet<>();
        
        // 몇 번 배열을 반복할 것인가
        for (int i = 1; i <= n.length(); i++) {
            // 하나씩 연결하는 수를 늘림
            for (int j = 0; j <= n.length() - i; j++) {
                String substring = n.substring(j, j + i);
                uniqueSubstrings.add(substring);
            }
        }
        
        System.out.println(uniqueSubstrings.size());
    }
}