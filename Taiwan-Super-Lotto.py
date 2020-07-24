import random

i = 0
section1 = []
section2 = []
while i <= 5:
    r = random.randint(1, 38)
    if r in section1:
    	continue

    section1.append(r)
    i += 1

r = random.randint(1, 8)
section2.append(r)
section1.sort()

print(section1, section2)
