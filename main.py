import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = int(input("Введите кол-во символов в пароле"))
pswrd = ""
for i in range(password):
    pswrd += random.choice(symbols)
print(pswrd)