def complex_num_as_str_is_valid(num_as_str):
    r = True
    try:
        complex(num_as_str.lower().replace(' ', '').replace('i', 'j'))
    except ValueError:
        r = False
    return r

def complex_num_as_str_to_complex(num_as_str):
    try:
        num_as_complex = complex(num_as_str.lower().replace(' ', '').replace('i', 'j'))
    except ValueError:
        num_as_complex = None
    return num_as_complex


def complex_num_sum(a, b):
    try:
        r = a + b
    except:
        r = None
    return r

def complex_num_sub(a, b):
    try:
        r = a - b
    except:
        r = None
    return r

def complex_num_mult(a, b):
    try:
        r = a * b
    except:
        r = None
    return r

def complex_num_div(a, b):
    try:
        r = a / b
    except:
        r = None
    return r


