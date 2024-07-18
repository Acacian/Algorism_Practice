import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class s2740 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] li = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                li[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        int[][] li2 = new int[M][K];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < K; j++) {
                li2[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 하나는 가로로 늘어나고, 하나는 세로로 늘어나서 이들의 곱들을 합해야 함
        // M 은 중복됨. 즉 무조건 대칭된다는 말 / ex) 3*2 2*3(2 중복)
        for (int i = 0; i < N; i++) {
            ArrayList<Integer> ans = new ArrayList<>();
            // 여기까지 해서 맨 위의 배열을 가져옴
            for (int k = 0; k < K; k++) {
                int tot = 0;
                for (int j = 0; j < M; j++) {
                    // 행렬 곱 : 맨 처음 행렬의 첫 번째 <<= 다른 행렬의 첫/두/세번째가 대칭
                    int lef = li[i][j];
                    int rig = li2[j][k];
                    tot += lef * rig;
                }
                ans.add(tot);
            }
            for (int a : ans) {
                System.out.print(a + " ");
            }
            System.out.println();
        }
    }
}