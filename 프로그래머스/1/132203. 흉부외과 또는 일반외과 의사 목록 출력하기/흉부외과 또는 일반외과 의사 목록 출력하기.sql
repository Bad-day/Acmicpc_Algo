-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, date_format(HIRE_YMD,'%Y-%m-%d')
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC

#시, 분 초, 제거, HIRE_YMD 내림차순, 고용일자가 같다면 이름순 오름차순