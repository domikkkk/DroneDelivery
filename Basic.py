from io import TextIOWrapper
from math import ceil
from matplotlib import pyplot as plt


class Products:
    amount = None
    weights = []
    
    def read_weights(self, filehandler : TextIOWrapper):
        self.amount = int(filehandler.readline())
        self.weights = [int(i) for i in filehandler.readline().split()]
        return


class Warehouse:
    def __init__(self, idx) -> None:
        self.idx = idx  # type

    def read_items(self, filehandler: TextIOWrapper):
        self.r, self.c = [int(i) for i in filehandler.readline().split()]
        self.items = [int(i) for i in filehandler.readline().split()]
        return


class Order:
    def __init__(self, idx) -> None:
        self.idx = idx  # type
    
    def read_needed_items(self, filehandler: TextIOWrapper):
        self.r, self.c = [int(i) for i in filehandler.readline().split()]
        self.number_of_items = int(filehandler.readline())
        self.needed_items = [int(i) for i in filehandler.readline().split()]
        return


class Dron:
    def __init__(self, idx, r, c, max_weight) -> None:
        self.idx = idx  # type
        self.r = r
        self.c = c
        self.max_weight = max_weight
        self.taken_items:dict[int|list[int]] = {}  # {0: [2, 100]} <=> item 0, amount 2, weight 100

    def go_to(self, r, c) -> int:
        """
            Return number of turns
        """
        dist = ((self.c - c)**2 + (self.r - r)**2)**0.5
        self.r = r
        self.c = c
        return ceil(dist)

    def load(self, warehaouse: Warehouse, type, amount):
        pass

    def deliver(self, order: Order, type):# amount isn't needed because only one item is delivered
        pass

    def unload(self, warehouse: Warehouse, type, amount):
        pass

    def wait(self, turn):
        pass


class All:
    p = Products()
    w:list[Warehouse] = []
    o:list[Order] = []
    d:list[Dron] = []

    def read_input(self, filename):
        with open(filename, 'r') as f:
            self.rows, self.columns, n, self.turns, max_weight = [
                int(i) for i in f.readline().split()
            ]
            self.p.read_weights(f)

            number_of_warehouses = int(f.readline())
            for i in range(number_of_warehouses):
                self.w.append(Warehouse(i))
                self.w[-1].read_items(f)

            number_of_orders = int(f.readline())
            for i in range(number_of_orders):
                self.o.append(Order(i))
                self.o[-1].read_needed_items(f)

            start_r, start_c = self.w[0].r, self.w[0].c
            for i in range(n):
                self.d.append(Dron(i, start_r, start_c, max_weight))
        return

    def draw_map(self):
        plt.xlabel('Columns')
        plt.ylabel('Rows')
        x, y = [], []
        for order in self.o:
            x.append(order.c)
            y.append(order.r)
        plt.scatter(x, y, s=1)
        x.clear()
        y.clear()
        for warehouse in self.w:
            x.append(warehouse.c)
            y.append(warehouse.r)
        plt.scatter(x, y, s=30)
        plt.legend(['orders', 'warehouses'])
        plt.savefig('Mapa.png')


if __name__ == "__main__":
    a = All()
    a.read_input('busy_day.in')
    a.draw_map()
