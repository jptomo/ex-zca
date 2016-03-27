from zope import component

from app import IOutputMessage, Greeter
from infra import OutputMessage


def main():
    component.provideUtility(OutputMessage(), IOutputMessage, 'output')
    Greeter().greet()


if __name__ == '__main__':
    main()
