# Python Program - Convert Celsius to Fahrenheit

print("Enter 'x' for exit.");
cel = input("Enter Temperature in Celsius: ");
if cel == 'x':
    exit();
else:
    celsius = float(cel);
    fahrenheit = (1.8*celsius) + 32;
    print("Temperature in Fahrenheit =",fahrenheit);
