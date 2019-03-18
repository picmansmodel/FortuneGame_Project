"""
From Modul import * (everthing)
"""

import random
import time
from OutputMessenges import *
from TarotCard_Funktions import one_card_for_today, all_cards_for_everthing # add functions here
from Dictionaries import big_arcanum # Add Decks here




#_________create a random inbetween message from the comment_lst:

inbetween_message = (random.choice(comment_lst))


#________user enters and exit the shope:

def exit_shop():
	time.sleep(2)
	print(goodbye_message)

def enter_shop():
	print(welcome_message)
	time.sleep(1)


#________after user enter the shop or would like to restart

def offering():
	print((offer_message1) + (offer_message2))
	time.sleep(1)
	user_choice = input(offer_question)
	time.sleep(2)
	while user_choice == "s" or "d" or "f" or "t" or "e" or "r":
		if user_choice == "s":
			print("snow_globe funktion is not implementet jet")
			break
		elif user_choice == "d":
			tarot()
			break
		elif user_choice == "f":
			print("fotune_cookie funktion is nor implementet jet")
			break
		elif user_choice == "t":
			print("tea_leave_reading funktion is not implementet jet")
			break
		elif user_choice == "e":
			exit_shop()
			break
		elif user_choice == "r":
			offering()
			break
		else:
			input(offer_question)


#_Tarot function
def tarot():
	tarot_first_desition = input((tarot_info_message) + (tarot_first_question))
	while tarot_first_desition == "t" or "a" or "e" or "r":
		time.sleep(1)
		if tarot_first_desition == "t":
			tarot_secound_desition = input(tarot_secound_question)
			while tarot_secound_desition == "b" or "a" or "e" or "r":
				if tarot_secound_desition == "b":
					print(shuffeling_message)
					time.sleep(1)
					print(random.choice(comment_lst))
					time.sleep(2)
					print(one_card_for_today(big_arcanum))
					time.sleep(1)
					break
				elif tarot_secound_desition == "a":		# Add all cards for today
					print("not implementet jet, sorry")
					break
				elif tarot_secound_desition == "e":
					exit_shop()
					break
				elif tarot_secound_desition == "r":
					offering()
				else:
					input(tarot_secound_reminder)
			break
		elif tarot_first_desition == "a":
			tarot_secound_desition = input(tarot_secound_question)
			while tarot_secound_desition == "b" or "a" or "e" or "r":
				if tarot_secound_desition == "b":
					print(shuffeling_message)
					time.sleep(1)
					print(random.choice(comment_lst))
					time.sleep(2)
					all_cards_for_everthing(big_arcanum)
					time.sleep(1)
					break
				elif tarot_secound_desition == "a":		# Add all cards for timeline
					print("not implementet jet, sorry")
					break
				elif tarot_secound_desition == "e":
					exit_shop()
					break
				elif tarot_secound_desition == "r":
					offering()
				else:
					input(tarot_secound_reminder)
			break
		elif tarot_first_desition == "e":
			exit_shop()
			break
		elif tarot_first_desition == "r":
			offering()
		else:
			input(tarot_first_reminder)



def main():
	#enter_shop()
	#offering()
	tarot()


main()



