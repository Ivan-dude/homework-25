from colorama import *
class Vehicle:
    _COLOR_VARIANTS = ['red', 'black', 'white']
    def __init__(self, owner, _model, _engine_power, _color):
        self.owner = owner
        self._model =_model
        self._engine_power = _engine_power
        self._color = _color
    def get_model(self):
        return f'Модель: {self._model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power}'
    def get_color(self):
        return f'Цвет: {self._color}'

    def print_info(self):
        if self.owner != 'John':
            print(Fore.BLUE + Vehicle.get_model(self), Vehicle.get_horsepower(self), Vehicle.get_color(self),
            f'{Fore.BLUE}Владелец:{Fore.GREEN}{self.owner}', sep='\n')
        else:
            print(Fore.BLUE + Vehicle.get_model(self), Vehicle.get_horsepower(self), Vehicle.get_color(self),
            f'{Fore.BLUE}Владелец:{self.owner}', sep='\n')
    def set_color(self, new_color):
        if new_color.lower() in Vehicle._COLOR_VARIANTS:
            self._color = Fore.GREEN + new_color
        else:
            print(f'{Fore.RED}Нельзя сменить цвет на {new_color}')
class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()