from collections import defaultdict

def defaultDICT():
    """
    默认字典的用法
    """
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)

    d2 = defaultdict(set)
    d2['a'].add(1)
    d2['a'].add(2)
    d2['b'].add(4)

    

    print(f"{d=},{d2=}")
