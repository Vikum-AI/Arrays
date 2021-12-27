# array functions (reverse, add all, number of elements)


class array:

    def __init__(self, a):

        reversed = []

        self.a = a
        self.total = 0
        self.length = len(self.a)
        self.index = "Use the .find() methord to find the index"

        for i in range(self.length):
            self.total = self.total + self.a[i]

        for i in range(self.length):
            reversed.append(self.a[self.length - 1 - i])

        self.reversed = reversed

    def find(self, arg):

        condition = False
        n = len(self.a)

        for i in range(n):
            if arg == self.a[i]:
                self.index = i
                condition = True

        if condition == False:
            self.index = "Not Found"


class list:

    def __init__(self, a):

        reversed = []

        self.a = a
        self.length = len(self.a)
        self.index = "Use the .find() methord to find the index"

        for i in range(self.length):
            reversed.append(self.a[self.length - 1 - i])

        self.reversed = reversed

    def find(self, arg):

        condition = False
        n = len(self.a)

        for i in range(n):
            if arg == self.a[i]:
                self.index = i
                condition = True

        if condition == False:
            self.index = "Not Found"
