board = [[' ' for _ in range(3)] for _ in range(3)]

def draw_board():
    for r in range(3):
        print(" " + board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if r != 2:
            print("---|---|---")

def check_win(player):
    # 가로, 세로, 대각선 확인
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_full():
    return all([cell != ' ' for row in board for cell in row])

while True:
    draw_board()
    try:
        x = int(input("다음 수의 x좌표 (0~2)를 입력하시오: "))
        y = int(input("다음 수의 y좌표 (0~2)를 입력하시오: "))
        if x not in range(3) or y not in range(3):
            print("범위를 벗어난 좌표입니다.")
            continue
    except ValueError:
        print("숫자를 입력해주세요.")
        continue

    if board[y][x] != ' ':
        print("이미 차 있는 자리입니다.")
        continue
    board[y][x] = 'X'
    if check_win('X'):
        draw_board()
        print("사용자 승리!")
        break
    if is_full():
        draw_board()
        print("무승부입니다!")
        break

    # 컴퓨터 턴
    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                done = True
                break
        if done:
            break
    if check_win('O'):
        draw_board()
        print("컴퓨터 승리!")
        break
    if is_full():
        draw_board()
        print("무승부입니다!")
        break
