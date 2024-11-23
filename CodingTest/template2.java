배열에서 최대값 찾기
class Solution {
    public int solution(int[] arr) {
        return Arrays.stream(arr).max().orElse(0); // 배열 스트림의 최댓값 반환
    }
}

중복제거
class Solution {
    public int[] solution(int[] arr) {
        return Arrays.stream(arr).distinct().toArray(); // 중복 제거 후 배열 반환
    }
}

배열 합
class Solution {
    public int solution(int[] arr) {
        return Arrays.stream(arr).sum(); // 배열 요소 합 반환
    }
}

짝수 필터링
class Solution {
    public int[] solution(int[] arr) {
        return Arrays.stream(arr).filter(num -> num % 2 == 0).toArray(); // 짝수 필터링
    }
}

배열뒤집기
class Solution {
    public int[] solution(int[] arr) {
        return IntStream.range(0, arr.length)
                        .map(i -> arr[arr.length - 1 - i]) // 뒤에서부터 매핑
                        .toArray();
    }
}

특정 값 카운트
class Solution {
    public long solution(int[] arr, int target) {
        return Arrays.stream(arr).filter(num -> num == target).count(); // 특정 값 필터링 후 개수 세기
    }
}

최소값 인덱스 찾기
class Solution {
    public int solution(int[] arr) {
        return IntStream.range(0, arr.length)
                        .reduce((i, j) -> arr[i] < arr[j] ? i : j) // 최소값 인덱스 찾기
                        .orElse(-1); // 빈 배열 예외 처리
    }
}

연속된 값 제거
class Solution {
    public int[] solution(int[] arr) {
        return IntStream.range(0, arr.length)
                        .filter(i -> i == 0 || arr[i] != arr[i - 1]) // 연속된 중복 제거
                        .map(i -> arr[i])
                        .toArray();
    }
}

