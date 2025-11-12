fellowship = {
    'Baggins': {'fname': 'Frodo', 'lname': 'Baggins', 'occupation': 'ring bearer', 'home': 'The Shire'},
    'Gamgee': {'fname': 'Sam', 'lname': 'Gamgee', 'occupation': 'gardener', 'home': 'The Shire'},
    'Brandybuck': {'fname': 'Meriadoc', 'lname': 'Brandybuck', 'occupation': 'knight of Rohan', 'home': 'The Shire'},
    'Took': {'fname': 'Peregrin', 'lname': 'Took', 'occupation': 'mischief maker', 'home': 'The Shire'},
    'Greyhame': {'fname': 'Gandalf', 'lname': 'Greyhame', 'occupation': 'meddler', 'home': 'Valinor'},
    'Arathornson': {'fname': 'Aragorn', 'lname': 'Arathornson', 'occupation': 'king of Gondor', 'home': 'Minas Tirith'},
    'Greenleaf': {'fname': 'Legolas', 'lname': 'Greenleaf', 'occupation': 'prince of Mirkwood', 'home': 'Mirkwood'},
    'Gloinson': {'fname': 'Gimli', 'lname': 'Gloinson', 'occupation': 'lord of the Glittering Caves', 'home': 'Ered Luin'},
    'Denethorson': {'fname': 'Boromir', 'lname': 'Denethorson', 'occupation': 'captain of the White Tower', 'home': 'Minas Tirith'}
}

print(fellowship.get('Took').get('lname'))

fellowship['Gamgee'].update({'fname': 'Samwise'})
print(fellowship.get('Gamgee').get('fname'))

fellowship.update({'Undomiel': {'fname': 'Arwen', 'lname': 'Undomiel', 'occupation': 'layabout', 'home': 'Rivendell'}})
print(fellowship.get('Undomiel').get('occupation'))

outer = ['the Pony', 'aka Smeagol']
inner = {'fname': '', 'lname': '', 'occupation': '', 'home': ''}

fellows = dict.fromkeys(outer, inner)
print(fellows)