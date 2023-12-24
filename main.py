import customtkinter as tk
import os

file_name = []
files = []
win=tk.CTk()
file_path = []

class File:
    def __init__(self, name, path):
        self.filename=name
        self.filepath=path

class Sector:
    def __init__(self, label, path, open_Button, delete_Button):
        self.Label=label
        self.Path=path
        self.openButton=open_Button
        self.deleteButton=delete_Button
def find_files(path):
    files=os.listdir(path)
    for item in files:
        if os.path.isdir(os.path.join(path,item)):
            find_files(os.path.join(path,item))
        else:
            file_name.append(os.path.basename(item))
            file_path.append(os.path.join(path,item))

def openFile(filePath):
    os.startfile(filePath)

def deleteFile(filePath, button, index):
    os.remove(filePath)
    button.destroy()

def reset(resetButton, frame,confirmButton, listFiles):
    #print(reset)
    resetButton.destroy()
    frame._scrollbar.destroy()
    frame._parent_frame.destroy()
    frame.destroy()
    confirmButton.configure(state="normal")
    listFiles.clear()

def delete_files(listFiles):
    print("misto")


def function(label,confirmButton):

    frame = tk.CTkScrollableFrame(win, width=550, height=300, fg_color="white")
    frame._parent_frame.configure(frame, width=500, height=300)
    #momentan singura metoda care functioneaza e cu scrollableframe si sa pui pack la labels si buttons
    #frame = tk.CTkCanvas(win, width=580, height=400, bg="white", scrollregion=(0,0,1000,3800))
    frame.place(x=15, y=95)

    folderInput = label.get("0.0", "end")
    folderInput = folderInput[:len(folderInput)-1]##without endline character
    #print(folderInput)
    label.delete("0.0", "end")
    find_files(folderInput)

    #print(file_name)
    #print(sorted(list([x for i, x in enumerate(file_name) if file_name.count(x) > 1])))
    # daca ai nevoie doar prima aparitie folosesti list(set())
    #files_listName = sorted(list([x for i, x in enumerate(file_name) if file_name.count(x) > 1]))

    files_listName = [x for i, x in enumerate(file_name) if file_name.count(x) > 1]

    files_listPath = [x for i, x in enumerate(file_path) if file_name.count(os.path.basename(x)) > 1]

    # print(files_listPath)
    # print(files_listName)
    STANDARD_X=20
    STANDARD_Y=0

    listFiles=[]
    buttonList=[]

    for i in range(len(files_listPath)):
        listFiles.append(File(files_listName[i], files_listPath[i]))

    listFiles = sorted(listFiles, key=lambda x:x.filename)

    label1=tk.CTkLabel(frame, text="Name", width=200, height=20)
    label2=tk.CTkLabel(frame, text="Path", width=200, height=20)
    label3=tk.CTkLabel(frame, text="Remove CheckBox")
    label1.grid(row=1, column=0)
    label2.grid(row=1, column=2)
    label3.grid(row=1, column=4)

    i=1
    for item in listFiles:
        resultName = tk.CTkTextbox(frame, width=200, height=20)
        resultName.insert("1.0", item.filename)

        resultName.configure(state="disabled")
        buttonOpen=tk.CTkButton(frame, text="Open", fg_color="lightgreen", text_color="black", width=50)
        buttonOpen.configure(command=lambda j=i: openFile(listFiles[j].filepath))
        buttonDelete=tk.CTkButton(frame, fg_color="lightgreen", text_color="black", width=50)
        buttonDelete.configure(command=lambda :delete_files(listFiles))
        i+=1
        #result.place(x=STANDARD_X, y=STANDARD_Y)
        #buttonOpen.place(x=300,y=STANDARD_Y)
        resultName.grid(row=i, column=0)
        resultPath=tk.CTkTextbox(frame, width=220, height=20)
        resultPath.insert("1.0", item.filepath)
        resultPath.configure(state="disabled")
        resultPath.grid(row=i, column=2)
        buttonOpen.grid(row=i, column=3)
        buttonDelete.grid(row=i, column=4)
        #STANDARD_Y+=30

    files_listName.clear()
    files_listPath.clear()
    file_path.clear()
    file_name.clear()

    confirmButton.configure(state="disabled")
    removeButton=tk.CTkButton(win, text="Reset", fg_color="lightgreen", text_color="black")
    removeButton.configure(command=lambda :reset(removeButton,frame,confirmButton, listFiles))
    removeButton.place(x=420, y=420)



def main():
    win.title("Duplicate finder")
    win.config(bg="white")
    win.geometry("600x500")
    win.resizable(width=False, height=False)


    tk.set_appearance_mode("light")

    text = """Duplicate finder
    Please insert your folder's path in order to find its duplicated files"""

    label = tk.CTkLabel(win , anchor="center", text=text, underline=15, fg_color="lightgreen",height = 5, width = 500, text_color="black",font=("Arial",18))
    textbox = tk.CTkTextbox(win, height = 5, width = 300, activate_scrollbars=False)


    confirmButton=tk.CTkButton(win, text="Confirm", fg_color="lightgreen", text_color="black")
    confirmButton.configure(command= lambda: function(textbox,confirmButton))


    label.pack()
    textbox.place(x = 0, y = 42)
    confirmButton.place(x = 320, y = 42)

    win.mainloop()

main()