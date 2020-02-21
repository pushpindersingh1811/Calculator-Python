from basic_calculator import calculator
from length_converter import l_c
from area_converter import a_c
from weight_converter import w_c
from temperature_converter import t_c

print("""
For 'BASIC CALCULATOR' = Press "b"
For 'LENGTH CONVERTER' = Press "l"
For 'AREA CONVERTER' = Press "a"
For 'WEIGHT CONVERTER' = Press "w"
For 'TEMPERATURE CONVERTER' = Press "t"

""")

option = input('Choice> ').lower()

if option == 'b':
    calculator()
elif option == 'l':
    l_c()
elif option == 'a':
    a_c()
elif option == 'w':
    w_c()
elif option == 't':
    t_c()
else:
    print('OPTION NOT AVAILABLE...')






