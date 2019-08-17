#제어문 = 코드의 흐름을 제어한다!
#제어문 - 분기문 = if문 = 컴퓨터에게 선택의 여지와 조건을 부여
#if(조건):// : 이랑 indent개중요 아니면 오류남

#예제 1) 85점이상 pass, or fail

score = int(input("점수를 입력해 주세요 : ")) #여기에 있는 한글 = 프롬프트

if (score >= 85):
    print("PASS")
else:
    print("FAIL")


#예제 2) 

activity = input("너 동아리 뭐해? : ")

if (activity == "멋쟁이사자처럼"):#일치여부연산자 == /대입연산자 =
    print("어, 너도 멋사야?")
else:
    print("...그래...")

#예제 3) 3가지 이상 비교조건이 있을 때
#else if 합친 문법 elif사용하면 가독성 올라감

money = int(input("돈 얼마 있어? "))

if(money >= 5000):
    print("아웃백 가자")
elif(money >= 3000):
        print("학식 먹자")
elif(money >= 1000):
    print("컵라면 먹자")
else:
     print("공기밥 가즈아아아ㅏㅏ")

