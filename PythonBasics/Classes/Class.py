class Greeter(object):
    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
            print('Hello %s!' % self.name.upper())
        else:
            print('Hello %s!' % self.name)


g = Greeter('Hoang')
g.greet()
g.greet(loud=True)
