""" Temperature comparison program """

result = ""
temperature = float(input("What is the temperature, in Celsius? "))
if temperature < 10:
    result = "It's cold!"
elif temperature >= 10 and temperature <= 25:
    result = "It's cool!"
elif temperature > 25:
    result = "It's hot!"

print(f"You entered {temperature:.1f} degrees. {result}")
