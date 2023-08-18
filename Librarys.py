
class Books():
    data_tank_book = []
    data_ID_books = []
    safe_box = []

    def __init__(self, namebook, IDbook, row, floor):
        self.namebook = namebook
        self.IDbook = IDbook
        self.row = row
        self.floor = floor

        Books.data_ID_books.append(IDbook)
        Books.data_tank_book.append(namebook)

    def search(self, value):
        if value in Books.data_tank_book:
            print(self.row, self.floor, self.IDbook)

    def borrow(self, NB):
        if NB in Books.data_tank_book:
            Books.safe_box.append(Books.data_tank_book.remove(NB))

    def __repr__(self):
        return f'{Books.data_tank_book}{Books.safe_box}'


class Users():
    __data_name_users = []
    __data_ID_users = []

    def __init__(self, name_lname, ID, phone_number):
        self.name_lname = name_lname
        self.ID = ID
        self.phon_number = phone_number

        Users.__data_name_users.append(name_lname)
        Users.__data_ID_users.append(ID)

    def login(self, name, ID):
        for x in range(3):
            if name in Users.__data_name_users and ID in Users.__data_ID_users:
                print('welcome to Library')
                break
            else:
                print('Try again')

    @property
    def get(self):
        return Users.__data_name_users

    @get.delattr
    def get(self, value):
        if value in Users.__data_name_users:
            return Users.__data_name_users and Users.__data_ID_users.remove(value)


class Borrowing(Users, Books):

    Borrower_ID = []

    def start_BW(self, name, ID, bookname):
        if bookname in Books.data_tank_book:
            if name in Users.__data_name_users and ID in Users.__data_ID_users:
                return Books.borrow
            else:
                print('your name not in library')
        else:
            print('your book not fuond')

            Borrowing.Borrower_ID.append(Users.__data_ID_users)



