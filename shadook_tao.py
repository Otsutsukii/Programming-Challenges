import sys
####################################################################
# dictionary for converting digit to shadook word and shadook to digit
base1 = {0:"Ga",1:"Bu",2:"Zo",3:"Meu"}
base2 = {"Ga":0,"Bu":1,"Zo":2,"Meu":3}

####################################################################
# function to convert a number in a base to a number in another base 

def convert_to_base(i,b):
    result = []
    while i > 0:
            result.insert(0, i % b)
            i = i // b
    return result
####################################################################
# function to process each word from shadook 
# if a digit or operator return it 
# otherwise convert the number from base 4 to 10 because it is a shadook word
# return a int or a str of operator
def process(number):
    if number in ["-","+","*","/"]:
        return number

    if number.isdigit():
        return int(number)
    else:
        if len(number) > 2:
            res = 0
            digits = number.split("-")
            l = len(digits)
            for i in range(len(digits)):
                res += base2[digits[i]]*(10**(l-1))
                l-=1
            return int(str(res),4)
        else:
            return int(str(base2[number]),4)
########################################################################################################################################
# function for evaluating the expression , it takes as input a list of string for example ["2","Meu",+]
# return a int in base 10

# the algorithm iterate the list of expression , and try to add to the stack if it is a number 
# otherwise if we encounter one of the operators + , - , / , * 
# we try to evaluate the expression by taking the last two numbers in the stack  
# at the end return the only element in the stack
def eval2(expression):
    stack = []
    operators = {'+':lambda x, y: x+y, '-':lambda x, y: x-y, '*':lambda x, y: x*y, '/':lambda x, y: x/y}
    for s in expression:
        try:
            stack.append(float(s))
        except:
            stack.append(int(operators[s](stack.pop(-2),stack.pop(-1))))
    return int(stack[-1])



if __name__ == "__main__":

    #getting input and the main loop for solving the problem 
    data = [d.rstrip().split()[:-1] for d in sys.stdin.readlines()]

    # processing the input , by converting each shadook word to base 10 number 
    # then convert each number , each converted shadook word to str 
    for i in range(1,len(data)):
        for j in range(len(data[i])):
            data[i][j] = str(process(data[i][j]))

    # for each expression , if it is a single number or a single shadook word , print the word 
    # otherwise evaluate the expression and convert it to shadoop word
    for d in data[1:]:
        if len(d) > 1 :
            res = eval2(d) # evaluate the expression 
            # corner case for my convert_to_base algorithm , when the result is 0 , i print("Ga")
            # because otherwise my convert_to_base function return a empty list 
            if res == 0:
                print("Ga")
            else:
                tmp = map(str,convert_to_base(res,4)) #convert the number from base 10 to base 4
                print("-".join([str(base1[int(l)]) for l in tmp])) # transform the number in base 4 to shadook word
        else:
            tmp = "".join(d) 
            # corner case for my convert_to_base algorithm , when the result is 0 print("Ga")
            # because otherwise my convert_to_base function return a empty list 
            if tmp == "0":
                print("Ga")
            else:
                tmp = convert_to_base(int(tmp),4) #convert the number from base 10 to base 4
                print("-".join([str(base1[int(l)]) for l in tmp]))  # transform the number in base 4 to shadook word