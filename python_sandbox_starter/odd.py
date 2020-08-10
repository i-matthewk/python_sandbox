#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


print("Odd number checker")

def isOdd(num):
    if (num % 2) == 0:
       print("{0} is Even".format(num))
       return False 
    else:
       print("{0} is Odd".format(num))
       return True 



# main entry point



if(len(sys.argv) is not 2):
    print("this script takes exactly one argument")

    exit()


print("the naME OF THE SCRIPT IS " + sys.argv[0])
print("the argument received is: " + sys.argv[1])



print(isOdd(int(sys.argv[1])))