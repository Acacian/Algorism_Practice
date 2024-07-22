import java.io.*;
import java.util.*;

public class g2580 {
    static int[][] stoku = new int[9][9];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        for (int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                stoku[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        backtracking(0);
    }

    static boolean backtracking(int depth) {
        if (depth == 81) {
            for (int[] row : stoku) {
                for (int num : row) {
                    System.out.print(num + " ");
                }
                System.out.println();
            }
            return true;
        }

        int y = depth / 9, x = depth % 9;
        if (stoku[y][x] != 0) {
            return backtracking(depth + 1);
        }

        for (int num = 1; num <= 9; num++) {
            // 행, 열, 3x3 박스 검사를 한 번에 수행
            boolean valid = true;
            
            // 행 검사
            for (int i = 0; i < 9; i++) {
                if (stoku[y][i] == num) {
                    valid = false;
                    break;
                }
            }
            
            // 열 검사
            if (valid) {
                for (int i = 0; i < 9; i++) {
                    if (stoku[i][x] == num) {
                        valid = false;
                        break;
                    }
                }
            }
            
            // 3x3 박스 검사
            if (valid) {
                int startY = (y / 3) * 3, startX = (x / 3) * 3;
                for (int i = startY; i < startY + 3; i++) {
                    for (int j = startX; j < startX + 3; j++) {
                        if (stoku[i][j] == num) {
                            valid = false;
                            break;
                        }
                    }
                    if (!valid) break;
                }
            }

            if (valid) {
                stoku[y][x] = num;
                if (backtracking(depth + 1)) {
                    return true;
                }
                stoku[y][x] = 0;
            }
        }

        return false;
    }
}