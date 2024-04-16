# setup.py
from cx_Freeze import setup, Executable


executables = [Executable("docX_Gen.py")]

setup(
    name="docX_Gen",
    version="1.0",
    description="Created to quickly generate Wecome to Classic Collision docX for Classic employee user accounts.",
    options={'build_exe': 
        {'packages': ['tkinter']}},
    executables=executables
)
