import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont

# ---------- App Setup ----------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("AI Study Planner 💖")
app.geometry("850x550")
app.resizable(False, False)

# ---------- Background Image ----------
try:
    bg = Image.open("bg.png").resize((850, 550))
    bg_photo = ImageTk.PhotoImage(bg)
    bg_label = ctk.CTkLabel(app, image=bg_photo, text="")
    bg_label.place(x=0, y=0)
except:
    app.configure(bg="#CACEF6")

# ---------- Overlay (Translucent) ----------
overlay = ctk.CTkFrame(app, width=850, height=550, corner_radius=0, fg_color="#bfd2fa")
overlay.place(x=0, y=0)

# ---------- Fonts ----------
title_font = ("Poppins", 26, "bold")
subtitle_font = ("Quicksand", 14, "italic")
input_font = ("Poppins", 13)
button_font = ("Poppins", 14, "bold")

# ---------- Title ----------
title = ctk.CTkLabel(overlay,
                     text="Welcome to Your Cute AI Study Planner 🌸",
                     font=title_font,
                     text_color="#1F1D27")
title.place(relx=0.5, rely=0.15, anchor="center")

subtitle = ctk.CTkLabel(overlay,
                        text="“Plan smarter • Stay motivated • Shine brighter ✨”",
                        font=subtitle_font,
                        text_color="#28065F")
subtitle.place(relx=0.5, rely=0.22, anchor="center")

# ---------- Login Card ----------
frame = ctk.CTkFrame(overlay,
                     width=350,
                     height=300,
                     corner_radius=25,
                     fg_color="#A1AAE0")
frame.place(relx=0.5, rely=0.6, anchor="center")

heading = ctk.CTkLabel(frame, text="Login 💕",
                       font=("Poppins", 22, "bold"),
                       text_color="#161320")
heading.pack(pady=15)

entry_user = ctk.CTkEntry(frame,
                          placeholder_text="Username",
                          width=250,
                          height=40,
                          corner_radius=12,
                          border_color="#12141D",
                          font=input_font)
entry_user.pack(pady=10)

entry_pass = ctk.CTkEntry(frame,
                          placeholder_text="Password",
                          width=250,
                          height=40,
                          corner_radius=12,
                          border_color="#120F19",
                          show="*",
                          font=input_font)
entry_pass.pack(pady=10)

# ---------- Login Action ----------
def login_action():
    u = entry_user.get()
    p = entry_pass.get()
    if u and p:
        messagebox.showinfo("Welcome", f"Hi {u}! 🌷 Let's get productive!")
    else:
        messagebox.showwarning("Oops!", "Please fill both fields!")

# ---------- Button ----------
ctk.CTkButton(frame,
              text="Login",
              width=180,
              height=40,
              corner_radius=20,
              fg_color="#DCD8E8",
              hover_color="#0D0C12",
              font=button_font,
              command=login_action).pack(pady=20)

# ---------- Bottom Text ----------
ctk.CTkLabel(frame,
             text="Don’t have an account? Sign up 💌",
             font=("Quicksand", 12),
             text_color="#12141D").pack()

# ---------- Run ----------
app.mainloop()
