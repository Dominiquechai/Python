import sys
from tkinter import *
from tkinter import filedialog

def mailSender(messageOfHTML=None, attachFile=None):
    root = Tk()
    #root.withdraw()
    #root.filename = filedialog.askopenfilename(initialdir="./", title="Open Data files", filetypes=(("data files", "*.csv;*.xls;*.xlsx"), ("all files", "*.*")))
    #root.filename = filedialog.askopenfilename()

    entry2 = Entry(root)
    entry2.pack()
    entry2.insert(0, "제목을 입력해주세요")
    
    entry3 = Entry(root)
    entry3.pack()
    entry3.insert(0, "제목을 입력해주세요")    
    
    def btn_Close(event):
        fileName = entry2.get()
        entry2.quit()

    def btn_Selection(event):
        #root.withdraw()
        #root.filename = filedialog.askopenfilename(initialdir="./", title="Open Data files", filetypes=(("data files", "*.csv;*.xls;*.xlsx"), ("all files", "*.*")))
        root.filename = filedialog.askopenfilename()
        entry2.insert(0, root.filename)
        
    b1 = Button(root, text='적용')
    b1.pack()

    b2 = Button(root, text='선택')
    b2.pack()

    b1.bind('<Button-1>', btn_Close)  

    b2.bind('<Button-1>', btn_Selection)  
    
    root.mainloop()

    print('HTML FILE is ' + messageOfHTML + ' and Attach FILE is ' +  root.filename)

if __name__ == "__main__":
    mailSender("1","2")
