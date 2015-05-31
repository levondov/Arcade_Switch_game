from switch import switch
import RPi.GPIO as GPIO

game = switch()

game.game_start()

GPIO.cleanup()