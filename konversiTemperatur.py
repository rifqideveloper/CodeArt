print('\n===program konveksi TEMPERATUR===\n')
print('        cersius(1)')
print('        reamur(2)')
print('        fahrenheit(3)')
print('        kelvin(4)')


def temperatur_Cersius():
    CERSIUS = float(input('masukan suhu dalam CERSIUS: '))
    print('suhu adalah', CERSIUS, 'CERSIUS')
    REAMUR = (4 / 5) * CERSIUS
    print('suhu adalah REAMUR       :', REAMUR)
    print('rumus:', '(4/5)*CERSIUS')
    FAHRENHEIT = ((9 / 5) * CERSIUS) + 32
    print('suhu adalah FAHRENHEAIT  :', FAHRENHEIT)
    print('rumus:', '((9/5)*CERSIUS) + 32')
    KELVIN = CERSIUS + 273
    print('suhu adalah KELVIN       :', KELVIN)
    print('rumus:', 'CERSIUS + 273')
    return


def temperatur_Reamur():
    REAMUR = float(input('masukan suhu dalam REAMUR: '))
    print('suhu adalah', REAMUR, 'REAMUR')
    CERSIUS = (5 / 4) * REAMUR
    print('suhu adalah CERSIUS      :', CERSIUS)
    print('rumus:', '(5/4)*REAMUR')
    FAHRENHEIT = ((9 / 4) * REAMUR) + 32
    print('suhu adalah FAHRENHEAIT  :', FAHRENHEIT)
    print('rumus:', '((9/4)*REAMUR)+32')
    KELVIN = ((5 / 4) * REAMUR) + 273
    print('suhu adalah KELVIN       :', KELVIN)
    print('rumus:', '((5/4)*REAMUR) + 273')
    return


def temperatur_Fahrenheit():
    FAHRENHEIT = float(input('masukan suhu dalam FAHRENHEIT: '))
    print('suhu adalah', FAHRENHEIT, 'FAHRENHEIT')
    CERSIUS = (FAHRENHEIT - 32) * 5 / 9
    print('suhu adalah CERSIUS      :', CERSIUS)
    print('rumus:', '(FAHRENHEIT - 32) * 5/9')
    REAMUR = (4 / 9) * FAHRENHEIT - 32
    print('suhu adalah REAMUR       :', REAMUR)
    print('rumus:', '(4/9)*FAHRENHEIT - 32')
    KELVIN = (FAHRENHEIT - 32) * 5 / 9 + 273.15
    print('suhu adalah KELVIN       :', KELVIN)
    print('rumus:', '(FAHRENHEIT - 32) * 5/9 + 273.15')
    return


def temperatur_Kelvin():
    KELVIN = float(input('masukan suhu dalam KELVIN: '))
    print('suhu adalah', KELVIN, 'KELVIN')
    CERSIUS = KELVIN - 273.15
    print('suhu adalah CERSIUS      :', CERSIUS)
    print('rumus:', 'KELVIN - 273.15')
    REAMUR = 4 / 5 * (KELVIN - 273)
    print('suhu adalah REAMUR       :', REAMUR)
    print('rumus:', '4/5*(KELVIN-273)')
    FAHRENHEIT = (KELVIN - 273.15) - 9 / 5 + 32
    print('suhu adalah FAHRENHEIT   :', FAHRENHEIT)
    print('rumus:', '(KELVIN - 273.15) - 9/5 + 32')
    return


def temperatur():
    x = input('Masukan nama suhu: ')
    if x == 1 or x == "(1)" or x.lower() == "c" or x.lower() == "cersius" or x.lower() == "cersius(1)":
        print(temperatur_Cersius())
    elif x == 2 or x == "(2)" or x.lower() == "r" or x.lower() == "reamur" or x.lower() == "reamur(2)":
        print(temperatur_Reamur())
    elif x == 3 or x == "(3)" or x.lower() == "f" or x.lower() == "fahrenheit" or x.lower() == "fahrenheit(3)":
        print(temperatur_Fahrenheit())
    elif x == 4 or x == "(4)" or x.lower() == "k" or x.lower() == "kelvin" or x.lower() == "kelvin(3)":
        print(temperatur_Kelvin())
    return


temperatur()
