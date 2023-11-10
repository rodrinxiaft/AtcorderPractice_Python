def is_even_or_odd(a,b):
  product_result = a*b
  if product_result%2==0:
    return 'Even'
  else:
    return 'Odd'

print(is_even_or_odd(4,5))
print(is_even_or_odd(3,3))

a, b = map(int, input().split())

product_result = a*b
if product_result%2==0:
    print('Even')
else:
    print('Odd')


