def l_c():
    print("""
    LENGTH CONVERTER    
    Functional Manual:- \n
    Kilometre(km)    Metre(m)    Centimetre(cm)    Millimetre(mm)
    Micrometre(um)     Nanometre(nm)    Mile(mi)    Yard(yd)
    Foot(ft)    Inch(in) 
      """)

    first_entry = float(input('From> '))
    unit = input('unit> ').lower()
    converted_unit = input('to> ')
    if unit == ('km' or 'kilometre' or 'kilo') and converted_unit == ('m' or 'metre'):
        print(f'{first_entry}km =', first_entry*1000, 'm')
    elif unit == ('km' or 'kilometre' or 'kilo') and converted_unit == ('cm' or 'centimetre' or 'centi'):
        print(f'{first_entry}km =', first_entry*(10**5), 'cm')
    elif unit == ('km' or 'kilometre' or 'kilo') and converted_unit == ('mm' or 'millimetre' or 'milli'):
        print(f'{first_entry}km =', first_entry * (10**6), 'mm')
    elif unit == ('km' or 'kilometre' or 'kilo') and converted_unit == ('um' or 'micrometre' or 'micro'):
        print(f'{first_entry}km =', first_entry * (10**9), 'um')
    elif unit == ('km' or 'kilometre' or 'kilo') and converted_unit == ('nm' or 'nanometre' or 'nano'):
        print(f'{first_entry}km =', first_entry * (10**12), 'nm')
    elif unit == ('km' or 'kilometre' or 'kilo') and converted_unit == ('mi' or 'miles'):
        print(f'{first_entry}km =', (first_entry / 1.609), 'miles')
    elif unit == ('km' or 'kilometre' or 'kilo') and converted_unit == ('yd' or 'yard'):
        print(f'{first_entry}km =', first_entry*1093.61, 'yard')
    elif unit == ('km' or 'kilometre' or 'kilo') and converted_unit == ('ft' or 'foot'):
        print(f'{first_entry}km =', first_entry*3280.84, 'ft')
    elif unit == ('km' or 'kilometre' or 'kilo') and converted_unit == ('in' or 'inch'):
        print(f'{first_entry}km =', first_entry*39370.1, 'inch')