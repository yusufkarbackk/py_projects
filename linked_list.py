from datetime import datetime


class LinkedList:
    def __init__(self):
        self.head = None  # head dari linked list bernilai awal None
        self.size = 0  # size awal dari linked list

    def addNode(self, data):
        if self.head == None:  # cek apakah head masih None
            new_node = Node(data)  # buat node baru
            self.head = new_node  # jadikan node baru sebagai head
            self.head.next = None  # next dari head tersebut adalah None
            self.size += 1  # size dari list ditambah 1
            return new_node.data  # kembalikan data dari node
            # print(f'{self.size}')
        else:
            new_node = Node(data)  # buat node baru
            current = self.head  # head sekarang disimpan kedalam variabel current

            while current.next != None:  # loop selama next dari current tidak None
                current = current.next  # ganti variabel current dengan next dari current sebelumnya

            current.next = new_node  # jadikan node baru sebagai next dari current
            new_node.next = None  # next dari node baru adalah None
            self.size += 1  # tambahkan size list dengan 1
            return new_node.data  # kembalikan data dari node baru
            # print(f'{self.size}')

    def calculateList(self):
        if self.size == 0:  # cek apakah list nya kosong
            return 'maaf list kosong'
        else:
            num_list = ""  # buat variabel num_list dengan isi string kosong
            current = self.head  # head sekarang di simpan dalam variabel current
            while current != None:  # loop selama current tidak None
                # tambahkan data kedalam variabel num_list
                num_list += str(current.data)
                current = current.next  # ganti isi variabel current dengan next dari current sebelumnya

            # hitung berdasarkan data yang ada di linked list
            new_node = Node(eval(num_list))

            self.head = new_node  # head sekarang bernilai hasil perhitungan
            self.head.next = None

            # memasukan hasil hitung dan tanggal kedalam variabel history
            history = f"{num_list} = {eval(num_list)}, {datetime.now()}"

            # menulis data dari variabel history kedalam file
            self.writeHistory(history)
            return eval(num_list)  # kembalikan hasil eval dari num_list

    def clearList(self):
        if self.size == 0:  # cek apakah list nya kosong
            print('maaf list kosong')
        else:
            current = self.head  # variabel current berisi head sekarang
            while current.next != None:  # loop selama next dari variabel current tidak None
                tmp = current.next  # simpan next dari current kedalam variabel tmp
                current = None  # hapus nilai current
                self.head = tmp  # jadikan variabel tmp sebagai head yang baru
                current = self.head  # masukan head sekarang kedalam variabel current
                self.size -= 1  # kurangi size linked list sebanyak 1
            self.head = None  # hapus head sekarang
            self.size -= 1

    def writeHistory(self, data):  # menerima 1 parameter yaitu data
        with open('history.txt', 'a') as file:  # membuat file history.txt
            file.write('\n')
            # menulis data yang diambil dari parameter kedalam file history.txt
            file.write(f"{data}\n")


class Node:
    def __init__(self, data):
        self.data = data  # data dari node
        self.next = None  # next dari node, nilai awal adalah None
