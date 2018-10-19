from Question import question
list = [
'1) what is capital of india? a. delhi  b. kolkata  c. kanpur  ',
'2) what is color of banana? a. red  b. yellow  c. green  ',
'3) which has red color?  a. mango  b. guava  c. apple  ' 
]

quiz = [question(list[0], "a"), question(list[1], "b"), question(list[2], "c")]
def run(quiz):
	score = 0
	for q in quiz:
		answer = input(q.que)
		if answer == q.answer:
			score += 1
	print("ur score is: ",score)
run(quiz)
