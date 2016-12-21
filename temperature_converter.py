# The simple script which allows to convert temperature from Celsius to Fahrenheit and backward.


def celcius():
    celcius_degree = int(input("Enter the Celsius temperature: "))
    fahrenheit_degree = celcius_degree * 1.8 + 32  # Conversion Formula
    print(celcius_degree, "C =", fahrenheit_degree, "F")


def fahrenheit():
    fahrenheit_degree = int(input("Enter the Fahrenheit temperature: "))
    celcius_degree = (fahrenheit_degree - 32) * 0.5555555555555556  # Conversion Formula
    print(fahrenheit_degree, "F =", celcius_degree, "C")


def main():  # Главное меню
    print("The temperature converter\n",
          "Main Menu.\n",
          "1 - Convert Celsius to Fahrenheit\n",
          "2 - Convert Fahrenheit to Celsius\n"
          )
    choice = int(input("Choose which one you want to convert: "))
    if choice == 1:
        celcius()
    elif choice == 2:
        fahrenheit()

main()
