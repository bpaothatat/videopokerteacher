from cards import *
from deck import *
from tkinter import *

root = Tk()
root.title("Deuces Wild")
root.geometry("1200x800")
root.configure(background="green")

game_frame = Frame(root, bg = "green")
game_frame.pack(pady=20)

hand_state = HandState.NEW_HAND
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

class HoldButton(Button):
    def __init__(self, frame, *args, **kwargs):
        super().__init__(frame, text='Hold', command=self.switchButtonState, *args, **kwargs)
        self._hold = False

    def switchButtonState(self):
        if not self._hold:
            self._hold = True
        else:
            self._hold = False
        print(self._hold)
        
    def isHold(self):
        return self._hold
        
first_card_hold = HoldButton(game_frame)
first_card_hold.grid(row=1, column=0, padx=10, ipadx=10, pady=10)
first_card_hold.grid_remove()

second_card_hold = HoldButton(game_frame)
second_card_hold.grid(row=1, column=1, padx=10, ipadx=10, pady=10)
second_card_hold.grid_remove()

third_card_hold = HoldButton(game_frame)
third_card_hold.grid(row=1, column=2, padx=10, ipadx=10, pady=10)
third_card_hold.grid_remove()

fourth_card_hold = HoldButton(game_frame)
fourth_card_hold.grid(row=1, column=3, padx=10, ipadx=10, pady=10)
fourth_card_hold.grid_remove()

fifth_card_hold = HoldButton(game_frame)
fifth_card_hold.grid(row=1, column=4, padx=10, ipadx=10, pady=10)
fifth_card_hold.grid_remove()

def display_hand():
    first_card.config(text= hand[0].rank.name + ' of ' + hand[0].suit.name)
    second_card.config(text= hand[1].rank.name + ' of ' + hand[1].suit.name)
    third_card.config(text= hand[2].rank.name + ' of ' + hand[2].suit.name)
    fourth_card.config(text= hand[3].rank.name + ' of ' + hand[3].suit.name)
    fifth_card.config(text= hand[4].rank.name + ' of ' + hand[4].suit.name)

def deal():
    global hand_state, hand, deck
    if hand_state is HandState.NEW_HAND:
        hand_state = HandState.DEALT
        hand = deck.deal_hand()
        first_card_hold.grid()
        second_card_hold.grid()
        third_card_hold.grid()
        fourth_card_hold.grid()
        fifth_card_hold.grid()
        display_hand()
    else:
        hand_state = HandState.NEW_HAND
        deck.redeal_hand(hand, [False, False, True, True, True])
        display_hand()
        first_card_hold.grid_remove()
        second_card_hold.grid_remove()
        third_card_hold.grid_remove()
        fourth_card_hold.grid_remove()
        fifth_card_hold.grid_remove()
        deck.reset()
        
deal_button = Button(game_frame, text="Deal", command=deal)
deal_button.grid(row=2, column=2, padx=20, pady=20)

root.mainloop()