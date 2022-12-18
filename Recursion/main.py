class Manager:
    def __init__(self) -> None:
        self.message(1)

    def message(self, n):
        print(n)
        self.message2(n+1)

    def message2(self, n):
        print(n)
        self.message3(n+1)

    def message3(self, n):
        print(n)
        self.message4(n+1)
        
    def message4(self, n):
        print(n)

class Manager2:
    def __init__(self) -> None:
        self.message(1)

    def message(self, n):
        print(n)
        if n >= 4:
            return
        self.message(n+1)



#   １つの関数で1回printできる
#   initで呼べるのは１つの関数だけ
#   １～４までをprintする

if __name__ == "__main__":
    m = Manager2()
