def isFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def main():
	lines = [line.strip() for line in open("grades.txt")]


	#calculates quiz score
	quizGrades = []
	labIndex = False
	for i in range(1, len(lines)):
		if isFloat(lines[i]):
			quizGrades.append(lines[i])
		else:
			labIndex = i+1
			break
	
	quizDivisor = 0
	quizTotal = 0
	for i in range(len(quizGrades)):
		quizTotal += float(quizGrades[i])
		quizDivisor = quizDivisor + 20
	quizAverage = quizTotal / quizDivisor

	print()
	print("Your quiz average is %.2f" % (quizAverage*100))

	
	labGrades = []
	for i in range(labIndex, len(lines)):
		if isFloat(lines[i]):
			labGrades.append(lines[i])
		else:
			break

	labDivisor = 0
	labTotal = 0
	for i in range(len(labGrades)):
		labTotal += float(labGrades[i])
		labDivisor = labDivisor + 10
	labAverage = labTotal / labDivisor

	print("Your lab average is %.2f" % (labAverage*100))

	participationAverage = 1
	print("Your participation average is %.2f" % (participationAverage*100))

	classAverage = quizAverage*.4 + labAverage*.5 + participationAverage*.1
	print()
	print("Your class average is %.2f" % (classAverage*100))




main()