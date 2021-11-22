userstring = input("On what floor of the buidling is your office?")
maximum_stories = int(userstring)

while maximum_stories >= 13:
    print(str(maximum_stories) + " Is not an available floor in this building, try entering a valid number from 1-12 ")
    userstring = input("Gimmie a Floor from 1-12. ")
    maximum_stories = int(userstring)

print(str(maximum_stories) + " ,Congrats, you've made it to the correct floor.")
