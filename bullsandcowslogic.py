import random

def generate_answer():
	answer = random.sample(range(0,9),4)
	if answer[0] == 0:
		answer.reverse()
	return int(''.join(str(e) for e in answer))

def calculate_bulls(answer, user_answer):
	count=0
	answer = list(str(answer))
	user_answer = list(str(user_answer))

	for i in range(4):
		if answer[i] == user_answer[i]:
			count = count + 1

	return count;


def calculate_cows(answer, user_answer):
	bulls = calculate_bulls(answer, user_answer)
	answer = set(str(answer))
	user_answer = set(str(user_answer))
	cows = len(answer.intersection(user_answer))
	#print("bulls:",bulls, " cows:", cows)
	return cows - bulls

#print(generate_answer())
#print(calculate_bulls(1234,4213))
#print(calculate_cows(1234,1230))

