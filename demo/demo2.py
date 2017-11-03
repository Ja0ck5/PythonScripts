# a = 100
# b=200
# result = a + b
# print("result:%d"%result)


# password= raw_input("please enter ur password:")
# print("password:%s"%password)

# c=9
# d=2.0
# result = c//d
# print("result:%d"%result)

# result = c**d
# print("result:%d"%result)


# e='hello'
# f='world'
# result = e+f
# print("result:%s"%result)

# age=20
# if not 18 < age :
# 	print("I am a man")
# print("I am a boy")

# score = 680
# score = 500
# if score >= 600 :
# 	print("University")
# else :
# 	print("high school")


# if score >= 600 :
# 	print("University")
# elif 500 == score :
# 	print("haha 500")
# else :		
# 	print("boo 400")

# target = 1
# station = 1
# if 1 == target:
# 		print("u can pass")	

# 		if 1 == station :
# 			print("u can go off the car")

# i = 0
# j=0
# while i < 100:
# 	print("Haha%d"%i)
# 	i+=1
# 	while j < 100:
# 		print("JAJA%d"%j)
# 		if j == 52 : 
# 			print("now break")
# 			break
# 		j+=1
							

# for i in range(10):
# 	print("-"*20)

# 	if i == 4 :
# 		print("now take a break")
# 		break

# 	print("i=%d"%i)	



# def printFive():
# 	print("=========================")
# 	print("=========================")
# 	print("=========================")
# 	print("=========================")
# 	print("=========================")

# def printName():
# 	print("=========================")
# 	print("=========================")
# 	print("ArmStrong")
# 	print("=========================")
# 	print("=========================")	


# # call function
# printFive()
# printName()


str = "hello world"
mystr = "hello world this is a python script"
# i=0
# while i< 11 :
# 	print("%s"%str[i])
# 	print("%s"%str[i:11])
# 	i+=1

# print("%s"%mystr.find("is"))

# print("%d"%mystr.find("is",10,15))

# print("%d"%mystr.count("is"))

# print("%d"%len(mystr))

# print("%s"%mystr.replace("is","si",mystr.count("is")))

# names = ['xioaxiao','dada','zz']

# tuple1 = ['xioaxiao','dada','zz',3.14159265358979626,100]

# names.append("test1")

# del names[2] 

# names.remove("test1")
# names.pop()

# i=0
# while i < len(names) : 
# 	print("name[%d]=%s"%(i,names[i])) 
# 	i+=1

# for j in tuple1 :
# 	print("j=%s"%j) 

info = {"name" : "hello","addr":"American","age":20}

print("%s"%info['name'])

info['name'] = "world"

print("%s"%info['name'])

info['gender'] = 'male'

print("%s"%info['gender'])

# del info['gender']

# print("%s"%info['gender'])

# print(info)

# info.clear()

# print(info)
print(info.keys())
print(info.values())
print(info.items())
print(info.has_key('who'))

for key in info.keys() : 
	print(key)

for value in info.values() : 
	print(value)

for item in info.items() : 
	print(item)	






	

