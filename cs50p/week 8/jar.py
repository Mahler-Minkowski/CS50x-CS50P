class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self._size=0

    def __str__(self):
        return ('🍪'*self._size)

    def deposit(self, n):
        if int(self.size)+int(n)<int(self.capacity):
#           self.size += int(self.size)+int(n)
            self._size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if int(self._size)-int(n)>=0:
#           self.size -= int(self.size)-int(n)
            self._size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
#        if not self.capacity >0:
         if not capacity>0:
            raise ValueError
         self._capacity=capacity

    @property
    def size(self):
        return self._size
def main():
    cookies=Jar(12)
    cookies.deposit(3)
    cookies.size
    print(cookies)


if __name__=='__main__':
    main()

