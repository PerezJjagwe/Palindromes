name = input("Hello there! \nWhat is your name? :")
word = input("Excuse me " + str(name) + ", please type the word or phrase you want to test :")
if word == word[::-1] :
    print("So " + str(name) + " lucky for you, the word/phrase you have input is a palindrome.")
else:
    print("So " + str(name) + " sadly, the word/phrase you have input is not a palindrome")

