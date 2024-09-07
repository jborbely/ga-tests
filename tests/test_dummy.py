from ctypes import *

def test_roszman1():

    lib = CDLL('Roszman1_x64.so')

    buffer = create_string_buffer(256)
    lib.GetFunctionName(buffer)
    assert buffer.value == "f1: Roszman1 f1=a1-a2*x-arctan(a3/(x-a4))/pi"

    num = c_int()
    lib.GetNumParameters(byref(num))
    assert num.value == 3

    lib.GetNumVariables(byref(num))
    assert num.value == 2
