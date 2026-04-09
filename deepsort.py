# it's just that if I'd try string the input within the recursion it would sort everything in alephbeitic order. I think.
def deep_sorted(x:any)->str:
    return str(deep_sorted_help(x))

def deep_sorted_help(x:any)->any:
    try:
        len(x)
    except TypeError:
        return
    for i in x:
        deep_sorted(i)
    return x.sort()



if __name__ == '__main__':
    # x=eval(input())
    # print(deep_sorted(x))
    import doctest
    print (doctest.testmod())
