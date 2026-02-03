from cdc import calc

def test_T_PUSH_REAL1():
    args = ['push','5','pop']
    assert calc(args) == "5 + j0"

def test_T_PUSH_CPLX1():
    args = ["push","-2.5", "-", "j0.25","pop"]
    assert calc(args) == "-2.5 - j0.25"

def test_T_PUSH_CPLX2():
    args = ["push","3", "+", "j", "4","pop"]
    assert calc(args) == "3 + j4"

def test_T_POP_ERR1():
    args = ["pop"]
    try:
        calc(args)
        assert False
    except Exception as e:
        assert str(e) == "Error: Stack underflow"

def test_ADD_REAL1():
    args = ["push", "2", "push", "5", "add", "pop"]
    assert calc(args) == "7 + j0"

def test_ADD_CPLX1():
    args = ["push", "3", "+", "j4", "push", "1", "-", "j2", "add", "pop"]
    assert calc(args) == "4 + j2"

def test_ADD_ERROR():
    args = ["push", "2", "add"]
    try:
        calc(args)
        assert False
    except Exception as e:
        assert str(e) == "Error: Stack underflow"

def test_SUB_REAL1():
    args = ["push", "5", "push", "2", "sub", "pop"]
    assert calc(args) == "3 + j0"

def test_SUB_CPLX1():
    args = ["push", "3", "+", "j4", "push", "1", "-", "j2", "sub", "pop"]
    assert calc(args) == "2 + j6"

def test_SUB_ERROR():
    args = ['sub']
    try:
        calc(args)
        assert False
    except Exception as e:
        assert str(e) == "Error: Stack underflow"

def test_MUL_REAL1():
    args = ["push", "3", "push", "-2", "mul", "pop"]
    assert calc(args) == "-6 + j0"

def test_MUL_CPLX1():
    args = ["push", "1", "+", "j2", "push", "3", "-", "j4", "mul", "pop"]
    assert calc(args) == "11 + j2"

def test_MUL_ERROR():
    args = ['mul']
    try:
        calc(args)
        assert False
    except Exception as e:
        assert str(e) == "Error: Stack underflow"

def test_DIV_REAL():
    args = ["push", "8", "push", "2", "div", "pop"]
    assert calc(args) == "4 + j0"

def test_DIV_CPLX1():
    args = ["push", "4", "+", "j2", "push", "1", "+", "j1", "div", "pop"]
    assert calc(args) == "3 - j1"

def test_DIV_ZERO_DENOM():
    args = ["push", "1", "push", "0", "div"]
    try:
        calc(args)
        assert False
    except Exception as e:
        assert str(e) == "Error: Division by zero"
def test_DIV_ZERO_DENOM_CPLX():
    args = ["push", "1", "+", "j0", "push", "0", "+", "j0", "div"]
    try:
        calc(args)
        assert False
    except Exception as e:
        assert str(e) == "Error: Division by zero"

def test_DEL_REAL():
    args = ["push", "1", "push", "2", "delete", "pop"]
    assert calc(args) == "1 + j0"

def test_DEL_CPLX():
    args = ["push", "1", "+", "j1", "push", "2", "+", "j3", "delete", "pop"]
    assert calc(args) == "1 + j1"

def test_DEL_ERROR():
    args = ["delete"]
    try:
        calc(args)
        assert False
    except Exception as e:
        assert str(e) == "Error: Stack underflow"