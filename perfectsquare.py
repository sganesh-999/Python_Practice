def isPerfectSquare(num):
    left = 1
    right = num

    while left < right:
        mid = (left + right) // 2
        if mid * mid == num:
            return True
        
        elif mid * mid < num:
            left = mid + 1
        
        elif mid * mid > num:
            right = mid
    return False

print(isPerfectSquare(49))
