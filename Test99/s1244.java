import java.io.*;
import java.util.*;
public class s1244 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        // 문제가 어렵다기보단 인덱스 에러 때문에 개고생한 문제
        int N = Integer.parseInt(br.readLine());
        int[] li = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            li[i] = Integer.parseInt(st.nextToken());
        }
        int studentsum = Integer.parseInt(br.readLine());
        // 사실 queue 를 import해서 fifo 방식으로 풀까도 생각했는데 귀찮음
        for (int s = 0; s < studentsum; s++) {
            // 성별 / 스위치 개수로 나눔
            st = new StringTokenizer(br.readLine());
            int sex = Integer.parseInt(st.nextToken());
            int switches = Integer.parseInt(st.nextToken());
            if (sex == 1) { // 남자아이 : 나눴을 때 나머지가 0이면 스위치 바꿈
                for (int i = 1; i <= N; i++) {
                    if (i % switches == 0) {
                        if (li[i-1] == 0) {
                            li[i-1] = 1;
                        } else {
                            li[i-1] = 0;
                        }
                    }
                }
            } else { // 여자아이 : 좌우 인덱스 비교해서 다를 때까지 (자기 포함해서 << 이거 몰라서 헛고생) 좌우 다 바꾸고, 다르면 자기만 바꿈
                //인덱스 번호 맞춰줌
                switches--;
                if (li[switches] == 1) {
                    li[switches] = 0;
                } else {
                    li[switches] = 1;
                }
                for (int i = 1; i < N; i++) {
                    if (switches - i < 0 || switches + i > N - 1) {
                        break;
                    }
                    if (li[switches-i] == li[switches+i]) {
                        if (li[switches-i] == 0 && li[switches+i] == 0) {
                            li[switches-i] = 1;
                            li[switches+i] = 1;
                        } else if (li[switches-i] == 1 && li[switches+i] == 1) {
                            li[switches-i] = 0;
                            li[switches+i] = 0;
                        } else {
                            break;
                        }
                    } else {
                        break;
                    }
                }
            }
        }
        // 20개마다 줄바꿈해야함
        for (int i = 1; i <= N; i++) {
            System.out.print(li[i-1] + " ");
            if (i % 20 == 0) {
                System.out.println();
            }
        }
    }
}