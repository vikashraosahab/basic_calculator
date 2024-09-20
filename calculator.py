""" CREATE
A PYTHON CALCULAT
"""
# PYTHON OKAY PYTHONG
# USING MATCH CASE AND USER DEFINED FUNCTIONS NAME AS CALCUATE WITH THREE PARAMETER NUM1,NUM2,OPERATOR
def calculate (val1,val2,operator):
    if operator not in ['+','-','/','*','**']:
        raise valueError ("Plesae enter valid input")

    if operator == '/':
        if val2 == 0:
            raise zeroDivisible ("Please not divide val / zero")
          
    match operator:
        case '+':
            return val1 + val2
        case '-':
            if va11 > val2:
                return val1-val2
            else:
                return val2 - val2
        case '*':
            return  val1 * val2
        case '/':
            return  val1 / val2
        case '**':
            return val1 ** val2

# INPUT BOTH NUMBERS
num1,num2 = map (int,input ("Enter value both values with space : ").split())
operator = input ("enter operator (+,-,/,*,**,// : ");
try:
    result = calculate (num1,num2,operator)
    print (f"result : {result}")
except valueError as a:
    print (a)
except zeroDivisible as e:
    print (e)
