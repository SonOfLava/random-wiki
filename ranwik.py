import selenium
from selenium import webdriver 
import wikipedia
def launchArt(randArt):
	browser = webdriver.Firefox()
	wikString = randArt.replace(" ", "_")
	browser.get("http://en.wikipedia.org/wiki/%s" %wikString)
	goAgain()
def goAgain():
	again = input("Want another? ")
	if again.lower() == "yes" or again.lower == "y":
		getArt()
	if again.lower() == "no" or again.lower() == "n":
		print("Goodbye!")
		quit()
def getArt():
	randArt = wikipedia.random(pages = 1)
	userInput = input("Would you like to read about %s? " %randArt)
	if userInput.lower() == "yes" or userInput.lower() == "y":
		launchArt(randArt)
	if userInput.lower() == "no" or userInput.lower() == "n":
		getArt()
getArt()
