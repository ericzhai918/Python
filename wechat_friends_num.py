import itchat
itchat.login()
friends = itchat.get_friends(update=True)
male = []
female = []
other = []

for person in friends:
    sex = person["Sex"]
    if sex == 1:
        male.append(person)
    elif sex == 2:
        female.append(person)
    else:
        other.append(person)

print(len(female))
print(len(male))
print(len(other))

for name in male:
    print(name)

print('------------------------------------------')

for name in female:
    print(name)