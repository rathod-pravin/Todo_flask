i = 0
First_Value = 0
Second_Value = 1
result=[]
Number =int(input("enter number"))
while(i < Number+1):
           if(i <= 1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           result.append(Next)

           i = i + 1
print(sum(result))