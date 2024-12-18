lst=[True,[False,[True,[False,[True]]]]]

def inlist(a):
    for i in a:
        if type(i)==set or type(i)==list or type(i)==tuple: 
            inlist(i)
        else:
            if i==True:
                print(i)
          
inlist(lst)
