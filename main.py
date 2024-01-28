import tkinter as tk

def verificar_ganador():
    for combinacion in combinaciones_ganadoras:
        simbolo = botones[combinacion[0][0]][combinacion[0][1]].cget("text")
        if simbolo and all(botones[i][j].cget("text") == simbolo for i, j in combinacion):
            return simbolo

    return None


def verificar_empate():
    for fila in range(3):
        for columna in range(3):
            if not botones[fila][columna].cget("text"):
                return False  
            
    return True


def manejar_clic(fila, columna):
    global jugador_actual
    text = "X" if jugador_actual == "O" else "O"
    boton = botones[fila][columna]
    boton.configure(text=text, state="disable")
    jugador_actual = text
    ganador = verificar_ganador()
    empate = verificar_empate()
    if ganador:
        label_turno.configure(text=f"{ganador} es el ganador!")
        for fila in range(3):
            for columna in range(3):
                boton = botones[fila][columna]
                boton.configure(state="disable")
        boton_play_again.configure(state="normal")
        boton_play_again.grid(row=5, column=0, columnspan=3)
    elif empate:
        boton_play_again.configure(state="normal")
        label_turno.configure(text="¡No hubo ganador! Es un empate.")
        boton_play_again.grid(row=5, column=0, columnspan=3)

jugador_actual = "X"

combinaciones_ganadoras = [
    # Combinaciones ganadoras horizontales
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    
    # Combinaciones ganadoras verticales
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    
    # Combinaciones ganadoras diagonales
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

def reiniciar_juego():
    for fila in range(3):
        for columna in range(3):
            boton = botones[fila][columna]
            boton.configure(text="", state="normal")
            boton_play_again.configure(state="disabled")
            label_turno.configure(text="")

def cerrar_aplicacion():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("TIC TAC TOE")

botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(ventana, text="", width=10, height=4,font=("Helvetica", 16), command=lambda f=fila, c=columna: manejar_clic(f, c))
        boton.grid(row=fila, column=columna)
        fila_botones.append(boton)
    botones.append(fila_botones)

label_turno = tk.Label(ventana, text="", font=("Helvetica", 14))
label_turno.grid(row=3, column=0, columnspan=3)

boton_salir = tk.Button(ventana, text="Exit", command=cerrar_aplicacion)
boton_salir.grid(row=4, column=0, columnspan=3)

boton_play_again = tk.Button(ventana, text="Play Again", command=reiniciar_juego)

ventana.mainloop()
