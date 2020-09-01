import tkinter as tk
import sys
from tkinter import HORIZONTAL, ttk, messagebox
# from tkinter.ttk import Combobox


WIDTH = 1200
HEIGHT = 800
DEFAULT = 'Arial'
TITLE_FONT = (DEFAULT, 60)
LABEL_TEXT = (DEFAULT, 12)
ENTRY_TEXT = (DEFAULT, 15)
LISTBOX_TEXT = (DEFAULT, 15)
FORM_TEXT = (DEFAULT, 11)

# 90%+ = S
# 80-90% = A
# 70-80% = B
# 60-70% = C
# 50-60% = D
# 40-50% = E
# Below 40% = F

cpu_dictionary = {"ryzen 3600": "A", "ryzen 3700X": "A", "ryzen 2600": "B", "ryzen 3900X": "A", "i7 9700k": "S"}

# 100%+ = S
# 80-100% = A
# 60-80% = B
# 40-60% = C
# 30-40% = D
# 20-30% = E
# Below 20% = F

gpu_dictionary = {"rtx 2070s": "S", "gtx 1060-6gb": "C", "rx 580": "C", "gtx 1070": "B", "rtx 2060": "A"}

# Game arrays.
gta = ["B", "C", 100, 8]  # CPU, GPU, STORAGE and RAM

# Game dictionary.
game_dictionary = {"Grand Theft Auto": gta}


# Main class in which we define what we want each class to inherit.
class TestApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Initialization method. Args = Arguments (variables), Kwargs = Key word arguments (such as dictionaries).
        tk.Tk.__init__(self, *args, **kwargs)  # Initializing tkinter.
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.configure(bg='#7a8aa3')

        self.frames = {}  # A dictionary used to contain all the page frames.

        for F in (StartPage, SysReq, Tutorial, Game):  # A for loop allowing us to loop through our pages (F stands for frame).

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)  # This makes it so the first frame we see is the menu.

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Main Menu Class.
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Creating a canvas to fill out the white background.
        mmbgc = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg='#7a8aa3', bd=0, highlightthickness=0, relief='ridge')
        mmbgc.pack()

        # Menu Menu Title.
        main_menu_title_frame = tk.Frame(mmbgc)
        main_menu_title_frame.place(relx=0.5, rely=0.15, relheight=0.1, relwidth=0.8, anchor="center")
        main_menu_title = tk.Label(main_menu_title_frame, font=TITLE_FONT, text="Main Menu", bg='#7a8aa3')
        main_menu_title.place(relheight=1, relwidth=1)

        # Main Menu Button Frame.
        button_frame = tk.Frame(mmbgc, bg='#7a8aa3')
        button_frame.place(relx=0.5, rely=0.5, relheight=0.4, relwidth=0.4, anchor="center")

        # Main Menu Buttons.
        tutorial_button = tk.Button(button_frame, text="Tutorial", font=25, command=lambda: controller.show_frame(Tutorial))
        tutorial_button.place(relx=0.5, rely=0.04, relwidth=0.8, relheight=0.2, anchor="n")
        system_button = tk.Button(button_frame, text="Enter System Specs", font=25,
                                  command=lambda: controller.show_frame(SysReq))
        system_button.place(relx=0.5, rely=0.28, relwidth=0.8, relheight=0.2, anchor="n")
        quit_button = tk.Button(button_frame, text="Quit", font=25, command=lambda: sys.exit())
        quit_button.place(relx=0.5, rely=0.52, relwidth=0.8, relheight=0.2, anchor="n")


# System Form Class.
class SysReq(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def promptOne():
            messagebox.showwarning("Error", "You have left one or more of the fields empty!")

        def save_details():
            pc_cpu = cpu_form.get().lower()
            pc_gpu = gpu_form.get().lower()
            pc_sto = sto_form.get()
            pc_ram = ram_slider.get()

            global comp_specs
            comp_specs = [pc_cpu, pc_gpu, pc_sto, pc_ram]
            print(comp_specs)

            if comp_specs[0] == ('') or comp_specs[1] == ('') or comp_specs[2] == ('') or comp_specs[3] == 0:
                print("You've left one or more of the fields empty.")
                promptOne()

        srbgc = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg='#a83951', bd=0, highlightthickness=0, relief='ridge')
        srbgc.pack()

        # System Spec Title
        spec_title_frame = tk.Frame(srbgc)
        spec_title_frame.place(relx=0.5, rely=0.15, relheight=0.1, relwidth=0.8, anchor="center")
        spec_title = tk.Label(spec_title_frame, font=TITLE_FONT, text="Specifications Form", bg='#a83951')
        spec_title.place(relheight=1, relwidth=1)

        # Form Frame.
        form_frame = tk.Frame(srbgc, bg='white')
        form_frame.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.6, anchor="center")

        # Form Labels.
        cpu_label = tk.Label(form_frame, font=LABEL_TEXT, text="Enter your CPU: ")
        cpu_label.place(relx=0.05, rely=0.05, relwidth=0.3, relheight=0.15)
        gpu_label = tk.Label(form_frame, font=LABEL_TEXT, text="Enter your GPU: ")
        gpu_label.place(relx=0.05, rely=0.30, relwidth=0.3, relheight=0.15)
        ram_label = tk.Label(form_frame, font=LABEL_TEXT, text="Select a RAM Amount (GB): ")
        ram_label.place(relx=0.05, rely=0.55, relwidth=0.3, relheight=0.15)
        sto_label = tk.Label(form_frame, font=LABEL_TEXT, text="Enter amount of \nFree Storage: ")
        sto_label.place(relx=0.05, rely=0.80, relwidth=0.3, relheight=0.15)

        # Form Input.
        cpu_form = tk.Entry(form_frame, font=ENTRY_TEXT)
        cpu_form.place(relx=0.4, rely=0.05, relwidth=0.5, relheight=0.15)
        gpu_form = tk.Entry(form_frame, font=ENTRY_TEXT)
        gpu_form.place(relx=0.4, rely=0.30, relwidth=0.5, relheight=0.15)
        ram_slider = tk.Scale(form_frame, font=LABEL_TEXT, from_=0, to=32, orient=HORIZONTAL, resolution=4)
        ram_slider.place(relx=0.4, rely=0.55, relwidth=0.5, relheight=0.15)
        sto_form = tk.Entry(form_frame, font=ENTRY_TEXT)
        sto_form.place(relx=0.4, rely=0.80, relwidth=0.5, relheight=0.15)

        # Bottom Button Frame
        sysreq_bottom_frame = tk.Frame(srbgc)
        sysreq_bottom_frame.place(relx=0.5, rely=0.85, relheight=0.1, relwidth=0.6, anchor="center")

        # Bottom buttons.
        back_button = tk.Button(sysreq_bottom_frame, text="Back", font=25, command=lambda: controller.show_frame(StartPage))
        back_button.place(relx=0.15, rely=0.5, relheight=0.8, relwidth=0.2, anchor="center")
        submit_button = tk.Button(sysreq_bottom_frame, text="Submit", font=25, command=lambda: save_details())
        submit_button.place(relx=0.60, rely=0.5, relheight=0.8, relwidth=0.2, anchor="center")
        next_page_button = tk.Button(sysreq_bottom_frame, text="Next", font=25, command=lambda: controller.show_frame(Game))
        next_page_button.place(relx=0.85, rely=0.5, relheight=0.8, relwidth=0.2, anchor="center")


# Game selection.
class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def promptTwo():
            messagebox.showwarning("Error", "You haven't input a game.")

        def get_game():
            game_choice = game_combo.get()

            if game_choice == "":
                promptTwo()

            compat_receipt = ""

            global converted_specs

            game_selection = game_choice

            cpu_component = comp_specs[0]

            gpu_component = comp_specs[1]

            ram_component = comp_specs[2]

            sto_component = comp_specs[3]

            if game_selection in game_dictionary:
                game_specifications = (game_dictionary[game_choice])
                if game_specifications[0] < cpu_component:
                    compat_receipt += str("Your CPU doesn't meet the requirements.\n")
                elif game_specifications[0] > cpu_component:
                    compat_receipt += str("Your CPU meets the requirements.\n")
                if game_specifications[1] < gpu_component:
                    compat_receipt += str("Your GPU doesn't meet the requirements.\n")
                elif game_specifications[1] > gpu_component:
                    compat_receipt += str("Your GPU meets the requirements.\n")
                if game_specifications[2] < sto_component:
                    compat_receipt += str("You do not have enough storage capacity.\n")
                else:
                    compat_receipt += str("You have enough storage capacity.\n")
                if int(game_specifications[3]) > int(ram_component):
                    compat_receipt += str("You do not have enough RAM.")
                elif int(game_specifications[3]) < int(ram_component):
                    compat_receipt += str("You have enough RAM.")

            print(compat_receipt)

            compat_complete_receipt = "Computer Compatibility Report:\n\n"
            compat_complete_receipt += compat_receipt
            game_text = tk.Text(game_text_label, bd=0, highlightthickness=0, relief='ridge', font=FORM_TEXT)
            game_text.pack()
            game_text.insert(tk.END, compat_complete_receipt)

        gsbgc = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg='#b199c7', bd=0, highlightthickness=0, relief='ridge')
        gsbgc.pack()

        game_title_frame = tk.Frame(gsbgc)
        game_title_frame.place(relx=0.5, rely=0.15, relheight=0.1, relwidth=0.8, anchor="center")
        game_title = tk.Label(game_title_frame, font=TITLE_FONT, text="Select a Game", bg='#b199c7')
        game_title.place(relheight=1, relwidth=1)

        game_frame = tk.Frame(gsbgc, bg='white')
        game_frame.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.6, anchor="center")

        game_list = ["Grand Theft Auto", "Space Engineers", "Elite Dangerous", "Astroneer", "No Man's Sky", "Star Trek Online", "Subnautica"]
        game_combo = ttk.Combobox(game_frame, values=game_list, font=ENTRY_TEXT)
        game_combo.place(relx=0.65, rely=0.15, relheight=0.12, relwidth=0.3, anchor="center")

        game_label = tk.Label(game_frame, font=LABEL_TEXT, text="Choose a Game: ")
        game_label.place(relx=0.3, rely=0.15, relheight=0.12, relwidth=0.3, anchor="center")

        game_text_label = tk.Label(game_frame)
        game_text_label.place(relx=0.35, rely=0.30, relheight=0.4, relwidth=0.40, anchor="n")

        game_image_label = tk.Label(game_frame)
        game_image_label.place(relx=0.6, rely=0.30, relheight=0.4, relwidth=0.2, anchor="nw")

        game_button = tk.Button(game_frame, text="Submit", font=25, command=lambda: get_game())
        game_button.place(relx=0.80, rely=0.80, relheight=0.12, relwidth=0.25, anchor="ne")

        back_button2 = tk.Button(game_frame, text="Back", font=25, command=lambda: controller.show_frame(SysReq))
        back_button2.place(relx=0.15, rely=0.80, relheight=0.12, relwidth=0.25, anchor="nw")


# Tutorial class.
class Tutorial(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        obgc = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg='#b8af84', bd=0, highlightthickness=0, relief='ridge')
        obgc.pack()

        # Tutorial Title.
        spec_title_frame = tk.Frame(obgc)
        spec_title_frame.place(relx=0.5, rely=0.15, relheight=0.1, relwidth=0.8, anchor="center")
        spec_title = tk.Label(spec_title_frame, font=TITLE_FONT, text="Tutorial", bg='#b8af84')
        spec_title.place(relheight=1, relwidth=1)

        # Bottom button frame.
        tutorial_bottom_frame = tk.Frame(obgc)
        tutorial_bottom_frame.place(relx=0.5, rely=0.85, relheight=0.1, relwidth=0.6, anchor="center")

        # Bottom buttons.
        back_button = tk.Button(tutorial_bottom_frame, text="Back", font=25, command=lambda: controller.show_frame(StartPage))
        back_button.place(relx=0.15, rely=0.5, relheight=0.8, relwidth=0.2, anchor="center")

        #  Placing the Reference Image.
        self.tutorial_image = tk.PhotoImage(file='tutorial_img.png')
        tutorial_image_label = tk.Label(obgc, image=self.tutorial_image)
        tutorial_image_label.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.7, anchor="center")


# App config.
app = TestApp()
app.title("Multi-Window Prototype")
app.resizable(False, False)
app.geometry("1200x800")
app.mainloop()
