"""

from structure import *
from seznam import *
import customtkinter as tk
import random
from structure import get_selected_categories
import pyperclip


# Warning sing
def check_warning(*args):
    if not (upper_var.get() and special_var.get() and numbers_var.get()):
        warning_label.configure(state="normal")
    else:
        warning_label.configure(state="disabled")


upper_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)

upper_var.trace_add("write", lambda *args: check_warning())
special_var.trace_add("write", lambda *args: check_warning())
numbers_var.trace_add("write", lambda *args: check_warning())

upper_checkbox.configure(variable=upper_var)
special_checkbox.configure(variable=special_var)
numbers_checkbox.configure(variable=numbers_var)


# Password generate
def generate_password():
    selected_categories = get_selected_categories(upper_var, special_var, numbers_var)

    # 'sign1' (lowercase letters) should always be included
    selected_categories.append("sign1")

    random_characters = []
    range1 = random.randint(20, 25)

    for _ in range(range1):
        category = random.choice(selected_categories)
        characters = character_dict[category]
        random_character = random.choice(characters)
        random_characters.append(random_character)

    password = ''.join(random_characters)

    password_box.configure(state="normal")
    password_box.delete("1.0", tk.END)
    password_box.insert("1.0", password)
    password_box.configure(state="disabled")


gen_button.configure(command=generate_password)

# Copy password


window.mainloop()



"""