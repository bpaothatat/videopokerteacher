from tkinter.ttk import Style
from cards import *
from deuces_wild_hand_validator import hand_evaluator
from deck import *
from tkinter import *

root = Tk()
style = Style()
root.title("Deuces Wild")
root.geometry("1200x800")
root.configure(background="green")

game_frame = Frame(root, bg = "green")
game_frame.grid(pady=20)

hand_state = HandState.NEW_HAND
deck = Deck()
hand = []

class CardDisplay(object):
    def __init__(self, frame:Frame, position:int, card:Card) -> None:
        self.label_frame = LabelFrame(frame, text= 'Position', bd=0)
        self.label_frame.grid(row=0, column=position, padx=10, ipadx=10)

        self.card_label = Label(self.label_frame, text=card.rank.name + ' of ' + card.suit.name)
        self.card_label.grid(padx=15)

        self._hold = False
        self.hold_button = Button(game_frame, text='Hold', command=self.switchButtonState)
        self.hold_button.grid(row=1, column=position, padx=10, ipadx=10, pady=10)
        self.hold_button.grid_remove()

    def switchButtonState(self):
        if not self._hold:
            self._hold = True
            self.label_frame.config(highlightbackground='red', highlightthickness=2)
        else:
            self._hold = False
            self.label_frame.configure(highlightthickness=0)

    def setCard(self, card:Card):
        self.card_label.config(text=card.rank.name + ' of ' + card.suit.name)

    def displayHold(self):
        self.hold_button.grid()

    def hideHold(self):
        self.hold_button.grid_remove()

    def remove_hold_boarder(self):
        self.label_frame.config(highlightthickness=0)

    def isHold(self):
        return self._hold
        
first_card = CardDisplay(game_frame, 0, Card(Suit.DIAMOND, Rank.TWO))
second_card = CardDisplay(game_frame, 1, Card(Suit.DIAMOND, Rank.ACE))
third_card = CardDisplay(game_frame, 2, Card(Suit.DIAMOND, Rank.THREE))
fourth_card = CardDisplay(game_frame, 3, Card(Suit.DIAMOND, Rank.FOUR))
fifth_card = CardDisplay(game_frame, 4, Card(Suit.DIAMOND, Rank.FIVE))

hand_display = [first_card, second_card, third_card, fourth_card, fifth_card]

hand_evaluation_label = Label(game_frame, text="Pending")
hand_evaluation_label.grid(row=2, column=2, padx=20, pady=20)
hand_evaluation_label.grid_remove()

def getHandHoldStatus():
    return [card.isHold() for card in hand_display]

def hide_hold_buttons():
    [card.hideHold() for card in hand_display]

def display_hold_buttons():
    [card.displayHold() for card in hand_display]

def remove_board():
    [card.remove_hold_boarder() for card in hand_display]

def display_hand():
    global hand, deck, hand_display
    deck.redeal_hand(hand, getHandHoldStatus())
    [card.setCard(hand[index]) for index, card in enumerate(hand_display)]

def deal():
    global hand_state, deck, hand
    if hand_state is HandState.NEW_HAND:
        hand_state = HandState.DEALT
        hand = deck.deal_hand()
        display_hand()
        display_hold_buttons()
        hand_evaluation_label.grid_remove()
    else:
        hand_state = HandState.NEW_HAND
        display_hand()
        hide_hold_buttons()
        remove_board()
        hand_evaluation_label.config(text=hand_evaluator(hand).name)
        hand_evaluation_label.grid()
        deck.reset()
        
deal_button = Button(game_frame, text="Deal", command=deal)
deal_button.grid(row=3, column=2, padx=20, pady=20)

root.mainloop()