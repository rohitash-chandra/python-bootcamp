

pi = 3.14  # global constant

#advanced way to set globals is given here: https://www.programiz.com/python-programming/variables-constants-literals


def area_circle(radius):

	area = pi * radius * radius

	return area 

def volume_sphere(radius):
	# you can try

	return 0



def volume_cylinder(radius, height):

	area = area_circle (radius)

	volume = area * height

	return volume







# now we call the above functions 

area = area_circle (33)
print(area, 'is the area in square meters')



volume = volume_cylinder (33, 44)
print(volume, 'is the volume  in cubic meters')


#warm up exercise. Try implementing different functions for the rest 
# of the examples here: https://byjus.com/volume-formulas/

