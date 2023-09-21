n = 0
nums = []
while n != -1:
    n = input('n:  ')
    nums.append(int(n))
    if n == '-1':
        nums.pop(-1)
        break

print('quantidade de elementos: {}'.format(len(nums)))
print('ordem inversa: {}'.format(sorted(nums, reverse=True)))
print('soma: {}'.format(sum(nums)))
media = sum(nums)/len(nums)
print('média: {: .2f}'.format(media))

acima = 0
abaixo = 0
for x in nums:
    if x > media:
        acima+=1
    elif x < media:
        abaixo+=1

print('acima da média: {}'.format(acima))
print('abaixo da média: {}'.format(abaixo))
print('mensagem')

    
