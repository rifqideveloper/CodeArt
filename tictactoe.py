import itertools
import time
start_time = time.time()

def win(courrent_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return  False

    # horizontal winner(-)
    for row in game:
        print(row)
        if all_same(row):
            print(f"player{row[0]} is winner horizonaly(-)")
            return True
    #vertical winner(|)
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"player{check[0]} is winner vertically(|)")
            return True
    #diagonal winner(/)(\)
    diags = []
    for col, row, in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"player{diags[0]} is winner diagonaly(/)")
        return True
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"player{diags[0]} is winner diagonaly(\\)")
        return True

    return False


#game board
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("posisi ini sudah ditempati silahkan pilih posisi lain.")
            return game_map, False
        #print('   0  1  2')
        print("   "+"  ".join([str(i) for i in range(game_size)]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("error: anda salah ketik coba lagi", e)
        return game_map, False
    except SyntaxError as e:
        print("error: ada kesalahan Syntax", e)
        return game_map, False
    except Exception as e:
        print("erro: ada yang salah dengan cript", e)
        return game_map, False
    except:
        print("error: penyebab tidak diketahui??? silahkan keluar dan masuk game lagi")
        return game_map, False
#jika ada permainan selesai
play = True
player = [1, 2]
while play:
    '''game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
'''
    game_size = int(input("ukuran berapa game yang anda ingin mainkan??? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"current_player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("kolum mana yang anda ingin mainkan? (0, 1, 2,):  "))
            row_choice = int(input("row mana yang anda ingin mainkan? (0, 1, 2,):  "))
            game, played = game_board(game, current_player, row_choice, column_choice)
        if win(game):
            game_won = True
            again = input("game selesai, apa kalian ingin main lagi???.(y/t) ")
            if again.lower() == "y":
                print("memulai ulang....")
            elif again.lower() == "t":
                print("selamat tinggal")
                play = False
            else:
                print("anda salah ketik seharusnya(y/t).selamat tinggal!!?")
                play = False
print(time.time() - start_time, "detik(waktu selesai)")
