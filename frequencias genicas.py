n = 1
s = 0.33
p = 0.00001 #frequencia gene melânico em 1848 
q = 1 - p 
while n < 50:
  n = n + 1
  plinha = p / (1 - s*q**2)
  p = plinha 
  q = 1 - plinha
  print(f'{p: .2f}  :   {q: .2f}')
