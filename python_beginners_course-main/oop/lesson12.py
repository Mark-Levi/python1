from typing import Any


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("__call__")
        self.__counter += 1
        return self.__counter


c = Counter()
print(c())
print(c())
print(c())
