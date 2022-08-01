#!/usr/bin/python3
""" the rectangle module """


class Rectangle:
    """ the Rectangle class """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rect """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the perimeter of the rect """
        if (self.__width == 0 or self.__height == 0):
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {}".format(my_rectangle.area()))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print("Area: {}".format(my_rectangle.area()))
