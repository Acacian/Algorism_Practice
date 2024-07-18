import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class s2003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine() , " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] li = new int[N];
        st = new StringTokenizer(br.readLine(), " "); // 새 줄을 읽어 st를 재초기화
        for (int i = 0; i < N; i++) {
            li[i] = Integer.parseInt(st.nextToken());
}
        
        int count = 0;
        for(int i = 0 ; i < N ; i++){
            int ans = 0;
            for(int j = i; j < N ; j++){
            ans = ans + li[j];
                if (ans > M){
                    break;
                }
                else if (ans == M){
                    count += 1;
                    break;
                }
            }
        }
    System.out.println(count);
    }
}

// for j in range(i, N):
// ans = ans + li[j]
// if ans > M:
//     break
// elif ans == M:
//     count += 1
//     break