import string as s

def fat(n):
    resultado = 1
    for n in range(1,n+1):
        resultado *= n
    return print(resultado)
    
while True:
    n = input('Fatorial de: ')
    if n != 'ok' and n not in s.ascii_letters:
        n = int(n)
        fat(n)
    elif n == 'ok':
        print('sair')
        break
    elif n in s.ascii_letters:
        print('insira um número')
        continue
    
    
    
  
    
