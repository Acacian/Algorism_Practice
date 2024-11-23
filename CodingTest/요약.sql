만약 재귀가 필요하다면
WITH RECURSIVE(SELECT FROM WHERE..
UNION ALL << 재귀적 결과를 결합
SELECT ...(위랑 같이)
JOIN ~~ ON ~~ = ~~
이 뒤 다시 SELECT...

보여줄 컬럼
SELECT ~~~~
추가 *
DISTINCT : 중복삭제
DATE_FORMAT(~~ , ' 형태(예 : %Y-%m-%d) ') AS ~~
FLOOR : 내림 / ROUND : 올림 그리고 ( , 숫자) 이렇게 뒤에 , 숫자 넣으면 소수점 ~~자리까지
MONTH(~~)
CASE ~~(ex : WHEN DATEDIFF(끝, 시작) + 1 >= 30) THEN ' '
ELSE ' '
END AS ~~~~(컬럼 이름)

FROM '테이블명'

테이블이 두 개 이상일 경우 동일 키를 이용해 묶어줌
JOIN ~~ ON a.~~ = b.~~
셀프 조인도 가능함(예 FROM ~~ a JOIN ~~ b ON a.ID = b.PARENT_ID)

문제에서 특정 부분 필터링이 필요한 경우
WHERE 조건~~ 또는 = ' ' 사용해서 필터
같이 사용 가능할 만한 것 : AND / BETWEEN / LIKE ' ' (~테이블 안에 ' '가 있는가?) / EXISTS, NOT EXISTS(SELECT = *, FROM ~~ WHERE ~~)

문제에 '~별'이라는 게 들어갈 경우
GROUP BY ~~
HAVING ~~ 또는 COUNT(*) > 1 이렇게 중첩 횟수(2개이상인것만) 제한 가능

문제에 '내림차순 / 오름차순'이 있는 경우
ORDER BY ~~ ASC 또는 DESC

같이 쓸 만한 것 :
LIMIT 3 -> 3개만 제한