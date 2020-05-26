from lcm_hcf import *
class rational:
	def __init__(self,numerator=0,denominator=1):
		self.__numerator=numerator
		self.__denominator=denominator
	def input(self):
		self.__numerator=int(input("Enter numerator : "))
		self.__denominator=int(input("Enter denominator : "))
		
	def __str__(self):
		return str(self.__numerator)+"/"+str(self.__denominator)
		
	def simplification(self):
		simplify=rational()
		simplify.__numerator=self.__numerator//hcf(abs(self.__numerator),abs(self.__denominator))
		simplify.__denominator=self.__denominator//hcf(abs(self.__numerator),abs(self.__denominator))
		return simplify
	
	def __add__(self,num):
		sum=rational()
		sum.__numerator=((self.__numerator)*(lcm(self.__denominator,num.__denominator))//self.__denominator) + ((num.__numerator)*(lcm(self.__denominator,num.__denominator))//num.__denominator)
		sum.__denominator=lcm(self.__denominator,num.__denominator)
		return sum.simplification()
	
	def __sub__(self,num):
		subtract=rational()
		subtract.__numerator=((self.__numerator)*(lcm(self.__denominator,num.__denominator))//self.__denominator) - ((num.__numerator)*(lcm(self.__denominator,num.__denominator))//num.__denominator)
		subtract.__denominator=lcm(self.__denominator,num.__denominator)
		return subtract.simplification()
	
	def __mul__(self,num):
		multiply=rational()
		multiply.__numerator=self.__numerator*num.__numerator
		multiply.__denominator=self.__denominator*num.__denominator
		return multiply.simplification()
		
	def __floordiv__(self,num):
		divide=rational()
		divide.__numerator=self.__numerator*num.__denominator
		divide.__denominator=self.__denominator*num.__numerator
		return divide.simplification()
		
if __name__=="__main__":
	o1=rational()
	o2=rational()
	while True:
		print()
		print("--------------------------")
		print("Rational Number Calculator ")
		print("--------------------------")
		print("        CHOICES")
		print("1. Addition")
		print("2. Subtraction")
		print("3. Multiplication")
		print("4. Division ")
		print("5. Simplification")
		print("6. Exit")
		choice=int(input("Enter your choice : "))
		
		if choice==1:
			print("Enter first number ")
			o1.input()
			print("Enter second number")
			o2.input()
			sum=o1+o2
			print(sum)
		elif choice==2:
			print("Enter first number ")
			o1.input()
			print("Enter second number")
			o2.input()
			subtract=o1-o2
			print(subtract)
		elif choice==3:
			print("Enter first number ")
			o1.input()
			print("Enter second number")
			o2.input()
			multiply=o1*o2
			print(multiply)
		elif choice==4:
			print("Enter first number ")
			o1.input()
			print("Enter second number")
			o2.input()
			divide=o1//o2
			print(divide)
		elif choice==5:
			print("Enter number")
			o1.input()
			simplify=o1.simplification()
			print(simplify)
		elif choice==6:
			break
		else:
			print("Wrong Choice !")