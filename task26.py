
username = input("GitHub username kiriting: ")


username_tozalangan = username.replace("-", "")


if username_tozalangan.isalnum():  
    print("Username to'g'ri")
else:
    print("Username noto'g'ri")
