import random
import string


length = int(input())
chars = string.ascii_letters
password = ''.join(random.choice(chars) for _ in range(length))
print(password)