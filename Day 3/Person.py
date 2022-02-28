#!/usr/bin/env python3

class Person:
    def __init__(self,fn,ln):
        self.fn=fn
        self.ln=ln
    def __str__(self):
        return("The full name is: %s %s" %(self.fn, self.ln))


p1=Person(input("Enter first name: "), input("Enter last name: "))
print(p1)