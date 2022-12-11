class Calculator:
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        addition = self.num1 + self.num2
        print(addition)
    def sub(self):
        subtract = self.num1 - self.num2
        print(subtract)
    def mul(self):
        multiply = self.num1 * self.num2
        print(multiply)
    def div(self):
        division = self.num1 / self.num2
        print(division)
obj = Calculator(50,10)
print("\nChallenge-2 Output:- ")
obj.add()
obj.sub()
obj.mul()
obj.div()