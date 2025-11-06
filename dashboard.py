import customtkinter as ctk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import random

# ---------- App Setup ----------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("AI Study Planner - Dashboard 📚")
        self.geometry("1200x700")
        self.resizable(False, False)
        
        # Sample data storage (replace with database later)
        self.subjects = []
        self.exams = []
        self.study_progress = {"Mon": 2, "Tue": 3.5, "Wed": 1.5, "Thu": 4, "Fri": 2.5, "Sat": 5, "Sun": 3}
        
        # Motivational quotes
        self.quotes = [
            "Success is the sum of small efforts repeated day in and day out. 💪",
            "The expert in anything was once a beginner. Keep going! 🌟",
            "Study while others are sleeping, work while others are playing. 🎯",
            "Your future self will thank you for the effort you put in today. ✨",
            "Don't watch the clock; do what it does. Keep going! ⏰",
            "The only way to learn mathematics is to do mathematics. 📐",
            "Education is not preparation for life; education is life itself. 📚"
        ]
        
        # Fonts
        self.header_font = ("Poppins", 24, "bold")
        self.title_font = ("Poppins", 16, "bold")
        self.normal_font = ("Poppins", 12)
        self.button_font = ("Poppins", 13, "bold")
        
        self.create_dashboard()
    
    def create_dashboard(self):
        # Main container
        main_frame = ctk.CTkFrame(self, fg_color="#F0F4F8", corner_radius=0)
        main_frame.pack(fill="both", expand=True)
        
        # ========== SIDEBAR ==========
        sidebar = ctk.CTkFrame(main_frame, width=250, fg_color="#2D3748", corner_radius=0)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)
        
        # Logo/Title
        ctk.CTkLabel(sidebar,
                     text="📚 Study Planner",
                     font=("Poppins", 20, "bold"),
                     text_color="white").pack(pady=(30, 10))
        
        ctk.CTkLabel(sidebar,
                     text="AI Powered Learning",
                     font=("Quicksand", 11, "italic"),
                     text_color="#A0AEC0").pack(pady=(0, 30))
        
        # Menu buttons
        menu_items = [
            ("🏠 Dashboard", "#4299E1"),
            ("📖 My Subjects", "#48BB78"),
            ("📅 Schedule", "#ED8936"),
            ("📊 Analytics", "#9F7AEA"),
            ("⚙️ Settings", "#718096"),
        ]
        
        for item, color in menu_items:
            btn = ctk.CTkButton(sidebar,
                               text=item,
                               width=220,
                               height=45,
                               corner_radius=10,
                               fg_color=color if item == "🏠 Dashboard" else "transparent",
                               hover_color="#4A5568",
                               font=("Poppins", 13),
                               anchor="w",
                               text_color="white")
            btn.pack(pady=8, padx=15)
        
        # Logout button at bottom
        ctk.CTkButton(sidebar,
                      text="🚪 Logout",
                      width=220,
                      height=40,
                      corner_radius=10,
                      fg_color="#E53E3E",
                      hover_color="#C53030",
                      font=("Poppins", 12, "bold"),
                      command=self.logout).pack(side="bottom", pady=20, padx=15)
        
        # ========== MAIN CONTENT AREA ==========
        content_area = ctk.CTkFrame(main_frame, fg_color="#F0F4F8", corner_radius=0)
        content_area.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ctk.CTkFrame(content_area, fg_color="transparent", height=60)
        header_frame.pack(fill="x", pady=(0, 20))
        header_frame.pack_propagate(False)
        
        ctk.CTkLabel(header_frame,
                     text="Welcome Back, Student! 👋",
                     font=self.header_font,
                     text_color="#2D3748",
                     anchor="w").pack(side="left")
        
        date_label = ctk.CTkLabel(header_frame,
                                  text=datetime.now().strftime("%B %d, %Y"),
                                  font=("Poppins", 12),
                                  text_color="#718096")
        date_label.pack(side="right")
        
        # Scrollable content
        scroll_frame = ctk.CTkScrollableFrame(content_area, 
                                              fg_color="transparent",
                                              height=550)
        scroll_frame.pack(fill="both", expand=True)
        
        # ========== ROW 1: Quick Actions ==========
        actions_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        actions_frame.pack(fill="x", pady=(0, 15))
        
        # Add Subject Card
        self.create_action_card(actions_frame, 
                               "📚 Add Subject", 
                               "#4299E1",
                               self.add_subject_dialog,
                               0)
        
        # Add Exam Card
        self.create_action_card(actions_frame,
                               "📅 Add Exam Date",
                               "#48BB78",
                               self.add_exam_dialog,
                               1)
        
        # Generate Schedule Card
        self.create_action_card(actions_frame,
                               "✨ Generate Schedule",
                               "#9F7AEA",
                               self.generate_schedule,
                               2)
        
        # ========== ROW 2: Motivation Quote ==========
        quote_frame = ctk.CTkFrame(scroll_frame, 
                                   fg_color="white",
                                   corner_radius=15,
                                   border_width=2,
                                   border_color="#E2E8F0")
        quote_frame.pack(fill="x", pady=15)
        
        ctk.CTkLabel(quote_frame,
                     text="💡 Daily Motivation",
                     font=self.title_font,
                     text_color="#2D3748",
                     anchor="w").pack(anchor="w", padx=20, pady=(15, 5))
        
        self.quote_label = ctk.CTkLabel(quote_frame,
                                       text=random.choice(self.quotes),
                                       font=("Quicksand", 14, "italic"),
                                       text_color="#4A5568",
                                       wraplength=850,
                                       justify="left")
        self.quote_label.pack(anchor="w", padx=20, pady=(5, 10))
        
        ctk.CTkButton(quote_frame,
                      text="🔄 New Quote",
                      width=120,
                      height=30,
                      corner_radius=8,
                      fg_color="#ED8936",
                      hover_color="#DD6B20",
                      font=("Poppins", 11),
                      command=self.refresh_quote).pack(anchor="e", padx=20, pady=(0, 15))
        
        # ========== ROW 3: Two Columns ==========
        columns_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        columns_frame.pack(fill="both", expand=True, pady=15)
        
        # Left Column - Subjects & Exams
        left_column = ctk.CTkFrame(columns_frame, fg_color="transparent")
        left_column.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # My Subjects
        subjects_card = ctk.CTkFrame(left_column, 
                                    fg_color="white",
                                    corner_radius=15,
                                    border_width=2,
                                    border_color="#E2E8F0")
        subjects_card.pack(fill="x", pady=(0, 15))
        
        ctk.CTkLabel(subjects_card,
                     text="📖 My Subjects",
                     font=self.title_font,
                     text_color="#2D3748",
                     anchor="w").pack(anchor="w", padx=20, pady=(15, 10))
        
        self.subjects_list = ctk.CTkTextbox(subjects_card,
                                           height=150,
                                           fg_color="#F7FAFC",
                                           corner_radius=8,
                                           font=self.normal_font)
        self.subjects_list.pack(fill="x", padx=20, pady=(0, 15))
        self.update_subjects_display()
        
        # Upcoming Exams
        exams_card = ctk.CTkFrame(left_column,
                                 fg_color="white",
                                 corner_radius=15,
                                 border_width=2,
                                 border_color="#E2E8F0")
        exams_card.pack(fill="x")
        
        ctk.CTkLabel(exams_card,
                     text="📅 Upcoming Exams",
                     font=self.title_font,
                     text_color="#2D3748",
                     anchor="w").pack(anchor="w", padx=20, pady=(15, 10))
        
        self.exams_list = ctk.CTkTextbox(exams_card,
                                        height=150,
                                        fg_color="#F7FAFC",
                                        corner_radius=8,
                                        font=self.normal_font)
        self.exams_list.pack(fill="x", padx=20, pady=(0, 15))
        self.update_exams_display()
        
        # Right Column - Progress Chart
        right_column = ctk.CTkFrame(columns_frame, fg_color="transparent")
        right_column.pack(side="left", fill="both", expand=True)
        
        chart_card = ctk.CTkFrame(right_column,
                                 fg_color="white",
                                 corner_radius=15,
                                 border_width=2,
                                 border_color="#E2E8F0")
        chart_card.pack(fill="both", expand=True)
        
        ctk.CTkLabel(chart_card,
                     text="📊 Weekly Study Progress",
                     font=self.title_font,
                     text_color="#2D3748",
                     anchor="w").pack(anchor="w", padx=20, pady=(15, 10))
        
        # Create chart
        self.create_progress_chart(chart_card)
    
    def create_action_card(self, parent, title, color, command, col):
        """Create action card button"""
        card = ctk.CTkFrame(parent, fg_color="white", corner_radius=15,
                           border_width=2, border_color="#E2E8F0")
        card.grid(row=0, column=col, padx=10, sticky="ew")
        parent.grid_columnconfigure(col, weight=1)
        
        btn = ctk.CTkButton(card,
                           text=title,
                           width=250,
                           height=80,
                           corner_radius=12,
                           fg_color=color,
                           hover_color=self.darken_color(color),
                           font=("Poppins", 15, "bold"),
                           command=command)
        btn.pack(padx=15, pady=15)
    
    def darken_color(self, hex_color):
        """Darken a hex color by 20%"""
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        r, g, b = int(r * 0.8), int(g * 0.8), int(b * 0.8)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def create_progress_chart(self, parent):
        """Create and display progress chart"""
        fig, ax = plt.subplots(figsize=(5, 3.5), facecolor='white')
        
        days = list(self.study_progress.keys())
        hours = list(self.study_progress.values())
        
        colors = ['#4299E1' if h >= 3 else '#ED8936' for h in hours]
        bars = ax.bar(days, hours, color=colors, alpha=0.8, width=0.6)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height}h',
                   ha='center', va='bottom', fontsize=9, fontweight='bold')
        
        ax.set_ylabel('Hours Studied', fontsize=10, fontweight='bold')
        ax.set_xlabel('Days', fontsize=10, fontweight='bold')
        ax.set_ylim(0, max(hours) + 1)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        plt.tight_layout()
        
        # Embed chart in tkinter
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(padx=20, pady=(0, 15))
    
    def add_subject_dialog(self):
        """Dialog to add new subject"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add New Subject")
        dialog.geometry("400x300")
        dialog.resizable(False, False)
        dialog.grab_set()
        
        ctk.CTkLabel(dialog,
                     text="Add New Subject 📚",
                     font=("Poppins", 18, "bold"),
                     text_color="#2D3748").pack(pady=(20, 30))
        
        ctk.CTkLabel(dialog, text="Subject Name:", font=("Poppins", 12)).pack(anchor="w", padx=40)
        subject_entry = ctk.CTkEntry(dialog, width=320, height=40, font=("Poppins", 12))
        subject_entry.pack(pady=(5, 15), padx=40)
        
        ctk.CTkLabel(dialog, text="Difficulty Level:", font=("Poppins", 12)).pack(anchor="w", padx=40)
        difficulty = ctk.CTkComboBox(dialog, 
                                     values=["Easy", "Medium", "Hard"],
                                     width=320,
                                     height=40,
                                     font=("Poppins", 12))
        difficulty.set("Medium")
        difficulty.pack(pady=(5, 30), padx=40)
        
        def save_subject():
            name = subject_entry.get().strip()
            if name:
                self.subjects.append({"name": name, "difficulty": difficulty.get()})
                self.update_subjects_display()
                messagebox.showinfo("Success", f"Subject '{name}' added successfully! 🎉")
                dialog.destroy()
            else:
                messagebox.showerror("Error", "Please enter subject name!")
        
        ctk.CTkButton(dialog,
                      text="Add Subject",
                      width=320,
                      height=45,
                      fg_color="#48BB78",
                      hover_color="#38A169",
                      font=("Poppins", 13, "bold"),
                      command=save_subject).pack(pady=10)
    
    def add_exam_dialog(self):
        """Dialog to add exam date"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Add Exam Date")
        dialog.geometry("400x350")
        dialog.resizable(False, False)
        dialog.grab_set()
        
        ctk.CTkLabel(dialog,
                     text="Add Exam Date 📅",
                     font=("Poppins", 18, "bold"),
                     text_color="#2D3748").pack(pady=(20, 30))
        
        ctk.CTkLabel(dialog, text="Subject:", font=("Poppins", 12)).pack(anchor="w", padx=40)
        subject_names = [s["name"] for s in self.subjects] if self.subjects else ["Add subjects first"]
        subject_combo = ctk.CTkComboBox(dialog,
                                       values=subject_names,
                                       width=320,
                                       height=40,
                                       font=("Poppins", 12))
        subject_combo.pack(pady=(5, 15), padx=40)
        
        ctk.CTkLabel(dialog, text="Exam Date (DD-MM-YYYY):", font=("Poppins", 12)).pack(anchor="w", padx=40)
        date_entry = ctk.CTkEntry(dialog, width=320, height=40, 
                                 placeholder_text="e.g., 25-12-2024",
                                 font=("Poppins", 12))
        date_entry.pack(pady=(5, 30), padx=40)
        
        def save_exam():
            subject = subject_combo.get()
            date_str = date_entry.get().strip()
            
            if not self.subjects:
                messagebox.showerror("Error", "Please add subjects first!")
                return
            
            if subject and date_str:
                try:
                    # Validate date format
                    datetime.strptime(date_str, "%d-%m-%Y")
                    self.exams.append({"subject": subject, "date": date_str})
                    self.update_exams_display()
                    messagebox.showinfo("Success", f"Exam for {subject} scheduled! 📅")
                    dialog.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Invalid date format! Use DD-MM-YYYY")
            else:
                messagebox.showerror("Error", "Please fill all fields!")
        
        ctk.CTkButton(dialog,
                      text="Schedule Exam",
                      width=320,
                      height=45,
                      fg_color="#4299E1",
                      hover_color="#3182CE",
                      font=("Poppins", 13, "bold"),
                      command=save_exam).pack(pady=10)
    
    def generate_schedule(self):
        """Generate AI study schedule"""
        if not self.subjects or not self.exams:
            messagebox.showwarning("Warning", 
                                 "Please add subjects and exam dates first!")
            return
        
        # Simple AI logic - generate schedule based on exam dates
        schedule_window = ctk.CTkToplevel(self)
        schedule_window.title("Generated Study Schedule")
        schedule_window.geometry("600x500")
        schedule_window.grab_set()
        
        ctk.CTkLabel(schedule_window,
                     text="✨ AI Generated Study Schedule",
                     font=("Poppins", 20, "bold"),
                     text_color="#2D3748").pack(pady=(20, 10))
        
        ctk.CTkLabel(schedule_window,
                     text="Optimized for your exam dates and subjects",
                     font=("Quicksand", 12, "italic"),
                     text_color="#718096").pack(pady=(0, 20))
        
        schedule_text = ctk.CTkTextbox(schedule_window,
                                       width=550,
                                       height=350,
                                       font=("Poppins", 11))
        schedule_text.pack(padx=20, pady=10)
        
        # Generate simple schedule
        schedule_content = "📅 YOUR PERSONALIZED STUDY SCHEDULE\n\n"
        
        for exam in sorted(self.exams, key=lambda x: datetime.strptime(x["date"], "%d-%m-%Y")):
            exam_date = datetime.strptime(exam["date"], "%d-%m-%Y")
            days_left = (exam_date - datetime.now()).days
            
            schedule_content += f"📚 {exam['subject']} - Exam Date: {exam['date']}\n"
            schedule_content += f"   ⏰ Days Remaining: {days_left} days\n"
            
            if days_left > 7:
                schedule_content += f"   ✅ Study Plan: 1-2 hours daily, focus on concepts\n"
            elif days_left > 3:
                schedule_content += f"   ⚡ Study Plan: 3-4 hours daily, practice problems\n"
            else:
                schedule_content += f"   🔥 Study Plan: 4-5 hours daily, REVISION MODE!\n"
            
            schedule_content += "\n"
        
        schedule_content += "\n💡 AI Tips:\n"
        schedule_content += "• Take 10-minute breaks every hour\n"
        schedule_content += "• Review difficult topics in the morning\n"
        schedule_content += "• Practice past papers 3 days before exam\n"
        schedule_content += "• Get 7-8 hours of sleep for better retention\n"
        
        schedule_text.insert("1.0", schedule_content)
        schedule_text.configure(state="disabled")
        
        ctk.CTkButton(schedule_window,
                      text="Close",
                      width=150,
                      height=40,
                      command=schedule_window.destroy).pack(pady=10)
    
    def update_subjects_display(self):
        """Update subjects list display"""
        self.subjects_list.configure(state="normal")
        self.subjects_list.delete("1.0", "end")
        
        if self.subjects:
            for i, subject in enumerate(self.subjects, 1):
                emoji = "🟢" if subject["difficulty"] == "Easy" else "🟡" if subject["difficulty"] == "Medium" else "🔴"
                self.subjects_list.insert("end", f"{i}. {emoji} {subject['name']} ({subject['difficulty']})\n")
        else:
            self.subjects_list.insert("end", "No subjects added yet. Click 'Add Subject' to start! 📚")
        
        self.subjects_list.configure(state="disabled")
    
    def update_exams_display(self):
        """Update exams list display"""
        self.exams_list.configure(state="normal")
        self.exams_list.delete("1.0", "end")
        
        if self.exams:
            sorted_exams = sorted(self.exams, key=lambda x: datetime.strptime(x["date"], "%d-%m-%Y"))
            for exam in sorted_exams:
                exam_date = datetime.strptime(exam["date"], "%d-%m-%Y")
                days_left = (exam_date - datetime.now()).days
                
                if days_left < 0:
                    status = "✅ Completed"
                elif days_left <= 3:
                    status = f"🔥 {days_left} days left!"
                else:
                    status = f"📅 {days_left} days left"
                
                self.exams_list.insert("end", f"• {exam['subject']} - {exam['date']} {status}\n")
        else:
            self.exams_list.insert("end", "No exams scheduled. Add exam dates to plan your studies! 📅")
        
        self.exams_list.configure(state="disabled")
    
    def refresh_quote(self):
        """Display new random quote"""
        new_quote = random.choice(self.quotes)
        self.quote_label.configure(text=new_quote)
    
    def logout(self):
        """Logout function"""
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.destroy()

# ---------- Run App ----------
if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()










    """
Streak Widget UI Component
Add this to your dashboard
"""

import customtkinter as ctk
from tkinter import messagebox
import math

class StreakWidget(ctk.CTkFrame):
    def __init__(self, parent, streak_manager, user_id, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.streak_manager = streak_manager
        self.user_id = user_id
        self.streak_data = None
        
        # Colors
        self.streak_color = "#FF6B6B"  # Coral red
        self.xp_color = "#4ECDC4"      # Turquoise
        self.badge_color = "#FFD93D"   # Gold
        
        self.configure(fg_color="white", corner_radius=15, border_width=2, border_color="#E2E8F0")
        
        self.create_widgets()
        self.load_data()
    
    def create_widgets(self):
        """Create all UI components"""
        
        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(15, 10))
        
        ctk.CTkLabel(header,
                     text="🔥 Your Study Streak",
                     font=("Poppins", 18, "bold"),
                     text_color="#2D3748").pack(side="left")
        
        self.refresh_btn = ctk.CTkButton(header,
                                         text="🔄",
                                         width=35,
                                         height=35,
                                         corner_radius=10,
                                         fg_color="#EDF2F7",
                                         text_color="#2D3748",
                                         hover_color="#E2E8F0",
                                         command=self.refresh_data)
        self.refresh_btn.pack(side="right")
        
        # Main streak display
        streak_frame = ctk.CTkFrame(self, fg_color="#FFF5F5", corner_radius=12)
        streak_frame.pack(fill="x", padx=20, pady=10)
        
        # Streak number with flame animation container
        self.streak_display = ctk.CTkFrame(streak_frame, fg_color="transparent")
        self.streak_display.pack(pady=20)
        
        self.streak_label = ctk.CTkLabel(self.streak_display,
                                         text="0",
                                         font=("Poppins", 48, "bold"),
                                         text_color=self.streak_color)
        self.streak_label.pack()
        
        ctk.CTkLabel(self.streak_display,
                     text="Day Streak",
                     font=("Poppins", 14),
                     text_color="#718096").pack()
        
        # Longest streak
        self.longest_label = ctk.CTkLabel(streak_frame,
                                          text="Longest: 0 days 🏆",
                                          font=("Poppins", 12),
                                          text_color="#4A5568")
        self.longest_label.pack(pady=(0, 15))
        
        # XP and Level Section
        xp_frame = ctk.CTkFrame(self, fg_color="#F0FFF4", corner_radius=12)
        xp_frame.pack(fill="x", padx=20, pady=10)
        
        xp_content = ctk.CTkFrame(xp_frame, fg_color="transparent")
        xp_content.pack(fill="x", padx=15, pady=15)
        
        # Level display
        level_frame = ctk.CTkFrame(xp_content, fg_color="transparent")
        level_frame.pack(side="left", expand=True)
        
        self.level_label = ctk.CTkLabel(level_frame,
                                        text="Level 1",
                                        font=("Poppins", 20, "bold"),
                                        text_color="#2D3748")
        self.level_label.pack(anchor="w")
        
        self.xp_label = ctk.CTkLabel(level_frame,
                                     text="0 / 100 XP",
                                     font=("Poppins", 12),
                                     text_color="#718096")
        self.xp_label.pack(anchor="w")
        
        # XP Progress bar
        self.xp_progress = ctk.CTkProgressBar(xp_content,
                                              width=200,
                                              height=12,
                                              corner_radius=6,
                                              fg_color="#E2E8F0",
                                              progress_color=self.xp_color)
        self.xp_progress.pack(side="right")
        self.xp_progress.set(0)
        
        # Study Stats
        stats_frame = ctk.CTkFrame(self, fg_color="#FFFAF0", corner_radius=12)
        stats_frame.pack(fill="x", padx=20, pady=10)
        
        stats_content = ctk.CTkFrame(stats_frame, fg_color="transparent")
        stats_content.pack(fill="x", padx=15, pady=15)
        
        # Total study days
        self.total_days_label = ctk.CTkLabel(stats_content,
                                             text="📚 Total Study Days: 0",
                                             font=("Poppins", 13),
                                             text_color="#2D3748")
        self.total_days_label.pack(anchor="w", pady=3)
        
        # Last study date
        self.last_study_label = ctk.CTkLabel(stats_content,
                                             text="📅 Last Study: Never",
                                             font=("Poppins", 13),
                                             text_color="#2D3748")
        self.last_study_label.pack(anchor="w", pady=3)
        
        # Badges Section
        badges_header = ctk.CTkFrame(self, fg_color="transparent")
        badges_header.pack(fill="x", padx=20, pady=(15, 5))
        
        ctk.CTkLabel(badges_header,
                     text="🏆 Badges Earned",
                     font=("Poppins", 16, "bold"),
                     text_color="#2D3748").pack(side="left")
        
        self.badge_count_label = ctk.CTkLabel(badges_header,
                                              text="0",
                                              font=("Poppins", 14, "bold"),
                                              text_color=self.badge_color)
        self.badge_count_label.pack(side="right")
        
        # Scrollable badges container
        self.badges_container = ctk.CTkScrollableFrame(self,
                                                       height=150,
                                                       fg_color="#F7FAFC",
                                                       corner_radius=12)
        self.badges_container.pack(fill="both", expand=True, padx=20, pady=(5, 15))
        
        # Action buttons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        ctk.CTkButton(button_frame,
                      text="📊 View Stats",
                      width=140,
                      height=40,
                      corner_radius=10,
                      fg_color="#A8B5FF",
                      hover_color="#8A9DE8",
                      font=("Poppins", 12, "bold"),
                      command=self.show_detailed_stats).pack(side="left", padx=5)
        
        ctk.CTkButton(button_frame,
                      text="✨ Log Study",
                      width=140,
                      height=40,
                      corner_radius=10,
                      fg_color="#9AE6B4",
                      hover_color="#7FD99D",
                      font=("Poppins", 12, "bold"),
                      command=self.quick_log_study).pack(side="left", padx=5)
    
    def load_data(self):
        """Load streak data from database"""
        try:
            self.streak_data = self.streak_manager.get_streak_data(self.user_id)
            
            if self.streak_data:
                self.update_display()
            else:
                # Initialize if no data
                self.streak_manager.initialize_streak(self.user_id)
                self.load_data()
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load streak data: {e}")
    
    def update_display(self):
        """Update all UI elements with current data"""
        if not self.streak_data:
            return
        
        streak_info = self.streak_data['streak']
        user_info = self.streak_data['user']
        badges = self.streak_data['badges']
        
        # Update streak
        current_streak = streak_info['current_streak'] or 0
        longest_streak = streak_info['longest_streak'] or 0
        total_days = streak_info['total_study_days'] or 0
        last_study = streak_info['last_study_date']
        
        self.streak_label.configure(text=str(current_streak))
        self.longest_label.configure(text=f"Longest: {longest_streak} days 🏆")
        self.total_days_label.configure(text=f"📚 Total Study Days: {total_days}")
        
        # Format last study date
        if last_study:
            from datetime import datetime
            last_date = last_study.strftime("%b %d, %Y") if isinstance(last_study, datetime) else str(last_study)
            self.last_study_label.configure(text=f"📅 Last Study: {last_date}")
        else:
            self.last_study_label.configure(text="📅 Last Study: Start today!")
        
        # Add flame animation if streak > 0
        if current_streak > 0:
            self.animate_streak()
        
        # Update XP and Level
        total_xp = user_info['total_xp'] or 0
        level = user_info['current_level'] or 1
        
        # Calculate XP for next level
        xp_for_next_level = (level * level) * 100
        xp_in_current_level = total_xp - ((level - 1) * (level - 1) * 100)
        xp_needed = xp_for_next_level - ((level - 1) * (level - 1) * 100)
        progress = xp_in_current_level / xp_needed if xp_needed > 0 else 0
        
        self.level_label.configure(text=f"⭐ Level {level}")
        self.xp_label.configure(text=f"{xp_in_current_level} / {xp_needed} XP")
        self.xp_progress.set(progress)
        
        # Update badges
        self.update_badges_display(badges)
    
    def update_badges_display(self, badges):
        """Display earned badges"""
        # Clear existing badges
        for widget in self.badges_container.winfo_children():
            widget.destroy()
        
        self.badge_count_label.configure(text=str(len(badges)))
        
        if not badges:
            ctk.CTkLabel(self.badges_container,
                         text="🎯 Complete study sessions to earn badges!",
                         font=("Poppins", 12),
                         text_color="#718096").pack(pady=20)
            return
        
        # Display badges
        for badge in badges:
            badge_frame = ctk.CTkFrame(self.badges_container,
                                       fg_color="white",
                                       corner_radius=10,
                                       border_width=2,
                                       border_color="#FFD93D")
            badge_frame.pack(fill="x", pady=5, padx=5)
            
            content = ctk.CTkFrame(badge_frame, fg_color="transparent")
            content.pack(fill="x", padx=15, pady=10)
            
            # Badge icon and name
            icon_label = ctk.CTkLabel(content,
                                      text=badge['badge_icon'],
                                      font=("Poppins", 24))
            icon_label.pack(side="left", padx=(0, 10))
            
            text_frame = ctk.CTkFrame(content, fg_color="transparent")
            text_frame.pack(side="left", fill="x", expand=True)
            
            ctk.CTkLabel(text_frame,
                         text=badge['badge_name'],
                         font=("Poppins", 13, "bold"),
                         text_color="#2D3748",
                         anchor="w").pack(anchor="w")
            
            ctk.CTkLabel(text_frame,
                         text=badge['description'] or "Achievement unlocked!",
                         font=("Poppins", 10),
                         text_color="#718096",
                         anchor="w",
                         wraplength=250).pack(anchor="w")
            
            # Earned date
            from datetime import datetime
            date_str = badge['earned_date'].strftime("%b %d") if isinstance(badge['earned_date'], datetime) else str(badge['earned_date'])
            ctk.CTkLabel(content,
                         text=date_str,
                         font=("Poppins", 10),
                         text_color="#A0AEC0").pack(side="right")
    
    def animate_streak(self):
        """Simple pulse animation for streak number"""
        original_size = 48
        
        def pulse(size=original_size, direction=1):
            if direction == 1 and size < original_size + 8:
                self.streak_label.configure(font=("Poppins", size, "bold"))
                self.after(30, lambda: pulse(size + 1, 1))
            elif direction == -1 and size > original_size:
                self.streak_label.configure(font=("Poppins", size, "bold"))
                self.after(30, lambda: pulse(size - 1, -1))
            elif direction == 1:
                pulse(size, -1)
        
        pulse()
    
    def refresh_data(self):
        """Refresh streak data"""
        self.load_data()
        
        # Show brief success message
        self.refresh_btn.configure(text="✓", fg_color="#9AE6B4")
        self.after(1000, lambda: self.refresh_btn.configure(text="🔄", fg_color="#EDF2F7"))
    
    def quick_log_study(self):
        """Quick log study session dialog"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Log Study Session")
        dialog.geometry("400x350")
        dialog.resizable(False, False)
        dialog.grab_set()
        
        ctk.CT





        



