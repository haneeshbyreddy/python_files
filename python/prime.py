'''def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes_in_range(rangeLeft, rangeRight):
    total_sum = 0
    for number in range(rangeLeft, rangeRight + 1):
        if is_prime(number):
            total_sum += number
    return total_sum

# Example usage:
rangeLeft = int(input("Enter the minimum boundary value (rangeLeft): "))
rangeRight = int(input("Enter the maximum boundary value (rangeRight): "))
print("Sum of all prime numbers in the range:", sum_of_primes_in_range(rangeLeft, rangeRight))


def maxEnergySum(numOfChem, energies):
    max_product = float('-inf')
    max_sum = 0
    
    for i in range(numOfChem):
        for j in range(i + 1, numOfChem):
            product = energies[i] * energies[j]
            if product > max_product:
                max_product = product
                max_sum = energies[i] + energies[j]
    
    return max_sum

    # Read input from user or standard input
numOfChem = int(input())
energies = list(map(int, input().split()))
    
result = maxEnergySum(numOfChem, energies)
print(result)
'''
def find_two_max_elements(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")
    
    first_max = second_max = float('-inf')
    
    for num in arr:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num
            
    if second_max == float('-inf'):
        raise ValueError("No second maximum element found.")
    
    return first_max,second_max

array = list(map(int, input().split()))

first_max, second_max = find_two_max_elements(array)
sum=first_max+second_max
print(sum)
