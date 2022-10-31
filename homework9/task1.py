class Triangle:
    def __init__(self):
        self._a = 0
        self._b = 0
        self._c = 0

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @a.setter
    def a(self, value):
        self._a = value

    @b.setter
    def b(self, value):
        self._b = value

    @c.setter
    def c(self, value):
        self._c = value

    def test_triangle(self):
        if self._a + self._b > self._c and self._a + self._c > self._b and self._b + self._c > self._a:
            return "Треугольник существует!"
        else:
            return "Треугольник не существует!"


triangle = Triangle()
while True:
    triangle.a = int(input("Введите сторону треугольника: "))
    triangle.b = int(input("Введите сторону треугольника: "))
    triangle.c = int(input("Введите сторону треугольника: "))
    print(triangle.test_triangle())
