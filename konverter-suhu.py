menu = """
Unit of Temperature :
| 1 | Celcius
| 2 | Fahrenheit
| 3 | Kelvin
"""

print("Welcome to Simple Converter App".center(80, "="))

while True: 
    print(menu)
    starting    = int(input("Starting Unit     [1/2/3] : "))
    destination = int(input("Destination Unit  [1/2/3] : "))
    temperature = float(input("Temperature      [ex: 30] : "))

    if (starting and destination) not in range(1,4):
        print("Input salah")
    else:
        if starting == 1:
            # 1. celcius ke fahrenheit
            # 2. celcius ke kelvin
            if destination == 2:
                result = ((temperature) * 9/5) + 32
            elif destination == 3:
                result = temperature + 273.15
        elif destination == 2:
            if destination == 1:
                result = ((temperature) - 32) * 5.9
            else:
                result = ((temperature) - 32) * 5/9 + 273.15
        else:
            if destination == 1:
                result = float(temperature) - 273.15
            else:
                result = (float(temperature) - 273.15) * 9/5 + 32

        print(f"Result : {result:.2f}")

    check = input("Convert again? [y or any key to quit]")
    if check == 'y':
        continue
    else:
        print("Thank you for using this app.".center(80, "="))
        break