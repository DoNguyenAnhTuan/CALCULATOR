from tkinter import *

class Game():
    def __init__(self):
        # Khởi tạo màn hình tkinter, kích thước, tiêu đề
        self.root = Tk()
        self.root.geometry("300x400")
        self.root.title("CALCULATOR")

        # Tạo khung hiển thị nội dung máy tính
        self.bar = Entry(self.root, width=22,
                         font=("Ubuntu", 18, "normal"),
                         fg="#ad3e02",
                         bg="#FFFFF0")
        self.bar.place(x=5, y=3)

        # X và Y là chiều dài và chiều rộng của các nút
        X = 75
        Y = 75

        ###################################################################################################

        # Nhập dấu
        def insert(num):
            # Khi có nội dung nhập vào thì background của khung sẽ thay đổi
            self.bar['fg'] = "#ad3e02"
            # Đọc dữ liệu mà bar đang có
            self.text = self.bar.get()
            # Nếu nội dung đang rỗng hoặc là các giá trị "/", "*", ")" thì chúng ta gán nó thành rỗng
            if (self.text.split() == []) and (num == "/" or num == "*" or num == ")"):
                num = ''
            # Nếu người dùng nhập vào 2 dấu phép toán liên tiếp thì chúng ta sẽ xóa dấu vừa nhập
            elif (self.text.endswith('*')) and (num in ["+", "-", "/", "*"]):
                self.BackSpace()
            elif (self.text.endswith('/')) and (num in ["+", "-", "/", "*"]):
                self.BackSpace()
            elif (self.text.endswith('+')) and (num in ["+", "-", "/", "*"]):
                self.BackSpace()
            elif (self.text.endswith('-')) and (num in ["+", "-", "/", "*"]):
                self.BackSpace()
            # Nếu là đấu chấm thì chúng ta gán nó thành giá trị rỗng
            elif (self.text.endswith('.')) and (num in [".", "+", "-", "/", "*"]):
                num = ''
            # Chèn số vào vị trí sau cùng
            self.bar.insert(END, num)

        def BackSpace():
            # Khi người dùng nhấn nút xóa, chúng ta sẽ đổi màu khung
            self.bar["fg"] = "#121111"
            # Dùng try except để bỏ qua những phát sinh lỗi và tiếp tục chương trình
            try:
                # Lấy nd trong khung bar đang chứa và chuyển thành list
                self.text = self.bar.get()
                self.l = list(self.text)
                # Lấy phần tử ở phía cuối và xóa nó đi
                self.l.pop()
                self.Text = ""
                for i in range(len(self.l)):
                    self.Text += self.l[i]
                # Mỗi lần nhấn phím backspace sẽ xóa 1 ký tự và thay thế bằng ký tự rỗng
                self.bar.delete(0, END)
                self.bar.insert(0, self.Text)
            except:
                pass

        # Hàm xóa toàn bộ
        def Delete():
            # Xóa toàn bộ công thức nhập trên bar
            self.bar["fg"] = "#121111"
            self.bar.delete(0, END)

        # Hàm kiểm tra dấu ngoặc
        def BracketCheck():
            # Để kiểm tra, cần lấy giá trị đg hiển thị trên bar
            self.text = str(self.bar.get())
            self.Text = list(self.text)
            # Chúng ta tạo ra hai biến a và b
            # a dùng để đếm số ngoặc mở
            self.a = 0
            for i in range(len(self.Text)):
                if self.Text[i] == "(":
                    self.a += 1
            self.b = 0
            for i in range(len(self.Text)):
                if self.Text[i] == ")":
                    self.b += 1
            self.Add = self.a - self.b
            return self.Add

        # Hàm tính toán và hiển thị kq
        def Answer():
            self.text = str(self.bar.get())
            # Lấy sl chênh lệch ngoặc
            self.Add = BracketCheck()
            if self.Add > 0:
                self.bar.insert(END, self.Add * ")")
            else:
                try:
                    self.Answer = eval(self.text)
                    Delete()
                    self.bar.insert(0, self.Answer)
                    self.bar["fg"] = "forestgreen"
                except:
                    self.bar["fg"] = "red"

        # Số
        self.n9 = Button(self.root, text="9", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Light cyan", command=lambda: insert("9"))
        self.n9.place(x=2 * X, y=(3 * Y) + 20)

        self.n8 = Button(self.root, text="8", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Light cyan", command=lambda: insert("8"))
        self.n8.place(x=X, y=(3 * Y) + 20)

        self.n7 = Button(self.root, text="7", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Light cyan", command=lambda: insert("7"))
        self.n7.place(x=0 * X, y=(3 * Y) + 20)

        self.n6 = Button(self.root, text="6", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Light cyan", command=lambda: insert("6"))
        self.n6.place(x=2 * X, y=(2 * Y) + 20)

        self.n5 = Button(self.root, text="5", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Light cyan", command=lambda: insert("5"))
        self.n5.place(x=X, y=(2 * Y) + 20)

        self.n4 = Button(self.root, text="4", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Light cyan", command=lambda: insert("4"))
        self.n4.place(x=0 * X, y=(2 * Y) + 20)

        self.n3 = Button(self.root, text="3", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Light cyan", command=lambda: insert("3"))
        self.n3.place(x=2 * X, y=(1 * Y) + 20)

        self.n2 = Button(self.root, text="2", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Light cyan", command=lambda: insert("2"))
        self.n2.place(x=X, y=(1 * Y) + 20)

        self.n1 = Button(self.root, text="1", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Light cyan", command=lambda: insert("1"))
        self.n1.place(x=0 * X, y=(1 * Y) + 20)

        self.n0 = Button(self.root, text="0", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Light cyan", command=lambda: insert("0"))
        self.n0.place(x=X, y=(4 * Y) + 20)

        # Dấu
        self.nbang = Button(self.root, text="=", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Blue", command=Answer)
        self.nbang.place(x=2 * X, y=(4 * Y) + 20)

        self.nnhan = Button(self.root, text="x", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Cyan", command=lambda: insert("*"))
        self.nnhan.place(x=3 * X, y=(1 * Y) + 20)

        self.nchia = Button(self.root, text=":", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Cyan", command=lambda: insert("/"))
        self.nchia.place(x=3 * X, y=(2 * Y) + 20)

        self.ncong = Button(self.root, text="+", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Cyan", command=lambda: insert("+"))
        self.ncong.place(x=3 * X, y=(3 * Y) + 20)

        self.ntru = Button(self.root, text="-", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Cyan", command=lambda: insert("-"))
        self.ntru.place(x=3 * X, y=(4 * Y) + 20)

        self.ncham = Button(self.root, text=".", font=("Courier New", 16, "bold"), padx=20, pady=16, bd=4, bg="Blue", command=lambda: insert("."))
        self.ncham.place(x=0 * X, y=(4 * Y) + 20)

        # Xóa
        self.xoaall = Button(self.root, text="AC", font=("Courier New", 16, "bold"), padx=14, pady=5, bd=4, bg="Green", command=Delete)
        self.xoaall.place(x=0, y=40)

        self.xoa = Button(self.root, text="DEL", font=("Courier New", 16, "bold"), padx=20, pady=5, bd=4, bg="Green", command=BackSpace)
        self.xoa.place(x=75, y=40)

        self.ngoac1 = Button(self.root, text="(", font=("Courier New", 16, "bold"), padx=20, pady=5, bd=4, bg="Green", command=lambda: insert("("))
        self.ngoac1.place(x=150, y=40)

        self.ngoac2 = Button(self.root, text=")", font=("Courier New", 16, "bold"), padx=20, pady=5, bd=4, bg="Green", command=lambda: insert(")"))
        self.ngoac2.place(x=225, y=40)

        # Chạy ứng dụng
        self.root.mainloop()

Game()
