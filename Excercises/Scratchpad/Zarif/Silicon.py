temp = input("Please give the temperature you want to convert: ")
degree = int(temp[:-1])
ai = temp[-1]
C = (5 / 9) * (degree - 32)
F = (9 * degree + (32 * 5)) / 5

if ai.upper() == "C":
    print(f"The {degree}°C is {F:.2f}°F")

elif ai.upper() == "F":
    print(f"The {degree}°F is {F:.2f}°C")
