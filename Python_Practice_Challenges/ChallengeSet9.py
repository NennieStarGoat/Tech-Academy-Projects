fellowship = 1
while fellowship < 100:
    fellowship += 1
    if fellowship < 9:
        print('The fellowship is not ready.')
        continue
    if fellowship == 9:
        print('The fellowship of the ring has been formed.')
    else:
        break

ringlords = ['Sauron', 'Isildur', 'Smeagol', 'Frodo', 'Boromir', 'Sam']
for lord in ringlords:
    if lord == 'Boromir':
        print('Boromir held the Ring briefly but was never a ringbearer.')
        continue
    if lord == 'Sam':
        break
    print(lord, 'is the current ringbearer and owner.')

for x in range(4):
    print('RING BEARER!')
    