from cards import *
from deuces_wild_hand_validator import hand_evaluator
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
hand = []

class CardFrame(LabelFrame):
     def __init__(self, frame, frame_name, column, *args, **kwargs):
        super().__init__(frame, text=frame_name, bd=0)
        self.grid(row=0, column=column, padx=10, ipadx=10)

class CardLabel(Label):
    def __init__(self, card_frame, card, *args, **kwargs):
        super().__init__(card_frame, text=card)
        self.grid(padx=20)

first_card_frame = CardFrame(game_frame, "First Card", 0)
first_card = CardLabel(first_card_frame, 'Two of Clubs')

second_card_frame = CardFrame(game_frame, "Second Card", 1)
second_card = CardLabel(second_card_frame, 'Ace of Diamonds')

third_card_frame = CardFrame(game_frame, "Third Card", 2)
third_card = CardLabel(third_card_frame,'Two of Diamonds')

fourth_card_frame = CardFrame(game_frame, "Fourth Card", 3)
fourth_card = CardLabel(fourth_card_frame, 'Three of Diamonds')

fifth_card_frame = CardFrame(game_frame, "Fifth Card", 4)
fifth_card = CardLabel(fifth_card_frame, 'Four of Diamonds')

hand_evaluation_label = Label(game_frame, text="Pending")
hand_evaluation_label.grid(row=2, column=2, padx=20, pady=20)
hand_evaluation_label.grid_remove()

class HoldButton(Button):
    def __init__(self, frame, column, *args, **kwargs):
        super().__init__(frame, text='Hold', command=self.switchButtonState, *args, **kwargs)
        self.grid(row=1, column=column, padx=10, ipadx=10, pady=10)
        self.grid_remove()
        self._hold = False

    def switchButtonState(self):
        if not self._hold:
            self._hold = True
        else:
            self._hold = False

    def isHold(self):
        return self._hold
        
first_card_hold = HoldButton(game_frame, 0)
second_card_hold = HoldButton(game_frame, 1)
third_card_hold = HoldButton(game_frame, 2)
fourth_card_hold = HoldButton(game_frame, 3)
fifth_card_hold = HoldButton(game_frame, 4)

def display_hand():
    first_card.config(text= hand[0].rank.name + ' of ' + hand[0].suit.name)
    second_card.config(text= hand[1].rank.name + ' of ' + hand[1].suit.name)
    third_card.config(text= hand[2].rank.name + ' of ' + hand[2].suit.name)
    fourth_card.config(text= hand[3].rank.name + ' of ' + hand[3].suit.name)
    fifth_card.config(text= hand[4].rank.name + ' of ' + hand[4].suit.name)

def getHandHoldStatus():
    return [first_card_hold.isHold(), second_card_hold.isHold(), third_card_hold.isHold(), fourth_card_hold.isHold(), fifth_card_hold.isHold()]

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
        hand_evaluation_label.grid_remove()
        display_hand()
    else:
        hand_state = HandState.NEW_HAND
        deck.redeal_hand(hand, getHandHoldStatus())
        display_hand()
        first_card_hold.grid_remove()
        second_card_hold.grid_remove()
        third_card_hold.grid_remove()
        fourth_card_hold.grid_remove()
        fifth_card_hold.grid_remove()
        hand_evaluation_label.config(text=hand_evaluator(hand).name)
        hand_evaluation_label.grid()
        deck.reset()
        
deal_button = Button(game_frame, text="Deal", command=deal)
deal_button.grid(row=3, column=2, padx=20, pady=20)

root.mainloop()