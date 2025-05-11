import random

password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

len = int(input('введите длину пароля:'))

save = ""

for i in range(len):
    save += random.choice(password)

    print(save)