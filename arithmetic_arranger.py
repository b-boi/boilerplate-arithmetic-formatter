import re
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(problems):

    if len(problems) > 5:
        return f"Error: Too many problems."
    else:
        elements = " ".join([str(x) for x in problems])
        split_string = re.split("[\s]",elements)
        split_num = len(split_string)
        num1 = split_string[0:12:3]
        num2 = split_string[2:12:3]
        operand = split_string[1]
        operand_list = split_string[1:12:3]
        print(num1)
        print(num2)
        #print(operand)
        print(operand_list)
        print(split_num)
        
    if elements in "/" "*":
        return f"Error: Operator must be '+' or '-'"
    else:
        arranged_problems = []
        #print(type(arranged_problems))
        for i in problems:
            #num1 = problems[0]
            #num2 = i[2]
            #operand = i[1]
            #print(i)
        #num1 = i[0]
        #print(num1)
            return arranged_problems


arithmetic_arranger(problems)
