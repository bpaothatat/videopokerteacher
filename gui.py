from cards import *
from deck import Deck
from tkinter import *

root = Tk()
root.title("Deuces Wild")
root.geometry("1200x800")
root.configure(background="green")

game_frame = Frame(root, bg = "green")
game_frame.pack(pady=20)

new_hand = True
deck = Deck()
hand = None

first_card_frame = LabelFrame(game_frame, text="First Card", bd=0)
first_card_frame.grid(row=0, column=0, padx=10, ipadx=10)

first_card = Label(first_card_frame, text='Two of Clubs')
first_card.pack(padx=20)

second_card_frame = LabelFrame(game_frame, text="Second Card", bd=0)
second_card_frame.grid(row=0, column=1, padx=10, ipadx=10)

second_card = Label(second_card_frame, text='Ace of Diamonds')
second_card.pack(padx=20)

third_card_frame = LabelFrame(game_frame, text="Third Card", bd=0)
third_card_frame.grid(row=0, column=2, padx=10, ipadx=10)

third_card = Label(third_card_frame, text='Two of Diamonds')
third_card.pack(padx=20)

fourth_card_frame = LabelFrame(game_frame, text="Fourth Card", bd=0)
fourth_card_frame.grid(row=0, column=3, padx=10, ipadx=10)

fourth_card = Label(fourth_card_frame, text='Three of Diamonds')
fourth_card.pack(padx=20)

fifth_card_frame = LabelFrame(game_frame, text="Fifth Card", bd=0)
fifth_card_frame.grid(row=0, column=4, padx=10, ipadx=10)

fifth_card = Label(fifth_card_frame, text='Four of Diamonds')
fifth_card.pack(padx=20)

first_card_hold = Button(game_frame, text='Hold')
first_card_hold.grid(row=1, column=0, padx=10, ipadx=10, pady=10)
first_card_hold.grid_remove()

second_card_hold = Button(game_frame, text='Hold')
second_card_hold.grid(row=1, column=1, padx=10, ipadx=10, pady=10)
second_card_hold.grid_remove()

third_card_hold = Button(game_frame, text='Hold')
third_card_hold.grid(row=1, column=2, padx=10, ipadx=10, pady=10)
third_card_hold.grid_remove()

fourth_card_hold = Button(game_frame, text='Hold')
fourth_card_hold.grid(row=1, column=3, padx=10, ipadx=10, pady=10)
fourth_card_hold.grid_remove()

fifth_card_hold = Button(game_frame, text='Hold')
fifth_card_hold.grid(row=1, column=4, padx=10, ipadx=10, pady=10)
fifth_card_hold.grid_remove()

def deal():
    global new_hand
    if new_hand:
        new_hand = False
        hand = deck.deal_hand()
        first_card_hold.grid_remove()
        second_card_hold.grid_remove()
        third_card_hold.grid_remove()
        fourth_card_hold.grid_remove()
        fifth_card_hold.grid_remove()
        first_card.config(text= hand[0].rank.name + ' of ' + hand[0].suit.name)
        second_card.config(text= hand[1].rank.name + ' of ' + hand[1].suit.name)
        third_card.config(text= hand[2].rank.name + ' of ' + hand[2].suit.name)
        fourth_card.config(text= hand[3].rank.name + ' of ' + hand[3].suit.name)
        fifth_card.config(text= hand[4].rank.name + ' of ' + hand[4].suit.name)
    else:
        new_hand = True
        first_card_hold.grid()
        second_card_hold.grid()
        third_card_hold.grid()
        fourth_card_hold.grid()
        fifth_card_hold.grid()
        deck.reset()
        
deal_button = Button(game_frame, text="Deal", command=deal)
deal_button.grid(row=2, column=2, padx=20, pady=20)

root.mainloop()