Temperature = int(input("Enter the temperature in celsius: "))

if Temperature > 54:
    print("Your climate is very hot. You should wear light colours like white.")
elif Temperature > 40:
    print("Your climate is hot. You should wear light colours like white, baby blue.")
elif Temperature > 30:
    print("Your climate is warm. You should wear light colours like peach, yellow, white, beige.")
elif Temperature > 21:
    print("Your climate is neutral. You should wear colours like green, blue, pink, orange.")
elif Temperature > 7:
    print("Your climate is cold. You should wear dark colours like purple,grey, dark blue, dark green, maroon.")
elif Temperature > -5:
    print("Your climate is very cold. You should wear dark colours like black, midnight blue.")
