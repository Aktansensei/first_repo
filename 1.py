def new_function():
    print('changed by lab2')
    print('one more changed by lab2')


def fibonacci1(n):
    res = [0,1]
    if n >= 2:
        for _ in range(n-1):
            res.append(res[-1] + res[-2])
    return res[n]

def fibonacci2(n):
    if n==0 or n==1:
        return n
    return fibonacci2(n-1) + fibonacci2(n-2)

print('fibonacci')
print(fibonacci1(10))
print(fibonacci2(10))

def matmul(A,B):
    if len(A[0]) == len(B):
        C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for a_row in range(len(A)):
            for b_row in range(len(B)):
                for b_col in range(len(B[b_row])):
                    C[a_row][b_col] += A[a_row][b_row] * B[b_row][b_col]
        return C
    return -1

A = [[1,2], [3,4], [5,6]]
B = [[7,8,9], [10,11,12]]
print('matrix mult')
print(matmul(A, B))

def shiftedMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    arr = [matrix[i][j] for i in range(rows) for j in range(cols)]

    arr = [arr[-1]] + arr[:-1]

    return [arr[i*cols:(i+1)*cols] for i in range(rows)]

C = [[1,2,3], [4,5,6], [7,8,9]]
print(shiftedMatrix(C))

def isSorted(arr, index=0):
    if len(arr) <= 1 or index == len(arr) - 1:
        return True
    if arr[index] > arr[index+1]:
        return False
    return isSorted(arr, index+1)

arr1 = [0,1,3,5,10,12,15]
arr2 = [0,1,3,5,12,10,12,15]
print('sorted True')
print(isSorted(arr1))
print('sorted False')
print(isSorted(arr2))

def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

print('gcd')
print(gcd(225, 125))

def areThereDuplicates(arr):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 0
        else:
            return True
    return False

print('duplicates')
print(areThereDuplicates([1,2,3,4,5,6,7]))
print(areThereDuplicates([1,2,3,4,5,6,3]))

def moveZeros(nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0
    return nums

nums = [0,1,4,0,3,0,1]
print(moveZeros(nums))

class UserStorage:
    def __init__(self, prime):
        self.prime = prime
        self.users = [[] for _ in range(self.prime)]

    def hash_function(self, username):
        num = 0
        for i in username:
            num = (num ^ ord(i)) << 5 + ord(i)
        return num % self.prime
    
    def add_user(self, username, password):
        index = self.hash_function(username)
        self.users[index].append((username, password))

    def get_password(self, username):
        index = self.hash_function(username)
        for i in self.users[index]:
            if i[0] == username:
                return i[1]
            
storage = UserStorage(1000)
storage.add_user("Bars", "4444")
storage.add_user("Aktan", "1111")
storage.add_user("Bars", "2222")
storage.add_user("Emil", "3333")
print("Emil", storage.get_password("Emil"))
print("Aktan", storage.get_password("Aktan"))
print("Bars", storage.get_password("Bars"))
