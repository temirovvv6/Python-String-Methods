
filename = input("Fayl nomini kiriting: ")

if filename.endswith((".pdf", ".docx", ".txt")):
    print("Fayl nomi to'g'ri")
else:
    print("Fayl nomi noto'g'ri")
