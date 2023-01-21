
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None: # リストに要素が入っていないとき、headが作成したノードになる
            self.head = new_node
        else: # 最後尾のノードのリンクを作成したノード（メモリアドレス）にする
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None: # リストに要素が入っていないとき、headが作成したノードになる
            self.head = new_node
        else: # 先頭のノードのリンクを作成したノード（メモリアドレス）にする
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
        
    def pop(self):
        if self.length == 0: # リストに要素が入っていないとき、何もしない。
            return None
        # リストのtailから探索開始
        temp = self.tail
        if self.length == 1: # リストに要素がなくなったとき、headとtailをNoneにする。
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev # tailに削除する要素の「前」の要素を入れる
            self.tail.next = None # tailになったポインタをNoneにする
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self):
        if self.length == 0: # リストに要素が入っていないとき、何もしない。
            return None
        # リストのhead探索開始
        temp = self.head
        if self.length == 1: # リストに要素がなくなったとき、headとtailをNoneにする。
            self.head = None
            self.tail = None
        else:
            self.head = temp.next # headに削除する要素の「次」の要素を入れる
            self.head.prev = None # headになったポインタの「前」をNoneにする
            temp.next = None
        self.length -= 1
        return temp.value
        
    def get(self, index):
        if index == -1:
            index = self.length - 1
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index == -1:
            return self.append(value)
        if index < 0 or index > self.length:
            return None
        if index == self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        
        new_node = Node(value) #新しいノードを作る

        prev_node = self.get(index-1) # indexの前のノードを取得する
        next_node = prev_node.next

        new_node.next = next_node # 新しいノードのポインタを設定する
        new_node.prev = prev_node # 新しいノードのポインタを設定する
        next_node.prev = new_node # 次のノードのポインタを新しいノードにする
        prev_node.next = new_node # 前のノードのポインタを新しいノードにする

        self.length += 1 # ノードの長さを増加する
        return True    

    def remove(self, index):
        if index == -1:
            return self.pop()
        if index < 0 or self.length <= index:
            return None
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.pop_first()    
            
        temp = self.get(index) # indexの前のノードを取得する

        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        temp.next = None
        temp.prev = None

        self.length -= 1 # ノードの長さを減少する
        return temp 

    def reverse(self):
        self.print(True,)
        

    def print(self, reverse=None):
        result = []
        if reverse:
            temp = self.tail
            while temp is not None:
                result.append(temp.value)
                temp = temp.prev
        else:
            temp = self.head
            while temp is not None:
                result.append(temp.value)
                temp = temp.next
        print(result)

# 2022/12/30
# doubleから。
if __name__ == '__main__':
    ll = [11, 3, 23, 7]

    # Create the LinkedList
    l = DoublyLinkedList(ll[0])
    # l.print()
    # print(l.head.value)

    l.append(ll[1])
    l.print()

    # print(l.pop())
    # print(l.pop())
    # print(l.pop())
    
    # l.pop_first()
    # l.print()
    # l.pop_first()
    # l.print()
    # l.pop_first()
    # l.print()
    # l.pop_first()
    # l.print()

    # print(l.get(0))
    # print(l.get(1))
    # print(l.get(2))
    # print(l.get(-1))
    # print(l.get(-2))
    # print(l.get(-3))

    l.insert(1, 100)
    l.print()
    # l.remove(1)
    # l.print()

    l.reverse()

