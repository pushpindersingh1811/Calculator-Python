def t_c():
    print("""
    TEMPERATURE CONVERTER
    Functional Abbreviation Options Manual:-
    Celsius = "C"   Fahrenheit = "F"    Kelvin = "K"
    
    """)

    first_entry = float(input('Enter the Value> '))
    unit = input('unit> ').lower()
    converted_unit = input('to> ')
    if unit == 'c' and converted_unit == 'f':
        print(f'{first_entry} C =', (first_entry*1.8)+32, 'F')
    elif unit == 'c' and converted_unit == 'c':
        print(f'{first_entry} c =  {first_entry} c')
    elif unit == 'c' and converted_unit == 'k':
        print(f'{first_entry} C =', first_entry + 273.15, 'K')
    elif unit == 'f' and converted_unit == 'c':
        print(f'{first_entry} F =', (first_entry-32)*0.55, 'C')
    elif unit == 'f' and converted_unit == 'f':
        print(f'{first_entry} F =  {first_entry} F')
    elif unit == 'f' and converted_unit == 'K':
        print(f'{first_entry} F =', (first_entry-32)*0.55+273.15, 'K')
    elif unit == 'k' and converted_unit == 'c':
        print(f'{first_entry} K =', first_entry-273.15, 'C')
    elif unit == 'k' and converted_unit == 'f':
        print(f'{first_entry} K =', (first_entry-273.15)*1.8+32, 'F')
    elif unit == 'K' and converted_unit == 'K':
        print(f'{first_entry} K =  {first_entry} K')
    else:
        print('Use abbreviation options given above...')

