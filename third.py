#######################################
자료형

인덱싱 
list = [1,2,3]
list[0] == 1
list[1] == 2
list[0:2] == [1,2]# 0번째부터 2번째 '전'까지 라는 뜻

list = [1,2,3] vs tuple = [1,2,3]
#list:변할 수도 있는 데이터들을 나란히 묶어주는 자료형
#tuple: 변할 수 없는 (변하면 안되는)데이터들을 나란히 묶어주는 자료형

list[1] = 10 <-list# 1번값이 달라질 수 있음
tuple[1] = 10 <- tuple #1번값이 절대 달라질 수 없음

#딕셔너리(해쉬)
#데이터 관리
#개념 = '대응'
#탐색기준, 키워드:key
#탐색의 기준에 대응되는 찾고자하는 값:value

#입력 형식
#{key1:value1, key2:value2}
#ex)
#운동선수 = {"김연아":"피겨스케이팅", "박지성":"축구"}
#운동선수['김연아'] == '피겨스케이팅'
################################################