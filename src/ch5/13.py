pw = 0
while pw != "pwpass":
    pw = input("비밀번호 :")
    if pw == "pwpass":
        break
    else:
        continue
print("Login Pass!")