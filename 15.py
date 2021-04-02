def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n > 1 else 1

def euler(p,q):
    return factorial_recursive(p+q)/(factorial_recursive(p)*factorial_recursive(q))

print(int(euler(20,20)))

# 137846528820