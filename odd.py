a = input("enter a number")


try :
	a = int(a)
	if a%2==0:
		print(a, "is even")
	else:
		print(a, "is odd")
except ValueError:
	print("plz enter num") 




