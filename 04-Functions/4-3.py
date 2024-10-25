import math
def triangle_area(a,b,c):
 result = (a + b + c)/2
 area = math.sqrt((result - a)*(result-b)*(result-c)* result)
 return area


print(f'the triangle area with sides a b and c is {triangle_area(3, 4, 5)}')