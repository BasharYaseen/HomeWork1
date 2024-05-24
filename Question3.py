#(Homework) Question 3
#First we create text file with the (20,Qestion and answer)
import json
questions = { }
#variable for the score
scores = 0
#question number
number=1
#loading exam question to the program
f = open("exam.txt",'r')
exam = json.load(f)
f.close()
print("Enter t for True or f for False only !!!!!")
#display the questions for the user
for ques in exam.keys():
    print("Question",number,": ", ques)
    ans = input("The answer is ")
    #testing the input result if true or false
    if ans.upper() == exam[ques].upper():
        scores = scores + 1
        print("Correct ")
    else:
        print ("Wrong")
    number = number + 1
#the score result in a separete file
result={name:scores}
z = open("result.txt",'w')
result = json.dump(result,z)
z.close()