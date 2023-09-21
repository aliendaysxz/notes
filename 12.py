from random import sample
def embaralha(p):
    p_random = ''
    for num in nums:
        print(p_random + p[num], end='')
    return p_random
        
p = input('palavra:  ').lower()

n = range(len(p))
nums = sample(n, len(p))
print(nums)
print(embaralha(p))



 
