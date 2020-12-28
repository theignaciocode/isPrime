def isPrime(number: int) -> bool:
    for numberTemp in range(2, int(number**(1/2))+1):
        if number % numberTemp == 0:
            return False
    return True


print(isPrime(5))   #True
print(isPrime(20))  #False 

# developer: theIGNACIOcode
