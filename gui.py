from tkinter.ttk import Style
from cards import *
from deuces_wild_hand_validator import hand_evaluator
from deck import *
from tkinter import *
from PIL import Image, ImageTk

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
        self.label_frame = LabelFrame(frame, bd=0, background='green')
        self.label_frame.grid(row=0, column=position, padx=10, pady=10, ipadx=0, ipady=0)

        self.card_label = Label(self.label_frame)
        self.set_card_image(card)
        self.card_label.grid(padx=0, pady=0, ipadx=0, ipady=0)

        self.hold = False
        self.hold_button = Button(game_frame, text='Hold', command=self.switch_button_state)
        self.hold_button.grid(row=1, column=position, padx=10, ipadx=10, pady=10)
        self.hold_button.grid_remove()

    def switch_button_state(self):
        if not self.hold:
            self.hold = True
            self.label_frame.config(highlightbackground='red', highlightthickness=2)
        else:
            self.hold = False
            self.label_frame.configure(highlightthickness=0)

    def display_hold(self):
        self.hold_button.grid()

    def hide_hold(self):
        self.hold_button.grid_remove()

    def remove_hold_boarder(self):
        self.label_frame.config(highlightthickness=0)

    def is_hold(self):
        return self.hold
    
    def remove_hold(self):
        self.hold = False

    def set_card_image(self, card:Card):
        image = Image.open(self.image_file_path(card))
        image = image.resize((200, 500))
        photo_image = ImageTk.PhotoImage(image)
        self.card_label.config(image=photo_image)
        self.card_label.image = photo_image

    def image_file_path(self,card:Card):
        card_name = card.rank.name.lower() + '_of_' + card.suit.name.lower() + 's.png'
        if card.rank.value <= 10:
            card_name = str(card.rank.value) + '_of_' + card.suit.name.lower() + 's.png'
        return "./images/" + card_name
        
first_card = CardDisplay(game_frame, 0, Card(Suit.DIAMOND, Rank.TWO))
second_card = CardDisplay(game_frame, 1, Card(Suit.DIAMOND, Rank.ACE))
third_card = CardDisplay(game_frame, 2, Card(Suit.DIAMOND, Rank.THREE))
fourth_card = CardDisplay(game_frame, 3, Card(Suit.DIAMOND, Rank.FOUR))
fifth_card = CardDisplay(game_frame, 4, Card(Suit.DIAMOND, Rank.FIVE))

hand_display = [first_card, second_card, third_card, fourth_card, fifth_card]

hand_evaluation_label = Label(game_frame, text="Pending")
hand_evaluation_label.grid(row=2, column=2, padx=20, pady=20)
hand_evaluation_label.grid_remove()

def get_hand_hold_status():
    return [card.is_hold() for card in hand_display]

def reset_holds():
    [card.hide_hold() for card in hand_display]
    [card.remove_hold() for card in hand_display]

def display_hold_buttons():
    [card.display_hold() for card in hand_display]

def remove_board():
    [card.remove_hold_boarder() for card in hand_display]

def display_hand():
    global hand, deck, hand_display
    deck.redeal_hand(hand, get_hand_hold_status())
    [card.set_card_image(hand[index]) for index, card in enumerate(hand_display)]

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
        reset_holds()
        remove_board()
        hand_evaluation_label.config(text=hand_evaluator(hand).name)
        hand_evaluation_label.grid()
        deck.reset()
        
deal_button = Button(game_frame, text="Deal", command=deal)
deal_button.grid(row=3, column=2, padx=20, pady=20)

root.mainloop()