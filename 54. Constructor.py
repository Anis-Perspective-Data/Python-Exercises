class A:
    def __init__(self):
        print("A class")
    def f():
        print("how are u doing")
    f()
class B(A):
    def __init__(self):
        print("B class")
        super().__init__()
o=B()