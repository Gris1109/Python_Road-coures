print ("----simple calculator----")
print ("let's add some numbers")
input1 = int(input("input your first value: "))
input2 = input("input your operator: ")
input3 = int(input("input your second value: "))

if input2 == '+':
 res = input1 + input3
 print (res)

elif input2 == '-':
 res = input1 - input3
 print (res)

elif input2 == '*':
 res = input1 * input3
 print (res)

elif input2 == '/':
 res = input1 / input3
 n = int(res)
 print (n)

else:
 print ("usage: the operator must be '+' or '-' or '*' or '/' ")

