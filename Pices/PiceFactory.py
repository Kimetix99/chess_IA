import abc


class PiceFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_pawn(self, x, y):
        pass

    @abc.abstractmethod
    def create_tower(self, x, y):
        pass

    @abc.abstractmethod
    def create_horse(self, x, y):
        pass

    @abc.abstractmethod
    def create_bishop(self, x, y):
        pass

    @abc.abstractmethod
    def create_queen(self, x, y):
        pass

    @abc.abstractmethod
    def create_king(self, x, y):
        pass
