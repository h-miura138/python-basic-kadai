class Humen:
  def __init__(self,name,age):
    self.name=""
    self.age=0

  def set_name(self, name):
        self.name = name
  def set_age(self, age):
        self.age = age

  def check_adult(self):
      if self.age>=20:
        print("大人です")

      else:
        print("大人ではありません")

name_age = Humen("yamada",23)

list_age = []

list_age.append(23)
list_age.append(20)
list_age.append(18)


for a in list_age:
  
  name_age.set_age(a)
  name_age.check_adult()
