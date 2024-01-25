from results import Result
from user_info import User
import customtkinter
from utils.generate_data import generate_fake_user_data

fake_user = generate_fake_user_data()

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")

class RegisterApp(customtkinter.CTkToplevel):

    def __init__(self):
        super().__init__()

        self.geometry("700x350")
        self.title("Python da Sorte")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Frame para o texto
        self.text_frame = customtkinter.CTkFrame(master=self, width=1280, height=200, corner_radius=20)
        self.text_frame.grid(row=0, column=1, padx=20, pady=20, stick="nsew")

        self.label = customtkinter.CTkLabel(self.text_frame, text="Realize seu registro", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.user_name_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Nome", height=40, width=280)
        self.user_name_entry.grid(row=1, column=0, padx=30, pady=20)
        self.user_name_entry.insert(0, fake_user["name"])

        self.chips_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Qt. de Fichas", height=40, width=280)
        self.chips_entry.grid(row=2, column=0, padx=30, pady=20)
        self.chips_entry.insert(0, fake_user["total_chips"])

        self.email_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Email", height=40, width=280)
        self.email_entry.grid(row=1, column=1, padx=30, pady=20)
        self.email_entry.insert(0, fake_user["email"])

        self.phone_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Telefone", height=40, width=280)
        self.phone_entry.grid(row=2, column=1, padx=30, pady=20)
        self.phone_entry.insert(0, fake_user["phone"])

        self.button = customtkinter.CTkButton(self, text="Entrar/Registrar", command=self.save_user)
        self.button.grid(row=1, column=1, padx=20, pady=20)

    def save_user(self):
        self.user = User(self.user_name_entry.get(), int(self.chips_entry.get()), self.email_entry.get(), self.phone_entry.get())
        print(self.user)
        self.destroy()
        

class LoginApp(customtkinter.CTkToplevel):
    
    def __init__(self):
        super().__init__()

        self.geometry("520x300")
        self.title("Python da Sorte")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Frame para o texto
        self.text_frame = customtkinter.CTkFrame(master=self, width=500, height=100, corner_radius=20)
        self.text_frame.grid(row=0, column=1, padx=20, pady=20, stick="nsew")

        self.label = customtkinter.CTkLabel(self.text_frame, text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.card_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Enter you card pass", height=40, width=280)
        self.card_entry.grid(row=1, column=1, padx=20, pady=20)

        self.button = customtkinter.CTkButton(self, text="Login", command=self.login)
        self.button.grid(row=1, column=1, padx=20, pady=20)

    def login(self):
        #user = Result().retrieve_data(self.card_entry.get())
        #self.user = User(**user)
        print("logado")
        self.destroy()


class AccessOption(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("520x300")
        self.title("Python da Sorte")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.sign_in)
        self.login_button.grid(row=0, column=0, padx=20, pady=20)
        
        self.register_button = customtkinter.CTkButton(self, text="Register", command=self.sign_up)
        self.register_button.grid(row=0, column=1, padx=20, pady=20)

    def sign_in(self):
        self.withdraw()  # Oculta a janela principal
        login = LoginApp()
        login.wait_window()  # Aguarda até que a janela seja fechada
        self.deiconify()  # Exibe a janela principal após o término da janela secundária
        self.destroy()

    def sign_up(self):
        self.withdraw()  # Oculta a janela principal
        register = RegisterApp()
        register.wait_window()  # Aguarda até que a janela seja fechada
        self.deiconify()
        self.destroy()


if __name__ == "__main__":
    access = AccessOption()
    access.mainloop()

