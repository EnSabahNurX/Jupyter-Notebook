class Order:
    def __init__(self, order, **kwargs):
        print('INIT of Order...!!!')
        self.order = order


class First(Order):

    def __init__(self, first, **kwargs):
        print('INIT of Fisrt...!!!')
        super().__init__(**kwargs)
        self.first = first


class Second(Order):

    def __init__(self, second, **kwargs):
        print('INIT of Second...!!!')
        super().__init__(**kwargs)
        self.second = second


class Third(Order):

    def __init__(self, third, **kwargs):
        print('INIT of Third...!!!')
        super().__init__(**kwargs)
        self.third = third


class Combined(First, Second, Third):

    # def __init__(self, order, first, second, third):
    def __init__(self, order=None, first=None, second=None, third=None):
        print('INIT of Combined...!!!')
        super().__init__(order=order, first=first, second=second, third=third)


c = Combined("Order", "Primeiro", "Segundo", "Terceiro")
print(c.order, c.first, c.second, c.third, Combined.__mro__)
d = Combined("One", "Two", "Three", "Four")
print(d.order, d.first, d.second, d.third, Combined.__mro__)
