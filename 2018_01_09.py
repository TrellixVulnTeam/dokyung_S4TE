def funtion_name(arg1, arg2, arg3, arg4=None, arg5='hi'):
    print('함수 내부')

    return 'funtion_return'


def funtion_2():
    print('hi')


funtion_name(1, 2, 3, 4, 5)
funtion_name(1, 2, 3)
funtion_name(1, 2, 3, arg4='hi', arg5=None)


# class = property + method
# 'class'는 필요한 데이터와 해당 데이터에 대한 연산을 패키징한거
# '객체'지향 프로그래밍(Object Oriented Programing)
# 프로그래밍 컨셉이 바뀜.
# 원래 우리가 하던것은 절차지향형. <- 한줄 한줄 실행하는거.
# 명령어들의 중복을 피하고자 함수를 사용하거나 함.
# 다시 돌아와서 '객체' 지향에서 '객체'란 마치 사람처럼 하나의 케릭터?
# 를 가지고 있음.
# 예를 들어 커피숍을 만든다 치면 주문 받는 사람과 바리스타가 필요함.
# 물론 바리스타 혼자 다 할 수도 있지만, 성격적으로 2 케릭터로 분리 가능.
# 기존 전차지향형 프로그래밍에서는 케릭터를 굳이 나눌 필요 없이 기능별로
# 절차적으로 구현함. 시간순서로 손님이 오면 주문을 받고, 그에 따라 커피를
# 만들고, 만든 커피를 돌려줌.
# 객체지향으로 접근하게 되면, 손님, 주문 받는 사람, 바리스타 3명이 서로
# 상호작용 하는 것으로 커피숍을 정의할 수 있음.
# 손님이 와서 주문을 하게 되면, 주문 받는 사람과 상호작용을 통해 주문을
# 결정함. 그 후 주문 받은 사람은 결정된 주문 내역을 바리스타에게 전송함.
# 바리스타는 받은 주문 내역을 바탕으로 커피를 제조하여 손님에게 건내줌.
# 이때 주문 받는 사람은 커피를 1도 못만들어도 됨. 바리스타는 손님이랑
# 말 한마디 섞을 수 없어도 됨. 즉 역할이 명확하게 정해져있음.
# 이런 컨셉으로 프로그램을 설계하는 것이 객체지향형 프로그램을 만드는 것.
# 필요한 역할들을 정의하고, 해당 역할을 하는 객체들간의 통신으로 프로그램
# 을 만드는 것. 정도로 정의할 수 있음.
# 중소규모 프로그램을 만들때는 오히려 객체지향 프로그래밍으로 인해 복잡해
# 질 수도 있음. 허나 확장성과 유지보수에 강점을 갖음.
# 다시 돌아와서, 객체는 property + method. 즉 프로그래밍에서 역할을
# 정의하기 위해 필요한 것? data와 그에 대한 연산.
# property는 클래스에 필요한 data들, method는 클래스에 필요한 기능(
# 함수)들이고 보통 property에 대한 연산들.

class MotherClassName:
    property1 = 123
    property2 = 3

    def method1(self, a):
        print('a')

    def method2(self):
        print(self.property1)
        self.property2 = 5

        return 'ok'

# 주의해야 할 것
# 위의 MotherClassName class는 class이다.
# 뭔 말이냐면, 얘는 틀. 실제적으로 사용되는건 얘가 아니고 얘의 instnace


mother_class_instance = MotherClassName()


# 우리가 보통 사용하는 녀석은 mother_class_instance
# MotherClassName.method2() 와 같은 호출은 불가능.
# 이걸 가능하게 하는 방식이 있기는 함. class method이란 개념
# 지금은 일단 무시


# 클래스의 강점은 상속. 상속을 하기 위해 맹근다고 해도 무방할 정도로 강점.


class Animal(object):
    bark_type = None

    def bark(self):
        print(self.bark_type, '하고 짖슴다.')
