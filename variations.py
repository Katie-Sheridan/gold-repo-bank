#formats a message string in different ways 

message = input("Enter a message: ")

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())

#enter a split screen format
words = message.split()
print("Words:", words)

# sort words automatically
sorted_words = sorted(words)
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])

