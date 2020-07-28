def traiangleArea(side1, side2, side3):
	s = (side1 + side2 + side3) / 2
	area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5
	return area

side1, side2, side3 = 5,6,7
area = traiangleArea(side1, side2, side3)
print('The area of the triangle is %0.2f' %area)
