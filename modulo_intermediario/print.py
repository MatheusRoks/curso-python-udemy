import pprint

def p_print(*args):
    pprint.pprint(args, sort_dicts=False, width=40)