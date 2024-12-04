import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class Register(tk.Tk):
    def __init__(self):
        super().__init__()
        image = Image.open('IMG/lll.png').resize((200,200))
        self.tk_image = ImageTk.PhotoImage(image)
        self.title('Form Đăng Kí')
        self.geometry('700x700+100+100')
        self.nation=['Việt Nam','Hàn Quốc','Nhật Bản','Mỹ',"Trung Quốc","Lào","Nga"]
        self.Creat_widget()

    def quit(self):
        self.destroy()

    def login(self):
        messagebox.showinfo('Thông Báo','Đã đăng nhập')

    def theme_white(self):
        self.config(bg='white')

    def theme_dark(self):
        self.config(bg='black')

    def set_font_size_15(self):
        self.current_size = 15

    def set_font_size_20(self):
        self.current_size = 20

    def set_font_size_30(self):
        self.current_size = 30
    
    
    def set_font_size(self, font_size):
        self.current_size = font_size
        self.lb1.config(font=(self.current_style,self.current_size))

    def set_font_arial(self):
        self.current_style = 'Arial'

    def set_font_times(self):
        self.current_style = 'Times'

    def set_font_crourier(self):
        self.current_style = 'Courier'

    def set_font_style(self, font_style):
        self.current_style = font_style
        self.lb1.config(font=(self.current_style,self.current_size))

    def Creat_widget(self):
        frame1=tk.Frame(self)
        frame1.pack()

        lb1=tk.Label(frame1, image=self.tk_image)
        lb1.grid(row=0,column=1,columnspan=3,padx=80)
        lb2=tk.Label(frame1,text='Form Đăng Kí')
        lb2.grid(row=1,column=1,columnspan=3,pady=25)

        lb3=tk.Label(frame1,text="Họ và tên")
        lb3.grid(row=2,column=0)

        en1=tk.Entry(frame1)
        en1.grid(row=2,column=1,padx=30,pady=20)

        lb4=tk.Label(frame1,text='Địa chỉ')
        lb4.grid(row=2,column=2)

        en2=tk.Entry(frame1)
        en2.grid(row=2,column=3,padx=30,pady=20)

        lb5=tk.Label(frame1,text="Ngày sinh")
        lb5.grid(row=3,column=0)
        
        en3=tk.Entry(frame1)
        en3.grid(row=3,column=1,padx=30,pady=20)

        lb6=tk.Label(frame1,text="Email")
        lb6.grid(row=3,column=2)

        en4=tk.Entry(frame1)
        en4.grid(row=3,column=3,padx=30,pady=20) 

        lb7=tk.Label(frame1,text="Quốc tịch")
        lb7.grid(row=4,column=0)
        
        combobox=ttk.Combobox(frame1,values=self.nation, state='readonly')
        combobox.grid(row=4,column=1,padx=30,pady=20)

        lb8=tk.Label(frame1,text="Số Điện thoại")
        lb8.grid(row=4,column=2)

        en5=tk.Entry(frame1)
        en5.grid(row=4,column=3,padx=30,pady=20)

        but1=tk.Button(frame1,text='Register',command=self.login)
        but1.grid(row=5,column=1,columnspan=1)

        but2=tk.Button(frame1,text='Quit',command=quit)
        but2.grid(row=5,column=2,columnspan=1)

        mainbar=tk.Menu(self)
        theme=tk.Menu(mainbar,tearoff=0)
        mainbar.add_cascade(label='theme',menu=theme)
        theme.add_command(label='Light',command=self.theme_white)
        theme.add_command(label='Dark',command=self.theme_dark)

        sizesetting=tk.Menu(mainbar,tearoff=0)
        mainbar.add_cascade(label='Size Setting',menu=sizesetting)
        sizesetting.add_command(label='size to 15',command=self.set_font_size_15)
        sizesetting.add_command(label='size to 20',command=self.set_font_size_20)
        sizesetting.add_command(label='size to 30',command=self.set_font_size_30)

        stylesetting=tk.Menu(mainbar,tearoff=0)
        mainbar.add_cascade(label='Style Setting',menu=stylesetting)
        stylesetting.add_command(label='Arial',command=self.set_font_arial)
        stylesetting.add_command(label='Times',command=self.set_font_times)
        stylesetting.add_command(label='Courier',command=self.set_font_crourier)

        self.config(menu=mainbar)


Form1=Register()
Form1.mainloop()