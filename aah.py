class RomanConverter:

    def convert(self, num):
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        roman = ""

        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman += sym[i]
                num -= val[i]
            i += 1

        return roman


number = int(input("Enter an integer: "))

obj = RomanConverter()

print("Roman numeral:", obj.convert(number))