"""
Calculate sum of integers from 1 to given N (including)

Example:
sum_upto_n(1) == 1
sum_upto_n(2) == 3
sum_upto_n(3) == 6
sum_upto_n(4) == 10

this function can be used in a variety of mathematical and algorithmic contexts,
such as in calculating the nth triangular number, determining the cost for certain operations in algorithms, etc

 t = half n (n+1)

"""

def sum_upto_n(num):
    half_num = num /2
    print(round(half_num))
    ans = half_num * (num + 1)
    print(ans)
    #return N*(N+1)//2  <-- Best solution just use the formula

sum_upto_n(3)

a = 'ab dv'
a.title()
