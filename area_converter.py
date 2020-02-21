def a_c():
    print("""
    AREA CONVERTER
    Functional Abbreviation Options Manual:-\n
    Square Kilometre = "sqkm"    Square Metre = "sqm"    Square Mile = "sqmi"    Square Yard = "sqyd"
    Square Foot = "sqft"    Square Inch = "sqin"    Hectare = "hec"    Acre = "acr"
    """)

    first_entry = float(input('Enter the Value> '))
    unit = input('unit> ').lower()
    converted_unit = input('to> ')
    if unit == 'sqkm' and converted_unit == 'sqm':
        print(f'{first_entry} sq. km =', first_entry * (10**6), 'sq. m')
    elif unit == 'sqkm' and converted_unit == 'sqkm':
        print(f'{first_entry} sq. km =  {first_entry} sq. km')
    elif unit == 'sqkm' and converted_unit == 'sqmi':
        print(f'{first_entry} sq. km =', (first_entry / 2.59), 'sq. mile')
    elif unit == 'sqkm' and converted_unit == 'sqyd':
        print(f'{first_entry} sq. km =', first_entry * (1.196*(10**6)), 'sq. yard')
    elif unit == 'sqkm' and converted_unit == 'sqft':
        print(f'{first_entry} sq. km =', first_entry * (1.076*(10**7)), 'sq. ft')
    elif unit == 'sqkm' and converted_unit == 'sqin':
        print(f'{first_entry} sq. km =', first_entry * (1.55*(10**9)), 'sq. inch')
    elif unit == 'sqkm' and converted_unit == 'hec':
        print(f'{first_entry} sq. km =', first_entry * 100, 'hectare')
    elif unit == 'sqkm' and converted_unit == 'acr':
        print(f'{first_entry} sq. km =', first_entry * 247.105, 'acre')
    elif unit == 'sqm' and converted_unit == 'sqkm':
        print(f'{first_entry} sq. m =', first_entry / (10**6), 'sq. km')
    elif unit == 'sqm' and converted_unit == 'sqm':
        print(f'{first_entry} sq. m =  {first_entry} sq. m')
    elif unit == 'sqm' and converted_unit == 'sqmi':
        print(f'{first_entry} sq. m =', first_entry / (2.59*(10**6)), 'sq. mile')
    elif unit == 'sqm' and converted_unit == 'sqyd':
        print(f'{first_entry} sq. m =', first_entry * 1.196, 'sq. yard')
    elif unit == 'sqm' and converted_unit == 'sqft':
        print(f'{first_entry} sq. m =', first_entry * 10.764, 'sq. ft')
    elif unit == 'sqm' and converted_unit == 'sqin':
        print(f'{first_entry} sq. m =', first_entry * 1550.003, 'sq. inch')
    elif unit == 'sqm' and converted_unit == 'hec':
        print(f'{first_entry} sq. m =', first_entry / 10000, 'hectare')
    elif unit == 'sqm' and converted_unit == 'acr':
        print(f'{first_entry} sq. m =', first_entry / 4046.856, 'acre')
    elif unit == 'sqmi' and converted_unit == 'sqkm':
        print(f'{first_entry} sq. mile =', first_entry * 2.59, 'sq. km')
    elif unit == 'sqmi' and converted_unit == 'sqm':
        print(f'{first_entry} sq. mile =', first_entry * (2.59*(10**6)), 'sq. m')
    elif unit == 'sqmi' and converted_unit == 'sqmi':
        print(f'{first_entry} sq. mile =  {first_entry} sq. mile')
    elif unit == 'sqmi' and converted_unit == 'sqyd':
        print(f'{first_entry} sq. mile =', first_entry * (3.098*(10**6)), 'sq. yard')
    elif unit == 'sqmi' and converted_unit == 'sqft':
        print(f'{first_entry} sq. mile =', first_entry * (2.788*(10**7)), 'sq. ft')
    elif unit == 'sqmi' and converted_unit == 'sqin':
        print(f'{first_entry} sq. mile =', first_entry * (4.014*(10**9)), 'sq. inch')
    elif unit == 'sqmi' and converted_unit == 'hec':
        print(f'{first_entry} sq. mile =', first_entry * 258.99, 'hectare')
    elif unit == 'sqmi' and converted_unit == 'acr':
        print(f'{first_entry} sq. mile =', first_entry * 640, 'acre')
    elif unit == 'sqyd' and converted_unit == 'sqkm':
        print(f'{first_entry} sq. yard =', first_entry / (1.196*(10**6)), 'sq. km')
    elif unit == 'sqyd' and converted_unit == 'sqm':
        print(f'{first_entry} sq. yard =', first_entry / 1.196, 'sq. m')
    elif unit == 'sqyd' and converted_unit == 'sqmi':
        print(f'{first_entry} sq. yard =', first_entry / (3.098*(10**6)), 'sq. mile')
    elif unit == 'sqyd' and converted_unit == 'sqyd':
        print(f'{first_entry} sq. yard =  {first_entry} sq. yard')
    elif unit == 'sqyd' and converted_unit == 'sqft':
        print(f'{first_entry} sq. yard =', first_entry * 9, 'sq. ft')
    elif unit == 'sqyd' and converted_unit == 'sqin':
        print(f'{first_entry} sq. yard =', first_entry * 1296, 'sq. inch')
    elif unit == 'sqyd' and converted_unit == 'hec':
        print(f'{first_entry} sq. yard =', first_entry / 11959.9, 'hectare')
    elif unit == 'sqyd' and converted_unit == 'acr':
        print(f'{first_entry} sq. yard =', first_entry / 4890, 'acre')
    elif unit == 'sqft' and converted_unit == 'sqkm':
        print(f'{first_entry} sq. ft =', first_entry / (1.076*(10**7)), 'sq. km')
    elif unit == 'sqft' and converted_unit == 'sqm':
        print(f'{first_entry} sq. ft =', first_entry / 10.764, 'sq. m')
    elif unit == 'sqft' and converted_unit == 'sqmi':
        print(f'{first_entry} sq. ft =', first_entry / (2.788*(10**7)), 'sq. mile')
    elif unit == 'sqft' and converted_unit == 'sqyd':
        print(f'{first_entry} sq. ft =', first_entry / 9, 'sq. yard')
    elif unit == 'sqft' and converted_unit == 'sqft':
        print(f'{first_entry} sq. ft =  {first_entry} sq. ft')
    elif unit == 'sqft' and converted_unit == 'sqin':
        print(f'{first_entry} sq. ft =', first_entry * 144, 'sq. inch')
    elif unit == 'sqft' and converted_unit == 'hec':
        print(f'{first_entry} sq. ft =', first_entry / 107639.104, 'hectare')
    elif unit == 'sqft' and converted_unit == 'acr':
        print(f'{first_entry} sq. ft =', first_entry / 43560, 'acre')
    elif unit == 'sqin' and converted_unit == 'sqkm':
        print(f'{first_entry} sq. inch =', first_entry / (1.55*(10**9)), 'sq. km')
    elif unit == 'sqin' and converted_unit == 'sqm':
        print(f'{first_entry} sq. inch =', first_entry / 1550.003, 'sq. m')
    elif unit == 'sqin' and converted_unit == 'sqmi':
        print(f'{first_entry} sq. inch =', first_entry / (4.014*(10**9)), 'sq. mile')
    elif unit == 'sqin' and converted_unit == 'sqyd':
        print(f'{first_entry} sq. inch =', first_entry / 1296, 'sq. yard')
    elif unit == 'sqin' and converted_unit == 'sqft':
        print(f'{first_entry} sq. inch =', first_entry / 144, 'sq. ft')
    elif unit == 'sqin' and converted_unit == 'sqin':
        print(f'{first_entry} sq. inch =  {first_entry} sq. inch')
    elif unit == 'sqin' and converted_unit == 'hec':
        print(f'{first_entry} sq. inch =', first_entry / (1.55*(10**7)), 'hectare')
    elif unit == 'sqin' and converted_unit == 'acr':
        print(f'{first_entry} sq. inch =', first_entry / (6.273*(10**6)), 'acre')
    elif unit == 'hec' and converted_unit == 'sqkm':
        print(f'{first_entry} hectare =', first_entry / 100, 'sq. km')
    elif unit == 'hec' and converted_unit == 'sqm':
        print(f'{first_entry} hectare =', first_entry / 10000, 'sq. m')
    elif unit == 'hec' and converted_unit == 'sqmi':
        print(f'{first_entry} hectare =', first_entry / 258.99, 'sq. mile')
    elif unit == 'hec' and converted_unit == 'sqyd':
        print(f'{first_entry} hectare =', first_entry * 11959.9, 'sq. yard')
    elif unit == 'hec' and converted_unit == 'sqft':
        print(f'{first_entry} hectare =', first_entry * 107639.104, 'sq. ft')
    elif unit == 'hec' and converted_unit == 'sqin':
        print(f'{first_entry} hectare =', first_entry * (1.55*(10**7)), 'sq. inch')
    elif unit == 'hec' and converted_unit == 'hec':
        print(f'{first_entry} hectare =  {first_entry} hectare')
    elif unit == 'hec' and converted_unit == 'acr':
        print(f'{first_entry} hectare =', first_entry * 2.471, 'acre')
    elif unit == 'acr' and converted_unit == 'sqkm':
        print(f'{first_entry} acre =', first_entry / 247.105, 'sq. km')
    elif unit == 'acr' and converted_unit == 'sqm':
        print(f'{first_entry} acre =', first_entry * 4046.856, 'sq. m')
    elif unit == 'acr' and converted_unit == 'sqmi':
        print(f'{first_entry} acre =', first_entry / 640, 'sq. mile')
    elif unit == 'acr' and converted_unit == 'sqyd':
        print(f'{first_entry} acre =', first_entry * 4840, 'sq. yard')
    elif unit == 'acr' and converted_unit == 'sqft':
        print(f'{first_entry} acre =', first_entry * 43560, 'sq. ft')
    elif unit == 'acr' and converted_unit == 'sqin':
        print(f'{first_entry} acre =', first_entry * (6.273*(10**6)), 'sq. inch')
    elif unit == 'acr' and converted_unit == 'hec':
        print(f'{first_entry} acre =', first_entry / 2.471, 'hectare')
    elif unit == 'acr' and converted_unit == 'acr':
        print(f'{first_entry} acre =  {first_entry} acre')
    else:
        print('Use abbreviation given in options above...')













