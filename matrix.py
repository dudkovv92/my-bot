class Matrix:
    def __init__(self, data):
        self.data = data

    def transpose(self):
        return [[row[i] for row in self.data] for i in range(len(self.data[0]))]

    def __str__(self):
        result = ""
        for row in self.data:
            result += str(row) + "\n"
        return result

m = Matrix([[1, 2, 3], [4, 5, 6]])
print(m)
print(m.transpose())