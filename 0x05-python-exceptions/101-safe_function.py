#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        ret = fct(*args)
        return ret
    except Exception as error:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
