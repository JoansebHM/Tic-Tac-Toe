import tkinter as tk

def checkWinner():
    for combination in winCombinations:
        symbol = buttons[combination[0][0]][combination[0][1]].cget("text")
        if symbol and all(buttons[i][j].cget("text") == symbol for i, j in combination):
            return symbol
    return None


def checkTie():
    for row in range(3):
        for column in range(3):
            if not buttons[row][column].cget("text"):
                return False              
    return True


def playAgain():
    for row in range(3):
        for column in range(3):
            boton = buttons[row][column]
            boton.configure(state="disable")
    playAgainButton.configure(state="normal")
    playAgainButton.grid(row=5, column=0, columnspan=3)


def clickEvent(row, column):
    global currentPlayer
    text = "X" if currentPlayer == "O" else "O"
    boton = buttons[row][column]
    boton.configure(text=text, state="disable")
    currentPlayer = text
    winner = checkWinner()
    tie = checkTie()

    if winner:

        turnLabel.configure(text=f"{winner} Is the winner!")
        playAgain()
        
    elif tie:

        turnLabel.configure(text="There's no winner, it's a draw")
        playAgain()

currentPlayer = "X"

winCombinations = [
    # horizontal winning combinations
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    
    # vertical winning combinations
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    
    # diagonal winning combinations
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

def restartGame():
    for fila in range(3):
        for columna in range(3):
            boton = buttons[fila][columna]
            boton.configure(text="", state="normal")
            playAgainButton.configure(state="disabled")
            turnLabel.configure(text="")

def closeApp():
    window.destroy()

window = tk.Tk()
window.title("TIC TAC TOE")

buttons = []
for row in range(3):
    buttonsRow = []
    for column in range(3):
        boton = tk.Button(window, text="", width=10, height=4,font=("Helvetica", 16), command=lambda f=row, c=column: clickEvent(f, c))
        boton.grid(row=row, column=column)
        buttonsRow.append(boton)
    buttons.append(buttonsRow)

turnLabel = tk.Label(window, text="", font=("Helvetica", 14))
turnLabel.grid(row=3, column=0, columnspan=3)

exitButton = tk.Button(window, text="Exit", command=closeApp)
exitButton.grid(row=4, column=0, columnspan=3)

playAgainButton = tk.Button(window, text="Play Again", command=restartGame)

window.mainloop()
