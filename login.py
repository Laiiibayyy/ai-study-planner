import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import re

# ---------- App Setup ----------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class AuthApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("AI Study Planner 💖")
        self.geometry("900x600")
        self.resizable(False, False)
        
        # Configure fonts
        self.title_font = ("Poppins", 28, "bold")
        self.subtitle_font = ("Quicksand", 13, "italic")
        self.input_font = ("Poppins", 12)
        self.button_font = ("Poppins", 14, "bold")
        self.label_font = ("Poppins", 11)
        
        # Main container
        self.main_container = ctk.CTkFrame(self, fg_color="#F5F7FF", corner_radius=0)
        self.main_container.pack(fill="both", expand=True)
        
        # Show login page initially
        self.show_login()
    
    def clear_container(self):
        """Clear all widgets from main container"""
        for widget in self.main_container.winfo_children():
            widget.destroy()
    
    def show_login(self):
        """Display login page"""
        self.clear_container()
        
        # Left side - Illustration/Info
        left_frame = ctk.CTkFrame(self.main_container, fg_color="#6C63FF", corner_radius=0)
        left_frame.place(relx=0, rely=0, relwidth=0.45, relheight=1)
        
        ctk.CTkLabel(left_frame,
                     text="✨ Welcome Back!",
                     font=("Poppins", 32, "bold"),
                     text_color="white").place(relx=0.5, rely=0.35, anchor="center")
        
        ctk.CTkLabel(left_frame,
                     text="Plan smarter, study better,\nachieve your goals with AI",
                     font=("Quicksand", 16),
                     text_color="#E8E6FF",
                     justify="center").place(relx=0.5, rely=0.45, anchor="center")
        
        # Decorative emoji
        ctk.CTkLabel(left_frame,
                     text="📚 🎯 🌟",
                     font=("Poppins", 40),
                     text_color="white").place(relx=0.5, rely=0.6, anchor="center")
        
        # Right side - Login Form
        right_frame = ctk.CTkFrame(self.main_container, fg_color="#F5F7FF", corner_radius=0)
        right_frame.place(relx=0.45, rely=0, relwidth=0.55, relheight=1)
        
        # Form container
        form_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
        form_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title
        ctk.CTkLabel(form_frame,
                     text="Login to Your Account",
                     font=self.title_font,
                     text_color="#2D3748").pack(pady=(0, 10))
        
        ctk.CTkLabel(form_frame,
                     text="Enter your credentials to continue",
                     font=self.subtitle_font,
                     text_color="#718096").pack(pady=(0, 30))
        
        # Username/Email
        ctk.CTkLabel(form_frame,
                     text="Username or Email",
                     font=self.label_font,
                     text_color="#4A5568",
                     anchor="w").pack(fill="x", padx=5)
        
        self.login_user = ctk.CTkEntry(form_frame,
                                       placeholder_text="Enter your username",
                                       width=350,
                                       height=45,
                                       corner_radius=10,
                                       border_width=2,
                                       border_color="#E2E8F0",
                                       fg_color="white",
                                       font=self.input_font)
        self.login_user.pack(pady=(5, 15))
        
        # Password
        ctk.CTkLabel(form_frame,
                     text="Password",
                     font=self.label_font,
                     text_color="#4A5568",
                     anchor="w").pack(fill="x", padx=5)
        
        self.login_pass = ctk.CTkEntry(form_frame,
                                       placeholder_text="Enter your password",
                                       width=350,
                                       height=45,
                                       corner_radius=10,
                                       border_width=2,
                                       border_color="#E2E8F0",
                                       fg_color="white",
                                       show="•",
                                       font=self.input_font)
        self.login_pass.pack(pady=(5, 10))
        
        # Forgot password (right aligned)
        forgot_btn = ctk.CTkButton(form_frame,
                                   text="Forgot Password?",
                                   font=("Poppins", 10),
                                   text_color="#6C63FF",
                                   fg_color="transparent",
                                   hover_color="#EDF2F7",
                                   width=100,
                                   height=20,
                                   command=self.forgot_password)
        forgot_btn.pack(anchor="e", pady=(0, 20))
        
        # Login button
        ctk.CTkButton(form_frame,
                      text="Login",
                      width=350,
                      height=45,
                      corner_radius=10,
                      fg_color="#6C63FF",
                      hover_color="#5B52D6",
                      font=self.button_font,
                      command=self.login_action).pack(pady=10)
        
        # Divider
        divider_frame = ctk.CTkFrame(form_frame, fg_color="transparent", height=30)
        divider_frame.pack(fill="x", pady=15)
        
        ctk.CTkFrame(divider_frame, height=1, fg_color="#E2E8F0").place(relx=0, rely=0.5, relwidth=0.4)
        ctk.CTkLabel(divider_frame, text="OR", font=("Poppins", 10), text_color="#A0AEC0").place(relx=0.5, rely=0.5, anchor="center")
        ctk.CTkFrame(divider_frame, height=1, fg_color="#E2E8F0").place(relx=0.6, rely=0.5, relwidth=0.4)
        
        # Sign up link
        signup_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        signup_frame.pack(pady=10)
        
        ctk.CTkLabel(signup_frame,
                     text="Don't have an account?",
                     font=("Poppins", 11),
                     text_color="#718096").pack(side="left", padx=(0, 5))
        
        ctk.CTkButton(signup_frame,
                      text="Sign Up",
                      font=("Poppins", 11, "bold"),
                      text_color="#6C63FF",
                      fg_color="transparent",
                      hover_color="#EDF2F7",
                      width=60,
                      height=25,
                      command=self.show_signup).pack(side="left")
    
    def show_signup(self):
        """Display signup page"""
        self.clear_container()
        
        # Left side - Illustration/Info
        left_frame = ctk.CTkFrame(self.main_container, fg_color="#FF6B9D", corner_radius=0)
        left_frame.place(relx=0, rely=0, relwidth=0.4, relheight=1)
        
        ctk.CTkLabel(left_frame,
                     text="🌟 Join Us!",
                     font=("Poppins", 32, "bold"),
                     text_color="white").place(relx=0.5, rely=0.3, anchor="center")
        
        ctk.CTkLabel(left_frame,
                     text="Create your account and start\nyour journey to academic success",
                     font=("Quicksand", 15),
                     text_color="#FFE5EE",
                     justify="center").place(relx=0.5, rely=0.42, anchor="center")
        
        ctk.CTkLabel(left_frame,
                     text="🎓 💝 ✨",
                     font=("Poppins", 40),
                     text_color="white").place(relx=0.5, rely=0.6, anchor="center")
        
        # Right side - Signup Form with scrollable frame
        right_frame = ctk.CTkFrame(self.main_container, fg_color="#F5F7FF", corner_radius=0)
        right_frame.place(relx=0.4, rely=0, relwidth=0.6, relheight=1)
        
        # Scrollable form container
        scroll_frame = ctk.CTkScrollableFrame(right_frame, 
                                              fg_color="transparent",
                                              width=450,
                                              height=520)
        scroll_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title
        ctk.CTkLabel(scroll_frame,
                     text="Create Your Account",
                     font=self.title_font,
                     text_color="#2D3748").pack(pady=(10, 5))
        
        ctk.CTkLabel(scroll_frame,
                     text="Fill in your details to get started",
                     font=self.subtitle_font,
                     text_color="#718096").pack(pady=(0, 25))
        
        # Name fields (side by side)
        name_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        name_frame.pack(fill="x", pady=5)
        
        # First Name
        fname_frame = ctk.CTkFrame(name_frame, fg_color="transparent")
        fname_frame.pack(side="left", expand=True, fill="x", padx=(0, 5))
        
        ctk.CTkLabel(fname_frame,
                     text="First Name *",
                     font=self.label_font,
                     text_color="#4A5568",
                     anchor="w").pack(fill="x")
        
        self.signup_fname = ctk.CTkEntry(fname_frame,
                                         placeholder_text="John",
                                         height=40,
                                         corner_radius=8,
                                         border_width=2,
                                         border_color="#E2E8F0",
                                         fg_color="white",
                                         font=self.input_font)
        self.signup_fname.pack(fill="x", pady=(3, 0))
        
        # Last Name
        lname_frame = ctk.CTkFrame(name_frame, fg_color="transparent")
        lname_frame.pack(side="left", expand=True, fill="x", padx=(5, 0))
        
        ctk.CTkLabel(lname_frame,
                     text="Last Name *",
                     font=self.label_font,
                     text_color="#4A5568",
                     anchor="w").pack(fill="x")
        
        self.signup_lname = ctk.CTkEntry(lname_frame,
                                         placeholder_text="Doe",
                                         height=40,
                                         corner_radius=8,
                                         border_width=2,
                                         border_color="#E2E8F0",
                                         fg_color="white",
                                         font=self.input_font)
        self.signup_lname.pack(fill="x", pady=(3, 0))
        
        # Email
        ctk.CTkLabel(scroll_frame,
                     text="Email Address *",
                     font=self.label_font,
                     text_color="#4A5568",
                     anchor="w").pack(fill="x", padx=5, pady=(15, 0))
        
        self.signup_email = ctk.CTkEntry(scroll_frame,
                                         placeholder_text="john.doe@example.com",
                                         width=400,
                                         height=40,
                                         corner_radius=8,
                                         border_width=2,
                                         border_color="#E2E8F0",
                                         fg_color="white",
                                         font=self.input_font)
        self.signup_email.pack(pady=(3, 10))
        
        # Institute Name
        ctk.CTkLabel(scroll_frame,
                     text="Institute/University Name *",
                     font=self.label_font,
                     text_color="#4A5568",
                     anchor="w").pack(fill="x", padx=5)
        
        self.signup_institute = ctk.CTkEntry(scroll_frame,
                                             placeholder_text="e.g., University of XYZ",
                                             width=400,
                                             height=40,
                                             corner_radius=8,
                                             border_width=2,
                                             border_color="#E2E8F0",
                                             fg_color="white",
                                             font=self.input_font)
        self.signup_institute.pack(pady=(3, 10))
        
        # Field of Study
        ctk.CTkLabel(scroll_frame,
                     text="Field of Study",
                     font=self.label_font,
                     text_color="#4A5568",
                     anchor="w").pack(fill="x", padx=5)
        
        self.signup_field = ctk.CTkEntry(scroll_frame,
                                         placeholder_text="e.g., Computer Science (Optional)",
                                         width=400,
                                         height=40,
                                         corner_radius=8,
                                         border_width=2,
                                         border_color="#E2E8F0",
                                         fg_color="white",
                                         font=self.input_font)
        self.signup_field.pack(pady=(3, 10))
        
        # Password
        ctk.CTkLabel(scroll_frame,
                     text="Password *",
                     font=self.label_font,
                     text_color="#4A5568",
                     anchor="w").pack(fill="x", padx=5)
        
        self.signup_pass = ctk.CTkEntry(scroll_frame,
                                        placeholder_text="Min. 8 characters",
                                        width=400,
                                        height=40,
                                        corner_radius=8,
                                        border_width=2,
                                        border_color="#E2E8F0",
                                        fg_color="white",
                                        show="•",
                                        font=self.input_font)
        self.signup_pass.pack(pady=(3, 10))
        
        # Confirm Password
        ctk.CTkLabel(scroll_frame,
                     text="Confirm Password *",
                     font=self.label_font,
                     text_color="#4A5568",
                     anchor="w").pack(fill="x", padx=5)
        
        self.signup_confirm = ctk.CTkEntry(scroll_frame,
                                           placeholder_text="Re-enter your password",
                                           width=400,
                                           height=40,
                                           corner_radius=8,
                                           border_width=2,
                                           border_color="#E2E8F0",
                                           fg_color="white",
                                           show="•",
                                           font=self.input_font)
        self.signup_confirm.pack(pady=(3, 10))
        
        # Terms checkbox
        self.terms_var = ctk.BooleanVar()
        terms_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        terms_frame.pack(fill="x", pady=15)
        
        ctk.CTkCheckBox(terms_frame,
                        text="I agree to the Terms & Conditions",
                        variable=self.terms_var,
                        font=("Poppins", 10),
                        text_color="#4A5568",
                        fg_color="#FF6B9D",
                        hover_color="#E55A88").pack(anchor="w")
        
        # Sign up button
        ctk.CTkButton(scroll_frame,
                      text="Create Account",
                      width=400,
                      height=45,
                      corner_radius=10,
                      fg_color="#FF6B9D",
                      hover_color="#E55A88",
                      font=self.button_font,
                      command=self.signup_action).pack(pady=15)
        
        # Login link
        login_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        login_frame.pack(pady=(5, 20))
        
        ctk.CTkLabel(login_frame,
                     text="Already have an account?",
                     font=("Poppins", 11),
                     text_color="#718096").pack(side="left", padx=(0, 5))
        
        ctk.CTkButton(login_frame,
                      text="Login",
                      font=("Poppins", 11, "bold"),
                      text_color="#FF6B9D",
                      fg_color="transparent",
                      hover_color="#EDF2F7",
                      width=60,
                      height=25,
                      command=self.show_login).pack(side="left")
    
    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def login_action(self):
        """Handle login"""
        username = self.login_user.get().strip()
        password = self.login_pass.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields!")
            return
        
        # TODO: Add database validation here
        messagebox.showinfo("Success", f"Welcome back, {username}! 🌟")
    
    def signup_action(self):
        """Handle signup with validation"""
        fname = self.signup_fname.get().strip()
        lname = self.signup_lname.get().strip()
        email = self.signup_email.get().strip()
        institute = self.signup_institute.get().strip()
        field = self.signup_field.get().strip()
        password = self.signup_pass.get()
        confirm = self.signup_confirm.get()
        
        # Validation
        if not all([fname, lname, email, institute, password, confirm]):
            messagebox.showerror("Error", "Please fill in all required fields (marked with *)!")
            return
        
        if not self.validate_email(email):
            messagebox.showerror("Error", "Please enter a valid email address!")
            return
        
        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long!")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        
        if not self.terms_var.get():
            messagebox.showerror("Error", "Please accept the Terms & Conditions!")
            return
        
        # TODO: Add database insertion here
        messagebox.showinfo("Success", f"Welcome aboard, {fname}! 🎉\nYour account has been created successfully!")
        self.show_login()
    
    def forgot_password(self):
        """Handle forgot password"""
        messagebox.showinfo("Forgot Password", "Password reset link will be sent to your email! 💌")

# ---------- Run App ----------
if __name__ == "__main__":
    app = AuthApp()
    app.mainloop()