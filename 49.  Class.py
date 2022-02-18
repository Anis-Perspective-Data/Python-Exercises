class test:
    x=0;
    def blood_group1(self):
        self.b="to donate only A+,AB+"
        return "a positive"
    def blood_group2(self):
        self.c="to donate only B+,AB+"
        return "b positive"
    def blood_group3(self):
        self.d="universal donator "
        return "o positive"
    print(x)
test()    
y=test()
print(y.blood_group1())
print(y.b)
print(y.blood_group2())
print(y.c)
print(y.blood_group3())
print(y.d)