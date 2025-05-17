import random
import string

passwd_size = int(input("generate olunacaq parolun uzunlugunu mueyyen edin: "))

letters = list(string.ascii_letters)
digits = list(string.digits)
punctuation = list(string.punctuation)
pool = letters + digits + punctuation


passwd = ''

for i in range(passwd_size):
    passwd += random.choice(pool)

print(f'parol yaradildi: {passwd}') 