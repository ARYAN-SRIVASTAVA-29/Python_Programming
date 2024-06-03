# age = 21

# if(age >= 18):
#     print("You can vote")
#     print("Yo can have license")
# elif(age<18):
#     print("You can't wait")

a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))

if(a > b and a > c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("Third is largest", c)
