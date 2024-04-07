class Dog:
    name = "dog"

    def eat(self, food: str) -> None:
        if food == 'meat':
            print('yummy')
        else:
            print(f'dog not eat {food}')
