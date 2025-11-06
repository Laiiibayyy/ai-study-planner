import customtkinter as ctk
import time

def splash_screen():
    ctk.set_appearance_mode("light")
    app = ctk.CTk()
    app.geometry("600x400")
    app.config(bg="#AC87F7")

    label = ctk.CTkLabel(app, text="✨ AI Study Planner ✨",
                         font=("Poppins", 30, "bold"), text_color="#0C0D12")
    label.place(relx=0.5, rely=0.5, anchor="center")

    # small fade-in animation effect
    app.after(2000, lambda: (app.destroy(), open_login()))
    app.mainloop()

def open_login():
    import login  # opens your login page

if __name__ == "__main__":
    splash_screen()
