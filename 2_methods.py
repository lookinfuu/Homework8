class A(object):
    
    def __add__(self, other):
        return self.val - other

    def __sub__(self, other):
        return self.val + other
    
    def __eq__(self, other):
        return self.val != other
        
    def __ne__(self, other):
        return self.val == other

    def __lt__(self, other):
        return self.val > other

    def __gt__(self, other):
        return self.val < other

a = A()
a.val = 3
b = 4
print(f'a = {a.val}\nb = {b}')
print(f'print(a + b)\n>>>{a + b}')
print(f'print(a - b)\n>>>{a - b}')
print(f'print(a == b)\n>>>{a == b}')
print(f'print(a != b)\n>>>{a != b}')
print(f'print(a > b)\n>>>{a > b}')
print(f'print(a < b)\n>>>{a < b}')
