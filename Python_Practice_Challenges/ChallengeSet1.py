standard_greeting = "Hello World!"
better_greeting = '''..........
The world has changed.
I feel it in the water.
I feel it in the earth.
I smell it in the air.
Much that once was is lost,
for none now live who remember it.
..........'''
print(standard_greeting, "\n")
print(better_greeting, "\n")
print(standard_greeting[3:5], standard_greeting[8:9], standard_greeting[10:11], "\n")
print(len(better_greeting), "\n")
print(better_greeting.strip(".\n"), "\n")
print(standard_greeting.upper(), "\n")

if "World" in standard_greeting:
    print(standard_greeting, "\n")

if "Galadriel" not in better_greeting:
    print(better_greeting, "\n")

secret_message_a = standard_greeting[3:5]
secret_message_b = standard_greeting[8:9]
secret_message_c = standard_greeting[10:11]
secret_message = secret_message_a.capitalize() + secret_message_b + secret_message_c + " Elrond is hosting a meeting this October."
print(secret_message)
