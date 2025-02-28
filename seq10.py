# Problem 5: Distance Between Two Points on Earth

# The surface of the Earth is curved, and the distance between degrees of longitude varies
# with latitude. As a result, finding the distance between two points on the surface of the
# Earth is more complicated than simply using the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s surface.
# The distance between these points, following the surface of the Earth, in kilometers is:
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))

# The value 6371.01 in the previous equation wasn’t selected at random. It is the average
# radius of the Earth in kilometers.
# Create a program that allows the user to enter the latitude and longitude of two points on
# the Earth in degrees. Your program should display the distance between the points,
# following the surface of the earth, in kilometers.

import math

# Input latitude and longitude of two points (in degrees)
t1 = float(input("Enter latitude of first point in degrees: "))
g1 = float(input("Enter longitude of first point in degrees: "))
t2 = float(input("Enter latitude of second point in degrees: "))
g2 = float(input("Enter longitude of second point in degrees: "))

# Convert degrees to radians
t1 = math.radians(t1)
g1 = math.radians(g1)
t2 = math.radians(t2)
g2 = math.radians(g2)

# Earth's radius in km
earth_radius = 6371.01

# Compute distance using the formula
distance = earth_radius * math.acos(math.sin(t1) * math.sin(t2) + 
                                    math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

# Display the result
print(f"The distance between the two points is: {distance:.2f} km")
