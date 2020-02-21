import math


def calculator():
    print("""
    BASIC CALCULATOR
    Operator Functional Abbreviation Manual:- \n
    Addition: Press '+'    Subtraction: Press '-'    Multiplication: Press '*'    Division: Press '/'         
    Exponentiation: Press '^'    Reciprocal: Press 'r'   Sign Change: Press 'c'   Square Root: Press 's' 
    Finding Percentage: Press '%'    
    """)
    number_1 = float(input('Operand> '))
    operator = input('Operator> ').lower()
    if operator == 'c':
        print(f'Sign. Change: ', -1*number_1)
    elif operator == 'r':
        print(f'Reciprocal of {number_1}: ', 1/number_1)
    elif operator == 's':
        print(f'Square root of {number_1}: ', math.sqrt(number_1))
    else:
        number_2 = float(input('Operand> '))
        if operator == '+':
            print(f'Answer of Addition: ', number_1 + number_2)
        elif operator == '-':
            print(f'Answer of Subtraction: ', number_1 - number_2)
        elif operator == '*':
            print(f'Answer of Multiplication: ', number_1 * number_2)
        elif operator == '/':
            print(f'Answer of Division: ', number_1 / number_2)
        elif operator == '^':
            print(f'Answer of Exponentiation: ', number_1 ** number_2)
        elif operator == '%':
            print(f'Percentage Value: ', int((number_1/number_2)*100),'%')
        else:
            print('OPTION NOT AVAILABLE...')


