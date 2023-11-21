#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
