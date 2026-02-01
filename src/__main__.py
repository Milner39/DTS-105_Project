import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
ctk.set_window_scaling(1.0)
ctk.set_widget_scaling(1.0)

app = ctk.CTk()  # create CTk window like you do with the Tk window

app.geometry("400x240")


def button_function():
  print("button pressed")


# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(
  master = app, text = "CTkButton", command = button_function
)
button.place(relx = 0.5, rely = 0.5, anchor = ctk.CENTER)

app.mainloop()
