class Print:
    arg1 = ""

    def __init__(self, arg: int ):
        self.arg1 = arg

    def print(self):
        print(f"Estás usando la clase Print {self.arg1}")