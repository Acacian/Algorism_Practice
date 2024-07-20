import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;

import java.util.*;

public class b1157{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String sr = br.readLine();
        
        // StringTokenizer는 length를 못 쓰네요. String으로 바꿨습니다.
        // charAt 처음 써 봐요 파이썬처럼 [ ] 로 문자열을 못 가져오더라고요
        // 몇 자 나올지 고정되있는게 아니니까 Arraylist 사용
        ArrayList<Character>word = new ArrayList<>();
        for (int i = 0; i < sr.length() - 1; i++) {
            word.add(Character.toUpperCase(sr.charAt(i)));
        }

        // 답이 전부다 대문자이므로 전체를 대문자로 정렬
        // sort 쓰려면 collection 가져와야해서 가져옴
        Collections.sort(word);
        int count = 0;
        int max = 0;
        char alphabet = ' ';
        // 브루트포스
        // 1부터 시작하는 이유는 /n 무시하고 시작하기 위해서
        int t = word.size();

        if (t == 0) {
            // arraylist는 get으로 가져옴
            System.out.println(word.get(0));
        } else {
            for (int i = 0; i < t - 1; i++) {
                if (word.get(i).equals(word.get(i + 1))) {
                    count++;
                    if (count == max) {
                        alphabet = '?';
                    } else if (count > max) {
                        alphabet = word.get(i);
                        max = count;
                    }
                } else {
                    count = 0;
                }
            }
            // 모든 알파벳이 다 한글자씩 있음
            if (count == 0 && max == 0) {
                alphabet = '?';
            }
        }

        System.out.println(alphabet);
    }
}