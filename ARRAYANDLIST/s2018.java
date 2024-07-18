import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class s2018 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int NN = 0;
        int count = 0;
        int ans = 0;

        if (N % 2 == 1){
            NN = N / 2 + 1;
        }else{
            NN = N / 2;
        }
        
        for (int i = 1; i < NN + 1; i++){
            ans = 0;
            for (int j = i; j < NN + 1;j++){
                ans = ans + j;
                if (ans > N){
                    break;
                }else if (ans == N){
                    count++;
                    break;
                }
            }
        }

        if (N >= 2){
            count += 1;
        }
        System.out.println(count);
    }
}

// if N % 2 == 1:
//     NN = N // 2 + 1
// else:
//     NN = N // 2

// count = 0
// for i in range(1,NN+1):
//     ans = 0
//     for j in range(i, NN+1):
//         ans = ans + j
//         if ans > N:
//             break
//         elif ans == N:
//             count += 1
//             break

// # 지 자신도 세야하니까 + 1(맨 마지막)
// # 단, 1일 때는 제외
// if N >= 2:
//     count += 1

// print(count)