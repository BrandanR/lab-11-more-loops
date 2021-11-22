userstring = input("Gimmie a number greater than 100 plz...")
usernum = int(userstring)

while usernum <= 100:
    print(str(usernum) + " is less than or equal to 100, dummy. Try again, I've got all day.")
    userstring = input("Gimmie a number greater than 100 plz...")
    usernum = int(userstring)

print(str(usernum) + " is over 100. Great job.")
