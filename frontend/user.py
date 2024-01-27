from user import User
import customtkinter
from utils.generate_data import generate_fake_user_data
from CTkMessagebox import CTkMessagebox

DEBUG_REGISTER_WINDOW = True 

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


class RegisterApp(customtkinter.CTkToplevel):

    def __init__(self):

        global fake_user

        super().__init__()

        self.geometry("700x350")
        self.title("Python da Sorte")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Frame para o texto
        self.text_frame = customtkinter.CTkFrame(master=self, width=1280, height=200, corner_radius=20)
        self.text_frame.grid(row=0, column=1, padx=20, pady=20, stick="nsew")

        self.label = customtkinter.CTkLabel(self.text_frame, text="Realize seu registro",
                                            compound="left", font=customtkinter.CTkFont(size=20, weight="bold", family="Hack Nerd Font"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.user_name_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Nome", height=40, width=280, 
                                                      font=customtkinter.CTkFont(family="Hack Nerd Font"))
        self.user_name_entry.grid(row=1, column=0, padx=30, pady=20)
        

        self.chips_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Qt. de Fichas", height=40, width=280, 
                                                      font=customtkinter.CTkFont(family="Hack Nerd Font"))
        self.chips_entry.grid(row=2, column=0, padx=30, pady=20)

        self.email_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Email", height=40, width=280, 
                                                      font=customtkinter.CTkFont(family="Hack Nerd Font"))
        self.email_entry.grid(row=1, column=1, padx=30, pady=20)

        self.phone_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Telefone", height=40, width=280, 
                                                      font=customtkinter.CTkFont(family="Hack Nerd Font"))
        self.phone_entry.grid(row=2, column=1, padx=30, pady=20)

        self.button = customtkinter.CTkButton(self, text="Entrar/Registrar", corner_radius=10, height=50, width=25, 
                                              font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"),
                                              command=self.save_user)
        self.button.grid(row=1, column=1, padx=20, pady=20)

        if DEBUG_REGISTER_WINDOW:
            fake_user = generate_fake_user_data()
            self.user_name_entry.insert(0, fake_user["name"])
            self.chips_entry.insert(0, fake_user["total_chips"])
            self.email_entry.insert(0, fake_user["email"])
            self.phone_entry.insert(0, fake_user["phone"])

    def save_user(self):
        self.user = User(self.user_name_entry.get(), int(self.chips_entry.get()), self.email_entry.get(), self.phone_entry.get())
        message_box = CTkMessagebox(master=self, title="Sign Up", message=f"Usuário criado com sucecsso. Seu código de acesso é: {self.user.card.upper()}", 
                            icon="check", option_1="Continue")
        message_box.wait_window()
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

        self.label = customtkinter.CTkLabel(self.text_frame, text="Login", font=customtkinter.CTkFont(size=20, weight="bold", family="Hack Nerd Font"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.card_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Enter you card pass", height=40, width=280)
        self.card_entry.grid(row=1, column=1, padx=20, pady=20)

        self.button = customtkinter.CTkButton(self, text="Login", command=self.login, font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"))
        self.button.grid(row=1, column=1, padx=20, pady=20)

    def login(self):
        try:
            self.user = User.from_code(self.card_entry.get())
            correct_pw = CTkMessagebox(master=self, title="Sign in", 
                                       message=f"Bem vindo! {self.user.name}. Você possui {self.user.total_chips} fichas. Deseja adicionar mais?",
                                       option_1="Sim", option_2="Não")
            correct_pw.wait_window()
            if correct_pw.get() == "Sim":
                self.withdraw()
                chips_option = ChipsOptions()
                chips_option.wait_window()
                self.user.total_chips += chips_option.added_chips
                self.deiconify()
        except (ValueError) as e:
            login_box_error = CTkMessagebox(master=self, title="Erro no login", message="Usuário ou senha incorreta", icon="cancel", option_1="Continue")
            login_box_error.wait_window()
        finally:
            self.destroy()


class AccessOption(customtkinter.CTkToplevel):

    def __init__(self):
        super().__init__()

        self.geometry("520x300")
        self.title("Python da Sorte")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1), weight=1)

        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.sign_in, font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"))
        self.login_button.grid(row=0, column=0, padx=20, pady=20)
        
        self.register_button = customtkinter.CTkButton(self, text="Register", command=self.sign_up, font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"))
        self.register_button.grid(row=0, column=1, padx=20, pady=20)

    def sign_in(self):
        try:
            self.withdraw()  # Oculta a janela principal
            login = LoginApp()
            login.wait_window()  # Aguarda até que a janela seja fechada
            self.user = login.user
            self.destroy()
        except AttributeError as e:
            self.deiconify()  # Exibe a janela principal após o término da janela secundária

    def sign_up(self):
        self.withdraw()  # Oculta a janela principal
        register = RegisterApp()
        register.wait_window()  # Aguarda até que a janela seja fechada
        self.user = register.user
        self.deiconify()
        self.destroy()


class ChipsOptions(customtkinter.CTkToplevel):

    def __init__(self):
        super().__init__()

        self.geometry("500x200")
        self.title("Jogo da cobrinha")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.value_entry = customtkinter.CTkEntry(master=self, placeholder_text="Qt. de fichas adicionadas", height=40, width=280, 
                                                  font=customtkinter.CTkFont(family="Hack Nerd Font"))
        self.value_entry.grid(row=0, column=0, padx=20, pady=20)


        self.confirm_button = customtkinter.CTkButton(self, text="Confirmar", corner_radius=10, height=40, width=25, 
                                              font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"),
                                              command=self.add_chips)
        self.confirm_button.grid(row=0, column=1, padx=20, pady=20)

    def add_chips(self):
        try:
            self.added_chips = int(self.value_entry.get())
        except ValueError as e:
            wrong_value = CTkMessagebox(master=self, title="Erro", message="Insira um valor numérico", icon="cancel", option_1="Continue")
            wrong_value.wait_window()
        finally:
            self.destroy()

