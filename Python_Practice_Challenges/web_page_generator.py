import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.default_html)
        self.btn.grid(padx=(10, 10), pady=(10, 10))

        self.lbl = Label(self.master, text="Enter custom text:")
        self.lbl.grid(row=1, column=0, padx=(10, 0), pady=(0, 5), sticky="w")

        self.entry = Entry(self.master, width=40)
        self.entry.grid(row=2, column=0, padx=(10, 0), pady=(0,10))

        self.btn_custom = Button(self.master, text="Generate Custom HTML Page", width=30, height=2, command=self.custom_html)
        self.btn_custom.grid(row=3, column=0, padx=(10, 0), pady=(0, 10))

    def default_html(self):
        html_text = "Stay tuned for our amazing summer sale!"
        html_file = open("index.html", "w")
        html_content = "<html>\n<body>\n<h1>" + html_text + "</h1>\n</body>\n</html>"
        html_file.write(html_content)
        html_file.close()
        webbrowser.open_new_tab("index.html")

    def custom_html(self):
        html_text = self.entry.get().strip()
        if not html_text:
            html_text = "No custom text provided."
        self.write_and_open(html_text)

    def write_and_open(self, html_text):
        html_content = f"<html>\n<body>\n<h1>{html_text}</hq>\n</body>\n</html>"
        with open("index.html", "w", encoding="utf-8") as html_file:
            html_file.write(html_content)
        webbrowser.open_new_tab("index.html")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
