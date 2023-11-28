#!/usr/bin/python3
"""
This is the "1-rectangle" module.
Which defines one class, Rectangle.
"""


class Rectangle:
    """A class Rectangle that defines a rectangle by:
        (based on 0-rectangle.py)"""
    def __init__(self, width=0, height=0):
        """Inits Rectangle.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """Retries width"""
            return self.__width

        @width.setter
        def width(self, width):
            """Sets width"""
            if type(width) is not int:
                raise TypeError('width must be an integer')
            if width < 0:
                raise ValueError('widht must be >= 0')
            self.__width = width

        @property
        def height(self):
            """Retrivies height"""
            return self.__height

        @height.setter
        def height(self, height):
            """Sets height"""
            if type(height) is not int:
                raise TypeError('height must be an integer')
            if height < 0:
                raise ValueError('height must be >= 0')
            self.__height = height
