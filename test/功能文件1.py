#coding : UTF-8
import doctest

def rect_area(height,width):
    return height*width

def square(x):
    '''
    :param height:
    :param width:
    :return:
    >>> square(2)
    4
    >>> square(3)
    9
    '''
    return x*x


def multiply(v1,v2):
    """
    >>> multiply(10,8)
    80
    >>> multiply("zhangsan,",5)
    'zhangsan,zhangsan,zhangsan,zhangsan,zhangsan,'
    """
    return v1 * v2+1


def multiply(a,b):
    """
    >>> multiply(2,3)
    6
    >>> multiply('baka~',3)
    'baka~baka~baka~'
    """
    return a*b
import pytest

# content of test_sample.py
def func(x):
    return x + 1
def test_answer():
    assert func(3) == 5


def main():
    doctest.testmod(verbose=True)
if __name__ == "__main__":
    # main()

    test_answer()





