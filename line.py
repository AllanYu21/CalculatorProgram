

m=0
b=0

def makeLine(point1, point2):
	global b
	global m
	m = (point2[1]-point1[1])/ (point2[0]-point1[0])
	b = point1[1] - m*point1[0] 




def newY(x):

	global m
	global b
	return m*x+b


if __name__ == "__main__":
	
	x1 = float(input("x1: "))
	y1 = float(input("y1: "))
	x2 = float(input("x2: "))
	y2 = float(input("y2: "))

	point1 = (x1,y1)
	point2 = (x2,y2)


	makeLine(point1,point2)



	choice = input("Enter a x: ")
	print("The Y value is ")
	print(newY(float(choice)))

