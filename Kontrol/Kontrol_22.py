def gcd(a, b):
    while b !=0:
        a, b = b, a % b
    return a

a = 77164189341682084692124351766096496451364840671846455244761
b = 46668734283684548617206823665104829826096872771679324943689

print ( 'НОД =', gcd(a, b))