
## tugas pertama

def convert(value, unit):
    if unit == 'C':
        fahrenheit = (value * 9/5) + 32
        return f"{value}°C = {fahrenheit}°F"
    elif unit == 'F':
        celsius = (value - 32) * 5/9
        return f"{value}°F = {celsius}°C"
    else:
        return "Unit ga diketahui. pke 'C' untuk Celsius atau 'F' untuk Fahrenheit."


print(convert(25, 'C'))  
print(convert(77, 'F'))  



## tugas kedua

import math

luas_lingkaran = lambda radius: math.pi * radius ** 2

print(luas_lingkaran(7))


##selesaiiii