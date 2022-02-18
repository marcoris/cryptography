from random import SystemRandom

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = "".join(SystemRandom().choice(alphabet) for _ in range(64))
password2 = "".join(SystemRandom().choice(alphabet) for _ in range(64))
password3 = "".join(SystemRandom().choice(alphabet) for _ in range(64))
password4 = "".join(SystemRandom().choice(alphabet) for _ in range(64))

print(password)
print(password2)
print(password3)
print(password4)