# Import the tkinter module
import tkinter as tk
from _ast import Lambda

HEIGHT = 700
WIDTH = 800

# Test function to present the users input
def test_function(entry):
    print("This is the entry:", entry)

# Root will be the main window that everything lives in
root = tk.Tk()

# We need to create a canvas that is bigger in size. The height and width were defined earlier
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")  # Define the canvas parameters
canvas.pack()  # Make the canvas show on the screen

background_image = tk.PhotoImage(file="GCJRhiA.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

# We need to create a frame to add our widgets to
# This will work in the root window
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# Let's add a simple button to our app
# This is done in a nesting fashion using out root area
# Instead of placing this in the root window, we will place it in our new frame
# We are using the lambda function to help with tying the button and entry box together
button = tk.Button(frame, text="Go!", font=40, command=lambda: test_function(entry.get()))  # Define the button parameters
button.place(relx=0.65, rely=0.2, relwidth=0.1, relheight=0.1)  # Make the button on the screen

# We will now create a label widget
label = tk.Label(frame, text="My Cool App", bg="#0f5b87")
label.place(relwidth=1, relheight=0.07)

# Let's create an entry, test entry box, widget as well
# entry = tk.Entry(frame, bg="white")
entry = tk.Entry(frame)
entry.place(relx=0.3, rely=0.2, relwidth=0.3, relheight=0.1)

lower_frame = tk.Frame(root, bg="#40a7e3", bd=10)
lower_frame.place(relx=0.2, rely=0.4, relwidth=0.63, relheight=0.4)

# We will now create a label widget
label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)


root.mainloop()
