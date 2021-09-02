

def arithmetic_arranger(problems):

    if len(problems) > 5:
        return f"Error: Too many problems."
    else:
        elements = " ".join([str(x) for x in problems])
        print(elements)
        if elements in "/" "*":
            return f"Error: Operator must be '+' or '-'"
        else:
            arranged_problems = problems
        #print(type(arranged_problems))

        for i in problems:
            #num1 = problems[0]
            #num2 = i[2]
            #operand = i[1]
            #print(i)
        #num1 = i[0]
        #print(num1)
    

    return arranged_problems


#arithmetic_arranger()

#["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]