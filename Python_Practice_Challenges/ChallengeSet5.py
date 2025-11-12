alive_members = {"Aragorn", "Gimli", "Legolas", "Gandalf", "Boromir", "Frodo", "Sam", "Merry", "Pippin"}
print(alive_members)
alive_members.add("Bill")
print(alive_members)
alive_members.remove("Boromir")
alive_members.remove("Frodo")
alive_members.remove("Gandalf")
print(alive_members)
original_members = {"Aragorn", "Gimli", "Bill", "Legolas", "Gandalf", "Boromir", "Frodo", "Sam", "Merry", "Pippin"}
result = original_members.difference(alive_members)
print(result)
