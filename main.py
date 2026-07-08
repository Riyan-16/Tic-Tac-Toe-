from tkinter import *


def next_turn(row, column):
    global player

    if buttons[row][column]["text"] == "" and check_winner() == False:

        buttons[row][column]["text"] = "X"

        if check_winner() == False:
            label.config(text="Computer's Turn")
            window.after(500, ai_move)

        elif check_winner() == True:
            label.config(text="You Win!")

        else:
            label.config(text="Tie!")


def ai_move():
    best_score = -1000
    move = None

    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                buttons[row][col]["text"] = "O"
                score = minimax(False)
                buttons[row][col]["text"] = ""

                if score > best_score:
                    best_score = score
                    move = (row, col)

    if move:
        buttons[move[0]][move[1]]["text"] = "O"

    if check_winner() == False:
        label.config(text="Your Turn")

    elif check_winner() == True:
        label.config(text="Computer Wins!")

    else:
        label.config(text="Tie!")


def minimax(is_maximizing):

    result = evaluate()

    if result is not None:
        return result

    if is_maximizing:

        best_score = -1000

        for row in range(3):
            for col in range(3):
                if buttons[row][col]["text"] == "":
                    buttons[row][col]["text"] = "O"
                    score = minimax(False)
                    buttons[row][col]["text"] = ""
                    best_score = max(score, best_score)

        return best_score

    else:

        best_score = 1000

        for row in range(3):
            for col in range(3):
                if buttons[row][col]["text"] == "":
                    buttons[row][col]["text"] = "X"
                    score = minimax(True)
                    buttons[row][col]["text"] = ""
                    best_score = min(score, best_score)

        return best_score


def evaluate():

    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            if buttons[row][0]["text"] == "O":
                return 1
            else:
                return -1

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            if buttons[0][col]["text"] == "O":
                return 1
            else:
                return -1

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        if buttons[0][0]["text"] == "O":
            return 1
        else:
            return -1

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        if buttons[0][2]["text"] == "O":
            return 1
        else:
            return -1

    if not empty_spaces():
        return 0

    return None


def check_winner():

    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    if not empty_spaces():
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="yellow")
        return "Tie"

    return False


def empty_spaces():

    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return True

    return False


def new_game():

    label.config(text="Your Turn")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")


window = Tk()
window.title("Tic Tac Toe with Minimax")

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(window, text="Your Turn", font=("consolas", 30))
label.pack()

restart = Button(window, text="Restart", font=("consolas", 20), command=new_game)
restart.pack()

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(
            frame,
            text="",
            font=("consolas", 40),
            width=5,
            height=2,
            command=lambda r=row, c=col: next_turn(r, c)
        )
        buttons[row][col].grid(row=row, column=col)

window.mainloop()