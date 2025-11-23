
class Library:
    def __init__(self):
        self.stock=[]
    def add (self,Title,Author,borrow_fee):
        self.stock.append({"Title":Title,
                           "Author":Author,
                           "borrow_fee":borrow_fee})
    def view(self):
         for books in self.stock:
          print(f"Title:{books['Title']},Author:{books['Author']},Borrow_fee:{books['borrow_fee']}")

    def search(self,find):
        find_book=[Title for Title in self.stock if find==library_1['Title']]
        if find_book:
            for book in find_book:
                print(f"Title:{library_1['Title']}\n{library_1['Author']}")

        else:
            print("Not Available")





library_1=Library()
library_1.add("Python","Unknown",50)

find=input("Enter book title to find")
library_1.search(find)

