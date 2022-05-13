class Symbol:
    def __init__(self, color: str, icon: str):
        self.color = color
        self.icon = icon


class Card(Symbol):
    def __init__(self, color: str, icon: str, value: str):
        super().__init__(color, icon)  #inherit attributes from the class Symbol
        self.value = value  #add new atrribute

    def __str__(self) -> str:  #use string representation to get output
        return f"{self.color} {self.icon} {self.value}"
