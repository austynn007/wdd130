import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry

def main():
    # Create the Tk root object.
    root = tk.Tk()
    # Create the main window.
    frm_main = Frame(root)
    frm_main.master.title("Circle Area")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)
    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put the labels, text entry boxes, and buttons into the main window.
    Parameter frm_main: the main frame (window)
    Return: nothing """
    # Create a label that displays "Radius:"
    lbl_radius = Label(frm_main, text="Radius:")
    # Create an integer entry box where the user will enter the radius.
    ent_radius = IntEntry(frm_main, width=4, lower_bound=1, upper_bound=100)
    # Create a label that displays "units"
    lbl_radius_units = Label(frm_main, text="units")
    # Create a label that displays "Area:"
    lbl_area = Label(frm_main, text="Area:")
    # Create labels that will display the results.
    lbl_result = Label(frm_main, width=10)
    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")
    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(row=0, column=0, padx=3, pady=3)
    ent_radius.grid(row=0, column=1, padx=3, pady=3)
    lbl_radius_units.grid(row=0, column=2, padx=0, pady=3)
    lbl_area.grid(row=1, column=0, padx=(30, 3), pady=3)
    lbl_result.grid(row=1, column=1, padx=3, pady=3)
    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")

    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the area of the circle."""
        try:
            # Get the user's radius.
            radius = ent_radius.get()
            # Compute the area of the circle.
            area = 3.14159 * radius ** 2
            # Display the area for the user to see.
            lbl_result.config(text=f"{area:.2f}")
        except ValueError:
            # When the user deletes all the digits in the radius
            # entry box, this will be called, and it will display
            # an empty string, indicating that there is no result.
            lbl_result.config(text="")
    # Call the calculate function whenever the user releases a key.
    ent_radius.bind("<KeyRelease>", calculate)

if __name__ == "__main__":
    main()
