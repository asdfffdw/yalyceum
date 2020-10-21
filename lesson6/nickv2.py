start_rock = int(input())
rock_user = int(input())
rock_system = 2
while start_rock != 0:
    if (rock_user < 4) and (rock_user > 0):
        start_rock = start_rock - rock_user
        print(rock_user, start_rock)
        start_rock = start_rock - rock_system
        print(rock_system, start_rock)
        rock_user = int(input())
    else:
        print('Некорректный ход:', rock_user)
        rock_user = int(input())