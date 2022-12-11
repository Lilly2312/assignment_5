class Student:
    def __init__(self,__name,__rollNum):
        self.__name = __name           
        self.__rollNum = __rollNum

    def __str__(self):
        return f"Student: \nname: {self.__name} \nrollNum: {self.__rollNum}"

    def set_name(self,__name):
        self.__name = __name

    def get_name(self):
        return self.__name

    def set_rollNum(self,__rollNum):
        self.brand = __rollNum

    def get_rollNum(self,__rollNum):
        return self.__rollNum

student = Student("kishan","30")
print("\nChallenge-3 Output:- \n",student)