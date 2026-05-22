user={"user_name":"Rakesh",
	"password":"222222222",
	"subscription":"Active"}
name=input("enter user_name \n")
r=user["user_name"]
pas=input("enter password \n")
len(pas)>8
le=user["password"]

print(r==name and pas==le)
print("True means login successful ")
print("False means login unsuccessful")


print("_______________________________")
login=r==name and pas==le
print("Enter generated otp \n")
OTP=eval(input())
print("To check wether the OTP will matches to the verifying OTP")
ver_otp=eval(input("Enter your OTP \n"))
if OTP==ver_otp:
	print("verification successful")
else:
	print("wrong otp")


print("______________________________")
print("enter age")
age_=int(input())
print(age_>=18)
print("True means you are eligible for account creation")
print("False means not eligible for accoutn creation")


print("_____________________________")
a=user["subscription"]
print("enter your subscription status like active/in active")
b=input()
print(a==b and login)
print("True means user have Premium subscription")
print("False means user have no premium subscription")
