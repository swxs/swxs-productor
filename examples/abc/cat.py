from .animal import Animal


class Cat:
    name = "cat"

    def eat(self, food: str) -> None:
        if food == 'fish':
            print('yummy')
        else:
            print(f'cat not eat {food}')


Animal.register(Cat)
