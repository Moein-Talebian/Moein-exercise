#!/usr/bin/env python3
class Fish:
    def __init__(self):
        self.members = ['Catfish', 'Goby Fish', 'Snapper']
    def printMembers(self):
        print('Printing members of the fish class')
        for member in self.members:
            print('\t%s' % member)