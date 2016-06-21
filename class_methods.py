class Methods(object):

    def __init__(self):
        super().__init__()

    def instance_method(self):
        print("Hello from instance method: {}".format(self))

    @classmethod
    def class_method(cls):
        print("I am a class method: {}".format(cls))

    @staticmethod
    def static_method():
        print("Static as a solid rock")


inst = Methods()

# call instance method
# TestCase.instance_method()
inst.instance_method()

# call class method
Methods.class_method()
inst.class_method()

# call static method
Methods.static_method()
inst.static_method()
