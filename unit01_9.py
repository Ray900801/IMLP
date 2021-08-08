analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
x=input("input a sentence:")
y=x.lower()
list_0=[]
for i in y:
    list_0.append(i)

fixed_string="".join(i for i in list_0 if i not in analphabeticList)    


reversedList = fixed_string[::-1] 

if fixed_string==reversedList: 
    print("The text you have entered is a palindrome!")
else: 
    print("The text you have entered is not a palindrome.")        
