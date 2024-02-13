class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  # Move the file pointer to the beginning
        lines = self.file.read().splitline1s()
        if not lines:
            print("No books available.")
        else:
            print("List of Books:")
            for line in lines:
                book_info = line.strip().split(',')  # Assuming the format is 'book_name,author'
                book_name = book_info[0]
                author = book_info[1]
                print(f"Book: {book_name}, Author: {author}")

    def add_book(self, book_name, author):
        self.file.write(f"{book_name},{author}\n")
        print(f"Book '{book_name}' by {author} added successfully.")

    def remove_book(self, book_name):
        self.file.seek(0)
        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()
        removed = False
        for line in lines:
            if book_name not in line:
                self.file.write(line)
            else:
                removed = True
        if removed:
            print(f"Book '{book_name}' removed successfully.")
        else:
            print(f"Book '{book_name}' not found in the library.")

lib = Library()

menu = "\n***MENU***\n1-List\n2-Add\n3-Remove\n4-Exit\n***********"



while True:
    library = Library()
    print(menu)
    
    num = input("Choose Number= ")
    if(num == "1"):
        library.list_books()
    elif(num == "2"):
        book_name= input("Book Name:")
        author_name = input("Author Name:")
        library.add_book(book_name,author_name)
    elif(num == "3"):
        library.list_books()
        book_name= input("Book Name:")
        library.remove_book(book_name)
    elif(num == "4"):
            print("the program is closed")
            quit()
        
            
        
