"""
Dictionaries for :

"Snow Globe"	> no good idea jet
"Destiny"		> Big Arcanum  + fath is implemented > Small one needs to be implemented + fath > use zip(big, small) to create all_card_dic
"Fotune Cooie"	> random wisedom from around the world
"A Tea Leaves Reading" > User should input a yes or no question > Buch der antworten

"""

#_________________________________________________Tarot Card Info____________________________________________________________________________________________________________________________

"""
A classic Tarot Card Deck consist of 72 cards.

It is spli up in Big Arcanum contains 22 Cards (21 + The Fool).
And the Small Arcanum, with 56 cards (4 Colors with 10 Numbers and 4 Picture cards).

"""

big_arcanum = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 
7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 
14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}


big_arcanum_good_discriptions = {1: "You have everthing you need.", 2: "Listen to your intuition not emotion or logic.", 3: "I see compassion. You are a peacekeeper.", 
4: "In this moment of time you have no discipline and obeying the rules.", 5: "I see pursuit of traditional knowledge.", 
6: "Someone loves you, but you may want to make a different choice.", 7: "Get in the Drivers seat!", 8: "Use honey not vinegar!", 9: "Take some time alone to think.",
10: "Things are changing fast around you.", 11: "Treat people fairly and you will be treated with cookies.", 12: "You need to make a sacrifice.", 13: "Accept the end of a situation.",
14: "Caution!The Situation needs your full attention!", 15:"I sence sexual desire and passion.", 16: "A setback causes you to rebuild.", 17: "Healing and rebirth is directly ahead.",
18: "Don't be deceived!", 19: "A wonderful experience is ahead of you!", 20 : "You need to listen more to your friend and furtune teller Zandra.", 
21: "You will have the freedom to choose a new path.", 22: "Take the risk but watch your step!"}

big_arcanum_evil_discriptions = {1:  "You are out of touch with reality", 2: "Something is blocking your higher self.", 3: "Domestic disharmony is waiting for you.", 
4: "You are irresponsible.", 5: "Think outside the box!", 6: "I can see a temporary romantic breakup.", 7: "You need a break.Delayed journey.", 
8: "Ayayay...I see a lot of arguments.", 9: "You need more social interaction.", 10: "A setback requires you to rethink your original plan.",
11: "I have the feeling that you being cheated out of something.", 12: "Don't be stubborn.", 13: "Baggage keeps you from moving forward.", 14: "What a waste of Time.",
15: "I can see victory over your emotions.", 16: "You need to strengthen your foundation.", 17 : "There´s a lack of faith. That means illness.", 18 : "Are there any mental health issues?",
19: "Meaning the Aura of low energy.", 20: "Don't run away from your feelings.", 21: "I can sence the aura of low self esteem.", 22: "There are things you need to address."}


fortune_time_line = {"past" : "Your past is resembeled by : ", "present" : "Your presents is resembeled by : ", "future" : "Your future is resembeled by : ",
"today" :"My advice for you today is: "}
