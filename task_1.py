user={"user_name":"Rakesh",
	"password":"222222222",
	"subscription":"active"}
name=input("enter user_name \n")
username=user["user_name"]
pas=input("enter password \n")
len(pas)>8
pass_word=user["password"]
print("login ",name==username and pas==pass_word)

print("_______________________________")
login=(name==username and pas==pass_word)
print("Enter generated otp \n")
OTP=eval(input())
print("To check wether the OTP will matches to the verifying OTP")
ver_otp=eval(input("Enter your OTP \n"))
print("otp verification " ,OTP==ver_otp)

print("______________________________")
print("enter age")
age_=int(input())
print("useer eligible to create account ",age_>=18)

print("_____________________________")
a=user["subscription"]
print("enter your subscription status like active/in active")
b=input()
print("user have premium subscribtion ",a==b and login)

