import turtle as t

t.setup(800, 600)

# Function to draw a rectangle
def draw_rectangle(width, height, x, y, bordercolor, fillcolor):
    """Draw a rectangle."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(bordercolor, fillcolor)
    t.begin_fill()
    t.left(-90)
    t.forward(height)
    t.left(-90)
    t.forward(width)
    t.left(-90)
    t.forward(height)
    t.left(-90)
    t.forward(width)
    t.end_fill()

def draw_rectangle_withoutfill(width, height, x, y, bordercolor):
    """Draw a rectangle."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(bordercolor)
    t.left(-90)
    t.forward(height)
    t.left(-90)
    t.forward(width)
    t.left(-90)
    t.forward(height)
    t.left(-90)
    t.forward(width)


# Function to draw the upper body of the car
def car_upperbody(color):
    """Draw the upper body of the car."""
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.color(color, color)
    t.begin_fill()
    t.left(125)
    t.forward(50)
    t.left(55)
    t.forward(70)
    t.left(45)
    t.forward(60)
    t.end_fill()

# Function to draw a circle
def draw_circle(x, y, radius, color):
    """Draw a circle."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw the car
def draw_car(color, width, height):
    """Draw a car."""
    # car lower body
    draw_rectangle(width, height, -55, 0, color, color)

    car_upperbody(color)

    # to create 2 trapezoid to make windows of car
    t.penup()
    t.goto(-105, 0)
    t.pendown()
    t.color("white", "white")
    t.begin_fill()
    t.left(-99)
    t.forward(45)
    t.left(55)
    t.forward(30)
    t.left(90)
    t.forward(35)
    t.end_fill()

    t.penup()
    t.goto(-175, 0)
    t.pendown()
    t.color("white", "white")
    t.begin_fill()
    t.left(180)
    t.forward(35)
    t.left(90)
    t.forward(24)
    t.left(45)
    t.forward(48)
    t.end_fill()

    draw_circle(-230, -60, 20, "black")
    draw_circle(-130, -60, 20, "black")

# Function to draw a person
def draw_person(color, height):
    """Draw a person."""
    global head
    global square
    global legs
    # Draw a person
    head = 0.3 * height
    square = height
    legs = 0.8 * height
    draw_circle(130, 24, head, color)
    draw_rectangle_withoutfill(100, square, 183, 15, "green")
    draw_rectangle(60, 7, 237, 15, "#e0ac69", "#e0ac69")
    draw_rectangle(60, 7, 84, 15, "#e0ac69", "#e0ac69")
    draw_rectangle(7, legs, 89, -height + (height / 2), "#e0ac69", "#e0ac69")
    draw_rectangle(7, legs, 183, -height + (height / 2), "#e0ac69", "#e0ac69")

#  Function to calculate the area of the car
def calculate_car_area(width, height):
    """Calculate the area of the car."""
    facade_area = width * height
    return facade_area


# Function to calculate the height of the person
def calculate_person_height(circleradius, squareheight, legsheight):
    """Calculate the height of the person."""
    total_height = circleradius + squareheight + legsheight
    return total_height

# Main function
def main():
    # Get user input
    height_person = int(input("Enter the height of person: "))
    color_person = str(input("Enter the color of person: "))
    width_car = int(input("Enter the width of car: "))
    height_car = int(input("Enter the height of car: "))
    color_car = str(input("Enter the color of car: "))

    # Draw person and car
    draw_person(color_person, height_person)
    draw_car(color_car, 225, 60)

    # Calculate and print area of the car
    car_area = calculate_car_area(225, 60)
    print(f"The area of the car is {car_area} square units.")

    # Calculate and print height of the person
    person_height = calculate_person_height(head, square, legs)
    print(f"The height of the person is {person_height} mt.")

    # Wait for user input to terminate the program
    input("Press any key to exit ...")


if __name__ == '__main__':
    main()
