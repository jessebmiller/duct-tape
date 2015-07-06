"""
some application that is very important and is expected to iterate quickely.

This will mean doing temporary code in order to learn things.
We might like to be reminded that we did some temp code.

"""

from tape import yell

def clean_code(var=None):
    print "nice clean code {}".format(var)


# this is crap code will be taken care of
yell()

def crap_duct_tape_code():
    print "+ Junk!#@! THAT bazcly wurkZZZ!"


clean_code()
clean_code(crap_duct_tape_code())
