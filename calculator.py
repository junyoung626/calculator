import math

class Calculator():
    
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

class UpgradeCal(Calculator):
    def pow(self):
        result = self.first ** self.second
        return result
    
    def div(self):
        if self.second == 0:
            return 0
        else:   
            return self.first / self.second
        return result
        

    while True:
        expression = input("수식을 입력하세요:")
        try:
            expression.split(" ")
            result = Calculator(expression)
            
            print("결과 :", result)
        except(NameError, TypeError):
            print("잘못된 수식입니다.")
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다")