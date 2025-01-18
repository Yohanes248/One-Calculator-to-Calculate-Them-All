#function to convert cm to mm
def cm_to_mm(cm_val):
    mm = cm_val * 10
    return mm



print("One Calculator to Calculate Them All!\n")
#Get the diameter of ring
d1 = float(input('Diameter of a ring (in cm)? '))
#Get the height of ring.
h1 = int(input('Height of a ring (in mm)? '))
#convert from cm to mm
f1 = cm_to_mm(d1)
#calculation for volume of a ring without inner cutout
vrwic1 = 3.14 * (f1//2)**2 * h1

print('Volume of a ring without the inner cutout is: ' + str(vrwic1) + ' mm^3')

ratio = float(input('Ratio of the inner cutout diameter (as a decimal)? '))
#calculation for volume of the inner cutout
vic1 = (vrwic1 * ratio * ratio)
#Store a rounded version of the volume for inner cutout.
vic2 = round(vic1, 2)

print('Volume of the inner cutout is: ' + str(vic2) + ' mm^3')
#calculation for the volume of a ring with the inner cutout.
vrIc = vrwic1 - vic2
vrIc2 = vrwic1 - vic1
vrIc3 = round(vrIc, 2)

print('Volume of a ring with the inner cutout is: ' + str(vrIc3) + ' mm^3')
print()
print('***Rings of Power***\n' )
#Ask the user for number of rings
num_rings = int(input('Number of rings? '))
#Ask the user for cost of material per cubic inch
costM = int(input('Cost of the material (in cents per cubic inch)? '))
#Ask the user for forging cost in cents per ring
costF = int(input('Forging cost (in cents per ring)? '))
#calculation for total material.
tmats = round((vrIc2 * num_rings), 2)

print('Total material needed is: ' + str(tmats) + ' mm^3')

multiplier = 25.4**-3
#Now get the unrounded amount of cubes.
cube1 = tmats * multiplier
#round up the number.
cube2 = int(cube1 + 1) - int(int(cube1 + 1) - cube1)

print('Total number of cubes to purchase is: ' + str(cube2) + ' cube(s)')
#Now I will do the operation to get the total cents and store it as a variable.
tC = (num_rings * costF) + (cube2 * costM)
"""
Now I can do the floor division operator to get the dollar amount and then
I can use the mod operator to get the amount of cents.
"""
dol = tC // 100
cent = tC % 100

d2 = str(dol)
c2 = str(cent)

print('Cost for the Rings of Power is: '+d2+ ' dollar(s) and ' +c2+ ' cent(s)!')
print()
print('***The One Ring***\n')
#get the cost of the material in cents per cubic inch.
cmc = int(input('Cost of the material (in cents per cubic inch)?'))

oneCube = vrIc3 * hint
#Now round it up
oneCube2 = int(oneCube + 1) - int(int(oneCube + 1) - oneCube)

print(' Number of cubes to purchase is: ' + str(oneCube2) + ' cube(s)')
"""
Now do the calculation for cost for the one ring, I will multiply the
amount of cubes and the cost of material per cubic inch then add the
forging cost to that product.
But first I must get the forging cost, which is just three
times the forging cost of a Ring of Power.
"""
costF2 = costF * 3
tC2 = costF2 + oneCube2 * cmc
#Now do floor division operator and modulus to get the dollar and cent amount.
dol3 = tC2 // 100
cent3 = tC2 % 100

d3 = str(dol3)
c3 = str(cent3)

print('Cost for the One Ring is: ' +d3+ ' dollar(s) and ' +c3+ ' cent(s)!')
print()
print('This Shall Not Fail!')
