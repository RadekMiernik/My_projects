def wybor_znaku_gracza():
    """Zwraca wybrany znak przez graczy i ich imiona"""
    global imie_1, imie_2, znak_gracza_1, znak_gracza_2, player_x, player_o #okazuje sie, że zmienne nie musza być inicjowane wcześniej
    imie_1 = input(print("Podaj imię pierwszego gracza: "))
    imie_2 = input(print("Podaj imię drugiego gracza: "))
    wybor = input(print("{} wybierasz X czy O? (domyślnie dostajesz X)".format(imie_1)))
    wybor = wybor.upper()
    if wybor == "X":
        znak_gracza_1 = "X"
        player_x = imie_1
        znak_gracza_2 = "O"
        player_o = imie_2
    elif wybor == "O":
        znak_gracza_1 = "O"
        player_o = imie_1
        znak_gracza_2 = "X"
        player_x = imie_2
    else:
        znak_gracza_1 = "X"
        player_x = imie_1
        znak_gracza_2 = "O"
        player_o = imie_2
    print("Gracz-PIERWSZY- to \t:::{}::: \ti wybrał ----------- > {}".format(imie_1, znak_gracza_1))
    print("Gracz---DRUGI-- to \t:::{}::: \ti pozostał mu -------> {}".format(imie_2, znak_gracza_2))
    return imie_1, imie_2, znak_gracza_1, znak_gracza_2, player_x, player_o

def zasady():
    """Wyswietla zasady gry"""
    print("""
        Witaj w grze KÓŁKO i KRZYŻYK
        
        Za chwilę GRACZ {g_1} zmierzy się z GRACZEM {g_2}
        
        Zasady są bardzo proste:
        \t-poniżej znajduje się plansza, którą należy wypełnić znakami
        \t-wybór pola następuje poprzez określenie go w turze danego gracza 
        \t-wybór dokonywany jest za pomocą numerów
        
        \t!POWODZENIA!
        
        Poniżej znajduje się wzór tablicy
        
        \t   |   |
        \t 1 | 2 | 3 \t {g_1} --- {z_1}
        \t___|___|___
        \t   |   |
        \t 4 | 5 | 6 \t vs----
        \t___|___|___         
        \t   |   |
        \t 7 | 8 | 9 \t {g_2} --- {z_2}
        \t   |   |   
        
        \t!DO BOJU!""".format(g_1=imie_1,z_1=znak_gracza_1,g_2=imie_2,z_2=znak_gracza_2))

def lista_ruchow():
    """Tworzy listę dostępnych ruchów, które naniesione zostaną na planszę"""
    global lista_ruchow, list_of_moves
    lista_ruchow = ["1","2","3","4","5","6","7","8","9"]
    list_of_moves = []
    return lista_ruchow, list_of_moves

def move_check(wybor,name):
    """
    INPUT --> player choice 
    OUTPUT -> True or False (based on possibility of player`s move)
    """
#    if wybor in range(1,10):
#        return lista_ruchow[wybor-1].isdigit()
#    else:
#        return True
    if wybor in range(1,10) and lista_ruchow[wybor-1].isdigit():
        return True
    elif wybor in range(1,10) and not lista_ruchow[wybor-1].isdigit():
        print("{} wybrałeś niedostepne miejsce.".format(name))
    elif wybor not in range(1,10):
        print("{} NIE SZALEJ wybrałeś pole poza planszą.".format(name))
    else:
        return False

def tablica_gry():
    """Wyświetla obecną tablicę w grze. Potem pojawią się wybrane pola obsadzone X lub O"""
    tablica = """
           |   |
         {A} | {B} | {C} \t {g_1} --- {z_1}
        ___|___|___
           |   |
         {D} | {E} | {F} \t vs----
        ___|___|___         
           |   |
         {G} | {H} | {I} \t {g_2} --- {z_2}
           |   |         
        """

    print(tablica.format(g_1=imie_1,z_1=znak_gracza_1,g_2=imie_2,z_2=znak_gracza_2,A=lista_ruchow[0],B=lista_ruchow[1],C=lista_ruchow[2],D=lista_ruchow[3],E=lista_ruchow[4],F=lista_ruchow[5],G=lista_ruchow[6],H=lista_ruchow[7],I=lista_ruchow[8]))

    
def win_check():
    """lista warunków zwycięstwa"""
    #można też lista_ruchow[0] == lista_ruchow [1] == lista_ruchow_2 == WYBRANY_ZNAK - jak zdefiniujesz to ulatwia
    war_X = ["X","X","X"] 
    war_X1 = war_X in (lista_ruchow[0:3],lista_ruchow[3:6],lista_ruchow[6:9])
    war_X2 = war_X in ([lista_ruchow[0],lista_ruchow[3],lista_ruchow[6]],[lista_ruchow[1],lista_ruchow[4],lista_ruchow[7]],[lista_ruchow[2],lista_ruchow[5],lista_ruchow[8]])
    war_X3 = war_X in ([lista_ruchow[0],lista_ruchow[4],lista_ruchow[8]],[lista_ruchow[2],lista_ruchow[4],lista_ruchow[6]])
    war_O = ["O","O","O"] 
    war_O1 = war_O in (lista_ruchow[0:3],lista_ruchow[3:6],lista_ruchow[6:9])
    war_O2 = war_O in ([lista_ruchow[0],lista_ruchow[3],lista_ruchow[6]],[lista_ruchow[1],lista_ruchow[4],lista_ruchow[7]],[lista_ruchow[2],lista_ruchow[5],lista_ruchow[8]])
    war_O3 = war_O in ([lista_ruchow[0],lista_ruchow[4],lista_ruchow[8]],[lista_ruchow[2],lista_ruchow[4],lista_ruchow[6]])
    if war_X1 == True or war_X2 == True or war_X3 == True:
        print("!!!BRAWO {} WYGRAŁEŚ!!!".format(player_x))
        win = True
        return win
    elif war_O1 == True or war_O2 == True or war_O3 == True:
        print("!!!BRAWO {} WYGRAŁEŚ!!!".format(player_o))
        win = True
        return win
    elif len(list_of_moves) == 9:
        win = "draw"
        return win
    else:
        print("!GRAMY DALEJ!")
        win = False
        return win
    
def ruch_gracza():
    """pętla ruchów graczy
    --- do rozwinięcia - uniemożliwić zajęcie już zajmowanego pola"""
    win = False
    gracz = 1
    wybor = None
    while win == False:
        while gracz == 1 and win == False:
            print("""
            Ok {} Twoja kolej
            pamiętaj, że grasz {}
            Obecna tablica do gry wygląda tak:""".format(imie_1, znak_gracza_1))
            print(tablica_gry())
            wybor = input(print("Które pole wybierasz? "))
            try:
                wybor = int(wybor)
                if move_check(wybor,imie_1) == True:
                    lista_ruchow[wybor-1] = znak_gracza_1
                    list_of_moves.append(znak_gracza_1)
                    gracz *= -1
                    win = win_check()
                else:
                    #print("Oj {}  głuptasie wziąłeś zajęte. Będziesz musiał spróbować ponownie.".format(imie_1))
                    break
            except ValueError:
                print("To nie jest numer.")
        while gracz == -1 and win == False:
            print("""
            Ok {} Twoja kolej
            pamiętaj, że grasz {}
            Obecna tablica do gry wygląda tak:""".format(imie_2, znak_gracza_2))
            tablica_gry()
            wybor = input(print("Które pole wybierasz? "))
            try:
                wybor = int(wybor)
                if move_check(wybor,imie_2) == True:
                    lista_ruchow[wybor-1] = znak_gracza_2
                    list_of_moves.append(znak_gracza_2)
                    gracz *= -1
                    win = win_check()
                else:
                    #print("Oj {} głuptasie wziąłeś zajęte. Będziesz musiał spróbować ponownie.".format(imie_2))
                    break
            except ValueError:
                print("To nie jest numer.")
    tablica_gry()
    if win == "draw":
        print("{} i {} osiągnęli REMIS - niekt nie wygrał.".format(imie_1,imie_2))
    print("KONIEC GRY!")

#def play():
#    wybor = input("Rozpocząć rozgrywkę? Y/N :").upper()
#    if wybor == "Y":
#        return True
#    else:
#        return False

def main():
    """funkcja główna"""
#    while play() == True:
    wybor_znaku_gracza()
    zasady()
    lista_ruchow()
    win_check()
    ruch_gracza()
#    else:
#        print("Dziękuję za spędzony czas.")

main()
