my_list = ["Nada","Halla","Rahaf","Ali","Hassan"]
name=input("Enter your name: ")
i=0
for my_list[i] in my_list:
    if name==my_list[i]:
        print("the user is graduated")
        break
    else:
        print("the user is not graduated")
    i=i+1
        
