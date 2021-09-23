from tkinter import *
import os


def main():
    i = 1
    file_number = int(filenumberentry.get())
    folder_number = str(foldernameentry.get())
    file_type = str(filetypeentry.get())
    os.mkdir("./" + folder_number)

    while i <= file_number:
        textvar = "./" + folder_number + "/" + str(i) + "." + file_type
        f = open(textvar, "w")
        i = i + 1


window = Tk()

window.title("Gerador de arquivos")
window.geometry("300x300")

filetypelabel = Label(window, text="Escolha o tipo de arquivo que você quer:")
filetypeentry = Entry(window)

filenumberlabel = Label(window, text="Escolha o número de arquivos:")
filenumberentry = Entry(window)

foldernamelabel = Label(window, text="Escolha o nome da pasta")
foldernameentry = Entry(window)

startbutton = Button(window, text="Start", command=main)

filetypelabel.pack()
filetypeentry.pack()

filenumberlabel.pack()
filenumberentry.pack()

foldernamelabel.pack()
foldernameentry.pack()

startbutton.pack()

window.mainloop()
