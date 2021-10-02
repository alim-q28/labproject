 def printParenthesis(b, x, y ):
    if x == y:
        print(chr(65 + x), end = "") #when at diagonals just print the matrix name
        return 0;
    else:
        print("(", end = "") #opening parenthesis
        printParenthesis(b, b[x][y] - 1, y) # evaluating between y to k
        printParenthesis(b, x, b[x][y])   # evaluating between k+1 to x combinning it we get y to x
        print (")", end = "" ) # closing paranthesis
def MatrixChainOrder(p, n):
    m = [[0 for s in range(n)] for s in range(n)]
    for l in range(2, n+1):
        for y in range(n-l+ 1):
            y + l-1 
            m[y][x] = int('Inf')

printParenthesis(b,n-1,0)
print("\nThe minimum cost of multiplying matrices: ",b[0][n-1])
arr = [int(x) for y in input().split()]
n = len(arr)-1
b = MatrixChainOrder(arr, n)
print("The parenthesis will be like: ",end="")

#imtiaj
