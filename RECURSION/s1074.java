import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class s1074 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        System.out.println(Z(N, r, c));
    }
    // 생각을 바꿈. 확장하는 게 아니라 DP처럼 큰 Z에서 작은 Z로 쪼개야 함
    // 총 네모 크기는 2의 c승이므로, 이걸 4등분해서 해결방안 생성
    // 종료 조건이 어디에 있든 이전에 지나친 값들은 컴퓨터에 의해 전부 계산했다고 가정

    public static int Z(int n, int r, int c) {
        if (n == 0) {
            return 0;
        }

        int half = 1 << (n - 1);  // 2^(n-1)
        int quad = half * half;

        if (r < half && c < half) {  // 1사분면
            return Z(n - 1, r, c);
        } else if (r < half && c >= half) {  // 2사분면
            return quad + Z(n - 1, r, c - half);
        } else if (r >= half && c < half) {  // 3사분면
            return 2 * quad + Z(n - 1, r - half, c);
        } else {  // 4사분면
            return 3 * quad + Z(n - 1, r - half, c - half);
        }
    }
}