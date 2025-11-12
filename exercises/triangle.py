import numbers

class Triangle:
    # x and y optional
    def __init__(self, base, height):
        self.base = base 
        self.height = height

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("must be a number")
        
        if value <= 0:
            raise ValueError("base must be larger than zero")
        self._base = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, numbers.Number):
            raise TypeError("must be a number")
        self._height = value

    @property
    def area(self):
        pass  

    # @property
    # def perimeter(self):
    #     pass  

    def __eq__(self, other):
        if not isinstance(self, other):
            return NotImplemented

    def __lt__(self, other):
        pass
    
    def __gt__(self, other):
        pass

    def __repr__(self):
        pass