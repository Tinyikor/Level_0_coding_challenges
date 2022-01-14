def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32
    fahrenheit = celsius_to_fahrenheit
    print(f"{celsius} celsius = {fahrenheit} fahrenheit")

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
    celsius = fahrenheit_to_celsius
    print(f"{fahrenheit} fahrenheit = {celsius} celsius")


celsius_to_fahrenheit(20)
fahrenheit_to_celsius(68)
