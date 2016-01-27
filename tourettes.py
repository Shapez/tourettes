import random
from pyfiglet import Figlet

f = Figlet(font='doh')

words = ['FUCK!','SHIT!','ASS!','PISS!','KNUCKLE!']
while True:
	print f.renderText(random.choice(words))
