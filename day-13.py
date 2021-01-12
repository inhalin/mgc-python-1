class Calc:
  def __init__(self, a,b): 
    self.a=a
    self.b=b

  def add(self):
    print(self.a+self.b)

  def sub(self):
    print(self.a-self.b)

  def multi(self):
    print(self.a*self.b)

  def divide(self):
    print(self.a/self.b)

my_obj=Calc(1,2)

my_obj.add()
my_obj.sub()
my_obj.multi()
my_obj.divide()

