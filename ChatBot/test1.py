import random
import wikipedia

flip = False

text_file = open("stopWord.txt", "r")
stopwords = text_file.read().split('\n')
stopwords.append("name")
text_file.close()

text_file = open("sad.txt", "r")
sadWordsfile = text_file.read().split('\n')
text_file.close()

text_file = open("happy.txt", "r")
happyWordsfile = text_file.read().split('\n')
text_file.close()

greetings = ['hola ', 'hello ', 'hi ', 'Hi ', 'hey! ','hey ', 'Wa Sup']
random_greeting = random.choice(greetings)

hairColour = ['Thats cool', 'That colour is fine', 'Look at you', 'sounds intersting']
random_hair = random.choice(hairColour)

nameQuestion = raw_input("What is your name ?")
wordList = nameQuestion.split(" ")
for word in wordList:
    if word.lower() not in stopwords:
        print (random_greeting + word)          
name = word

feelingQuestion = raw_input ('How are you feeling today? ')

feelingWord = feelingQuestion.split(" ")
for word in feelingWord:
    if word.lower() == "not": flip = True
    elif word in happyWordsfile: emotion = "good"
    elif word in sadWordsfile: emotion = "bad"
    
if flip and emotion == "good": print ("Oh dear, sound like you need a beer!")
if not flip and emotion == "good": print ("Thats really good " + name)
if flip and emotion == "bad": print ("Thats really good " + name)
if not flip and emotion == "bad": print ("Oh dear, sound like you need a beer!")
        
yourColour = raw_input("What is your hair colour ?")
print(random_hair)

while True:
    search = raw_input("Want  to find some information about any subject>>")
    search_words = search.split(" ")
    for word in search_words:
        if (word not in stopwords) and (len(word.strip()) > 0):
            print("Just about to search for " + word)
            results = wikipedia.search(word)
            print(wikipedia.summary(results[0], sentences=1))
           