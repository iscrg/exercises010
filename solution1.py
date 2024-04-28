class Circle:
    """
    Circle class.

    Attributes:
        all_circles - list of all circles
        pi - the number of pi
    """
    all_circles = []
    pi = 3.1415

    def __init__(self, radius: float = 1) -> None:
        """
        Initialising object.
        :param radius: Circle radius
        """
        self.radius = radius
        self.all_circles.append(self)

    def area(self) -> float:
        """
        :return: Area of this circle.
        """
        return self.pi * self.radius ** 2

    @staticmethod
    def total_area() -> float:
        """
        Calculates the total radius of all circles
        :return: The total radius of all circles
        """
        return float(sum(circle.area() for circle in Circle.all_circles))

    def __repr__(self) -> str:
        """
        :return: Radius.
        """
        return str(self.radius)
