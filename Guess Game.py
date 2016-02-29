from random import randrange
randomNumber = randrange(1, 100)

guessCount = 0

response = ""

response = int(raw_input("Enter guess between 1-100 >>> "))

while not response == randomNumber:
        print ""
        if(abs(response-randomNumber) < 10 and not int(response) == randomNumber):
                print "You are very close!"
        if(response > 100 or response < 0):
                print "Your guess has to between 0-100!"
                response = int(raw_input("Enter guess between 1-100 >>> "))
                guessCount = guessCount - 1
        elif(response < randomNumber):
                response = int(raw_input("Guess a bigger number than " + str(response) + "! >>> "))
        elif(response > randomNumber):
                response = int(raw_input("Guess a smaller number than " + str(response) + "! >>> "))
        guessCount += 1

print "That's correct! The number was " + str(randomNumber) + ". You guessed in " + str(guessCount) + " tries!"
