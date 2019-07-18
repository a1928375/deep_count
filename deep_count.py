def is_list(p):
    return isinstance(p, list)

def deep_count(p):
    sum=0
    for i in p:
        if not is_list(i):
            sum=sum+1
        else:
            if i==[]:
                sum=sum+1
            else:
                sum=sum+1+deep_count(i)
    return sum

print deep_count([1, 2, 3])
print deep_count([1, [], 3]) 
print deep_count([1, [1, 2, [3, 4]]])
print deep_count([[[[[[[[1, 2, 3]]]]]]]])
