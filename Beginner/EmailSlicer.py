#!/Users/Dillan/PersonalProgramming/Python/Project_Env/bin/python

#Email Slicer

#Gets the username and domain name from an email address

class Email:
    username = str
    domain = str
    position = str
    def __init__(self,email):
        self.email = email
        self.username = Email.username
        self.domain = Email.domain
        self.position = Email.position

    def slicinguser(self):
        self.domain = self.email.find("@")
        email = list(self.email)
        self.username = email[0:self.domain]
        self.username = "".join(self.username)
        # return self.username
        return "Username --> "+self.username

    def slicingdomain(self):
        a = self.email.find("@")
        b = self.email.find(".com")
        email = list(self.email)
        self.domain = email[a+1:b]
        self.domain = "".join(self.domain)
        return "Domain Name --> "+self.domain


email = "testing@email.com"
x = Email(email)

x.slicinguser()
x.slicingdomain()
print(x.slicinguser())
print(x.slicingdomain())
