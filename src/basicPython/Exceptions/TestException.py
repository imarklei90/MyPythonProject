try:
    x = input("enter first number...")
    y = input("enter second number...")
    print x / y
# except ZeroDivisionError:
#     print "can't input 0"
# except TypeError:
#     print "input wrong format number"
# except NameError:
#     print "input wrong name"
except (ZeroDivisionError,TypeError,NameError), e:
    print e
    print "Many Wrongs"