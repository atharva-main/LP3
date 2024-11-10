def non_recursive_fibonacci(n):
    num1, num2 = 0, 1
    for _ in range(n):
        print(num1, end=" ")
        num1, num2 = num2, num1 + num2


def recursive_fibonacci(n):
    # Function 
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Main function 
if __name__ == "__main__":
    N = 10
    print("This is output from recursive fibonacci algorithm: ")
    for i in range(N):
        print(recursive_fibonacci(i), end=" ")

    print("\nThis is output from non recursive fibonacci algorithm: ")
    non_recursive_fibonacci(N)
