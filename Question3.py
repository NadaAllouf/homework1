
#python quiz program that takes a text file ("qa.txt")as input
#creat a text file (question_quiz) to use it as input for a python quiz program
def write_file(file_name,text):
    w=open(file_name,"w")
    text=[line+"\n" for line in text]
    w.writelines(text)
    w.close()

question_quiz=["Question1: How many days are in a week?; 7","Question2: How many letters are in the english alphabet?; 26", 
"Question3: How many colors are in the rainbow?; 7","Question4: How many days are in a year?; 365",
"Question5: How many hours are in a day?; 29","Question6: What is the capital of India?;Delhi",        
"Question7: How many continents are in the world?; 7","Question8: Which direction does the sun set in?;west",
"Question9: How many years are there in a millenium?; 1000","Question10: Which is the smallest continent?; Australia" ,
"Question11: What color are apples?; Red","Question12: What color are Bananas? ;yellow",
"Question13: What color are strawberies?;Red","Question14: What color is the cucumber?;Green",
"Question15: What is the capital of Syria?; damascus","Question16: What is the capital of Jordan?; amman" ,
"Question17: What is the capital of Lebanon?; beirut","Question18: What is the capital of Iraq? ;baghdad",
"Question19: What is the capital of Tunisia? ;tunisia","Question20: What is the capital of Qatar?;Doha"
]
write_file("qa.txt",question_quiz)

#python quiz program that takes a text file ("qa.txt")as input

def read_file(file_name):
    file1=open("qa.txt","r")
    l=[ line.rstrip().split(";")for line in file1]
    return l
    file1.close()
question_quiz=read_file("qa.txt")
print("welcom")
name=input("please enter your name: ")
ID=input("please enter your number: ")
#calculating the result
result=open("result.txt","w")
result.write(name+"\n")
result.write(ID+"\n")
result=open("result.txt","a")
marks=0
for i in range(0,20):
    y=input(question_quiz[i][0])
    if y==question_quiz[i][1]:
        marks+=1
        result.write("{}\n the answer:{}\n your answer is correct\n".format(question_quiz[i][0],question_quiz[i][1]))
    else: 
       result.write("{}\nyour answer is wrong,the right answer is: {}\n".format(question_quiz[i][0],question_quiz[i][1]))   
result.write("you scord {} marks".format(marks))
result.close()
print(open("result.txt","r").read())
result.close()

        

 
