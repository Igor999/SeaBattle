import random


player = []
computer = []
player_ban = []
computer_ban = []


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
            if 0 <= keep[0] - 1 and 0 <= keep[1] - 1:
                if (keep[0] - 1, keep[1] - 1) not in player_ban:
                    player_ban.append((keep[0] - 1, keep[1] - 1))
            if 0 <= keep[0] - 1:
                if (0 <= keep[0] - 1, keep[1]) not in player_ban:
                    player_ban.append((keep[0] - 1, keep[1]))
            if 0 <= keep[0] - 1 and keep[1] + 1 < 6:
                if (keep[0] - 1, keep[1] + 1) not in player_ban:
                    player_ban.append((keep[0] - 1, keep[1] + 1))
            if 0 <= keep[1] - 1:
                if (keep[0], keep[1] - 1) not in player_ban:
                    player_ban.append((keep[0], keep[1] - 1))
            if keep[1] + 1 < 6:
                if (keep[0], keep[1] + 1) not in player_ban:
                    player_ban.append((keep[0], keep[1] + 1))
            if keep[0] + 1 < 6 and 0 <= keep[1] - 1:
                if (keep[0] + 1, keep[1] - 1) not in player_ban:
                    player_ban.append((keep[0] + 1, keep[1] - 1))
            if keep[0] + 1 < 6:
                if (keep[0] + 1, keep[1]) not in player_ban:
                    player_ban.append((keep[0] + 1, keep[1]))
            if keep[0] + 1 < 6 and keep[1] + 1 < 6:
                if (keep[0] + 1, keep[1] + 1) not in player_ban:
                    player_ban.append((keep[0] + 1, keep[1] + 1))
        return player_ban
    if PorC == 1:
        for keep in ban:
            if 0 <= keep[0] - 1 and 0 <= keep[1] - 1:
                if (keep[0] - 1, keep[1] - 1) not in computer_ban:
                    computer_ban.append((keep[0] - 1, keep[1] - 1))
            if 0 <= keep[0] - 1:
                if (0 <= keep[0] - 1, keep[1]) not in computer_ban:
                    computer_ban.append((keep[0] - 1, keep[1]))
            if 0 <= keep[0] - 1 and keep[1] + 1 < 6:
                if (keep[0] - 1, keep[1] + 1) not in computer_ban:
                    computer_ban.append((keep[0] - 1, keep[1] + 1))
            if 0 <= keep[1] - 1:
                if (keep[0], keep[1] - 1) not in computer_ban:
                    computer_ban.append((keep[0], keep[1] - 1))
            if keep[1] + 1 < 6:
                if (keep[0], keep[1] + 1) not in computer_ban:
                    computer_ban.append((keep[0], keep[1] + 1))
            if keep[0] + 1 < 6 and 0 <= keep[1] - 1:
                if (keep[0] + 1, keep[1] - 1) not in computer_ban:
                    computer_ban.append((keep[0] + 1, keep[1] - 1))
            if keep[0] + 1 < 6:
                if (keep[0] + 1, keep[1]) not in computer_ban:
                    computer_ban.append((keep[0] + 1, keep[1]))
            if keep[0] + 1 < 6 and keep[1] + 1 < 6:
                if (keep[0] + 1, keep[1] + 1) not in computer_ban:
                    computer_ban.append((keep[0] + 1, keep[1] + 1))
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

class ShipTypes:
    def __init__(self, coordinates, new_coordinates):
        self.coordinates = coordinates
        self.new_coordinates = new_coordinates
    def Deck(self):
        if len(self.coordinates) == 1:
            if (self.coordinates[0][0]+1, self.coordinates[0][1]) == self.new_coordinates:
                return False
            elif (self.coordinates[0][0]-1, self.coordinates[0][1]) == self.new_coordinates:
                return False
            elif (self.coordinates[0][0], self.coordinates[0][1]-1) == self.new_coordinates:
                return False
            elif (self.coordinates[0][0], self.coordinates[0][1]+1) == self.new_coordinates:
                return False
            else:
                print("Корабль разделить невозможно")
                return True
        elif len(self.coordinates) == 2:
            if (self.coordinates[0][0], self.coordinates[0][1]) != self.new_coordinates and (self.coordinates[1][0], self.coordinates[1][1]) != self.new_coordinates:
                if (self.coordinates[0][0] + 1, self.coordinates[0][1]) == self.new_coordinates:
                    return False
                elif (self.coordinates[0][0] - 1, self.coordinates[0][1]) == self.new_coordinates:
                    return False
                elif (self.coordinates[0][0], self.coordinates[0][1]-1) == self.new_coordinates:
                    return False
                elif (self.coordinates[0][0], self.coordinates[0][1]+1) == self.new_coordinates:
                    return False
                elif (self.coordinates[1][0] + 1, self.coordinates[1][1]) == self.new_coordinates:
                    return False
                elif (self.coordinates[1][0] - 1, self.coordinates[1][1]) == self.new_coordinates:
                    return False
                elif (self.coordinates[1][0], self.coordinates[1][1]-1) == self.new_coordinates:
                    return False
                elif (self.coordinates[1][0], self.coordinates[1][1]+1) == self.new_coordinates:
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
    print(third)
    TrueFalse = ErrorPosition(third, computer_ban)
computer.append(third)
computer_ban.append(third)
ban.append(third)
print("Поле компьютера")
SP = Ship(player, computer)
SP.ShowTableComputer()
coordinates_of_deck = [third]

# third вместо second_third чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    third = (random.randint(0, 5), random.randint(0, 5))
    print(third)
    TrueFalse = ErrorPosition(third, computer_ban)
    DeckRes = ShipTypes(coordinates_of_deck, third)
    TrueFalse = DeckRes.Deck()
computer.append(third)
computer_ban.append(third)
ban.append(third)
print("Поле компьютера")
SP = Ship(player, computer)
SP.ShowTableComputer()
coordinates_of_deck.append(third)

# third вместо second_third чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    third = (random.randint(0, 5), random.randint(0, 5))
    print(third)
    TrueFalse = ErrorPosition(third, computer_ban)
    if TrueFalse == True:
        continue
    else:
        DeckRes = ShipTypes(coordinates_of_deck, third)
        TrueFalse = DeckRes.Deck()
computer.append(third)
computer_ban.append(third)
ban.append(third)
print("Поле компьютера")
SP = Ship(player, computer)
SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
print("Нельзя ставить: ", computer_ban)


ban = []
TrueFalse = True
while TrueFalse == True:
    two = (random.randint(0, 5), random.randint(0, 5))
    print(two)
    TrueFalse = ErrorPosition(two, computer_ban)
computer.append(two)
computer_ban.append(two)
ban.append(two)
print("Поле компьютера")
SP = Ship(player, computer)
SP.ShowTableComputer()
coordinates_of_deck = [two]



# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = (random.randint(0, 5), random.randint(0, 5))
    print(two)
    TrueFalse = ErrorPosition(two, computer_ban)
    if TrueFalse == True:
        continue
    else:
        DeckRes = ShipTypes(coordinates_of_deck, two)
        TrueFalse = DeckRes.Deck()
computer.append(two)
computer_ban.append(two)
ban.append(two)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
print("Нельзя ставить: ", computer_ban)


ban = []
# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = (random.randint(0, 5), random.randint(0, 5))
    print(two)
    TrueFalse = ErrorPosition(two, computer_ban)
computer.append(two)
computer_ban.append(two)
ban.append(two)
print("Поле компьютера")
SP = Ship(player, computer)
SP.ShowTableComputer()
coordinates_of_deck = [two]

# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = (random.randint(0, 5), random.randint(0, 5))
    print(two)
    TrueFalse = ErrorPosition(two, computer_ban)
    if TrueFalse == True:
        continue
    else:
        DeckRes = ShipTypes(coordinates_of_deck, two)
        TrueFalse = DeckRes.Deck()
computer.append(two)
computer_ban.append(two)
ban.append(two)
print("Поле компьютера")
SP = Ship(player, computer)
SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
print("Нельзя ставить: ", computer_ban)

ban = []
TrueFalse = True
while TrueFalse == True:
    one = (random.randint(0, 5), random.randint(0, 5))
    print(one)
    TrueFalse = ErrorPosition(one, computer_ban)
computer.append(one)
computer_ban.append(one)
ban.append(one)
print("Поле компьютера")
SP = Ship(player, computer)
SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
print("Нельзя ставить: ", computer_ban)

ban = []
# one вместо second_one чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    one = (random.randint(0, 5), random.randint(0, 5))
    print(one)
    TrueFalse = ErrorPosition(one, computer_ban)
computer.append(one)
computer_ban.append(one)
ban.append(one)
print("Поле компьютера")
SP = Ship(player, computer)
SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
print("Нельзя ставить: ", computer_ban)

ban = []
# one вместо second_one чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    one = (random.randint(0, 5), random.randint(0, 5))
    print(one)
    TrueFalse = ErrorPosition(one, computer_ban)
computer.append(one)
computer_ban.append(one)
ban.append(one)
print("Поле компьютера")
SP = Ship(player, computer)
SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
print("Нельзя ставить: ", computer_ban)

ban = []
# one вместо second_one чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    one = (random.randint(0, 5), random.randint(0, 5))
    print(one)
    TrueFalse = ErrorPosition(one, computer_ban)
computer.append(one)
computer_ban.append(one)
ban.append(one)
print("Поле компьютера")
SP = Ship(player, computer)
SP.ShowTableComputer()
BorderAndCorner(ban, PorC=1)
print("Нельзя ставить: ", computer_ban)







# УСТАНОВКА КОРАБЛЕЙ ИГРОКА



print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()


ban = []
TrueFalse = True
while TrueFalse == True:
    third = ((int(input("Введите первую координату первой палубы трехпалубника: "))-1),
        (int(input("Введите вторую координату первой палубы трехпалубника: "))-1))
    TrueFalse = ErrorPosition(third, player_ban)
player.append(third)
player_ban.append(third)
ban.append(third)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
coordinates_of_deck = [third]


# third вместо second_third чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    third = ((int(input("Введите первую координату второй палубы трехпалубника: "))-1),
             (int(input("Введите вторую координату второй палубы трехпалубника: "))-1))
    TrueFalse = ErrorPosition(third, player_ban)
    DeckRes = ShipTypes(coordinates_of_deck, third)
    TrueFalse = DeckRes.Deck()
player.append(third)
player_ban.append(third)
ban.append(third)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
coordinates_of_deck.append(third)

# third вместо second_third чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    third = ((int(input("Введите первую координату третьей палубы трехпалубника: "))-1),
             (int(input("Введите вторую координату третьей палубы трехпалубника: "))-1))
    TrueFalse = ErrorPosition(third, player_ban)
    DeckRes = ShipTypes(coordinates_of_deck, third)
    TrueFalse = DeckRes.Deck()
player.append(third)
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
    two = ((int(input("Введите первую координату первой палубы первого двупалубника: "))-1),
           (int(input("Введите вторую координату первой палубы первого двупалубника: "))-1),)
    TrueFalse = ErrorPosition(two, player_ban)
player.append(two)
player_ban.append(two)
ban.append(two)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
coordinates_of_deck = [two]



# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = ((int(input("Введите первую координату второй палубы первого двупалубника: "))-1),
           (int(input("Введите вторую координату второй палубы первого двупалубника: "))-1),)
    TrueFalse = ErrorPosition(two, player_ban)
    DeckRes = ShipTypes(coordinates_of_deck, two)
    TrueFalse = DeckRes.Deck()
player.append(two)
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
    two = ((int(input("Введите первую координату первой палубы второго двупалубника: ")) - 1),
           (int(input("Введите вторую координату первой палубы второго двупалубника: ")) - 1),)
    TrueFalse = ErrorPosition(two, player_ban)
player.append(two)
player_ban.append(two)
ban.append(two)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
coordinates_of_deck = [two]

# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = ((int(input("Введите первую координату второй палубы второго двупалубника: ")) - 1),
           (int(input("Введите вторую координату второй палубы второго двупалубника: ")) - 1),)
    TrueFalse = ErrorPosition(two, player_ban)
    DeckRes = ShipTypes(coordinates_of_deck, two)
    TrueFalse = DeckRes.Deck()
player.append(two)
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
    one = ((int(input("Введите первую координату первого однопалубника: "))-1),
          (int(input("Введите вторую координату первого однопалубника: "))-1))
    TrueFalse = ErrorPosition(one, player_ban)
player.append(one)
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
    one = ((int(input("Введите первую координату второго однопалубника: "))-1),
           (int(input("Введите вторую координату второго однопалубника: "))-1))
    TrueFalse = ErrorPosition(one, player_ban)
player.append(one)
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
    one = ((int(input("Введите первую координату третьего однопалубника: "))-1),
           (int(input("Введите вторую координату третьего однопалубника: "))-1))
    TrueFalse = ErrorPosition(one, player_ban)
player.append(one)
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
    one = ((int(input("Введите первую координату четвертого однопалубника: "))-1),
           (int(input("Введите вторую координату четвертого однопалубника: "))-1))
    TrueFalse = ErrorPosition(one, player_ban)
player.append(one)
player_ban.append(one)
ban.append(one)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban, PorC=0)
print("Нельзя ставить: ", player_ban)

print(player)



