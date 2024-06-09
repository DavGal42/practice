"""
Author: David Galstyan
Description: 

"""

import tkinter as tk

def create_first_window():
    first_window = tk.Tk()
    first_window.title("Download File")
    first_window.geometry("600x400")
    first_window.configure(bg='#1a2445')

    button = tk.Button(first_window, text="Download", bg='yellow', fg='#1a2445', font=('Roboto', 20, 'bold'))

    button.pack(expand=True, padx=20, pady=20)

    first_window.protocol("WM_DELETE_WINDOW", lambda: (first_window.destroy(), create_second_window()))

    first_window.mainloop()


def create_second_window():
    second_window = tk.Tk()
    second_window.title("Download file")
    second_window.geometry("300x200")

    label = tk.Label(second_window, text="This is the second window!")
    label.pack(pady=20)

    second_window.mainloop()


def main():
    """
        The main function
    """
    create_first_window()


if __name__ == '__main__':
    main()
    