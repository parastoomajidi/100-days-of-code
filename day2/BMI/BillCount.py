print("Wellcome to the tip Calculator")
s1= float(input("what was the total bill? $"))
s2= int(input("How mutch tip would you like to give? like 10, 12 or 15"))
s3= input("How many people to split the bill?")
total =  s2 / 100 * s1 + s2
print(f"each person should pay :{total} ")