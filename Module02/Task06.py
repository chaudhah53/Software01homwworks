import random

code3 = "".join(str(random.randint(0, 9)) for _ in range(3))
code4 = "".join(str(random.randint(1, 6)) for _ in range(4))

print("3-digit lock code:", code3)
print("4-digit lock code:", code4)
