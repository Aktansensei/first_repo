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

def matmul(A,B):
    if len(A[0]) == len(B):
        C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for a_row in range(len(A)):
            for b_row in range(len(B)):
                for b_col in range(len(B[b_row])):
                    C[a_row][b_col] += A[a_row][b_row] * B[b_row][b_col]
        return C
    return -1

def shiftedMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    arr = [matrix[i][j] for i in range(rows) for j in range(cols)]

    arr = [arr[-1]] + arr[:-1]

    return [arr[i*cols:(i+1)*cols] for i in range(rows)]

def isSorted(arr, index=0):
    if len(arr) <= 1 or index == len(arr) - 1:
        return True
    if arr[index] > arr[index+1]:
        return False
    return isSorted(arr, index+1)

def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

def areThereDuplicates(arr):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 0
        else:
            return True
    return False

def moveZeros(nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1
    for i in range(non_zero_index, len(nums)):
        nums[i] = 0
    return nums

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