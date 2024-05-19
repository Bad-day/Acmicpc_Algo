-- ECT REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE(SELECT AVG(CAST(REVIEW_SCORE AS DECIMAL(10,2)) FROM REST_REVIEW)
-- fROM REST_INFO, REST_REVIEW
-- ORDER BY SCORE DESC, FAVORITES DESC
SELECT Tbl1.REST_ID, Tbl1.REST_NAME, Tbl1.FOOD_TYPE, Tbl1.FAVORITES, Tbl1.ADDRESS, 
ROUND(AVG(Tbl2.REVIEW_SCORE),2)as SCORE
FROM REST_INFO Tbl1
JOIN REST_REVIEW Tbl2 ON Tbl1.REST_ID = Tbl2.REST_ID
WHERE Tbl1.ADDRESS Like '서울%'
GROUP BY Tbl1.REST_ID, Tbl1.REST_NAME, Tbl1.FOOD_TYPE, Tbl1.FAVORITES, Tbl1.ADDRESS
ORDER BY SCORE DESC, Tbl1.FAVORITES DESC;