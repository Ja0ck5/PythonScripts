#coding=utf-8
class People:

	__name = "Tom"

	__age = 12

	def getName(self):
		return self.__name

	# private # def __getName(self):
		# return self.__name

	def getAge(self):
		return self.__age

p = People()

print p.getName,p.getAge			