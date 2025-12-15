# English to Hausa dictionary (20 words)
hausa = {
    "hello": "sannu",
    "goodbye": "sai an jima",
    "thank you": "na gode",
    "yes": "eh",
    "no": "a'a",
    "man": "namiji",
    "woman": "mace",
    "child": "yaro",
    "food": "abinci",
    "water": "ruwa",
    "house": "gida",
    "school": "makaranta",
    "book": "littafi",
    "money": "kudi",
    "love": "so",
    "friend": "aboki",
    "morning": "safe",
    "night": "dare",
    "work": "aiki",
    "God": "Allah"
}

print("Choose a language:")
print("1. Hausa")

choice = input("Enter 1: ")

word = input("Enter an English word: ").lower()

if choice == "1":
    if word in hausa:
        print("Hausa translation:", hausa[word])
    else:
        print("Word not found in Hausa dictionary.")
else:
    print("Invalid choice.")