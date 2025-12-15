tiv = {
    "hello": "m sugh",
    "goodbye": "a ngohol",
    "thank you": "m sugh u",
    "yes": "ee",
    "no": "ga",
    "man": "or",
    "woman": "kwase",
    "child": "wan",
    "food": "mnger",
    "water": "mnyam",
    "house": "ya",
    "school": "ya iember",
    "book": "buku",
    "money": "tor",
    "love": "soo",
    "friend": "ember",
    "morning": "kya msen",
    "night": "kya zan",
    "work": "lu",
    "God": "Aondo"
}

print("Choose a language:")
print("1. Tiv")

choice = input("Enter 1 : ")

word = input("Enter an English word: ").lower()

if choice == "1":
    if word in tiv:
        print("Tiv translation:", tiv[word])
    else:
        print("Word not found in Tiv dictionary.")
else:
    print("Invalid choice.")