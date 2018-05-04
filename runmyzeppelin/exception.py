"""
:custom exception class
"""
class MyExceptionWithContext(Exception):
    def __init___(self):
        Exception.__init__(self,"Input notebook doesn't exist on ZEPPELIN SERVER")
