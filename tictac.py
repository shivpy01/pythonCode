#tic tac toe game on cmd 


def board(position):
	
	print(position["1"]," |",position["2"],"|",position["3"])
	print("---|---|---")
	print(position["4"]," |",position["5"],"|",position["6"])
	print("---|---|---")
	print(position["7"]," |",position["8"],"|",position["9"])


position = {
"1" : "1",
"2" : "2",
"3" : "3",
"4" : "4",
"5" : "5",
"6" : "6",
"7" : "7",
"8" : "8",
"9" : "9",
}


board(position)


def player1():
	p = int(input("player 1 enter any position:  "))
	st = str(p)
	position[st] = "x"
	board(position)
	

def player2():
	po = int(input("player 2 enter any position:  "))
	sr = str(po)
	position[sr] = "o"
	board(position)
	

def condition():
	if position["1"]== position["2"] and position["2"] == position["3"]:
		
		if position["1"] == "x":
			print("player 1 win")
			exit()
			
		else:
			print("player 2 win")
			exit()

	elif position["4"]== position["5"] and position["5"] == position["6"]:
		
		if position["4"] == "x":
			print("player 1 win")
			exit()
			
		else:
			print("player 2 win")
			exit()

	elif position["7"]== position["8"] and position["8"] == position["9"]:
		
		if position["7"] == "x":
			print("player 1 win")
			exit()
			
		else:
			print("player 2 win")
			exit()

	elif position["1"]== position["4"] and position["4"] == position["7"]:
		if position["1"] == "x":
			
			print("player 1 win")
			exit()
			
		else:
			
			print("player 2 win")
			exit()

	elif position["2"]== position["5"] and position["5"] == position["8"]:
		if position["2"] == "x":
			
			print("player 1 win")
			exit()
			
		else:
			print("player 2 win")
			exit()

	elif position["3"]== position["6"] and position["6"] == position["9"]:
		if position["3"] == "x":
			
			print("player 1 win")
			exit()
			
		else:
			print("player 2 win")
			exit()

	elif position["1"]== position["5"] and position["5"] == position["9"]:
		if position["1"] == "x":
			
			print("player 1 win")
			exit()
			
		else:
			print("player 2 win")
			exit()
			
	elif position["3"]== position["5"] and position["5"] == position["7"]:
		if position["3"] == "x":
			
			print("player 1 win")
			exit()
		else:
			print("player 2 win")
			exit()

def condi():
	if position["1"]== position["2"] and position["2"] == position["3"]:
		if position["1"] == "x":
			print("player 1 win")
			exit()
		else:
			print("player 2 win")
			exit()

	elif position["4"]== position["5"] and position["5"] == position["6"]:
		if position["4"] == "x":
			print("player 1 win")
			exit()
		else:
			print("player 2 win")
			exit()

	elif position["7"]== position["8"] and position["8"] == position["9"]:
		if position["7"] == "x":
			print("player 1 win")
			exit()
		else:
			print("player 2 win")
			exit()

	elif position["1"]== position["4"] and position["4"] == position["7"]:
		if position["1"] == "x":
			print("player 1 win")
			exit()
		else:
			print("player 2 win")
			exit()

	elif position["2"]== position["5"] and position["5"] == position["8"]:
		if position["2"] == "x":
			print("player 1 win")
			exit()
		else:
			print("player 2 win")
			exit()

	elif position["3"]== position["6"] and position["6"] == position["9"]:
		if position["3"] == "x":
			print("player 1 win")
			exit()
		else:
			print("player 2 win")
			exit()

	elif position["1"]== position["5"] and position["5"] == position["9"]:
		if position["1"] == "x":
			print("player 1 win")
			exit()
		else:
			print("player 2 win")
			exit()
			
	elif position["3"]== position["5"] and position["5"] == position["7"]:
		if position["3"] == "x":
			print("player 1 win")
			exit()
		else:
			print("player 2 win")
			exit()
	else:
		print("tied")

player1()

print("")

condition()

player2()

print("")

condition()

print("")

player1()

print("")

condition()

player2()

print("")

condition()
			
player1()

print("")

condition()

player2()

print("")

condition()

player1()

print("")

condition()

player2()

print("")

condition()

player1()

print("")

condi()
