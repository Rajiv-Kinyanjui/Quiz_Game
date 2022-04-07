def give_options(x,y,z):
    print("a):",x)
    print("b):",y)
    print("c):",z)

print("Hello! Welcome to my quiz \nEvery answer is worth 10 points")
ans = input("\nAre you ready to play?(Yes/No)\n")
disc = "Note: Write the actual answer NOT the option"

score = 0
total_questions = 5

if (ans.lower() == 'yes'):
    print(disc)

    #Question 1
    print("\n1. What is the best programming language?")
    give_options("Python","C++","Java")
    ans = input("My answer is: ")

    if (ans.lower() == 'python'):
        score += 1
        print("\t correct")
    else:
        print("\t incorrect")


    #Question 2
    print("\n2. Who is the founder of Apple Inc.?")
    give_options("Mark Zuckerberg","Bill Gates","Steve Jobs")
    ans = input("My answer is: ")

    if (ans.lower() == 'steve' or 'steve jobs' or 'stevejobs'):
        score += 1
        print("\t Correct")
    else:
        print("\tIncorrect")


    #score system
    i = score * 10
    if i < 20:
        print("\nYour score is "+str(i)+"/50, Better luck next time")
    elif (i>=20 and i<40):
        print("\nYour score is "+str(i)+"/50, Good trial.")
    else:
        print("\nYour score is "+str(i)+"/50, Well done")

else:
    print("Program Ended!")
    
    