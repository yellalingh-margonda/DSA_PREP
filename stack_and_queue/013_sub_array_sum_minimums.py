def sumSubarrayMins(arr):
    MOD = 10**9 + 7
    n = len(arr)

    # Previous Less Element (PLE)
    prev_less = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        prev_less[i] = stack[-1] if stack else -1
        stack.append(i)

    # Next Less Element (NLE)
    next_less = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        next_less[i] = stack[-1] if stack else n
        stack.append(i)

    # Calculate result
    result = 0
    for i in range(n):
        left = i - prev_less[i]
        right = next_less[i] - i
        result = (result + arr[i] * left * right) % MOD

    return result
array=[2,2]
print(sumSubarrayMins(array))

