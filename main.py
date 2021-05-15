from tkinter import *
from tkinter.filedialog import asksaveasfile,askopenfilename
import subprocess


compiler = Tk()
compiler.title('PyStudio')
File_path = ''

def set_file_path(path):
    global File_path()
    File_path = path

def run():
    if File_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()

    command = f'python{File_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True  )
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)
def Save_as():
    if File_path == '':
        path = asksaveasfile(filetypes=['Python Files','*.py'])
    else:
        path = File_path
    with open(path,'w') as file:
        code = editor.get('1.0',END)
        file.write(code)
        set_file_path(path)

def Open():
    path = askopenfilename(filetypes=['Python Files','*.py'])
    with open(path,'r') as file:
        code = editor.get('1.0',END)
        file.read()
        editor.delete('1.0',END)
        editor.insert('1.0', code)
        set_file_path(path)



menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=Open)
file_menu.add_command(label='Save', command=Save_as)
file_menu.add_command(label='Save As', command=Save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label = 'File', menu=file_menu)


run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)
compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=7)
code_output.pack
compiler.mainloop()
