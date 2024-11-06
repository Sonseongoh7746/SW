class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"[{self.book_id}] {self.title} - {self.author} ({self.year})"


class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, node):
        if node is not None:
            node.link = self.link
            self.link = node

    def popNext(self):
        next_node = self.link
        if next_node is not None:
            self.link = next_node.link
        return next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, pos, elem):
        node = Node(elem)
        before = self.getNode(pos - 1)
        if before is None:
            node.link = self.head
            self.head = node
        else:
            before.append(node)

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before is None:
            if self.head is not None:
                self.head = self.head.link
        else:
            before.popNext()

    def getNode(self, pos):
        if pos < 0:
            return None
        ptr = self.head
        for i in range(pos):
            if ptr is None:
                return None
            ptr = ptr.link
        return ptr

    def size(self):
        count = 0
        ptr = self.head
        while ptr is not None:
            count += 1
            ptr = ptr.link
        return count

    def display(self):
        print("현재 등록된 도서 목록:")
        ptr = self.head
        if ptr is None:
            print("현재 등록된 도서가 없습니다.")
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.link

    def find_by_title(self, title):
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return ptr.data
            ptr = ptr.link
        return None

    def find_pos_by_title(self, title):
        pos = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return pos
            ptr = ptr.link
            pos += 1
        return -1


class BookManager:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self, book_id, title, author, year):
        if self.books.find_pos_by_title(title) != -1:
            print("오류: 중복된 책 제목입니다.")
            return
        for i in range(self.books.size()):
            if self.books.getNode(i).data.book_id == book_id:
                print("오류: 중복된 책 번호입니다.")
                return
        self.books.insert(self.books.size(), Book(book_id, title, author, year))
        print(f"{title} 도서가 추가되었습니다.")

    def remove_book(self, title):
        pos = self.books.find_pos_by_title(title)
        if pos == -1:
            print("오류: 해당 도서가 존재하지 않습니다.")
        else:
            self.books.delete(pos)
            print(f"{title} 도서가 삭제되었습니다.")

    def view_book(self, title):
        book = self.books.find_by_title(title)
        if book is None:
            print("오류: 해당 도서가 존재하지 않습니다.")
        else:
            print(book)

    def display_books(self):
        self.books.display()

    def run(self):
        while True:
            print("\n===== 도서 관리 프로그램 =====")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")
            choice = input("선택: ")

            if choice == "1":
                book_id = int(input("책 번호: "))
                title = input("책 제목: ")
                author = input("저자: ")
                year = int(input("출판 연도: "))
                self.add_book(book_id, title, author, year)
            elif choice == "2":
                title = input("삭제할 책 제목: ")
                self.remove_book(title)
            elif choice == "3":
                title = input("조회할 책 제목: ")
                self.view_book(title)
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")

# 프로그램 실행
manager = BookManager()
manager.run()
