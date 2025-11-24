class Book:
    def __init__(self, book_id: int, title: str, author: str, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None

    def __repr__(self):
        return f"BookID={self.book_id}, Title='{self.title}', Author='{self.author}', Status={self.status}"


class BookLinkedList:
    def __init__(self):
        self.head = None

    def insertBook(self, book: Book):
        if self.head is None:
            self.head = book
            return True
        if self.searchBook(book.book_id) is not None:
            print(f"Book ID {book.book_id} already exists!")
            return False
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = book
        return True

    def deleteBook(self, book_id: int):
        prev = None
        cur = self.head
        while cur:
            if cur.book_id == book_id:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def searchBook(self, book_id: int):
        cur = self.head
        while cur:
            if cur.book_id == book_id:
                return cur
            cur = cur.next
        return None

    def displayBooks(self):
        books = []
        cur = self.head
        while cur:
            books.append(repr(cur))
            cur = cur.next
        return books


class Transaction:
    def __init__(self, action: str, book_id: int, previous_status: str):
        self.action = action
        self.book_id = book_id
        self.previous_status = previous_status

    def __repr__(self):
        return f"{self.action} BookID={self.book_id} (was {self.previous_status})"


class TransactionStack:
    def __init__(self):
        self._stack = []

    def push(self, transaction: Transaction):
        self._stack.append(transaction)

    def pop(self):
        if not self._stack:
            return None
        return self._stack.pop()

    def is_empty(self):
        return len(self._stack) == 0

    def viewTransactions(self):
        return list(reversed(self._stack))


def demo():
    lib = BookLinkedList()
    tx = TransactionStack()

    lib.insertBook(Book(101, "Introduction to Algorithms", "Cormen"))
    lib.insertBook(Book(102, "Clean Code", "Robert C. Martin"))
    lib.insertBook(Book(103, "The Pragmatic Programmer", "Andrew Hunt"))

    print("Initial books:")
    for b in lib.displayBooks():
        print(" ", b)

    b = lib.searchBook(102)
    if b and b.status == "Available":
        prev = b.status
        b.status = "Issued"
        tx.push(Transaction("ISSUE", b.book_id, prev))
        print("\nIssued Book 102")

    b = lib.searchBook(102)
    if b and b.status == "Issued":
        prev = b.status
        b.status = "Available"
        tx.push(Transaction("RETURN", b.book_id, prev))
        print("Returned Book 102")

    t = tx.pop()
    if t:
        book = lib.searchBook(t.book_id)
        if book:
            book.status = t.previous_status
            print("\nUndo performed:", t)

    print("\nCurrent books after operations:")
    for b in lib.displayBooks():
        print(" ", b)


if __name__ == "__main__":
    demo()
