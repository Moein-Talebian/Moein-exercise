#!/usr/bin/env python3

class Person (object):
    def __init__(self,fn,ln):
        self.fn=fn
        self.ln=ln
    def getfn(self):
        return self.fn
    def getln(self):
        return self.ln
    def __str__(self):
        return("The full name is: %s %s" %(self.fn, self.ln))

class Student(Person):
    def __init__(self, fn, ln, subject):
        Person.__init__(self,fn, ln)
        self.subject=subject
    def getsubject(self):
        return self.subject
    def __str__(self):
        return("The full name is %s %s and the subject is %s" %(self.fn, self.ln, self.subject))    

p1=Student(input("Enter first name: "), input("Enter last name: "), input("Enter subject: "))
print(p1)