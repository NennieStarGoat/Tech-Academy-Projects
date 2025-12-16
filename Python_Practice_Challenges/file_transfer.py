import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import time
from tkinter import messagebox


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        # Sets title of GUI window
        self.master.title("File Transfer (Last 24 Hours)")

        # Creates button to select files from source directory
        self.source_dir_btn = Button(text="Select Source", width=20, command=self.source_dir)
        # Positions source button in GUI using tkinter grid
        self.source_dir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        # Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        # Positions entry in GUI using tkinter grid() padx and pady are teh same as the button to ensure they'll line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        # Creates button to select destination of files from destination directory
        self.dest_dir_btn = Button(text="Select Destination", width=20, command=self.dest_dir)
        # Positions entry in GUI using tkinter grid
        self.dest_dir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        # Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        # Positions entry in GUI using tkinter grid() padx and pady are the same as the button to ensure they'll line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        # Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transfer_files)
        # Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        # Creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        # Positions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    def source_dir(self):
        select_source_dir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the entry widget which allows the path to be inserted properly
        self.source_dir.delete(0, END)
        # The .insert method will insert the user selection to the source_dir entry
        self.source_dir.insert(0, select_source_dir)

    def dest_dir(self):
        select_dest_dir = tkinter.filedialog.askdirectory()
        # The .delete(0, END) will clear the content that is inserted in the entry widget which allows the path to be inserted properly
        self.destination_dir.delete(0, END)
        # The .insert method will insert the user selection to the dest_dir entry
        self.destination_dir.insert(0, select_dest_dir)

    def transfer_files(self):
        # Gets source directory
        source = self.source_dir.get().strip()
        # Gets destination directory
        destination = self.destination_dir.get().strip()
        # Error handling for incorrect inputs or missing inputs
        if not source or not destination:
            messagebox.showerror("Error", "Please select both source and destination directories.")
            return
        if not os.path.isdir(source):
            messagebox.showerror("Error", f"Source path is not a directory:\n{source}")
            return
        if not os.path.isdir(destination):
            messagebox.showerror("Error", f"Destination path is not a directory:\n{destination}")
            return
        # set cutoff time to search between now and 24 hours ago
        cutoff = time.time() - 24 * 60 * 60
        # counts of files that were transferred or skipped
        transferred = 0
        skipped = 0
        # checks each file and moves if appropriate, skipping if not or if there is an error.
        try:
            for name in os.listdir(source):
                if not name:
                    continue
                src_path = os.path.join(source, name)

                # only processes files (skips directories within the folders)
                if not os.path.isfile(src_path):
                    continue

                try:
                    mtime = os.path.getmtime(src_path)
                except OSError:
                    skipped += 1
                    print(f"Failed to read mtime for {name}")
                    continue

                if mtime >= cutoff:
                    try:
                        shutil.move(src_path, destination)
                        transferred += 1
                        print(f"{name} was successfully transferred.")
                    except Exception as e:
                        skipped += 1
                        print(f"Failed to move {name}: {e}")
                else:
                    skipped += 1

            messagebox.showinfo(
                "Transfer Complete",
                f"Transferred: {transferred}\nSkipped (older or error): {skipped}"
            )
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: \n{e}")

    def exit_program(self):
        # Root is the main GUI window, the Tkinter destroy method, tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
