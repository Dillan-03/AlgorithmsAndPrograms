#!/Users/Dillan/PersonalProgramming/Python/Project_Env/bin/python

#To check if a year is a leap or not
class Year:

    def __init__(self,user):
        self.user = user

    def leapyear(self):
        if self.user % 4 = 0 :
            if self.user % 100:
                if self.user % 400:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

user = int(input("Enter a year to find out whether it is a leap year: "))
x = Year(user)

x.leapyear()

print(x.leapyear())
