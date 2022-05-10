decimal = int(input("Enter a decimal number : "))
binary = 0
i= 0
temp = decimal
list_binary=[]
while(temp > 0):
    binary =((temp%2)*(10**i)) + binary
    t1=temp%2
    temp = int(temp//2)
    i += 1
print("Binary of {x} is : {y}".format(x=decimal,y=binary))
list_binary.append(t1)
print(list_binary)
list_binary.reverse()
print(list_binary)

