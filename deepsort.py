# I shouldn't sort the structure, only write it sorted.
def deep_sorted(x:any)->str:
    return "".join(str(sorted(i)) for i in x)



if __name__ == '__main__':
    # x=eval(input())
    # print(deep_sorted(x))
    import doctest
    print (doctest.testmod())
