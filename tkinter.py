import sys
from tkinter import *
from tkinter import filedialog




def mailSender(messageOfHTML=None, attachFile=None):
    def btn_Close(event):
        fileName = titleInput.get()
        titleInput.quit()

    def btn_Selection(event):
        #root.withdraw()
        #root.filename = filedialog.askopenfilename(initialdir="./", title="Open Data files", filetypes=(("data files", "*.csv;*.xls;*.xlsx"), ("all files", "*.*")))
        root.filename = filedialog.askopenfilename()
        titleInput.insert(0, root.filename)    

    root = Tk()
    #root.withdraw()
    #root.filename = filedialog.askopenfilename(initialdir="./", title="Open Data files", filetypes=(("data files", "*.csv;*.xls;*.xlsx"), ("all files", "*.*")))
    #root.filename = filedialog.askopenfilename()

    root.geometry("600x600")

    titleLabel = Label(root, text="이메일 제목")
    titleLabel.pack()
    titleLabel.place(x=0, y=0)

    titleInput = Entry(root, width=30)
    titleInput.pack(ipady=14)
    titleInput.place(x=140, y=0)

    HTMLLabel = Label(root, text="메일본문 HTML 파일명")
    HTMLLabel.pack(ipady=14)
    HTMLLabel.place(x=0, y=20)

    HTMLInput = Entry(root, width=30)
    HTMLInput.pack(ipady=25)
    HTMLInput.place(x=140, y =20)

    selectHTML = Button(root, text='선택')
    selectHTML.pack()    
    selectHTML.place(x=355, y=16)

    b1 = Button(root, text='적용')
    b1.pack(side=BOTTOM)


    b1.bind('<Button-1>', btn_Close)  

    selectHTML.bind('<Button-1>', btn_Selection)  
    
    root.mainloop()

    print('HTML FILE is ' + messageOfHTML + ' and Attach FILE is ' +  root.filename)



if __name__ == "__main__":
    mailSender("1","2")
