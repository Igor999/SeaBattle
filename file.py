player = []
computer = []
player_ban = []
computer_ban = []

def ErrorPosition(ship, pl_ban):
    if ship in pl_ban:
        print("Данная координата занята или вы ставите впритык к другому окраблю, попробуйте снова")
        return True
    elif ship[0] < 0 or ship[0] > 5 or ship[1] < 0 or ship[1] > 5:
        print("Вы вышли за пределы поля боя, попробуйте снова")
        return True
    else:
        return False

def BorderAndCorner(ban):
    global player_ban
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

SP = Ship(player, computer)
SP.ShowTablePlayer()


ban = []
third = ((int(input("Введите первую координату первой палубы трехпалубника: "))-1),
        (int(input("Введите вторую координату первой палубы трехпалубника: "))-1))
player.append(third)
player_ban.append(third)
ban.append(third)
SP = Ship(player, computer)
SP.ShowTablePlayer()

# third вместо second_third чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    third = ((int(input("Введите первую координату второй палубы трехпалубника: "))-1),
             (int(input("Введите вторую координату второй палубы трехпалубника: "))-1))
    TrueFalse = ErrorPosition(third, player_ban)
player.append(third)
player_ban.append(third)
ban.append(third)
SP = Ship(player, computer)
SP.ShowTablePlayer()

# third вместо second_third чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    third = ((int(input("Введите первую координату третьей палубы трехпалубника: "))-1),
             (int(input("Введите вторую координату третьей палубы трехпалубника: "))-1))
    TrueFalse = ErrorPosition(third, player_ban)
player.append(third)
player_ban.append(third)
ban.append(third)
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban)
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
SP = Ship(player, computer)
SP.ShowTablePlayer()

# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = ((int(input("Введите первую координату второй палубы первого двупалубника: "))-1),
           (int(input("Введите вторую координату второй палубы первого двупалубника: "))-1),)
    TrueFalse = ErrorPosition(two, player_ban)
player.append(two)
player_ban.append(two)
ban.append(two)
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban)
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
SP = Ship(player, computer)
SP.ShowTablePlayer()

# two вместо second_two чтобы не забивать память (перезапись переменной)
TrueFalse = True
while TrueFalse == True:
    two = ((int(input("Введите первую координату второй палубы второго двупалубника: ")) - 1),
           (int(input("Введите вторую координату второй палубы второго двупалубника: ")) - 1),)
    TrueFalse = ErrorPosition(two, player_ban)
player.append(two)
player_ban.append(two)
ban.append(two)
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban)
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
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban)
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
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban)
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
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban)
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
SP = Ship(player, computer)
SP.ShowTablePlayer()
BorderAndCorner(ban)
print("Нельзя ставить: ", player_ban)



print(player)

