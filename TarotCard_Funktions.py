"""
Tarot Card Functions 
"""
import random
import time
from Dictionaries import *



#___Should the outcome of the Card be good or evil?
def deside_fate(random_card):     
	fate = ["good","evil"]     
	random_fate = random.choice(fate)     
	if random_fate == "good": # name zipped list : good_decriptions / bad_discriptions and use them as general input
		return (big_arcanum_good_discriptions[random_card])     
	if random_fate == "evil":
		return (big_arcanum_evil_discriptions[random_card])


#___Get Key Numbers from Dictiopnary and store it in a list Function:

def create_key_lst(card_deck):
	card_numbers = []				# create empty list
	for number in card_deck:		# for every key in card deck do
		card_numbers.append(number)	# append it to list
	return card_numbers				# return list


#___Today Fotune Card Funktion:

def one_card_for_today(card_deck):
	card_number_lst = create_key_lst(card_deck)		# call create_key_lst Funktion and store it in variable
	today_card = random.choice(card_number_lst)		# get random number out of variable list
	today_fate = deside_fate(today_card) 			# call disde_fath funktion with random number
	return (fortune_time_line["today"]) + (card_deck[today_card]) + "\n" + (today_fate) + "\n"
	# Return :
	# The Value from key ["today"] = String "My advice for you today is: "
	# + The Value from key [today_card] from the input deck = String  
	# + The Variable today_fate with stores the fate result = String


#__Past,Present and Future Card Funktion:

def all_cards_for_everthing(card_deck):
	card_number_lst = create_key_lst(card_deck)
	card_count = []
	for card_count in range(0,3):
		time.sleep(2)
		card_number = random.choice(card_number_lst)
		card_number_lst. remove(card_number)
		fate = deside_fate(card_number)
		if card_count == 0:
			print ((fortune_time_line["past"]) + (card_deck[card_number]) + "\n" + (fate) + "\n\n")   
		elif card_count == 1:
			print ((fortune_time_line["present"]) + (card_deck[card_number]) +  "\n" + (fate)+ "\n\n")
		elif card_count == 2:
			print ((fortune_time_line["present"]) + (card_deck[card_number]) +  "\n" + (fate)+ "\n\n")
	



