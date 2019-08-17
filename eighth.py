#class 개념
#파이썬에서 객체는 객체를 구분할 수 있는 class에 의해 정의된다.
#클래스를 사용하는 이유는 추상화된 현실의 개념을 구체적인 파이썬 코드로 표현하기 위해서이다.
#클래스 -> 인스턴스 ( 색, 이름 등 구체적값을 가짐, 나타남)
#class 클래스이름(부모클래스이름):
      #정의부

#class things:
#   pass
#class AAA(things):
#   pass
#class BBB(things):
#   pass
#class AA(AAA):
#   pass
#things 가 부모, AAA, BBB는 자식

###클래스 정의
class Cat:
    def meow(self):# ...self = 내가 속한 줄기에서 가져오겠다
        print("야옹 야옹~~~")
###인스턴스생성과 메소드 호출
        cat1 = Cat() #cat1 = 인스턴스 Cat()을 참조하는 참조변수, Cat()과같이 함수처럼 호출하여 인스턴스 생성
        cat1.meow() #cat1객체가 참조하고 있는 클래스의 메소드 meow()호출
##결과 : 야옹 야옹~~~

##고양이를 한마리 더 만들고 싶다
        cat2 = Cat()
        cat2.meow()
##결과 : 야옹 야옹~~~
#        야옹 야옹~~~
 
class Cat:
    def info(self): #info()메소드
#파이썬의 self는 클래스의 인스턴스를 지칭하며 self키워드를 통해 클래스의 메소드와 속성에 접근할 수 있다.
#모든 메소드의 첫 번째 매개변수는 자기 자신을 가리키는 self변수이다. 즉 이 메소드를 호출한 현재 객체를 의미한다.
        self.name = "나비" #인스턴스 변수 name 생성
        self.color = "검정색" #인스턴스 변수 color
        print('고양이 이름은', self.name, '색깔은', self.color)

cat = Cat()
cat.info()

##결과 : 고양이 이름은 나비 색깔은 검정색
##메서드 초기화!
class Book:

    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print '제목 : ', self.title
        print '가격 : ', self.price
        print '저자 : ', self.author
#####################################
    def __init__(self):
        print '책 객체를 새로 만들었어요~'
######################################

class Cat:
    def __init__(self, name="나비", color="흰색"): #나비, 흰색 없어도 무방
        self.name = name
        self.color = color
    def info(self):
        print('고양이 이름은', self.name, '색깔은 ', self.color)

cat1 = Cat()("네로", "검정색") #여기에서 초기화한 함수의 self는 cat1
cat2 = Cat()("미미", "갈색")

cat1.info()
cat2.info()