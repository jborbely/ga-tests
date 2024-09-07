import math

from ctypes import *

import pytest

def test_roszman1():

    lib = CDLL('./Roszman1_x64.so')

    buffer = create_string_buffer(256)
    lib.GetFunctionName(buffer)
    assert buffer.value.decode() == "f1: Roszman1 f1=a1-a2*x-arctan(a3/(x-a4))/pi"

    num = c_int()
    lib.GetNumParameters(byref(num))
    assert num.value == 4

    lib.GetNumVariables(byref(num))
    assert num.value == 1

    x = -4868.68
    a1, a2, a3, a4 = (0.2, -6e-6, 1.2e3, -1.8e2)
    x_c = c_double(x)
    a = (c_double * 4)(a1, a2, a3, a4)
    y = c_double()
    lib.GetFunctionValue(byref(x_c), byref(a), byref(y))
    assert y.value == a1-a2*x-math.arctan(a3/(x-a4))/math.pi
