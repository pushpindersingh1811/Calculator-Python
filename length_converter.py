def l_c():
    print("""
    LENGTH CONVERTER    
    Functional Abbreviation Options Manual:- \n
    Kilometre= "km"    Metre= "m"    Centimetre= "cm"    Millimetre= "mm"
    Micrometre(um)     Nanometre(nm)    Mile= "mi"    Yard= "yd"
    Foot= "ft"    Inch = "in" 
      """)

    first_entry = float(input('Enter the Value> '))
    unit = input('unit> ').lower()
    converted_unit = input('to> ')
    if unit == 'km' and converted_unit == 'm':
        print(f'{first_entry} km =', first_entry*1000, 'm')
    elif unit == 'km' and converted_unit == 'km':
        print(f'{first_entry} km =  {first_entry} km')
    elif unit == 'km' and converted_unit == 'cm':
        print(f'{first_entry} km =', first_entry*(10**5), 'cm')
    elif unit == 'km' and converted_unit == 'mm':
        print(f'{first_entry} km =', first_entry * (10**6), 'mm')
    elif unit == 'km' and converted_unit == 'um':
        print(f'{first_entry} km =', first_entry * (10**9), 'um')
    elif unit == 'km' and converted_unit == 'nm':
        print(f'{first_entry} km =', first_entry * (10**12), 'nm')
    elif unit == 'km' and converted_unit == 'mi':
        print(f'{first_entry} km =', (first_entry / 1.609), 'miles')
    elif unit == 'km' and converted_unit == 'yd':
        print(f'{first_entry} km =', first_entry*1093.61, 'yard')
    elif unit == 'km' and converted_unit == 'ft':
        print(f'{first_entry} km =', first_entry*3280.84, 'ft')
    elif unit == 'km' and converted_unit == 'in':
        print(f'{first_entry} km =', first_entry*39370.1, 'inch')
    elif unit == 'm' and converted_unit == 'km':
        print(f'{first_entry} m =', first_entry/1000, 'km')
    elif unit == 'm' and converted_unit == 'm':
        print(f'{first_entry} m = {first_entry} m')
    elif unit == 'm' and converted_unit == 'cm':
        print(f'{first_entry}m =', first_entry*100, 'cm')
    elif unit == 'm' and converted_unit == 'mm':
        print(f'{first_entry}m =', first_entry * 1000, 'mm')
    elif unit == 'm' and converted_unit == 'um':
        print(f'{first_entry}m =', first_entry * (10**6), 'um')
    elif unit == 'm' and converted_unit == 'nm':
        print(f'{first_entry}m =', first_entry * (10 ** 9), 'nm')
    elif unit == 'm' and converted_unit == 'mi':
        print(f'{first_entry}m =', first_entry/1609.344, 'mile')
    elif unit == 'm' and converted_unit == 'yd':
        print(f'{first_entry}m =', first_entry * 1.094, 'yard')
    elif unit == 'm'and converted_unit == 'ft':
        print(f'{first_entry}m =', first_entry * 3.281, 'ft')
    elif unit == 'm' and converted_unit == 'in':
        print(f'{first_entry}m =', first_entry * 39.37, 'inch')
    elif unit == 'cm' and converted_unit == 'km':
        print(f'{first_entry}cm =', first_entry / 100000, 'km')
    elif unit == 'cm' and converted_unit == 'm':
        print(f'{first_entry}cm =', first_entry/100, 'm')
    elif unit == 'cm' and converted_unit == 'cm':
        print(f'{first_entry} cm = {first_entry} cm')
    elif unit == 'cm' and converted_unit == 'mm':
        print(f'{first_entry}cm =', first_entry * 10, 'mm')
    elif unit == 'cm' and converted_unit == 'um':
        print(f'{first_entry}cm =', first_entry * 10000, 'um')
    elif unit == 'cm' and converted_unit == 'nm':
        print(f'{first_entry}cm =', first_entry * (10 ** 7), 'nm')
    elif unit == 'cm' and converted_unit == 'mi':
        print(f'{first_entry}cm =', first_entry / 160934.4, 'mile')
    elif unit == 'cm' and converted_unit == 'yd':
        print(f'{first_entry}cm =', first_entry / 91.44, 'yard')
    elif unit == 'cm' and converted_unit == 'ft':
        print(f'{first_entry}cm =', first_entry / 30.48, 'ft')
    elif unit == 'cm' and converted_unit == 'in':
        print(f'{first_entry}cm =', first_entry / 2.54, 'inch')
    elif unit == 'mm' and converted_unit == 'km':
        print(f'{first_entry}mm =', first_entry / 1000000, 'km')
    elif unit == 'mm' and converted_unit == 'm':
        print(f'{first_entry}mm =', first_entry / 1000, 'm')
    elif unit == 'mm' and converted_unit == 'cm':
        print(f'{first_entry}mm =', first_entry / 10, 'cm')
    elif unit == 'mm' and converted_unit == 'mm':
        print(f'{first_entry} mm = {first_entry} mm')
    elif unit == 'mm' and converted_unit == 'um':
        print(f'{first_entry}mm =', first_entry * 1000, 'um')
    elif unit == 'mm' and converted_unit == 'nm':
        print(f'{first_entry}mm =', first_entry * (10 ** 6), 'nm')
    elif unit == 'mm' and converted_unit == 'mi':
        print(f'{first_entry}mm =', first_entry / 1.609*(10**6), 'mile')
    elif unit == 'mm' and converted_unit == 'yd':
        print(f'{first_entry}mm =', first_entry / 914.4, 'yard')
    elif unit == 'mm' and converted_unit == 'ft':
        print(f'{first_entry}mm =', first_entry / 304.8, 'ft')
    elif unit == 'mm' and converted_unit == 'in':
        print(f'{first_entry}mm =', first_entry / 25.4, 'inch')
    elif unit == 'um' and converted_unit == 'km':
        print(f'{first_entry}um =', first_entry / (10**9), 'km')
    elif unit == 'um' and converted_unit == 'm':
        print(f'{first_entry}um =', first_entry / (10**6), 'm')
    elif unit == 'um' and converted_unit == 'cm':
        print(f'{first_entry}um =', first_entry / (10**4), 'cm')
    elif unit == 'um' and converted_unit == 'mm':
        print(f'{first_entry}um =', first_entry / 1000, 'mm')
    elif unit == 'um' and converted_unit == 'um':
        print(f'{first_entry} um = {first_entry} um')
    elif unit == 'um' and converted_unit == 'nm':
        print(f'{first_entry}um =', first_entry * 1000, 'nm')
    elif unit == 'um' and converted_unit == 'mi':
        print(f'{first_entry}um =', first_entry / 1.609*(10**9), 'mile')
    elif unit == 'um' and converted_unit == 'yd':
        print(f'{first_entry}um =', first_entry / 914400, 'yard')
    elif unit == 'um' and converted_unit == 'ft':
        print(f'{first_entry}um =', first_entry / 304800, 'ft')
    elif unit == 'um' and converted_unit == 'in':
        print(f'{first_entry}um =', first_entry / 25400, 'inch')
    elif unit == 'nm' and converted_unit == 'km':
        print(f'{first_entry}nm =', first_entry / (10**12), 'km')
    elif unit == 'nm' and converted_unit == 'm':
        print(f'{first_entry}nm =', first_entry / (10**9), 'm')
    elif unit == 'nm' and converted_unit == 'cm':
        print(f'{first_entry}nm =', first_entry / (10**7), 'cm')
    elif unit == 'nm' and converted_unit == 'mm':
        print(f'{first_entry}nm =', first_entry / (10**6), 'mm')
    elif unit == 'nm' and converted_unit == 'um':
        print(f'{first_entry}nm =', first_entry / 1000, 'um')
    elif unit == 'nm' and converted_unit == 'nm':
        print(f'{first_entry} nm = {first_entry} nm')
    elif unit == 'nm' and converted_unit == 'mi':
        print(f'{first_entry}nm =', first_entry / 1.609*(10**12), 'mile')
    elif unit == 'nm' and converted_unit == 'yd':
        print(f'{first_entry}nm =', first_entry / 9.144*(10**8), 'yard')
    elif unit == 'nm' and converted_unit == 'ft':
        print(f'{first_entry}nm =', first_entry / 3.048*(10**8), 'ft')
    elif unit == 'nm' and converted_unit == 'in':
        print(f'{first_entry}nm =', first_entry / 2.54*(10**7), 'inch')
    elif unit == 'mi' and converted_unit == 'km':
        print(f'{first_entry} miles =', first_entry * 1.609, 'km')
    elif unit == 'mi' and converted_unit == 'm':
        print(f'{first_entry} miles =', first_entry * 1609.34, 'm')
    elif unit == 'mi' and converted_unit == 'cm':
        print(f'{first_entry} miles =', first_entry * 160934.4, 'cm')
    elif unit == 'mi' and converted_unit == 'mm':
        print(f'{first_entry} miles =', first_entry * 1.609*(10**6), 'mm')
    elif unit == 'mi' and converted_unit == 'um':
        print(f'{first_entry} miles =', first_entry * 1.609*(10**9), 'um')
    elif unit == 'mi' and converted_unit == 'nm':
        print(f'{first_entry} miles =', first_entry * 1.609*(10**12), 'nm')
    elif unit == 'mi' and converted_unit == 'mi':
        print(f'{first_entry} mile = {first_entry} mile')
    elif unit == 'mi' and converted_unit == 'yd':
        print(f'{first_entry} miles =', first_entry * 1760, 'yard')
    elif unit == 'mi' and converted_unit == 'ft':
        print(f'{first_entry} miles =', first_entry * 5280, 'ft')
    elif unit == 'mi' and converted_unit == 'in':
        print(f'{first_entry} miles =', first_entry * 63360, 'inch')
    elif unit == 'yd' and converted_unit == 'km':
        print(f'{first_entry} yard =', first_entry / 1093.613, 'km')
    elif unit == 'yd' and converted_unit == 'm':
        print(f'{first_entry} yard =', first_entry / 1.094, 'm')
    elif unit == 'yd' and converted_unit == 'cm':
        print(f'{first_entry} yard =', first_entry * 91.44, 'cm')
    elif unit == 'yd' and converted_unit == 'mm':
        print(f'{first_entry} yard =', first_entry * 914.4, 'mm')
    elif unit == 'yd' and converted_unit == 'um':
        print(f'{first_entry} yard =', first_entry * 914400, 'um')
    elif unit == 'yd' and converted_unit == 'nm':
        print(f'{first_entry} yard =', first_entry * 9.144*(10**8), 'nm')
    elif unit == 'yd' and converted_unit == 'mile':
        print(f'{first_entry} yard =', first_entry / 1760, 'mile')
    elif unit == 'yd' and converted_unit == 'yd':
        print(f'{first_entry} yard = {first_entry} yard')
    elif unit == 'yd' and converted_unit == 'ft':
        print(f'{first_entry} yard =', first_entry * 3, 'ft')
    elif unit == 'yd' and converted_unit == 'in':
        print(f'{first_entry} yard =', first_entry * 36, 'inch')
    elif unit == 'ft' and converted_unit == 'km':
        print(f'{first_entry} ft =', first_entry / 3280.84, 'km')
    elif unit == 'ft' and converted_unit == 'm':
        print(f'{first_entry} ft =', first_entry / 3.281, 'm')
    elif unit == 'ft' and converted_unit == 'cm':
        print(f'{first_entry} ft =', first_entry * 30.48, 'cm')
    elif unit == 'ft' and converted_unit == 'mm':
        print(f'{first_entry} ft =', first_entry * 304.8, 'mm')
    elif unit == 'ft' and converted_unit == 'um':
        print(f'{first_entry} ft =', first_entry * 304800, 'um')
    elif unit == 'ft' and converted_unit == 'nm':
        print(f'{first_entry} ft =', first_entry * (3.048*(10**8)), 'nm')
    elif unit == 'ft' and converted_unit == 'mi':
        print(f'{first_entry} ft =', first_entry / 5280, 'mile')
    elif unit == 'ft' and converted_unit == 'yd':
        print(f'{first_entry} ft =', first_entry / 3, 'yard')
    elif unit == 'ft' and converted_unit == 'ft':
        print(f'{first_entry} ft = {first_entry} ft')
    elif unit == 'ft' and converted_unit == 'in':
        print(f'{first_entry} ft =', first_entry * 12, 'inch')
    elif unit == 'in' and converted_unit == 'km':
        print(f'{first_entry} inch =', first_entry / 39370.079, 'km')
    elif unit == 'in' and converted_unit == 'm':
        print(f'{first_entry} inch =', first_entry / 39.37, 'm')
    elif unit == 'in' and converted_unit == 'cm':
        print(f'{first_entry} inch =', first_entry * 2.54, 'cm')
    elif unit == 'in' and converted_unit == 'mm':
        print(f'{first_entry} inch =', first_entry * 25.4, 'mm')
    elif unit == 'in' and converted_unit == 'um':
        print(f'{first_entry} inch =', first_entry * 25400, 'um')
    elif unit == 'in' and converted_unit == 'nm':
        print(f'{first_entry} inch =', first_entry * (2.54*(10**7)), 'nm')
    elif unit == 'in' and converted_unit == 'mi':
        print(f'{first_entry} inch =', first_entry / 63360, 'mile')
    elif unit == 'in' and converted_unit == 'yd':
        print(f'{first_entry} inch =', first_entry / 36, 'yard')
    elif unit == 'in' and converted_unit == 'ft':
        print(f'{first_entry} inch =', first_entry / 12, 'ft')
    elif unit == 'in' and converted_unit == 'in':
        print(f'{first_entry} inch = {first_entry} inch')
    else:
        print('Use abbreviation given in options above....')










