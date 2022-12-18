# Linked list are values stored in different places in memory. One value point to the next one, so we find all the nodes
# リンクリストはメモリアドレスにランダムに保存されています。
# １つの要素はノードという名前です。ノードの中には、ノードの値と次のノードのポインタが入っています。
# Head and tail are pointers
# headとtailはポインターです。
"""
Head               Tail
11  => 3  => 23  => 7  => None
"""

# List are values stored continuously in memory, so we can use indexes
"""
11 3 23 7
0  1 2  3
"""
# What is a Node ?
"""
A Node is a dictionary 
{
    "value": 11,
    "next": None
}
"""

# What is a linkedlist ?
"""
The entire linked list is a nested dictionary
Head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23
            "next": {
                "value": 7,
                "next": None     <== Tail
            }
        }
    }
}
"""

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
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
        self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0: # リストに要素が入っていないとき、何もしない。
            return None
        # リストのheadから探索開始
        temp = self.head
        pre = self.head # preは「前」の意味。
        while temp.next: # temp.nextがNone以外であれば進める
            pre = temp
            temp = temp.next
        self.tail = pre # tailに削除する要素の「前」の要素を入れる
        self.tail.next = None # tailになったポインタをNoneにする
        self.length -= 1
        if self.length == 0: # リストに要素がなくなったとき、headとtailをNoneにする。
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0: # リストに要素が入っていないとき、何もしない。
            return None# リストのheadから探索開始
        temp = self.head
        self.head = self.head.next
        temp.next = None # tempは、削除前のノード。temp.next=Noneにすると、ポインタを削除する。
        self.length -= 1
        if self.length == 0: # リストに要素がなくなったとき、headとtailをNoneにする。
            self.tail = None
        return temp

    def get(self, index):
        if index == -1:
            index = self.length - 1
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
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
        temp = self.get(index-1) # indexの前のノードを取得する
        new_node.next = temp.next # 新しいノードのポインタを設定する
        temp.next = new_node # 前のノードのポインタを新しいノードにする
        self.length += 1 # ノードの長さを増加する
        return True    


    def print(self):
        temp = self.head
        result = []
        while temp is not None:
            result.append(temp.value)
            temp = temp.next
        print(result)


if __name__ == '__main__':
    ll = [11, 3, 23, 7]

    # Create the LinkedList
    l = LinkedList(ll[0])
    # l.print()
    # print(l.head.value)

    l.append(ll[1])
    # l.print()

    print(l.pop())
    print(l.pop())
    print(l.pop())
    l.prepend(ll[0])
    l.print()
    l.prepend(ll[1])
    l.print()
    l.prepend(ll[2])
    l.print()
    print(l.get(-1))
    l.set_value(-1, 1000)
    # l.pop_first()
    # l.pop_first()
    # l.pop_first()
    l.insert(0, 12345)
    l.print()
    l.insert(-1, 223344)
    l.print()
    l.insert(2, 333333)
    l.print()


