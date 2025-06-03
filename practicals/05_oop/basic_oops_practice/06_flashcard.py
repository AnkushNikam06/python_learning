# Take the word and its meaning as input from the user.
# Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.
# Now we use the __str__() function to return a string that contains the word and meaning.
# Store the returned strings in a list named flash.
# Use a while loop to print all the stored flashcards.

class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"{self.word} {self.meaning}"

flash = []
print("Welcome to flashcard application")

while(True):
    word = str(input("Enter a word you want to add to flashcard: "))
    meaning = str(input("Enter the meaning of the word: "))

    flash.append(Flashcard(word, meaning))
    option = int(input("Enter 0, if you want to add another flashcard: "))

    if(option):
        break

print("Your flashcards")
for i in flash:
    print(">", i)
