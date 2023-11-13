class Product:
  def __init__(self):
    self.name=""
    self.age=0

  def set_name(self, name):
        self.name = name
  def set_age(self, age):
        self.age = age

  def show_name_age(self):
        print(self.name,self.age)

Humen = Product()

Humen.set_name("miura")
Humen.set_age(23)
Humen.show_name_age()
