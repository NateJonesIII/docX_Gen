# DocX User Credentials Generator

## Description

Welcome to the **DocX User Credentials Generator**! This Python script is designed to quickly generate a "Welcome" word document in docX format for [Company Name] employee user accounts. With its intuitive interface and robust functionality, this tool simplifies the process of generating user credentials, ensuring efficiency and accuracy in document creation.

## Table of Contents:

- [Preview](#preview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [How_to_Contribute](#how-to-contribute)
- [Testing](#testing)
- [Technologies](#technologies)
- [Methodologies](#methodologies)
- [Code Snippets](#code-snippets)
- [Ouput](#ouput)
- [Creator](#creator)

## Preview

<img width="500" height="400" alt="GUI" src="https://github.com/NateJonesIII/docX_Gen/blob/main/assets/img/GUI.PNG">

<img width="500" alt="Success Message" src="https://github.com/NateJonesIII/docX_Gen/blob/main/assets/img/GUI_Success.PNG">

<img width="500" alt="WordDoc" src="https://github.com/NateJonesIII/docX_Gen/blob/main/assets/img/Word_Doc.PNG">

## Installation:

To install and run the **DocX User Credentials Generator**, follow these steps:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the Python script `docX_Gen.py`.

## Usage:

To generate user credentials using the **DocX User Credentials Generator**:

1. Enter the user's first name, last name, and password in the corresponding fields.
2. Click the "Generate DocX" button to create a Word document with the user's credentials.

## Features:

**Libraries Used:**

- `tkinter`: Provides the graphical user interface (GUI) for the application, including text entry fields and buttons.
- `docx`: Facilitates the creation and manipulation of Word documents, allowing for the generation of user credentials.

## How to Contribute:

- If you'd like to contribute to the **DocX User Credentials Generator**, feel free to submit a pull request or open an issue on GitHub.

## Testing:

To ensure the reliability and accuracy of the **DocX User Credentials Generator**, the following testing approach was employed:

1. **Unit Testing:** Individual components of the script were tested in isolation to verify their functionality.
2. **Integration Testing:** The script was tested as a whole to ensure seamless interaction between its various components.
3. **User Acceptance Testing (UAT):** End-to-end testing was performed to validate the user interface and overall user experience.

## Technologies:

- **Python:** The primary programming language used for developing the script, leveraging its versatility and extensive library support.
- **tkinter:** Provides the graphical user interface (GUI) for the application, facilitating user interaction and input.
- **docx:** Enables the creation and manipulation of Word documents, allowing for the generation of user credentials.

## Methodologies:

- **Agile Development:** The project was developed using agile methodologies, with iterative refinement and continuous feedback driving its evolution.
- **Test-Driven Development (TDD):** Testing was integrated into the development process from the outset, ensuring that each feature was thoroughly tested before implementation.
- **Code Reviews:** Regular code reviews were conducted to maintain code quality and identify potential areas for improvement.

## Code Snippets:

### Setup.py

```
from cx_Freeze import setup, Executable

# Define the list of executable scripts
executables = [Executable("docX_Gen.py")]

# Setup configuration
setup(
    name="docX_Gen",
    version="1.0",
    description="Created to quickly generate Wecome to [Compnay Name] docX for [Compnay Name] employee user accounts.",
    options={'build_exe': {'packages': ['tkinter']}},
    executables=executables
)
```

### docX_Gen.py(main.py)

```
# Python Imports
import tkinter as tk
from tkinter import messagebox
from docx import Document
from tkinter import PhotoImage

# Define word document generation function
def generate_document():
    # Get user inputs
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    password = password_entry.get()

    # Check if all fields are filled
    if not first_name or not last_name or not password:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Extract first initial from first_name
    first_initial = first_name[0]

    # Create a new Word document
    doc = Document()
    # Add document content
    doc.add_heading(f'Welcome to [Company Name Here] {first_name} {last_name}', level=1)
    doc.add_paragraph("")  # Empty line
    doc.add_paragraph("")  # Empty line
    doc.add_paragraph(f"[Company Name Here]Email: {first_initial}.{last_name}@[Company Domain]")
    doc.add_paragraph(f"Desktop Username/Login: {first_initial}.{last_name}")
    doc.add_paragraph(f"[Company Name Here] Password: {password}")
    # More content...

    # Save the document with user's name
    doc.save(f"Welcome_{first_name}.docx")

    # Show success message
    messagebox.showinfo("Success", "Document created successfully. **Double Check username available in AD!**")

# Define window centering function
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    return f"{width}x{height}+{x}+{y}"

# Create the main GUI window
root = tk.Tk()
root.title("DocX User Credentials Generator")

# Set window dimensions and position
window_geometry = center_window(root, 400, 600)
root.geometry(window_geometry)

# Load and display the company logo image
image = PhotoImage(file="assets/img/ccLogoS.png")
image = image.subsample(9)
image_label = tk.Label(root, image=image)
image_label.pack()

# Create labels and entry fields for user input
first_name_label = tk.Label(root, text="First Name:")
first_name_label.pack()
first_name_entry = tk.Entry(root)
first_name_entry.pack()

last_name_label = tk.Label(root, text="Last Name:")
last_name_label.pack()
last_name_entry = tk.Entry(root)
last_name_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*") # hides password
password_entry.pack()

# Create the "Generate DocX" button
generate_button = tk.Button(root, text="Generate DocX", command=generate_document)
generate_button.pack()

# Start the GUI event loop
root.mainloop()
```

## Ouput:

### Word Doc

```
Welcome to [Company Name Here] Test Test 1


[Company Name Here]Email: T.Test 1@[compay domain].com
Desktop Username/Login: T.Test 1
[Company Name Here] Password: Test2
[Company Name Here] Username: T.Test 1@[compay domain]
[Company Name Here] Password: Test2

Voicemail Password is your phone extension followed by a 0

A Technician as completed the following to your workstation:

⚬    Logged in and configured Outlook/Email
⚬    Logged in and configured MS Teams
⚬    Logged in and Launched [Application]
⚬    Configured [software], [software], and [software]
⚬    Installed Default Printers
⚬    Tested Scanner(If Applicable)
⚬    Created a desktop icon for email access

Wifi: [SSID]: [Employee password]

```

## Creator:

- [Profile](https://github.com/NateJonesIII/ "Nathaniel Jones") - [LinkedIn](https://www.linkedin.com/in/nathaniel-jones/) - [Email](mailto:15nate.jones@gmail.com?subject=Hello "Hello Nate!")
