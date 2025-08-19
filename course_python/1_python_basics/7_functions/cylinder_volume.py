
def find_cylinder_volume(radius, height=7):
    print("radius:", radius)
    print("height:", height)
    volume = 3.14*(radius**2)*height
    print(volume)
    return volume

r = 5
h = 10

# v = find_cylinder_volume(height=h, radius=r)
# print("Volume of the cylinder with radius", r, "and height", h, "is:", v)

print(find_cylinder_volume(r, h))