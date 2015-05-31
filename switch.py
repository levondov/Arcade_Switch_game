import RPi.GPIO as GPIO
from kbhit import KBHit
import time

GPIO.setmode(GPIO.BCM)
pinList = [2,3,4,17,27,22,10,9]


class switch:
	"""Switch class for game"""
	pos = 1;
	def __init__(self):
		self.pos = 0
	def game_start(self,position=0):
	
		for i in range(position,8):
			round = self.game_round(i)
			if round == False:
				print "Sorry, try again."
				break
			print "Win! Next round..."
		print "Finished Game!"
			
		
	def game_round(self,position):
		# set round speed and guess
		speed = 1./(1+position)
		guess = -1
		stop = False
		
		# turn on GPIO pins
		for i in pinList[position:]:
			GPIO.setup(i, GPIO.OUT)
			GPIO.output(i, GPIO.HIGH)
		
		# turn on correct guesses
		for i in pinList[0:position]:
			GPIO.output(i, GPIO.LOW)
			
		#start kbhit 
		kb = KBHit()
		
		# start loop
		while True:
			for i in pinList[position:]:
				GPIO.output(i, GPIO.LOW)
				
				# check keypress
				if kb.kbhit():
					c = kb.getch()
					if ord(c) != 27:
						stop = True
						guess = pinList.index(i)-1
						break
				time.sleep(speed)
			# check keypress
			if stop:
				break
				
			pinList.reverse()
			for i in pinList[0:len(pinList)-position]:
				GPIO.output(i,GPIO.HIGH)
				if kb.kbhit():
					c = kb.getch()
					if ord(c) != 27:
						stop = True
						guess = len(pinList)-(pinList.index(i)+1)
						pinList.reverse()
				time.sleep(speed)
			if stop:
				break
			pinList.reverse()
		# check results
		print guess
		print position
		return (guess == position)
	
	

	