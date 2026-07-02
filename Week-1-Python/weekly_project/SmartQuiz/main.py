from question import Question
#questions for quiz
q1=Question("Which keyword is used to create a function in Python ?\n"
    "a) fun\nb) define\nc) def\nd) function\nAnswer: ",
    "c",1)
q2=Question("Which Data Type is used to store string ?\n"
    "a) int\nb) str\nc) list\nd) float\nAnswer: ",
    "b",1)
q3=Question("Which symbol is used for comments in Python?\n"
    "a) *\nb) **\nc) !\nd) #\nAnswer: ",
    "d",1)
q4=Question("Which keyword is used to create a class in Python?\n"
    "a) struct\nb) fuc\nc) class\nd) classes\nAnswer: ",
    "c",1)
q5=Question("Which function is used to take input from user?\n"
    "a) get\nb) int\nc) cin\nd) input\nAnswer: ",
    "d",1)
#list of questions
questions=[q1,q2,q3,q4,q5]
score=0 #track score
print("==========Quiz Start============")
name=str(input("Enter your Name: "))
for q in questions:
    user_answer=input(q.question).lower()
    if user_answer==q.answer:
        print("Correct Answer !!")
        score+=1
    else:
        print("Wrong Answer !!")
        print("Correct Answer is :",q.answer)
print("===== Quiz Finished =====")
print("Your Final Score is:", score, "/5")
print("Saving Score...")
#Save score using file handling concept
file=open("score.txt","a")
file.write(name +":"+str(score)+"/5\n")
file.close()
print("Score saved successfully!")