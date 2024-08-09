"""def fib1(n,memo={}):
    if n in memo: return memo[n]
    if n<=2: return 1
    memo[n]=fib1(n-1,memo)+fib1(n-2,memo)
    return memo[n]

print(fib1(50))"""

"""def fib(n):
    if n<=2: return 1
    return fib(n-1)+fib(n-2)

print(fib(50))"""


"""fib works on traditional recursive approach 
whereas fib1 workson dynamic programming of memorisation 
each and every value are added to set object called suring function call
the time complexity of fib is O(2^n) and fib1 is way less than O(2^n)"""

"""def fib2(n,memo={}):
    if n in memo: return memo[n]
    if n<2:
        return 1
    memo[n]=fib2(n-1)+fib2(n-2)
    return memo[n]

n=100
for i in range(n):
    print(fib2(i))"""

"""this fib2 function displays all the numbers  from 0 to speciied n value
with good time complexity"""

