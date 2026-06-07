from re import sub


class MyLibrary:
    books = ["Book1","Book2","Book3","Book4"]
    def __init__(self,books):
        if books is not None:
            self.books = books

    def getAvailableBooks(self):
        return self.books
    
    def subscribeBook(self,bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            return bookName
        else:
            print("bookName not found during subscribe:",bookName)
            return None
        
    def unsubscribeBook(self,bookName):
        if bookName in self.books:
            print("bookName not found during unsubscribe:",bookName)
            return False
        else:
            self.books.append(bookName)
            return True
            
mylib = MyLibrary(None)
print("Available books - {}".format(mylib.getAvailableBooks()))

for r in range(3):
    bookName = input("Enter Book to be subscribed ...")
    mybook = mylib.subscribeBook(bookName)
    if mybook is not None:
        print("Book subscribed:",mybook)
    else:
        print("Book not found in Library.")

print("Available books - {}".format(mylib.getAvailableBooks()))

bookNames = input("Enter Books to be un subscribed ...")
booklist = bookNames.split()
for bookName in booklist:
    if mylib.unsubscribeBook(bookName):
        print("Book unsubscribed:",bookName)
    else:
        print("Book not found in Library.")

print("Available books - {}".format(mylib.getAvailableBooks()))