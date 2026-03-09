class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]


# take input from user
text = input("Enter a string: ")

# create object
obj = Reverse(text)

# print reversed string
print("Reversed string:", obj.reverse_string())