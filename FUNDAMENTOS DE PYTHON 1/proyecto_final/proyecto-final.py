from random import randrange

def display_board(board): # Crea el caudro con los espacios.
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|      " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    ok = False # Se pone así para entrar en el bucle.
    while not ok:
        move = input("Ingresa tu movimiento: ")
        ok = len(move) == 1 and move >= "1" and move <= "9" # Se valida lo que ingresa el usuario.
        if not ok:
            print("Movimiento erróneo, ingresa nuevamente") # se pide volver a ingresar.
            continue
        move = int(move) - 1 # Número de celda del 0 al 8.
        row = move // 3      # Fila de la celda.
        col = move % 3       # Columna de la celda.
        sign = board[row][col] # Marca el cuadro elegido.
        ok = sign not in ["O","X"]
        if not ok:
            print("¡Cuadro ocupado, ingresa nuevamente!")
            continue
        board[row][col] = "O" # Colocar '0' al cuadro seleccionado.

def make_list_of_free_fields(board):
    free = [] # La lista está vacía al inicio.
    for row in range(3): # Se itera a través de las filas.
        for col in range(3): # Itera en las columnas.
            if board[row][col] not in ["O","X"]:# Está la celda libre.
                free.append((row.col)) # Agrega una nueva tupla a la lista.
    return free

def victory_for(board,sgn):
    if sgn == "X": # ¿Estamos buscando 'X'?
        who = "me" # Sí, es la máquina.
    elif sgn == "O": # ... ¿O estámos buscando 'O'?
        who = "you" # Sí, es el usuario.
    else:
        who = None # ¡No debemos caer aquí!
    cross1 = croos2 = True # Para las diagolanes
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn: # check row rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
            return who
        if board[rc][rc] != sgn: # revisar la primer diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sgn: # revisar la segunda diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None

def draw_move(board):
	free = make_list_of_free_fields(board) # crea una lista de los cuadros vacios o libres
	cnt = len(free)
	if cnt > 0:	# si la lista no esta vacía, elegir un lugar para 'X' y colocarla
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'