"""Traditional approach of the grd traveller
Problem statement
1.person starts at starting position 0,0 of the matrix
2.Can travel only in downward and right direction
3.destination is m,n cell of the matrix"""

'''Traditional approach'''


def GridTraveller(m, n):
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    return GridTraveller(m-1,n)+GridTraveller(m,n-1)

print(GridTraveller(1,1))
print(GridTraveller(0,1))
print(GridTraveller(1,0))
print(GridTraveller(58,58))