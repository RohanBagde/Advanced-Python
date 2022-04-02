#aop.py
class Aop:
	def  readvalues(self):
		self.a=float(input("Enter Value of a:"))
		self.b=float(input("Enter Value of b:"))
	def aop_operations(self):
		x1=self.a+self.b
		x2=self.a-self.b
		x3=self.a*self.b
		x4=self.a/self.b
		x5=self.a//self.b
		x6=self.a%self.b
		x7=self.a**self.b
		return x1,x2,x3,x4,x5,x6,x7
	def dispvalues(self, result):
		print("-"*40)
		print("Arithmetic Operations")
		print("-"*40)
		print("Sum({},{})={}".format(self.a,self.b,result[0]))
		print("Sub({},{})={}".format(self.a,self.b,result[1]))
		print("Mul({},{})={}".format(self.a,self.b,result[2]))
		print("Div({},{})={}".format(self.a,self.b,result[3]))
		print("Floor Div({},{})={}".format(self.a,self.b,result[4]))
		print("Mod({},{})={}".format(self.a,self.b,result[5]))
		print("Expo({},{})={}".format(self.a,self.b,result[6]))
		print("-"*40)
#main program
ao=Aop()
print("id of a in main program=",id(ao))
ao.readvalues()
res=ao.aop_operations()
ao.dispvalues(res)