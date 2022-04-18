# Python tkinter hello world program
# TODO: This is a work in progress

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x300")
frame = Frame(root)
frame.pack(fill=BOTH, expand=TRUE)

html_bool = BooleanVar()
text_bool = BooleanVar()
links_bool = BooleanVar()
images_bool = BooleanVar()

titel = Label(frame, text="WebScraper GUI")
titel.pack(side=TOP, pady=5)

url_frame = Frame(frame)
url_label = Label(url_frame, text="URL:")
url_label.pack(side=LEFT, padx=22)
url_input = Entry(url_frame)
url_input.pack(fill=X, padx=20)
url_frame.pack(fill=X, pady=20)

dir_frame = Frame(frame)
dir_label = Label(dir_frame, text="Directory:")
dir_label.pack(side=LEFT, padx=8)
dir_input = Entry(dir_frame)
dir_input.pack(fill=X, padx=20)
dir_frame.pack(fill=X, pady=20)

check_frame = Frame(frame)
html_check = Checkbutton(check_frame, text="HTML", variable=html_bool, onvalue=True, offvalue=False)
html_check.pack(side=LEFT, padx=20)
text_check = Checkbutton(check_frame, text="Text", variable=text_bool, onvalue=True, offvalue=False)
text_check.pack(side=LEFT, padx=20)
links_check = Checkbutton(check_frame, text="Links", variable=links_bool, onvalue=True, offvalue=False)
links_check.pack(side=RIGHT, padx=20)
images_check = Checkbutton(check_frame, text="Images", variable=images_bool, onvalue=True, offvalue=False)
images_check.pack(side=RIGHT, padx=20)
check_frame.pack(fill=X, pady=20)


def retrieve_data():
    from scraper import Scraper
    url = str(url_input.get())
    direct = str(dir_input.get())

    try:
        scrap = Scraper(url, direct)
        print(scrap.response)
        if not html_bool.get() and not text_bool.get() and not links_bool.get() and not images_bool.get():
            messagebox.showinfo("Nothing selected", "You didn't select any option")
        else:
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


submit_button = Button(frame, text="Submit", command=retrieve_data)
submit_button.pack(side=BOTTOM, pady=30)


root.title("WebScraper Gui")
root.mainloop()
