from zope import component
from zope.interface import Interface
from zope.interface.interface import Method


class IOutputMessage(Interface):
    output = Method(''' output message to some devices. ''')


class Greeter:
    def __init__(self):
        self.out = component.getUtility(IOutputMessage, 'output')

    def greet(self):
        self.out.output('hello, world.')
