# Jose Contreras
# date 10/30/21

# the first program will print Hello World 100 times

for x in range(100):
    print("hello world")

# the second program will write a loop that prints each number in a new line
# and a loop that prints each number and its square on a new line
'''
Problem says, print each number. Your list has string elements.
Don't use a quotation mark for number element: [12, 10, 32, 3, 66, 17, 42, 99, 20]
'''
for number in ["12", "10", "32", "3", "66", "17", "42", "99", "20"]:
    for e in number:
        print(e)
    for e in number:
        #sqr = e * e
        print("sqaure of", e, "is", e**2) #optimize the code :two lines -> one line

# the third program will ask the user for number of sides and length and color of a line to make a rectangle
import turtle

Sides = int(input(" how many sides?"))
long = int(input(" How long are the sides?"))
color = int(input("what color lines?"))
color_b = int(input("what is the inside color?"))

wn = turtle.Screen()
Draw = turtle.Turtle()
Draw.begin_fill
for i in range(Sides):
    Draw.forward(long)
    Draw.prncolor(color)    #place this line before the loop starts.
    Draw.fillcolor(color_b) #place this line before the loop starts.
    Draw.left(360 / Sides)
Draw.end_fill()
wn.exitonclick()

# Fourth problem, A program that iterates the integers from 1-50. For multiples of three and five, and both
'''
Change the order of checking the conditions.
'''
for i in range(0, 51):
    if i % 3 == 0:
        print(i, "divisible by 3")
    elif i % 5 == 0:
        print(i, "divisible by 5")
    else:
        print(i)
    if i % 3 == 0 and i % 5 == 0:
        print(i, "divisible by both")

# write a program to draw a picture
import turtle

wn = turtle.Screen()
jose = turtle.Turtle()
color = ["blue", "purple", "red", "green"]
jose.begin_fill()
for c in range(360):
    jose.forward(3 + c / 2)
    jose.right(20 - c / 4)
    jose.color(color(c % 4))
    jose.speed(50)
jose.end_fill()
wn.exitonclick

