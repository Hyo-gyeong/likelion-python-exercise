#딕셔너리 (내장함수)

pairs = {'잔나비' : '뜨거운 여름밤은 가고 남은 건 볼품없지만', 'sg워너비' : '내사람', '음료' : '커피'}

#하나의 키:value 추가하는 방법
# => 딕셔너리형 변수[키] = value

print(pairs)

pairs['스텐딩 에그'] = '휴식'

print(pairs)

#특정 키와 value삭제하는 방법
# => del 변수[키]

del pairs['잔나비'] #del 리스트와 튜플에서도 사용 가능
print(pairs)

#key로 'vlaue'를 얻기 : 변수.get[키]

v = pairs.get('음료')
print(v)