from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("420x350")
frame = Frame(root, bg="#CAF5CD")
frame.pack(fill=BOTH, expand=TRUE)

# Booleans to determine if the checkboxes are checked or not
html_bool = BooleanVar()
text_bool = BooleanVar()
links_bool = BooleanVar()
images_bool = BooleanVar()

# Fonts
title_font = ("Comic Sans MS", 20, "bold")
normal_text = ("Comic Sans MS", 10, "normal")
button_font = ("Comic Sans MS", 15, "bold")

# Colors
frame_background = "#CAF5CD"

# Title of the GUI
titel = Label(frame, text="WebScraper GUI", font=title_font, fg="red", bg=frame_background)
titel.pack(side=TOP, pady=5)

# Frame that contains the Label specifying where to insert the URL and the Entry
url_frame = Frame(frame, bg=frame_background)
url_label = Label(url_frame, text="URL:", font=normal_text, bg=frame_background)
url_label.pack(side=LEFT, padx=25)
url_input = Entry(url_frame)
url_input.pack(fill=X, padx=20)
url_frame.pack(fill=X, pady=20)

# Same as the url_frame
dir_frame = Frame(frame, bg=frame_background)
dir_label = Label(dir_frame, text="Directory:", font=normal_text, bg=frame_background)
dir_label.pack(side=LEFT, padx=8)
dir_input = Entry(dir_frame)
dir_input.pack(fill=X, padx=20)
dir_frame.pack(fill=X, pady=20)

# A frame that contains all the checkboxes
check_frame = Frame(frame, bg=frame_background)
html_check = Checkbutton(check_frame, text="HTML", variable=html_bool, onvalue=True, offvalue=False, font=normal_text,
                         bg=frame_background)
html_check.pack(side=LEFT, padx=20)
text_check = Checkbutton(check_frame, text="Text", variable=text_bool, onvalue=True, offvalue=False, font=normal_text,
                         bg=frame_background)
text_check.pack(side=LEFT, padx=20)
links_check = Checkbutton(check_frame, text="Links", variable=links_bool, onvalue=True, offvalue=False,
                          font=normal_text, bg=frame_background)
links_check.pack(side=LEFT, padx=20)
images_check = Checkbutton(check_frame, text="Images", variable=images_bool, onvalue=True, offvalue=False,
                           font=normal_text, bg=frame_background)
images_check.pack(side=LEFT, padx=20)
check_frame.pack(fill=X, pady=20)


# Function that gets triggered on Button-click: Retrieves all the data from the Entries and executes the Scraper
def retrieve_data():
    # We import the scraper here because else its code would be executed earlier
    from scraper import Scraper
    url = str(url_input.get())
    direct = str(dir_input.get())

    try:
        # Creates an instance of the Scraper
        scrap = Scraper(url, direct)
        # Shows a warning if no option is selected
        if not html_bool.get() and not text_bool.get() and not links_bool.get() and not images_bool.get():
            messagebox.showwarning("Nothing selected", "You didn't select any option")
        else:
            # If selected, execute its action (functions of the Scraper class)
            if html_bool.get():
                scrap.get_html()
            if text_bool.get():
                scrap.get_text()
            if links_bool.get():
                scrap.get_links()
            if images_bool.get():
                scrap.get_images()
            messagebox.showinfo("Done", "Website has been scraped")
    except Exception as err:
        print(err)
        messagebox.showerror("Error", str(err))


# Button to trigger the fucntion above
submit_button = Button(frame, text="Submit", command=retrieve_data, font=button_font, fg="green")
submit_button.pack(side=BOTTOM, pady=20, ipadx=50)

# Creates the GUI-loop
root.title("WebScraper Gui")
root.mainloop()
