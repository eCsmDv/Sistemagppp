class Observer:
    def update(self, message):
        pass

class Customer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Notificação para {self.name}: {message}")

class OrderNotifier:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_all(self, message):
        for observer in self.observers:
            observer.update(message)
