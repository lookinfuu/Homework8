import mymodule
from mymodule import check_int_number


class A:

    def __init__(self, val):
        self.val = val
    
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


while True:
    a = input('a:')
    a = check_int_number(a)
    if type(a) != int:
        print(a)
        continue
    b = input('b:')
    b = check_int_number(b)
    if type(b) != int:
        print(b)
        continue
    print('Ниже приведены обратные операции:')
    print(f'{a} + {b} = {A(a) + b}')
    print(f'{a} - {b} = {A(a) - b}')
    print(f'{a} == {b} its {A(a) == b}')
    print(f'{a} != {b} its {A(a) != b}')
    print(f'{a} < {b} its {A(a) < b}')
    print(f'{a} > {b} its {A(a) > b}')
    break