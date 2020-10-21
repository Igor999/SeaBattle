import random

player = []
computer = []
player_ban = []
computer_ban = []


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
computer_ban.append(one)
ban.append(one)
print("ПКомпьютер поставил четвертый однопалубный")
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
player_ban.append(one)
ban.append(one)
print("Поле игрока")
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban, PorC=0)
print("Нельзя ставить: ", player_ban)

print(player)