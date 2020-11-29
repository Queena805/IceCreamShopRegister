class icecream:

    icecream_menu = {
        'Peach':8,
        'Mango':7,
        'Strawberry':10,
        'Vanilla':6,
        'Oreo':11,
        'Chocolate':9.5,
        'Rocky road': 9

    }


    def __init__(self):
        self.total = 0
        self.items = []

    def add(self,item):
        self.items.append(item)
        self.total += self.icecream_menu[item]

    def bill_total(self,tax=8,service=10):
        tax = (tax/100)*self.total
        service = (service/100)* self.total
        total = self.total + tax + service

        for item in self.items:
            print(f'{item:25} ${self.icecream_menu[item]}')   

        print(f'{"The total":25} ${total:.3f}')


