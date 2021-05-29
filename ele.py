import abc

class Shape():
  __color='black'
  @abc.abstractmethod
  def calculate_area():
    pass
  def show_color(self):
    if str(self.__class__.__name__)=='Rectangle':
      return self._Rectangle__color
    elif str(self.__class__.__name__)=='Circle':
      return self._Circle__color
    else:
      return self._Triangle__color
  def __cmp__(self, other):
    try:
      self.area!=-23040230420 and other.area!=-42323   
    except:
      self.calculate_area()
      other.calculate_area()
    finally:
      li=sorted([self.area,other.area])
      if self.area==li[0] and self.area!=other.area:
        return f'{self.__class__.__name__} < {other.__class__.__name__}'
      elif self.area==li[-1] and self.area!=other.area:
        return f'{self.__class__.__name__} > {other.__class__.__name__}'
      else:
        return f'{self.__class__.__name__} == {other.__class__.__name__}'
  def __add__(self, other):
    try:
      return self.area+other.area
    except:
      self.calculate_area()
      other.calculate_area()
      return (self.area+other.area)
  def __sub__(self, other):
    try:
      return self.area-other.area
    except:
      self.calculate_area()
      other.calculate_area()
      try:
        return (self.area-other.area)
      except ArithmeticError:
        print('ArithmeticError has ocured !')
  

class Rectangle(Shape):
  def __init__(self,length,width,*args):
    try:
      self.__color=args[0]
    except:
      pass
    self.length=length
    self.width=width
  def calculate_area(self):
    self.area=self.length*self.width
  

class Triangle(Shape):
  def __init__(self,length,height,*args):
    try:
      self.__color=args[0]
    except:
      pass
    self.length=length
    self.height=height
  def calculate_area(self):
    self.area=(self.length*self.height)/2
  def show_color(self):
    return self._Shape__color
  
  
class Circle(Shape):
  def __init__(self,radius,*args):
    try:
      self.__color=args[0]
    except:
      pass
    self.radius=radius
  def calculate_area(self):
    self.area=self.radius**2*3.14
  def show_color(self):
    return self._Shape__color
