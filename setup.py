import sys
from cx_Freeze import setup, Executable
from tkinter import *
from tkinter.messagebox import showinfo
from config.get_start import NavegarColaborar

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable('app.py', base=base)]

buildOptions = dict(
    packages = ['tkinter', 'tkinter.messagebox', 'bs4', 'playwright', 'playwright.sync_api'],
    includes = ['config.get_start'],
    include_files = ['config/'],
    excludes = []
)

setup(
    name = 'ColaborarEAD',
    version = '1.0.0',
    author = 'Gustavo de Oliveira',
    description = "Gerador PDF atividades colaborar",
    options = dict(build_exe = buildOptions),
    executables = executables
)