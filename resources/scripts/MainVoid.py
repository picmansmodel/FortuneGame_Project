"""
From Modul import * (everthing)
"""

import random
import time
from OutputMessenges import *
from TarotCard_Funktions import one_card_for_today, all_cards_for_everthing 
from Dictionaries import big_arcanum, fortune_cookie_lst # Dont forget to add Decks here

##########################__MAIN__#######################################

def main():
	enter_shop()
	offering()

#########################################################################


#___Offering Funktion:

def offering():
	#_WIP INFO
	print(construction_points)
	print(construction_messages)
	print(construction_points)
	#_del up later
	print(inbetween_message)
	time.sleep(1)
	print(dramatic_mute_points)
	print(offer_question)
	while True:
		user_choice = input("").strip()
		if user_choice == "s":
			print(headline_points_snow_globe)
			print("snow_globe funktion is not implementet jet")
			break
		elif user_choice == "d":
			print(headline_points_tarot)
			tarot()
			break
		elif user_choice == "f":
			fortune_cookie()
			break
		elif user_choice == "t":
			print(headline_points_tea_leaves_reading)
			print("tea_leave_reading funktion is not implementet jet")
			break
		elif user_choice == "e":
			exit_shop()
			break
		elif user_choice == "r":
			offering()
			break

#___Create a random inbetween message from comment_lst for printing befor offering:

inbetween_message = (random.choice(comment_lst))


#___Enter and Exit Shop Messanges:

def exit_shop():
	print(single_line_points)
	print(goodbye_message)

def enter_shop():
	print(dobble_line_points)
	print(enter_shop_message)
	print(dobble_line_points)
	time.sleep(1)



#___Exit or Restart Funktion:

def exit_or_restart():
	print(desition_points)
	print(exit_or_restart_message)
	user_choice = input(exit_or_restart_question)
	while True:
		user_choice == input("").strip()
		if user_choice == "r":
			print(dobble_line_points)
			offering()
			break
		elif user_choice == "e":
			exit_shop()
			break



#___Fortune Cookié Funktion:
def fortune_cookie():
	print(headline_points_fortune_cookie)
	fortune_cookie = (random.choice(fortune_cookie_lst))
	print(fortune_cookie)
	exit_or_restart()



#___Tarot function

def tarot():
	tarot_first_desition = input((tarot_info_message) + (desition_points) + (tarot_first_question))
	while True:
		tarot_first_desition = input("").strip()
		if tarot_first_desition == "t":
			print(shuffeling_message)
			time.sleep(2)
			print(one_card_for_today(big_arcanum))
			time.sleep(1)
			exit_or_restart()
			break
		elif tarot_first_desition == "a":
			print(shuffeling_message)
			time.sleep(2)
			all_cards_for_everthing(big_arcanum)
			time.sleep(1)
			exit_or_restart()
			break
		elif tarot_first_desition == "e":
			exit_shop()
			break
		elif tarot_first_desition == "r":
			offering()





def main():
	enter_shop()
	offering()


main()



