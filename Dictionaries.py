"""
Dictionaries for :

"Snow Globe"	> no good idea jet
"Destiny"		> Big Arcanum Tarot Deck, other card decks ar possible
"Fotune Cookie"	> random wisedom from around the world
"A Tea Leaves Reading" > User should input a yes or no question > Buch der antworten

"""

#_________________________________________________Fortune Cookie_____________________________________________________________________________________________________________________________

fortune_cookie_lst = ["The early bird gets the worm, but the secound mouse gets the cheese.", "Your road to glory will be rocky, but fulfilling.", "Patience is your alley at the moment. Don’t worry!",
"Courage is not the absence of fear; it is the conquest of it.", "All things are difficult before they are easy.", "A ship in harbor is safe, but that’s not why ships are built.", 
"If you want the rainbow, you have to tolerate the rain.", "Fear is interest paid on a debt you may not owe.", "The usefulness of a cup is in its emptiness.", "Zandra knows your future.", 
"Of all our human resources, the most precious is the desire to improve.", "People learn little from success, but much from failure.", "A person who won’t read has no advantage over a person who can’t read.",
"Never forget that a half truth is a whole lie.", "No snowflake in an avalanche ever feels responsible", "If you eat something and nobody sees you eat it. It has noe calories.", 
"You don´t have to be faster than the bear, you just have to be faster than the slowest guy running from it.", "You look pretty. In youth and beauty, wisdom is rare.",
"There will be money in your future---  it is not yours though.", "Three can keep a secret, if you get rid of two", "Love is on the horizon.The stars predict\nhe will be tall,dark and a centaur.",
"You laugh now, wait till you get home.", "Your resemblance to a muppet will prevent the world from taking you seriously", "What´s the speed of dark?", 
"Your fortune said you need to make a donation. Give it to Zandra.", "A real patriot is a fellow who gets a parking ticket \nand rejoices that the system works.", "When in danger, sing the alphabet",
"Fear is like fire. It can burn your house down \nand you can warm your hands on it.", "Pregnancy is a gift.\nAnd in your case it will also be a surprise.", "The fortune you seek is in another cookie.", 
"A foolosh man is listens to his heart\nA wise man is listen to cookies and Zandra.", "You suck az parking.", "Foot: A device for finding furniture in the dark.", "No one reads reads your blog."]


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
11: "I have the feeling that you being cheated out of something.", 12: "Don\'t be stubborn.", 13: "Baggage keeps you from moving forward.", 14: "What a waste of Time.",
15: "I can see victory over your emotions.", 16: "You need to strengthen your foundation.", 17 : "There´s a lack of faith. That means illness.", 18 : "Are there any mental health issues?",
19: "Meaning the Aura of low energy.", 20: "Don't run away from your feelings.", 21: "I can sence the aura of low self esteem.", 22: "There are things you need to address."}


fortune_time_line = {"past" : "Your past is resembeled by : ", "present" : "Your presents is resembeled by : ", "future" : "Your future is resembeled by : ",
"today" :"My advice for you today is: "}

#_________________________________________________CRYSTAL SKULL Info____________________________________________________________________________________________________________________________

crystal_skull_colors = {
1: "\n-----------THE CRYSTAL SKULL STARTS TO TURN RED--------\n", 
2: "\n-----------THE CRYSTAL SKULL STARTS TO TURN BLUE--------\n",
3: "\n-----------THE CRYSTAL SKULLS EYES STARTS TO TURN GREEN--------\n",
4: "\n-----------THE CRYSTAL SKULL STARTS TO TURN PURPLE--------\n",
5: "\n-----------THE CRYSTAL SKULL STARTS TO TURN YELLOW--------\n",
6: "\n-----------THE CRYSTAL SKULL STARTS TO DISAPPEAR--------\n"}

crystal_skull_colors_discriptions = {
	1: "You are LAVA. Fire walks with you.\n",
	2: "The skull is quieted, just like you.\n",
	3: "I didn´t had this in a long time. Next time you need to focus harder.\n",
	4: "I sence disire and a mystic aura around you. You allready have all the answers.\n",
	5: "Yellow it is then. My advise for you is: Plan to be more spontaneous tomorrow.\n",
	6: "Concratulation! That´s 200$. Next time you focus on yourself, please.\n"
	}