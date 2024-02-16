import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import time

class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")
        self.form = tk.Tk()
        self.form.title('Library')
        self.form.geometry("1200x700")
        self.form.config(bg="#03A89E")    
        self.time()
        self.buttons = [
            ("1)List", self.list_books),
            ("2)Add", self.add_book_entry),
            ("3)Remove", self.remove_book_entry),
            ("Q)EXIT", self.quit)
        ]
        self.display_buttons()
        self.image()
        self.button_number()
        
        
        

    def button_number(self):
        text = tk.Label(text="You can Click the Button ",font='Times 20')
        text.pack()
        text.place(x=100,y=80)
        text1 = tk.Label(text="Or Choose Number(1/2/3/Q)",font='Times 20')
        text1.pack()
        text1.place(x=100,y=120)
        num = tk.Entry(font=('Times 17'))
        num.pack()
        num.place(x=150,y=160,width=40)
        num_button = tk.Button(text="Submit",command= lambda: self.number_choice(num.get()))
        num_button.pack()
        num_button.place(x=150,y=200)

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.destroy_widgets()
        self.file.seek(0)  
        lines = self.file.read().splitlines()
        if not lines:
            text1 = tk.Label(text="No books available.",font='Times 20')
            text1.pack()
            text1.place(x=100,y=80)
        else:
            text2 = tk.Label(text="List of Books:",font='Times 25 bold underline italic')
            text2.pack()
            text2.place(x=100,y=80)
            x = 100
            y = 140
            for line in lines:
                book_info = line.strip().split(',')  
                book_name = book_info[0]
                author = book_info[1]
                page = book_info[2]
                date = book_info[3]
                time = book_info[4]
                text3 = tk.Label(text=f"Book: {book_name},   Author: {author},   Pages:{page},   Date:{date},   Time:{time}",font='Times 17',relief="groove")
                text3.pack()
                text3.place(x=x,y=y)
                y += 40
        self.back()

    def add_book_entry(self):
        self.destroy_widgets()
        book_name_txt = tk.Label(text="Book Name:",font=('Times 17'),)
        book_name_txt.pack()
        book_name_txt.place(x=100,y=80)
        book_name = tk.Entry(font=('Times 17'))
        book_name.pack()
        book_name.place(x=250,y=80)
        author_txt = tk.Label(text="Author Name:",font=('Times 17'))
        author_txt.pack()
        author_txt.place(x=100,y=120)
        author = tk.Entry(font=('Times 17'))
        author.pack()
        author.place(x=250,y=120)
        page_txt = tk.Label(text="Pages:",font=('Times 17'))
        page_txt.pack()
        page_txt.place(x=100,y=160)
        page = tk.Entry(font=('Times 17'))
        page.pack()
        page.place(x=250,y=160)
        date_txt = tk.Label(text="Release year:",font=('Times 17'))
        date_txt.pack()
        date_txt.place(x=100,y=200)
        date = tk.Entry(font=('Times 17'))
        date.pack()
        date.place(x=250,y=200)
        time_txt = tk.Label(text="Time",font=('Times 17'))
        time_txt.pack()
        time_txt.place(x=100,y=240)
        time = self.time()
        time_label = tk.Label(text=time,state='normal',font=('Times 17'))
        time_label.pack()
        time_label.place(x=250,y=240)
        add = tk.Button(text="Add", command=lambda: self.add_book(book_name.get(), author.get(),page.get(),date.get()),font=('Times 17'))
        add.pack()
        add.place(x=180,y=290)
        self.back()
        
    def add_book(self,book_name,author,page,date):
        if book_name == "" or author == "":
            add_error_text = tk.Label(text="Book and author names cannot be left blank.",font='Times 14')
            add_error_text.pack()
            add_error_text.place(x=110,y=340)
        else:
            time = self.time()
            self.file.write(f"{book_name},{author},{page},{date},{time},\n")
            text4 = tk.Label(text=f"Book '{book_name}' by {author} added successfully.",font='Times 14')
            text4.pack()
            text4.place(x=110,y=340)


    def remove_book_entry(self):
        self.destroy_widgets()
        self.file.seek(0) 
        lines = self.file.read().splitlines()
        if not lines:
            text1 = tk.Label(text="No books available.",font='Times 20')
            text1.pack()
            text1.place(x=100,y=250)
        else:
            text2 = tk.Label(text="List of Books:",font='Times 25 bold underline italic',bd=3)
            text2.pack()
            text2.place(x=100,y=250)
            x = 100
            y = 310
            for line in lines:
                book_info = line.strip().split(',')  
                book_name = book_info[0]
                text3 = tk.Label(text=f"Book: {book_name}",font='Times 17',relief="groove")
                text3.pack()
                text3.place(x=x,y=y)
                y += 40
        book_name_txt = tk.Label(text="Book Name: ",font=('Times 17'))
        book_name_txt.pack()
        book_name_txt.place(x=100,y=80)
        book_name = tk.Entry(font=('Times 17'))
        book_name.pack()
        book_name.place(x=250,y=80)
        Remove = tk.Button(text="Remove", command=lambda: self.remove_book(book_name.get()),font=('Times 17'))
        Remove.pack()
        Remove.place(x=160,y=150)
        
        self.back()
        

    def remove_book(self, book_name):
        self.file.seek(0)
        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()
        removed = False
        for line in lines:
            book_info = line.strip().split(',')
            current_book_name = book_info[0]
            if book_name != current_book_name:
                self.file.write(line)
            else:
                removed = True
        if removed:
            text5 = tk.Label(text=f"Book '{book_name}' removed successfully.")
            text5.pack()
            text5.place(x=110,y=200)
        else:
            text6 = tk.Label(text=f"Book '{book_name}' not found in the library.")
            text6.pack()
            text6.place(x=110,y=200)


    def destroy_widgets(self):
        for widget in self.form.winfo_children():
            widget.destroy()

    def quit(self):
        self.form.quit()
        
    def display_buttons(self):
        self.destroy_widgets()
        self.image()
        self.button_number()
        x=10
        y=10
        for text, command in self.buttons:
          button =  tk.Button(self.form, text=text, command=command, width=10, height=5)
          button.pack()
          button.place(x=x,y=y)
          y+=80
        

    def number_choice(self,number):
        if(number == "1"):
            self.list_books()
        elif(number == "2"):
            self.add_book_entry()
        elif(number == "3"):
            self.remove_book_entry()
        elif(number == "q" or number == "Q"):
            self.quit()
        else:
            error = tk.Label(text="enter valid value")
            error.pack()
            error.place(x=110,y=230)
    
    def back(self):
        back =tk.Button(text="Back", command=self.display_buttons,font=('Times 17'),bd=5,activeforeground="Orange")
        back.pack()
        back.place(x=10,y=10)
    
    def time(self): 
        self.time_label=tk.Label(bg='white',font='Times 35 bold')
        self.time_label.pack()
        self.time_label.place(x=500,y=10)
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text= current_time)
        self.form.after(1000,self.time)
        return current_time
    
    def image(self):
        self.original_image = Image.open("book1.png")
        self.new_width = 200
        self.new_height = 200
        self.resized_image = ImageOps.fit(self.original_image, (self.new_width, self.new_height))
        self.my_image = ImageTk.PhotoImage(self.resized_image)
        lbl = tk.Label(image=self.my_image, bd=1)
        lbl.pack()
        lbl.place(x=500, y=100)

    def run(self):
        self.form.mainloop()
        
    

if __name__ == "__main__":
    library = Library()
    library.run()
            
        