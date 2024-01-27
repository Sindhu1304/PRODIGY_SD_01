def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def convert_temperature(value, unit):
    unit = unit.lower()
    if unit == 'celsius':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return fahrenheit, kelvin
    elif unit == 'fahrenheit':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return celsius, kelvin
    elif unit == 'kelvin':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return celsius, fahrenheit
    else:
        raise ValueError("Unknown temperature unit. Please use Celsius, Fahrenheit, or Kelvin.")


def main():
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ")


    try:
        converted_values = convert_temperature(value, unit)
        if unit.lower() == 'celsius':
            print(f"{value} degrees Celsius is {converted_values[0]} degrees Fahrenheit and {converted_values[1]} Kelvin")
        elif unit.lower() == 'fahrenheit':
            print(f"{value} degrees Fahrenheit is {converted_values[0]} degrees Celsius and {converted_values[1]} Kelvin")
        elif unit.lower() == 'kelvin':
            print(f"{value} Kelvin is {converted_values[0]} degrees Celsius and {converted_values[1]} degrees Fahrenheit")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

