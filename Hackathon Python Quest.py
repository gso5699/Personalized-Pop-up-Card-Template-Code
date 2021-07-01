word = "AARON"


import turtle
turtle.setup(900,600)
wn = turtle.Screen()

def instructions():
    turtle.penup()
    turtle.goto(-400,-105)
    turtle.write("1) In the IDLE file, change line 1 to the pop-up word of your liking.", font=("Arial",8, "normal"), align = 'LEFT')
    turtle.goto(-400,-120)
    turtle.write("2) Use left and right arrow keys to shift text toward the centre.", font=("Arial",8, "normal"), align = 'LEFT')
    turtle.goto(-400,-150)
    turtle.write("3) Use up and down arrow keys to increase or decrease the spacing between letters.\nEnsure each letter overlaps with adjacent letters at either the top or bottom.", font=("Arial",8, "normal"), align = 'LEFT')
    turtle.goto(-400,-180)
    turtle.write("4) Using the mouse, click points at the top and bottw of the word at the ascent and descent (top/bottom flat parts) \nof the letters. This is where the folding slits will be made.", font=("Arial",8, "normal"), align = 'LEFT')
    turtle.goto(-400,-195)
    turtle.write("5) Press 'Enter' when finished.", font=("Arial",8, "normal"), align = 'LEFT')
    turtle.goto(-400,-225)
    turtle.write("6) Take a screen capture of the word. Open a word processing document, resize the image, and align the \ncentre blue line to to centre of the page, ensuring the page is in portrait orientation. .", font=("Arial",8, "normal"), align = 'LEFT')
    turtle.goto(-400,-255)
    turtle.write("7) Print the page and use it as a stencil. Retrace the image on another paper. Cut at black lines and fold at blue lines. \nWhere the blue line is in the black word, do not fold.", font=("Arial",8, "normal"), align = 'LEFT')
    turtle.goto(-400,-270)
    turtle.write("8) Once folded into the appropriate shape, glue the sheet onto a new sheet of paper. Pop-up card is complete.", font=("Arial",8, "normal"), align = 'LEFT')
    


turtle.pendown()

x_word = int(-100)
y_word = int(-100)
letter_spacing = int(120)
font_size = int(150)

def print_word(x_word, y_word, letter_spacing):
    turtle.speed(0)
    instructions()

    for i in range(len(word)):
        turtle.penup()
        turtle.goto(x_word+i*letter_spacing,y_word)
        turtle.write(word[i], font=("Arial Black", font_size, "normal"), align = 'CENTER')

print_word(x_word,y_word,letter_spacing)

#1 Shift word into screen using keyboard arrows. Press enter when satisfied.
def shift_left():
    shift_left.counter +=1
    turtle.clear()
    print_word(x_word-shift_left.counter*40, y_word, letter_spacing-smaller_space.counter*10) 
shift_left.counter = 0

def shift_right():
    shift_left.counter -=1
    turtle.reset()
    print_word(x_word-shift_left.counter*40, y_word, letter_spacing-smaller_space.counter*10)
shift_left.counter = 0

def smaller_space():
    smaller_space.counter +=1
    turtle.reset()
    print_word(x_word-shift_left.counter*40,y_word, letter_spacing-smaller_space.counter*5)
smaller_space.counter = 0

def larger_space():
    smaller_space.counter -=1
    turtle.reset()
    print_word(x_word - shift_left.counter*40,y_word, letter_spacing-smaller_space.counter*5)
smaller_space.counter = 0
 
def done_shift():
    turtle.left(90)
    sumy= 0
    for j in range(len(coordinatesy)):
        sumy += coordinatesy[j]
    averagey = sumy/len(coordinatesy)
    for i in range(len(coordinatesx)):
        turtle.penup()
        turtle.goto(coordinatesx[i],averagey)
        turtle.pendown()
        turtle.forward(40)
        
   #    print(coordinatesx[i],coordinatesy[i])
    coordinatesx.sort()
    coordinatesx.reverse()
    turtle.left(90)

    special_num = int((len(coordinatesx)-6)/2)


    turtle.pencolor("blue")
    for k in range(0, len(coordinatesx)//2+ special_num, 2):
        turtle.goto(coordinatesx[k+1], averagey+40)
        turtle.penup()
        turtle.goto(coordinatesx[k+2],averagey+40)
        turtle.pendown()
        turtle.goto(coordinatesx[k+3], averagey+40)

    turtle.penup()
    turtle.goto(coordinatesx[0],averagey)
    turtle.pendown()

    
    for p in range(0,len(coordinatesx)//2+special_num, 2):
        turtle.goto(coordinatesx[p+1], averagey+2)
        turtle.penup()
        turtle.goto(coordinatesx[p+2], averagey+2)
        turtle.pendown()
        turtle.goto(coordinatesx[p+3], averagey+2)

    bcoordinatesx.sort()
    turtle.right(180)
    turtle.penup()
    sumby = 0
    special_numb = int((len(bcoordinatesx)-6)/2)

    for n in range(len(bcoordinatesy)):
        sumby += bcoordinatesy[n]
    averageby = sumby/len(bcoordinatesy)
    turtle.goto(bcoordinatesx[0], averageby-3)
    turtle.pendown()
    
    for m in range(0,len(bcoordinatesx)//2+special_numb, 2):
        turtle.goto(bcoordinatesx[m+1], averageby-4)
        turtle.penup()
        turtle.goto(bcoordinatesx[m+2],averageby-4)
        turtle.pendown()
        turtle.goto(bcoordinatesx[m+3], averageby-4)

    turtle.penup()
    turtle.goto(-700,6)
    turtle.pendown()
    turtle.forward(1200)

    
        
wn.onkey(shift_left, "Left")
wn.onkey(shift_right, "Right")
wn.onkey(smaller_space, "Down")
wn.onkey(larger_space, "Up")
wn.onkey(done_shift, "Return")


coordinatesx=[]
coordinatesy=[]
bcoordinatesx =[]
bcoordinatesy= []

#4 Explain where to insert slits (flat parts at top+bottom. Indicate where points are picked with colour.

def buttonclick(x,y):
    if y > 10:
        coordinatesx.append(x)
        coordinatesy.append(y)
    elif y < 10:
        bcoordinatesx.append(x)
        bcoordinatesy.append(y)
    
    
turtle.onscreenclick(buttonclick,1)
turtle.listen()
turtle.speed(10)
turtle.done()


wn.listen() 
wn.mainloop()

    
    

#5 Make those lines (dotted lines) another colour
#6 Make flaps on top by drawing straight lin up (matching coordinates selected). Connect ends with dotted colour
#7 Add centre line (distance of it from bottom of letters = length of top flap
#8 Centre the centre line to the centre of the paper
#9 Make PDF
    



