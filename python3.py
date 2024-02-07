w = int(input("Choose 1 to calculate the area of a rectangle, 2 to calculate the area of a circle, 3 for the volume of a sphere: "))

if w == 1:
    def recarea(length, width):
        return length * width

    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print(f'Area of rectangle with length {length} and width {width} is {recarea(length, width)}')

elif w == 2:
    def circlearea(radius):
        return radius * radius * (22 / 7)

    radius = float(input("Enter the radius of the circle: "))
    print(f'Area of circle with radius {radius} is {circlearea(radius)}')

elif w == 3:
    def spheresvolume(radius):
        return (4 / 3) * (22 / 7) * (radius ** 3)

    radius = float(input("Enter the radius of the sphere: "))
    print(f'Volume of sphere with radius {radius} is {spheresvolume(radius)}')

else:
    print("Invalid choice. Please choose 1, 2, or 3.")