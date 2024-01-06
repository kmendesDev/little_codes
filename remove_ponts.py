ponts = '''<,>.?/:;"'-_{}\[]|()*&%$#@!`'''

text = input("texto: ")

sem_pts = ""
for c in text:
    if c not in ponts:
        sem_pts = sem_pts+c

print(sem_pts)