import math

class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.side = 0.0
        self.perimeter = 0.0
        self.area = 0.0
        self.alpha = 0.0
        self.beta = 0.0
        self.calc_side()
        self.calc_perimeter()
        self.calc_area()
        self.calc_alpha()
        self.calc_beta()

    def set_base(self, newbase):
        self.base = newbase

    def set_height(self, newheight):
        self.height = newheight
        
    def calc_side(self):
        bh = (self.base**2 + 4 * self.height**2)
        self.side = 0.5*math.sqrt(bh)
        return self.side
    
    def calc_perimeter(self):
        self.perimeter = 2 * self.side + self.base
        return self.perimeter
    
    def calc_area(self):
        self.area = 0.5 * self.base * self.height
        return self.area
    
    def calc_alpha(self):
        self.alpha = math.degrees(math.atan(self.height / (self.base * 0.5)))
        return self.alpha
    
    def calc_beta(self):
        self.beta = 180 - 2 * self.alpha
        return self.beta
   
    def print_all(self) -> None:
        print(f"------------------------------") 
        print(f"base     : {self.base}") 
        print(f"height   : {self.height}") 
        print(f"side     : {self.side}") 
        print(f"perimeter: {self.perimeter}") 
        print(f"area     : {self.area}") 
        print(f"alpha    : {self.alpha}") 
        print(f"beta     : {self.beta}") 
        print(f"------------------------------")

tri = Triangle(2,3)
tri.print_all()
tri = Triangle(2,5)
tri.print_all()
