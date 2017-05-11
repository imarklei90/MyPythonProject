f = open("e:\\projects\\MyPythonProject\\src\\basicPython\\FileIO\\writeData.txt",'w')

#
# print f.read()
# print f.readline()

# f.close()
#
# from __future__ import with_statement
#
# with open("") as somefile:
#     do(somefile)

# read(n)
# print f.read(8)
# print f.read(200)
# f.close()

# print f.read()
# f.close()

# for i in range(3):
#     print str(i) + ":" + f.readline()
# f.close()

# import pprint
# pprint.pprint(f.readlines())

# WRITE
# f.write("this is add contents")
# f.close()

f1 = open(r'e:\\projects\\MyPythonProject\\src\\basicPython\\FileIO\\TestData.txt')
lines = f1.readlines()
f1.close()
lines[1] = "A"
f1 = open(r'e:\\projects\\MyPythonProject\\src\\basicPython\\FileIO\\Data.txt','w')
f1.writelines(lines)
f1.close()