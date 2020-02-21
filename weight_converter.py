def w_c():
    print("""
    WEIGHT CONVERTER
    Functional Abbreviation Options Manual:-\n
    Tonne = "t"    Kilogram = "kg"   gram = "g" 
    Milligram = "mg"    Pound = "lbs"    Ounce = "oz"
    
    """)

    first_entry = float(input('Enter the Value> '))
    unit = input('unit> ').lower()
    converted_unit = input('to> ')
    if unit == 't' and converted_unit == 'kg':
        print(f'{first_entry} t =', first_entry * 1000, 'kg')
    elif unit == 't' and converted_unit == 't':
        print(f'{first_entry} t =  {first_entry} t')
    elif unit == 't' and converted_unit == 'g':
        print(f'{first_entry} t =', first_entry * (10**6), 'g')
    elif unit == 't' and converted_unit == 'mg':
        print(f'{first_entry} t =', first_entry * (10**9), 'mg')
    elif unit == 't' and converted_unit == 'lbs':
        print(f'{first_entry} t =', first_entry * 2204.623, 'lbs')
    elif unit == 't' and converted_unit == 'oz':
        print(f'{first_entry} t =', first_entry * 35273.962, 'oz')
    elif unit == 'kg' and converted_unit == 't':
        print(f'{first_entry} kg =', first_entry / 1000, 't')
    elif unit == 'kg' and converted_unit == 'kg':
        print(f'{first_entry} kg =  {first_entry} kg')
    elif unit == 'kg' and converted_unit == 'g':
        print(f'{first_entry} kg =', first_entry * 1000, 'g')
    elif unit == 'kg' and converted_unit == 'mg':
        print(f'{first_entry} kg =', first_entry * (10**6), 'mg')
    elif unit == 'kg' and converted_unit == 'lbs':
        print(f'{first_entry} kg =', first_entry * 2.205, 'lbs')
    elif unit == 'kg' and converted_unit == 'oz':
        print(f'{first_entry} kg =', first_entry * 35.274, 'oz')
    elif unit == 'g' and converted_unit == 't':
        print(f'{first_entry} g =', first_entry / (10**6), 't')
    elif unit == 'g' and converted_unit == 'kg':
        print(f'{first_entry} g =', first_entry / 1000, 'kg')
    elif unit == 'g' and converted_unit == 'g':
        print(f'{first_entry} g =  {first_entry} g')
    elif unit == 'g' and converted_unit == 'mg':
        print(f'{first_entry} g =', first_entry * 1000, 'mg')
    elif unit == 'g' and converted_unit == 'lbs':
        print(f'{first_entry} g =', first_entry / 453.592, 'lbs')
    elif unit == 'g' and converted_unit == 'oz':
        print(f'{first_entry} g =', first_entry / 28.35, 'oz')
    elif unit == 'mg' and converted_unit == 't':
        print(f'{first_entry} mg =', first_entry / (10**9), 't')
    elif unit == 'mg' and converted_unit == 'kg':
        print(f'{first_entry} mg =', first_entry / (10**6), 'kg')
    elif unit == 'mg' and converted_unit == 'g':
        print(f'{first_entry} mg =', first_entry / 1000, 'g')
    elif unit == 'mg' and converted_unit == 'mg':
        print(f'{first_entry} mg =  {first_entry} mg')
    elif unit == 'mg' and converted_unit == 'lbs':
        print(f'{first_entry} mg =', first_entry / 453592.37, 'lbs')
    elif unit == 'mg' and converted_unit == 'oz':
        print(f'{first_entry} mg =', first_entry / 28349.523, 'oz')
    elif unit == 'lbs' and converted_unit == 't':
        print(f'{first_entry} lbs =', first_entry / 2204.623, 't')
    elif unit == 'lbs' and converted_unit == 'kg':
        print(f'{first_entry} lbs =', first_entry / 2.205, 'kg')
    elif unit == 'lbs' and converted_unit == 'g':
        print(f'{first_entry} lbs =', first_entry * 453.592, 'g')
    elif unit == 'lbs' and converted_unit == 'mg':
        print(f'{first_entry} lbs =', first_entry * 453592.37, 'mg')
    elif unit == 'lbs' and converted_unit == 'lbs':
        print(f'{first_entry} lbs =  {first_entry} lbs')
    elif unit == 'lbs' and converted_unit == 'oz':
        print(f'{first_entry} lbs =', first_entry * 16, 'oz')
    elif unit == 'oz' and converted_unit == 't':
        print(f'{first_entry} oz =', first_entry / 35273.962, 't')
    elif unit == 'oz' and converted_unit == 'kg':
        print(f'{first_entry} oz =', first_entry / 35.274, 'kg')
    elif unit == 'oz' and converted_unit == 'g':
        print(f'{first_entry} oz =', first_entry * 28.35, 'g')
    elif unit == 'oz' and converted_unit == 'mg':
        print(f'{first_entry} oz =', first_entry * 28349.523, 'mg')
    elif unit == 'oz' and converted_unit == 'lbs':
        print(f'{first_entry} oz =', first_entry / 16, 'lbs')
    elif unit == 'oz' and converted_unit == 'oz':
        print(f'{first_entry} oz =  {first_entry} oz')
    else:
        print('Use abbreviation options given above...')








