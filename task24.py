email = input("Email kiriting: ")

boshlanmasin = not email.startswith("@")


tugash = email.endswith(".com")


print("Email @ bilan boshlanmagan:", boshlanmasin)
print("Email .com bilan tugagan:", tugash)
