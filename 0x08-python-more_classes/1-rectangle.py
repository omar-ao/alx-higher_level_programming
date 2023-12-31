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
        self.width = width
        self.height = height

        @property
        def width(self):
            """Retries width"""
            return self.__width

        @property
        def height(self):
            """Retrivies height"""
            return self.__height

        @width.setter
        def width(self, value):
            """Sets width"""
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @height.setter
        def height(self, value):
            """Sets height"""
            if not isinstance(height, int):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
