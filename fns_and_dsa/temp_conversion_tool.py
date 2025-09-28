# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    # formula: (F - 32) * 5/9
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    # formula: (C * 9/5) + 32
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    temp_input = input("Enter the temperature to convert: ")
    
    # check if the input can be a number
    if not temp_input.replace(".", "", 1).isdigit() and not (temp_input.startswith("-") and temp_input[1:].replace(".", "", 1).isdigit()):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    temp = float(temp_input)
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
