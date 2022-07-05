import tkinter
import tkinter.messagebox
import customtkinter
import csv

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class RegisterWindow(customtkinter.CTk):

    WIDTH: int = 780
    HEIGHT: int = 520

    def __init__(self) -> None:
        super().__init__()

        self.title("Register new player")
        self.geometry(f"{RegisterWindow.WIDTH}x{RegisterWindow.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.button_event)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=180)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Name",
                                            corner_radius=10)
        self.entry.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky="ew")

        self.entry2 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Age")
        self.entry2.grid(row=1, column=0, columnspan=2, pady=5, padx=10, sticky="ew")

        self.entry3 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Register a value to enter the cassino: ")
        self.entry3.grid(row=2, column=0, columnspan=2, pady=5, padx=10, sticky="ew")

        self.entry4 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Enter an email")
        self.entry4.grid(row=3, column=0, columnspan=2, pady=5, padx=10, sticky="ew")

        self.confirm = customtkinter.CTkButton(master=self.frame_right,
                                                text="Register",
                                                border_width=2,
                                                fg_color=None,
                                                command=self.button_event)
        self.confirm.grid(row=4, column=0, columnspan=1, pady=20, padx=20, sticky="we")

        self.frame_info = customtkinter.CTkFrame(master=self.frame_left)
        self.frame_info.grid(row=0,
                            column=0,
                            rowspan=4,
                            pady=20,
                            padx=20,
                            sticky="nsew")

        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info = customtkinter.CTkLabel(master=self.frame_info, 
                                                text="Please, fill in the blanks\n" + 
                                                    "on the side" +
                                                    "to start the game.\n\n" +
                                                    "The game is only available\n" +
                                                    "to people over 21 years old.\n\n" +
                                                    "Can't start the game with\n" +
                                                    "a value lower than $100",
                                                text_font=("Roboto", -16),
                                                height=100,
                                                fg_color=("white", "gray38"), 
                                                justify=tkinter.LEFT)
        self.label_info.grid(column=0, row=0, sticky="nwe", padx=15, pady=15, ipadx=3, ipady=10)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:", text_font=("Roboto Medium", -16))
        self.label_mode.grid(row=9, column=0, pady=3, padx=10, sticky="w")
        self.option_var = tkinter.StringVar(value="Dark")
        self.option_menu_1 = customtkinter.CTkSwitch(master=self.frame_left,
                                                    text="Dark Mode",
                                                    variable=self.option_var,
                                                    onvalue="Dark",
                                                    offvalue="Light")
        self.option_menu_1.configure(command=self.change_appearance_mode)
        self.option_menu_1.grid(row=10, column=0, padx=20, pady=10, sticky="w")

    def button_event(self, event: int = 0) -> None:
        """Stop the main loop"""
        self.save_data()
        self.destroy()

    def change_appearance_mode(self) -> None:
        """Switch dark mode to light mode and vice-versa"""
        customtkinter.set_appearance_mode(self.option_menu_1.get())

    def save_data(self) -> None:
        """Save the data before closing the window"""

        with open('data.csv', mode='w') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow([
                                self.entry.get().lower(),
                                self.entry2.get(),
                                self.entry3.get(),
                                self.entry4.get()])

if __name__ == "__main__":
    app = RegisterWindow()
    app.mainloop()
