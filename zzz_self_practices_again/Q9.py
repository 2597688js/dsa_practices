def fahrenheit_to_celsius(fahrenheit_temp:float) -> float:
    celsius_temp = (fahrenheit_temp - 32) * 5/9
    return celsius_temp


if __name__ == "__main__":
    fah = float(input("Enter the temperature in fahrenheit : "))
    cel = fahrenheit_to_celsius(fah)
    print(f"Temprerature in Celsius is : {cel}")