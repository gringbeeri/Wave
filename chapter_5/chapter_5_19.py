#19
lists = []
for numbering in range(2, 100):
    def is_prime(numbering):
        for numbers in range(2, numbering):
            if numbering % numbers == 0:
                return False
        lists.append(numbering) 
    is_prime(numbering)
print(lists)
