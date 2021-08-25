

pi = 3.14  # global constant

#advanced way to set globals is given here: https://www.programiz.com/python-programming/variables-constants-literals


def area_circle(radius):

	area = pi * radius * radius

	#print(area, ' is print statement in the func')

	return area 

def volume_sphere(radius):
	# you can try

	return 0



def volume_cylinder(radius, height):

	area = area_circle (radius)

	volume = area * height

	return volume, area




#----------------------------------


# now we call the above functions 

#ask the user (exercise)
radius = 5555

area = area_circle (radius)
print(area, 'is the area in square meters')


height = 44
vol, ar = volume_cylinder (radius, height)


print(vol, 'is the volume  in cubic meters')


print(area, 'is the area of the top of the cylinder')



#warm up exercise. Try implementing different functions for the rest 
# of the examples here: https://byjus.com/volume-formulas/

# try to ask the user to input information (such as base, height, radius etc)

