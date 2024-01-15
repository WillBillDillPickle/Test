# 1 1 1 0 0 1 1 1 0 0 1 1 1 0 0 1 1 1 1 0 0 0 1 1 


# Using readlines()
# file1 = open('cow_infection.in', 'r')
# Lines = file1.readlines()
# all_cow = Lines[0].split()

all_cow = [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1,]
 
print(all_cow)
N = len(all_cow) # Number of total cows = N
print(N)




A = [0]*N
B = [0]*N
count = 0

#print(all_cow[0],all_cow[-1])

# left end
i = 0
while all_cow[i] == 1:
    A[0] += 1
    i += 1
    print(i,A[0])
B[0] = A[0]

#right end
i = -1
while all_cow[i] == 1:
    A[1] += 1
    i -= 1
    print(i,A[1])
B[1] = A[1]

# in the middle
m = 2
tag_iland = 0
for i in range(A[0], N-A[1]):
#    print(i)
    if all_cow[i] == 1:
        tag_iland = 1
        A[m] += 1
    if all_cow[i] == 0 and tag_iland == 1:
        tag_iland = 0
        B[m] = (A[m]+1)//2
        m += 1
    
#    print(all_cow[i])
print(m,'\n',A,'\n',B)

N_min = 10000
Sum_A = 0   #  total infected cows
for i in range(m):
    Sum_A += A[i]
    if B[i] < N_min:
        N_min = B[i]     # minimun days infection started

print('N_min, Sum_A = ',N_min, Sum_A)
N_total = 0

for i in range(m):
    print(A[i]%(2*N_min - 1), N_min, A[i], 2*N_min -  1)
    if A[i]%(2*N_min - 1) == 0:
        N_total += A[i] // (2*N_min - 1)
        print("i = ", i, A[i] // (2*N_min - 1), A[i])
    else:
        N_total += A[i] // (2*N_min - 1) + 1
        print("else i = ", i, A[i] // (2*N_min - 1))
print(N_total)
print(2%3)
