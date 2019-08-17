#문자열 (내장함수)

#덧셈

str = "멋쟁'이 사자'처'럼"
str2 = "은, 좋은, 동아리,입니다."

print(str+str2)

print(str[1])

print(len(str)) #공백포함 글자수

print(str[1:4])

#문자열 내에서 특정 문자의 등장 횟수 : 문자열 변수.count('특정문자')

print(str.count('사'))

#문자열을 (특정 기준으로) 나누기 : 문자열 변수.split()

print(str.split())#() = 공백기준 (',') = 쉼표기준

print(str.split("'"))#작은 따옴표 기준
print(str.split(','))

#찾고자 하는 문자의 인덱스를 반환
print(str.find('사'))#찾고자 하는 문자가 없을 때 -1을 출력
print(str.index('사'))#찾고자 하는 문자가 없을 때 오류 일으킴