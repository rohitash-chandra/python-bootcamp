

pi = 3.14  # global constant

#advanced way to set globals is given here: https://www.programiz.com/python-programming/variables-constants-literals


def area_circle(radius):
	area = pi * radius * radius
	return area 

def volume_sphere(radius):
	return 0

def volume_cylinder(radius, height):
	area = area_circle (radius)
	volume = area * height
	return volume, area
#----------------------------------


# now we call the above functions 

#ask the user (exercise)
print('Radius?')
radius = float(input())

area = area_circle (radius)
print(area, 'is the area in square meters')

print('Height?')
height = float(input())
vol, ar = volume_cylinder (radius, height)

print(vol, 'is the volume  in cubic meters')
print(area, 'is the area of the top of the cylinder')