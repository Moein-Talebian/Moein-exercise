#!/usr/bin/env python3
class Mammals:
    def __init__(self):
        self.members = ['Tiger', 'Elephant', 'Wild cat']
    def printMembers(self):
        print('Printing members of the mammals class')
        for member in self.members:
            print('\t%s' % member)