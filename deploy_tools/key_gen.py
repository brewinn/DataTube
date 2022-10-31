import random

key_file = "secret_key.py"
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+='
key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
with open(key_file, 'w') as f:
    line = "SECRET_KEY = "+"'"+key+"'"
    f.write(line)
