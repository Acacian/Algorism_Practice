import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class s7785 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Set<String> employees = new HashSet<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String name = st.nextToken();
            String action = st.nextToken();
            
            if (action.equals("enter")) {
                employees.add(name);
            } else {
                employees.remove(name);
            }
        }

        List<String> sortedEmployees = new ArrayList<>(employees);
        sortedEmployees.sort(Collections.reverseOrder());

        for (String name : sortedEmployees) {
            System.out.println(name);
        }
    }
}
