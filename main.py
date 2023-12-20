from tkinter import *
import customtkinter as tk
import random
tk.set_appearance_mode("dark")

# Window
window = tk.CTk()
window.title("Password Generator")
window.geometry("430x370")
window.resizable(False, False)
window.iconbitmap("logo.ico")
window.configure(fg_color="#038C7F")

# generate_button
gen_button = tk.CTkButton(window, text="Generate", width=160, height=40)
gen_button.place(x=50, y=290)
gen_button.configure(fg_color="#012626", text_color="#c9e7da", font=("Tahoma", 17))
# copy_button
copy_button = tk.CTkButton(window, text="Copy", width=140, height=40)
copy_button.place(x=230, y=290)
copy_button.configure(fg_color="#012626", text_color="#c9e7da", font=("Tahoma", 17))

# checkboxes
upper_checkbox = tk.CTkCheckBox(window, text="Uppercase letters")
upper_checkbox.place(x=55, y=85)
upper_checkbox.configure(fg_color="#01403A", border_color="#01403A", text_color="#c9e7da", font=("Tahoma", 14))
upper_checkbox.select(1)
special_checkbox = tk.CTkCheckBox(window, text="Special signs")
special_checkbox.place(x=55, y=115)
special_checkbox.configure(fg_color="#01403A", border_color="#01403A", text_color="#c9e7da", font=("Tahoma", 14))
special_checkbox.select(1)
numbers_checkbox = tk.CTkCheckBox(window, text="Numbers")
numbers_checkbox.place(x=55, y=145)
numbers_checkbox.configure(fg_color="#01403A", border_color="#01403A", text_color="#c9e7da", font=("Tahoma", 14))
numbers_checkbox.select(1)

# Label Password Generator
label = tk.CTkLabel(window, text="PASSWORD GENERATOR")
label.place(x=75, y=30)
label.configure(text_color="#c9e7da", font=("Tahoma", 25))

# Warning label
warning_label = tk.CTkLabel(window, text="Warning! Your password may not be strong enough.", wraplength=100)
warning_label.place(x=260, y=92)
warning_label.configure(text_color="#e10000", font=("Tahoma", 15))

# password text
password_box = tk.CTkTextbox(window, width=320, height=55)
password_box.configure(state="disabled", fg_color="#01403A")
password_box.place(x=50, y=210)
password_box.insert("0.0", "HESLO")


# Main loop
window.mainloop()

