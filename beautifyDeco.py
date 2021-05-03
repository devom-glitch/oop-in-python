from functools import wraps

def make_post(func):
    """ This is Decorator function"""    
    @wraps(func)
    def wrapper():
        a='+----------+'
        b='|          |'
        c=' Fibonacci  '
        d='\n'
        return a+d+b+d+c+d+b+d+a
    return wrapper

def bold(func):
    ''' Bold Decorator'''
    @wraps(func)
    def wrapper():
        ''' return html bold tags '''
        result = '<b>' + func() + '</b>'
        return result
    return wrapper

def italic(func):
    ''' Italic Decorator'''
    @wraps(func)
    def wrapper():
        ''' return html Italic tags '''
        result = '<i>' + func() + '</i>'
        return result
    return wrapper

# @make_post
@bold
@italic
def pfib():
    """ Print the Fibonacci"""
    return 'Fibonacci'

# args
def argpass(para1,*args):
    print(para1)
    print(*args)

# kwargs
def kargspass(para1,**kargs):
    print(para1)
    print(kargs)
    
# args and kwargs
def akargs(*args, **kwargs):
    print(args)
    print(kwargs)
    
# Decorator with *args and **kwargs

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        #do something befor
        print('inside wrapper')
        result = func(*args,**kwargs)
        # Do something after
        return result
    return wrapper

@decorator
def func():
    ''' implement generic function'''
    pass

if __name__ == '__main__':
    print(pfib())
    argpass(1,2,3,4,5)
    kargspass('email',body='hi learner \n welcome to edusail.',subject='welcome to edusail')
    akargs(1,2,3,message='task number has been assigned')
    func()
    # print(pfib.__name__)
    # print(pfib.__doc__)