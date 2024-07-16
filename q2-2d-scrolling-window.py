# Import everything from the tkinter module
from tkinter import *

# Create the main window (root window) for the GUI application
window = Tk()

# Create a Frame widget to hold the Text widget and the Scrollbars
frame = Frame(window)
frame.pack()

# Create a Text widget, 24 characters wide and 10 characters high
text_widget = Text(frame, width=24, height=10, wrap="none")
text_widget.grid(row=0, column=0)

# Add some sample text to the Text widget
sample_text = """
Scripts.com
Bee Movie
By Jerry Seinfeld

NARRATOR:
(Black screen with text; The sound of buzzing bees can be heard)
According to all known laws
of aviation,
 :
there is no way a bee
should be able to fly.
 :
Its wings are too small to get
its fat little body off the ground.
 :
The bee, of course, flies anyway
 :
because bees don't care
what humans think is impossible.
BARRY BENSON:
(Barry is picking out a shirt)
Yellow, black. Yellow, black.
Yellow, black. Yellow, black.
 :
Ooh, black and yellow!
Let's shake it up a little.
JANET BENSON:
Barry! Breakfast is ready!
BARRY:
Coming!
 :
Hang on a second.
(Barry uses his antenna like a phone)
 :
Hello?
ADAM FLAYMAN:

(Through phone)
- Barry?
BARRY:
- Adam?
ADAM:
- Can you believe this is happening?
BARRY:
- I can't. I'll pick you up.
(Barry flies down the stairs)
 :
MARTIN BENSON:
Looking sharp.
JANET:
Use the stairs. Your father
paid good money for those.
BARRY:
Sorry. I'm excited.
MARTIN:
Here's the graduate.
We're very proud of you, son.
 :
A perfect report card, all B's.
JANET:
Very proud.
(Rubs Barry's hair)
BARRY=
Ma! I got a thing going here.
JANET:
- You got lint on your fuzz.
BARRY:
- Ow! That's me!

JANET:
- Wave to us! We'll be in row 118,000.
- Bye!
(Barry flies out the door)
JANET:
Barry, I told you,
stop flying in the house!
(Barry drives through the hive,and is waved at by Adam who is reading a
newspaper)
BARRY==
- Hey, Adam.
ADAM:
- Hey, Barry.
(Adam gets in Barry's car)
 :
- Is that fuzz gel?
BARRY:
- A little. Special day, graduation.
ADAM:
Never thought I'd make it.
(Barry pulls away from the house and continues driving)
BARRY:
Three days grade school,
three days high school...
ADAM:
Those were awkward.
BARRY:
Three days college. I'm glad I took
a day and hitchhiked around the hive.
ADAM==
You did come back different.
(Barry and Adam pass by Artie, who is jogging)
ARTIE:
- Hi, Barry!

BARRY:
- Artie, growing a mustache? Looks good.
ADAM:
- Hear about Frankie?
BARRY:
- Yeah.
ADAM==
- You going to the funeral?
BARRY:
- No, I'm not going to his funeral.
 :
Everybody knows,
sting someone, you die.
 :
Don't waste it on a squirrel.
Such a hothead.
ADAM:
I guess he could have
just gotten out of the way.
(The car does a barrel roll on the loop-shaped bridge and lands on the
highway)
 :
I love this incorporating
an amusement park into our regular day.
BARRY:
I guess that's why they say we don't need vacations.
(Barry parallel parks the car and together they fly over the graduating
students)
Boy, quite a bit of pomp...
under the circumstances.
(Barry and Adam sit down and put on their hats)
 :
- Well, Adam, today we are men.
"""
text_widget.insert(END, sample_text)

# Create a vertical Scrollbar and associate it with the Text widget
v_scrollbar = Scrollbar(frame, orient=VERTICAL, command=text_widget.yview)
v_scrollbar.grid(row=0, column=1, sticky='ns')
text_widget.config(yscrollcommand=v_scrollbar.set)

# Create a horizontal Scrollbar and associate it with the Text widget
h_scrollbar = Scrollbar(frame, orient=HORIZONTAL, command=text_widget.xview)
h_scrollbar.grid(row=1, column=0, sticky='ew')
text_widget.config(xscrollcommand=h_scrollbar.set)

# Start the main event loop, waiting for user interaction
window.mainloop()
