import math

def circle_stats(radius):
  area =  math.pi * radius ** 2
  circumference = 2 * math.pi * radius
  return area, circumference

circle_area, circle_circumference = circle_stats(3)

print(f"Area of Circle: {round(circle_area, 2)} \nCircumference of Circle: {round(circle_circumference, 2)}")