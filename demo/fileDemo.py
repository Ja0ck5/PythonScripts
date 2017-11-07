#coding=utf-8

# f = open('D:/f.txt','w')
# f = open('D:/f.txt','r')
# f.write('Hello world,Who am I')

# content = f.read(3)

# print(content)

# content= f.readlines()

# print(type(content))
# for temp in content :
# 	print(temp)
# f.close()

# content = f.read(10)

# while len(content)>0 :
# 	print(content)	
# 	content = f.read(0)

# f.close()
oldFileName = 'D:/f.txt'
oldFile = open(oldFileName,'r')


num = oldFileName.rfind('.')

left = oldFileName[0:num]
right = oldFileName[num:]

newFile = open(left +'-copy' + right,'w')

content = oldFile.readline()
print(content)
while len(content)>0 :
	newFile.write(content)
	content = oldFile.readline()


oldFile.close()
newFile.close()