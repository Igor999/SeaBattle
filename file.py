import random

player = []
player_ones = []
player_twoes1 = []
player_twoes2 = []
player_threes = []
computer = []
computer_ones = []
computer_twoes1 = []
computer_twoes2 = []
computer_threes = []
player_ban = []
computer_ban = []
player_shots_yes = []
player_shots_no = []
computer_shots_yes = []
computer_shots_no = []

def TryExc(first, second):
    try:
        coor = ((int(input(first)) - 1),
                (int(input(second)) - 1))
    except ValueError:
        print("Вы не ввели координату")
        return TryExc(first, second)
    else:
        return coor

def ErrorPosition(ship, pl_ban):
    if ship in pl_ban:
        print("Данная координата занята или вы ставите впритык к другому кораблю, попробуйте снова")
        return True
    elif ship[0] < 0 or ship[0] > 5 or ship[1] < 0 or ship[1] > 5:
        print("Вы вышли за пределы поля боя, попробуйте снова")
        return True
    else:
        return False


def BorderAndCorner(ban, PorC):
    global player_ban
    global computer_ban
    if PorC == 0:
        for keep in ban:
            print("Кип ", keep)
            player_ban.append((keep[0] - 1, keep[1] - 1))
            player_ban.append((keep[0] - 1, keep[1]))
            player_ban.append((keep[0] - 1, keep[1] + 1))
            player_ban.append((keep[0], keep[1] - 1))
            player_ban.append((keep[0], keep[1] + 1))
            player_ban.append((keep[0] + 1, keep[1] - 1))
            player_ban.append((keep[0] + 1, keep[1]))
            player_ban.append((keep[0] + 1, keep[1] + 1))
        counters = []
        for point in player_ban:
            if point[0] < 0 or point[1] < 0 or point[0] > 5 or point[1] > 5:
                counters.append(point)
        for BadNumbers in counters:
            player_ban.remove(BadNumbers)
        return player_ban
    if PorC == 1:
        for keep in ban:
            computer_ban.append((keep[0] - 1, keep[1] - 1))
            computer_ban.append((keep[0] - 1, keep[1]))
            computer_ban.append((keep[0] - 1, keep[1] + 1))
            computer_ban.append((keep[0], keep[1] - 1))
            computer_ban.append((keep[0], keep[1] + 1))
            computer_ban.append((keep[0] + 1, keep[1] - 1))
            computer_ban.append((keep[0] + 1, keep[1]))
            computer_ban.append((keep[0] + 1, keep[1] + 1))
        counters = []
        for point in player_ban:
            if point[0] < 0 or point[1] < 0 or point[0] > 5 or point[1] > 5:
                counters.append(point)
        for BadNumbers in counters:
            player_ban.remove(BadNumbers)
        return computer_ban


class Ship:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def ShowTablePlayer(self):
        for i in range(6):
            for j in range(6):
                if (i, j) in self.player:
                    print("| ■ ", end='')
                else:
                    print("| O ", end='')
            print("|")

    def ShowTableComputer(self):
        for i in range(6):
            for j in range(6):
                if (i, j) in self.computer:
                    print("| ■ ", end='')
                else:
                    print("| O ", end='')
            print("|")


class Battle:
    def __init__(self, player_shots_yes, player_shots_no, computer_shots_yes, computerr_shots_no):
        self.player_shots_yes = player_shots_yes
        self.player_shots_no = player_shots_no
        self.computer_shots_yes = computer_shots_yes
        self.computerr_shots_no = computerr_shots_no
    def ShowTablePlayer(self):
        for i in range(6):
            for j in range(6):
                if (i, j) in self.player_shots_yes:
                    print("| T ", end='')
                elif (i, j) in self.player_shots_no:
                    print("| X ", end='')
                else:
                    print("| O ", end='')
            print("|")

    def ShowTableComputer(self):
        for i in range(6):
            for j in range(6):
                if (i, j) in self.computer_shots_yes:
                    print("| T ", end='')
                elif (i, j) in self.computer_shots_no:
                    print("| X ", end='')
                else:
                    print("| O ", end='')
            print("|")


class ShipTypes:
    def __init__(self, coordinates, new_coordinates):
        self.coordinates = coordinates
        self.new_coordinates = new_coordinates

    def Deck(self):
        if len(self.coordinates) == 1:
            if (self.coordinates[0][0] + 1, self.coordinates[0][1]) == self.new_coordinates:
                return False
            elif (self.coordinates[0][0] - 1, self.coordinates[0][1]) == self.new_coordinates:
                return False
            elif (self.coordinates[0][0], self.coordinates[0][1] - 1) == self.new_coordinates:
                return False
            elif (self.coordinates[0][0], self.coordinates[0][1] + 1) == self.new_coordinates:
                return False
            else:
                print("Корабль разделить невозможно")
                return True
        elif len(self.coordinates) == 2:
            if (self.coordinates[0][0], self.coordinates[0][1]) != self.new_coordinates and (
            self.coordinates[1][0], self.coordinates[1][1]) != self.new_coordinates:
                if (self.coordinates[0][0] + 1, self.coordinates[0][1]) == self.new_coordinates:
                    return False
                elif (self.coordinates[0][0] - 1, self.coordinates[0][1]) == self.new_coordinates:
                    return False
                elif (self.coordinates[0][0], self.coordinates[0][1] - 1) == self.new_coordinates:
                    return False
                elif (self.coordinates[0][0], self.coordinates[0][1] + 1) == self.new_coordinates:
                    return False
                elif (self.coordinates[1][0] + 1, self.coordinates[1][1]) == self.new_coordinates:
                    return False
                elif (self.coordinates[1][0] - 1, self.coordinates[1][1]) == self.new_coordinates:
                    return False
                elif (self.coordinates[1][0], self.coordinates[1][1] - 1) == self.new_coordinates:
                    return False
                elif (self.coordinates[1][0], self.coordinates[1][1] + 1) == self.new_coordinates:
                    return False
                else:
                    print("Корабль разделить невозможно")
                    return True
            else:
                return True


# РАССТАНОВКА КОРАБЛЕЙ КОМПЬЮТЕРА

print("Поле компьютера")
SP = Ship(player, computer)
SP.ShowTableComputer()

ban = []
TrueFalse = True
while TrueFalse == True:
    third = (random.randint(0, 5), random.randint(0, 5))
    # print(third)
    TrueFalse = ErrorPosition(third, computer_ban)
computer.append(third)
computer_threes.append(third)
computer_ban.append(third)
ban.append(third)
# print("Поле компьютера")
# SP = Ship(player, computer)
# SP.ShowTableComputer()
print("Компьютер поставил первую палубу трепалубного")
coordinates_of_deck = [third]

# third вместо second_third чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    third = (random.randint(0, 5), random.randint(0, 5))
    # print(third)
    TrueFalse = ErrorPosition(third, computer_ban)
    if TrueFalse == True:
        continue
    else:
        DeckRes = ShipTypes(coordinates_of_deck, third)
        TrueFalse = DeckRes.Deck()
computer.append(third)
computer_threes.append(third)
computer_ban.append(third)
ban.append(third)
print("Компьютер поставил вторую палубу трехпалубного")
# SP = Ship(player, computer)
# SP.ShowTableComputer()
coordinates_of_deck.append(third)

# third вместо second_third чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    third = (random.randint(0, 5), random.randint(0, 5))
    # print(third)
    TrueFalse = ErrorPosition(third, computer_ban)
    if TrueFalse == True:
        continue
    else:
        DeckRes = ShipTypes(coordinates_of_deck, third)
        TrueFalse = DeckRes.Deck()
computer.append(third)
computer_threes.append(third)
computer_ban.append(third)
ban.append(third)
print("Компьютер поставил третью палубу трехпалубного")
# SP = Ship(player, computer)
# SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
# print("Нельзя ставить: ", computer_ban)

ban = []
TrueFalse = True
while TrueFalse == True:
    two = (random.randint(0, 5), random.randint(0, 5))
    # print(two)
    TrueFalse = ErrorPosition(two, computer_ban)
computer.append(two)
computer_twoes1.append(two)
computer_ban.append(two)
ban.append(two)
print("Компьютер поставил первую палубу первого двухпалубного")
# SP = Ship(player, computer)
# SP.ShowTableComputer()
coordinates_of_deck = [two]

# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = (random.randint(0, 5), random.randint(0, 5))
    # print(two)
    TrueFalse = ErrorPosition(two, computer_ban)
    if TrueFalse == True:
        continue
    else:
        DeckRes = ShipTypes(coordinates_of_deck, two)
        TrueFalse = DeckRes.Deck()
computer.append(two)
computer_twoes1.append(two)
computer_ban.append(two)
ban.append(two)
print("Компьютер поставил вторую палубу первого двухпалубного")
# SP = Ship(player, computer)
# SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
# print("Нельзя ставить: ", computer_ban)

ban = []
# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = (random.randint(0, 5), random.randint(0, 5))
    # print(two)
    TrueFalse = ErrorPosition(two, computer_ban)
computer.append(two)
computer_twoes2.append(two)
computer_ban.append(two)
ban.append(two)
print("Компьютер поставил первую палубу второго двухпалубного")
# SP = Ship(player, computer)
# SP.ShowTableComputer()
coordinates_of_deck = [two]

# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = (random.randint(0, 5), random.randint(0, 5))
    # print(two)
    TrueFalse = ErrorPosition(two, computer_ban)
    if TrueFalse == True:
        continue
    else:
        DeckRes = ShipTypes(coordinates_of_deck, two)
        TrueFalse = DeckRes.Deck()
computer.append(two)
computer_twoes2.append(two)
computer_ban.append(two)
ban.append(two)
print("Компьютер поставил вторую палубу второго двухпалубного")
# SP = Ship(player, computer)
# SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
# print("Нельзя ставить: ", computer_ban)

ban = []
TrueFalse = True
while TrueFalse == True:
    one = (random.randint(0, 5), random.randint(0, 5))
    # print(one)
    TrueFalse = ErrorPosition(one, computer_ban)
computer.append(one)
computer_ones.append(one)
computer_ban.append(one)
ban.append(one)
print("Компьютер поставил первый однопалубный")
# SP = Ship(player, computer)
# SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
# print("Нельзя ставить: ", computer_ban)

ban = []
# one вместо second_one чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    one = (random.randint(0, 5), random.randint(0, 5))
    # print(one)
    TrueFalse = ErrorPosition(one, computer_ban)
computer.append(one)
computer_ones.append(one)
computer_ban.append(one)
ban.append(one)
print("Компьютер поставил второй однопалубный")
# SP = Ship(player, computer)
# SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
# print("Нельзя ставить: ", computer_ban)

ban = []
# one вместо second_one чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    one = (random.randint(0, 5), random.randint(0, 5))
    # print(one)
    TrueFalse = ErrorPosition(one, computer_ban)
computer.append(one)
computer_ones.append(one)
computer_ban.append(one)
ban.append(one)
print("Компьютер поставил третий однопалубный")
# SP = Ship(player, computer)
# SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
# print("Нельзя ставить: ", computer_ban)

ban = []
# one вместо second_one чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    one = (random.randint(0, 5), random.randint(0, 5))
    # print(one)
    TrueFalse = ErrorPosition(one, computer_ban)
computer.append(one)
computer_ones.append(one)
computer_ban.append(one)
ban.append(one)
print("Компьютер поставил четвертый однопалубный")
# SP = Ship(player, computer)
# SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
# print("Нельзя ставить: ", computer_ban)

# УСТАНОВКА КОРАБЛЕЙ ИГРОКА


print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()

ban = []
TrueFalse = True
while TrueFalse == True:
    third = TryExc("Введите первую координату первой палубы трехпалубника: ",
                  "Введите вторую координату первой палубы трехпалубника: ")
    TrueFalse = ErrorPosition(third, player_ban)
player.append(third)
player_threes.append(third)
player_ban.append(third)
ban.append(third)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
coordinates_of_deck = [third]

# third вместо second_third чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    third = TryExc("Введите первую координату второй палубы трехпалубника: ",
                 "Введите вторую координату второй палубы трехпалубника: ")
    TrueFalse = ErrorPosition(third, player_ban)
    if TrueFalse == True:
        continue
    else:
        DeckRes = ShipTypes(coordinates_of_deck, third)
        TrueFalse = DeckRes.Deck()
player.append(third)
player_threes.append(third)
player_ban.append(third)
ban.append(third)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
coordinates_of_deck.append(third)

# third вместо second_third чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    third = TryExc("Введите первую координату третьей палубы трехпалубника: ",
                 "Введите вторую координату третьей палубы трехпалубника: ")
    TrueFalse = ErrorPosition(third, player_ban)
    if TrueFalse == True:
        continue
    else:
        DeckRes = ShipTypes(coordinates_of_deck, third)
        TrueFalse = DeckRes.Deck()
player.append(third)
player_threes.append(third)
player_ban.append(third)
ban.append(third)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban, PorC=0)
print("Нельзя ставить: ", player_ban)

ban = []
TrueFalse = True
while TrueFalse == True:
    two = TryExc("Введите первую координату первой палубы первого двупалубника: ",
                  "Введите вторую координату первой палубы первого двупалубника: ")
    TrueFalse = ErrorPosition(two, player_ban)
player.append(two)
player_twoes1.append(two)
player_ban.append(two)
ban.append(two)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
coordinates_of_deck = [two]

# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = TryExc("Введите первую координату второй палубы первого двупалубника: ",
           "Введите вторую координату второй палубы первого двупалубника: ")
    TrueFalse = ErrorPosition(two, player_ban)
    if TrueFalse == True:
        continue
    else:
        DeckRes = ShipTypes(coordinates_of_deck, two)
        TrueFalse = DeckRes.Deck()
player.append(two)
player_twoes1.append(two)
player_ban.append(two)
ban.append(two)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban, PorC=0)
print("Нельзя ставить: ", player_ban)

ban = []
# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = TryExc("Введите первую координату первой палубы второго двупалубника: ",
           "Введите вторую координату первой палубы второго двупалубника: ")
    TrueFalse = ErrorPosition(two, player_ban)
player.append(two)
player_twoes2.append(two)
player_ban.append(two)
ban.append(two)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
coordinates_of_deck = [two]

# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = TryExc("Введите первую координату второй палубы второго двупалубника: ",
           "Введите вторую координату второй палубы второго двупалубника: ")
    TrueFalse = ErrorPosition(two, player_ban)
    if TrueFalse == True:
        continue
    else:
        DeckRes = ShipTypes(coordinates_of_deck, two)
        TrueFalse = DeckRes.Deck()
player.append(two)
player_twoes2.append(two)
player_ban.append(two)
ban.append(two)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban, PorC=0)
print("Нельзя ставить: ", player_ban)

ban = []
TrueFalse = True
while TrueFalse == True:
    one = TryExc("Введите первую координату первого однопалубника: ",
           "Введите вторую координату первого однопалубника: ")
    TrueFalse = ErrorPosition(one, player_ban)
player.append(one)
player_ones.append(one)
player_ban.append(one)
ban.append(one)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban, PorC=0)
print("Нельзя ставить: ", player_ban)

ban = []
# one вместо second_one чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    one = TryExc("Введите первую координату второго однопалубника: ",
           "Введите вторую координату второго однопалубника: ")
    TrueFalse = ErrorPosition(one, player_ban)
player.append(one)
player_ones.append(one)
player_ban.append(one)
ban.append(one)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban, PorC=0)
print("Нельзя ставить: ", player_ban)

ban = []
# one вместо second_one чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    one = TryExc("Введите первую координату третьего однопалубника: ",
           "Введите вторую координату третьего однопалубника: ")
    TrueFalse = ErrorPosition(one, player_ban)
player.append(one)
player_ones.append(one)
player_ban.append(one)
ban.append(one)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban, PorC=0)
print("Нельзя ставить: ", player_ban)

ban = []
# one вместо second_one чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    one = TryExc("Введите первую координату четвертого однопалубника: ",
           "Введите вторую координату четвертого однопалубника: ")
    TrueFalse = ErrorPosition(one, player_ban)
player.append(one)
player_ones.append(one)
player_ban.append(one)
ban.append(one)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban, PorC=0)
print("Нельзя ставить: ", player_ban)

print(player)

# while True:
#     coin = int(input("Орел - 0, Решка - 1"))
#     if coin == 0 or coin == 1:
#         break
#     else:
#         print("Вы вышли за пределы вариантов выпадения монеты")

# first_step = random.randint(0, 1)
coin = 1
first_step = 1

threes = []
twoes = []
def play(coin, first_step):
    global threes
    global twoes
    global player_shots_no
    global player_shots_yes
    global player_ones
    global player_threes
    global player_twoes1
    global player_twoes2
    global computer_shots_yes
    global computer_shots_no
    global computer_ones
    global computer_twoes1
    global computer_twoes2
    global computer_threes
    if len(player_shots_yes) == 11:
        print("Игрок победил")
        return True
    if len(computer_shots_yes) == 11:
        print("Компьютер победил")
        return True
    if coin == first_step:
        shot = TryExc("Введите первую координату: ", "Введите вторую координату: ")
        if shot in player_shots_yes:
            print("Вы сюда уже стреляли и попали")
            return play(coin, first_step)
        elif shot in player_shots_no:
            print("Вы сюда уже стреляли и НЕ попали либо здесь не может находиться корабль")
            return play(coin, first_step)
        else:
            if shot in computer:
                player_shots_yes.append(shot)
                if shot in computer_ones:
                    print("Убил")
                    player_shots_no.append((shot[0] - 1, shot[1] - 1))
                    player_shots_no.append((shot[0] - 1, shot[1]))
                    player_shots_no.append((shot[0] - 1, shot[1] + 1))
                    player_shots_no.append((shot[0], shot[1] - 1))
                    player_shots_no.append((shot[0], shot[1] + 1))
                    player_shots_no.append((shot[0] + 1, shot[1] - 1))
                    player_shots_no.append((shot[0] + 1, shot[1]))
                    player_shots_no.append((shot[0] + 1, shot[1] + 1))
                elif shot in computer_twoes1:
                    if len(computer_twoes1) > 1:
                        print("Ранил")
                        twoes.append(shot)
                        computer_twoes1.remove(shot)
                    else:
                        print("Убил")
                        twoes.append(shot)
                        computer_twoes1.remove(shot)
                        for paluba in twoes:
                            if paluba not in player_shots_yes:
                                player_shots_no.append((paluba[0] - 1, paluba[1] - 1))
                                player_shots_no.append((paluba[0] - 1, paluba[1]))
                                player_shots_no.append((paluba[0] - 1, paluba[1] + 1))
                                player_shots_no.append((paluba[0], paluba[1] - 1))
                                player_shots_no.append((paluba[0], paluba[1] + 1))
                                player_shots_no.append((paluba[0] + 1, paluba[1] - 1))
                                player_shots_no.append((paluba[0] + 1, paluba[1]))
                                player_shots_no.append((paluba[0] + 1, paluba[1] + 1))
                        twoes = []
                elif shot in computer_twoes2:
                    if len(computer_twoes2) > 1:
                        print("Ранил")
                        computer_twoes2.remove(shot)
                    else:
                        print("Убил")
                        computer_twoes2.remove(shot)
                        for paluba in twoes:
                            player_shots_no.append((paluba[0] - 1, paluba[1] - 1))
                            player_shots_no.append((paluba[0] - 1, paluba[1]))
                            player_shots_no.append((paluba[0] - 1, paluba[1] + 1))
                            player_shots_no.append((paluba[0], paluba[1] - 1))
                            player_shots_no.append((paluba[0], paluba[1] + 1))
                            player_shots_no.append((paluba[0] + 1, paluba[1] - 1))
                            player_shots_no.append((paluba[0] + 1, paluba[1]))
                            player_shots_no.append((paluba[0] + 1, paluba[1] + 1))
                        twoes = []
                elif shot in computer_threes:
                    if len(computer_threes) > 1:
                        print("Ранил")
                        computer_threes.remove(shot)
                    else:
                        print("Убил")
                        computer_threes.remove(shot)
                        for paluba in threes:
                            player_shots_no.append((paluba[0] - 1, paluba[1] - 1))
                            player_shots_no.append((paluba[0] - 1, paluba[1]))
                            player_shots_no.append((paluba[0] - 1, paluba[1] + 1))
                            player_shots_no.append((paluba[0], paluba[1] - 1))
                            player_shots_no.append((paluba[0], paluba[1] + 1))
                            player_shots_no.append((paluba[0] + 1, paluba[1] - 1))
                            player_shots_no.append((paluba[0] + 1, paluba[1]))
                            player_shots_no.append((paluba[0] + 1, paluba[1] + 1))
                        threes = []
                return play(coin, first_step)
            else:
                print("Мимо")
                player_shots_no.append(shot)
                if coin == 1:
                    coin = 0
                else:
                    coin = 1
                return play(coin, first_step)





play(coin, first_step)