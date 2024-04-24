class Singleton:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name: str):
        self.name = name

if __name__ == '__main__':

    a = Singleton("Первый")
    print(f"{a.name = }, {a._instance = }")
    b = Singleton("Второй")
    print(f"{a is b = }")
    print(f"{a.name = }\n{b.name = }, {b._instance = }")
    c = Singleton("Третий")
    print(f"{a is c = }")
    print(f"{a.name = }\n{c.name = }, {c._instance = }")