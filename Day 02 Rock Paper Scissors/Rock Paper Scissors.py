opponent_code = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

response_code = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors" 
}

beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

lose = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}


strategy = []

with open("./input.txt", "r") as f:
    for line in f:
        opponent_move, response_move = line.split()
        strategy.append((opponent_move, response_move))
    

#Part 1
score = 0
for opponent_move, response_move in strategy:
    opponent_move = opponent_code[opponent_move]
    response_move = response_code[response_move]

    score += points[response_move]
    if opponent_move == response_move:
        score += 3
    elif beats[response_move] == opponent_move:
        score += 6
 
print(score)

#Part 2
score = 0
for opponent_move, response_move in strategy:
    opponent_move = opponent_code[opponent_move]

    if response_move == "X":
        response_move = beats[opponent_move]
        score +=  points[response_move]
    elif response_move == "Y":
        score += 3 + points[opponent_move]
    else:
        response_move = lose[opponent_move]
        score += 6 + points[response_move]
    
print(score)