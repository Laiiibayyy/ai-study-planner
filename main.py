from splash import SplashScreen
from login import AuthApp
from dashboard import DashboardApp
import tkinter as tk

# Start the app
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # hide the root until splash ends

    # Show splash screen first
    splash = Splash_screen(root)
    splash.after(3000, lambda: open_login(root, splash))
    root.mainloop()


def open_login(root, splash):
    splash.destroy()  # close splash
    root.deiconify()
    app = AuthApp(root)  # open login/signup screen
    root.mainloop()
