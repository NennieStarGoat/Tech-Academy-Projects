fellowship = ["Frodo", "Sam", "Merry", "Pippin", "Aragorn", "Boromir", "Legolas", "Gimli", "Gandalf"]
for member in fellowship:
    print(member)
print()
fellowship.append("Bill")

true_fellowship = fellowship.copy()
print(true_fellowship)

fellowship_last = ["Baggins", "Gamgee", "Brandybuck", "Took", "Arathornson", "Denethorson", "of the Woodland Realm", "Gloinson", "the Grey", "the Pony"]

true_fellowship = [i + " " + j for i, j in zip(fellowship, fellowship_last)]

print(true_fellowship)
true_fellowship.reverse()
print(true_fellowship)