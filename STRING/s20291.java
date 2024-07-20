import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class s20291 {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
				
				// 확장자별로 정리해서, 그 안에 있는 개수만 세면 됨
				// 해시맵 사용
        Map<String, Integer> extensionCount = new HashMap<>();

        for (int i = 0; i < n; i++) {
		        // . 기준으로 분리함 
            String[] parts = reader.readLine().split("\\.");
            String ext = parts[1];
            extensionCount.put(ext, extensionCount.getOrDefault(ext, 0) + 1);
        }

        List<Map.Entry<String, Integer>> sortedList = new ArrayList<>(extensionCount.entrySet());
        sortedList.sort(Map.Entry.comparingByKey());

        for (Map.Entry<String, Integer> entry : sortedList) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}
