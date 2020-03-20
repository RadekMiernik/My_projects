import random

suits = ("|_hearts_|", "|_diamonds_|", "|_clubs_|", "|_spades_|")
figures = ('|_2_|','|_3_|','|_4_|','|_5_|','|_6_|','|_7_|','|_8_|','|_9_|','|_10_|',\
          '|_Jack_|','|_Queen_|','|_King_|','|_Ace_|')
values = {'|_2_|':2,'|_3_|':3,'|_4_|':4,'|_5_|':5,'|_6_|':6,'|_7_|':7,'|_8_|':8,\
              '|_9_|':9,'|_10_|':10,'|_Jack_|':10,'|_Queen_|':10,'|_King_|':10,'|_Ace_|':11}

class Card():
    
    def __init__(self,suit,figure):
        self.suit = suit
        self.figure = figure
            
    def __str__(self):
        return str(self.figure +'of'+ self.suit)

class Deck():
    
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for figure in figures:
                self.deck.append(Card(suit,figure))
        random.shuffle(self.deck)
        print("Deck has been created! And shuffled!")
    
    def __str__(self):
        to_show = ''
        for card in self.deck:
            to_show += '\n '+card.__str__()
        return 'In deck we have cards:' + to_show
        
    def pick(self):
        picked = self.deck.pop()
        return picked
    
class Hand():
    
    def __init__(self):
        self.cards = []
        self.points = 0
        self.aces = 11
    
    def __str__(self):
        to_show = ''
        for card in self.cards:
            to_show += " : " + card.__str__() + " : "
        return to_show + 'and this is ---' + str(self.points) + '--- POINTS'
    
    def cards_without_points(self):
        to_show = ''
        for card in self.cards:
            to_show += " : " + card.__str__() + " : "
        return to_show
        
    def add_cards(self,card):
        self.cards.append(card)
        return self.cards
    
    def add_points(self):
        self.points = 0
        for card in self.cards:
            if card.figure == '|_Ace_|':
                self.points += self.aces
            else:
                point = values.get(card.figure)
                self.points += point
    
    def aces_value(self):
        for card in self.cards:
            if card.figure == '|_Ace_|':
                ace_value = 0
                while ace_value == 0:
                    declaration = input('ACE is in your hand. Is it worth 1 or 11?')
                    if declaration == '1':
                        self.aces = 1
                        break
                    elif declaration == '11':
                        self.aces = 11
                        break
                    else:
                        print('Only 1 or 11. I am going to ask you again')
        
class Chips():
    
    def __init__(self):
        self.bet = 0
        while True:
            _ = input('You are going to start a game. You have to place some money for enter.')
            if _.isdigit():
                total = int(_)
                if total > 0:
                    self.total = total
                    break
                else:
                    print('No, you need some money to play!')
            else:
                print('Round numbers only!')
        print('Deck is ready. Game is going to start. You have ---{}$---'.format(self.total))
        
    def __str__(self):
        print('Your bet is: {}$'.format(self.bet))
        print('You have --- {}$ --- total.'.format(self.total))
        
    def player_bet(self,bet):
        self.bet = bet
    
    def win_bet(self): 
        self.total += 2*self.bet
        self.bet = 0
        print("You won and now you have --- {}$".format(self.total))
    
    def lose_bet(self):
        #self.total -= self.bet
        self.bet = 0
        print("You lost and now you have --- {}$".format(self.total))
    
def take_bet():
    print('You know your cards. It is time to place a bet!')
    attempt = True
    while attempt:
        try:
            bet = int(input("Place your bet: "))
            if bet <= chips.total and bet >0:
                chips.bet = bet
                chips.total -= bet
                break
            elif bet > chips.total:
                print('You can only bet {} or less.'.format(chips.total))
                print('I am going to ask you again.\n')
            elif bet <1:
                print('Nice try but you are not able to do this.')
                print('I am going to ask you again.\n')
        except ValueError:
            print("You have to put a round value (0 - {}). I am going to ask you again.\n".format(chips.total))
    chips.__str__()
            
def hit(hand_player,deck,auto=0):
    choice = None
    while choice == None:
        if auto == 1:
            pick = deck.pick()
            print("Your picked kard is:",pick)
            hand_player.add_cards(pick)
            hand_player.aces_value()
            hand_player.add_points()
            show_some(hand_player,hand_dealer)
            break
        choice = input(print('''Your cards are:
        {}
        Wanna hit? y/n '''.format(hand_player)))
        if choice == "y":
            pick = deck.pick()
            print(pick)
            hand_player.add_cards(pick)
            hand_player.aces_value()
            hand_player.add_points()
            show_some(hand_player,hand_dealer)
            break
        elif choice == "n":
            show_some(hand_player,hand_dealer)
            break
        else:
            print("I have to ask you again.")
            choice = None
    
def hit_or_stand(hand_cards,deck):
    '''
    Returns 
    - TRUE if hit
    - FALSE if stand
    '''
    choice = None 
    while choice == None:
        choice = input('''Your cards are:
        {}\n
        Your bet is: --- {}$ ---\n
        Wanna hit or stand? h/s '''.format(hand_cards,chips.bet))
        if choice == 'h':
            hit(hand_cards,deck,auto=1)
            return True
            break
        elif choice == 's':
            return False
            break
        else:
            print("Just put 'h' or 's', there is no other option.")
            choice = None

def show_some(player,dealer):
    dealer_show = []
    for _ in dealer.cards[0:-1]:
        dealer_show.append(_.__str__())
    dealer_show.append('|_X_|')
    hand_dealer.add_points()
    print('''
    |||||||||||||||
    PLAYER cards:
    {p}
    PLAYER bet:
    \t------------ {b}$ ------------\n
    DEALER cards:
    {d1}{d2}
    |||||||||||||||\n'''.format(p=player,b=chips.bet,d1=dealer_show[0],d2=dealer_show[1:]))
    
def show_all(player,dealer):
    print('''
    |||||||||||||||
    PLAYER cards:
    {}\n
    DEALER cards:
    {}
    |||||||||||||||\n'''.format(player,dealer))
    
def player_lost(player,dealer):
    show_all(player,dealer)
    chips.lose_bet()
    
def player_wins(player,dealer):
    show_all(player,dealer)
    chips.win_bet()

def play():
    loop = True
    while loop:
        _ = input('Wanna play again? y/n')
        if _.lower() == "y":
            return True
            break
        elif _.lower() == "n":
            return False
            break
        else:
            print('Only y or n work. Try again.')
            
def rules():
    print('''
 
|                     |
|WELCOME TO BLACK_JACK|
|                     |
            ''')
    
def chips_and_hands_player_and_dealer():
    chips = Chips()
    hand_player = Hand()
    hand_dealer = Hand()
    return hand_player, hand_dealer
    
def first_pick():
    i = 0
    while i <2:
        pick = deck.pick()
        hand_player.add_cards(pick)
        pick = deck.pick()
        hand_dealer.add_cards(pick)
        i+=1
    print('Your cards are:',hand_player.cards_without_points())
    hand_player.aces_value()
    hand_player.add_points()
    hand_dealer.add_points()

rules()
play_loop = True
chips = Chips()
while play_loop:
    deck = Deck()
    hand_player = Hand()
    hand_dealer = Hand()
    first_pick()
    take_bet()
    show_some(hand_player,hand_dealer)
    _ = True
    while _:
        if hand_player.points == 21:
            player_wins(hand_player,hand_dealer)
            _ = False
            play_loop = play()
            break
        elif hand_player.points > 21:
            player_lost(hand_player,hand_dealer)
            #play_loop = play()
            break
        else:
            _ = True
        _ = hit_or_stand(hand_player,deck)
        while _ == False:
            if hand_dealer.points < 17:
                pick = deck.pick()
                hand_dealer.add_cards(pick)
                show_some(hand_player,hand_dealer)
            else:
                a = hand_player.points
                b = hand_dealer.points
                #show_all(hand_player,hand_dealer)
                if b > 21:
                    if abs(a-21) < abs(b-21):
                        player_wins(hand_player,hand_dealer)
                        break
                    else:
                        player_lost(hand_player,hand_dealer)
                        break
                elif a == 21:
                    player_wins(hand_player,hand_dealer)
                    break                            
                elif a>b:
                    player_wins(hand_player,hand_dealer)
                    break
                elif a<b:
                    player_lost(hand_player,hand_dealer)
                    break
                elif a==b:
                    print('It is a draw!')
                    chips.total+=chips.bet
                    chips.bet=0
                    break
    if chips.total == 0:
        print('This is your time now. You should go home - YOU ARE BROKE.')
        play_loop = False
    else:
        play_loop = play()
    print("Thank you for playing.")
