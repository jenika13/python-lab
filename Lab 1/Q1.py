from datetime import datetime 
current=datetime.now() 
year=current.strftime("%Y") 
name=input("Enter your Name : ")
age=int(input("Enter your age : "))
hyear=(int(year)+100)-age
print("Hello " + name + ". You will be 100 year old in the year {} ".format(hyear))