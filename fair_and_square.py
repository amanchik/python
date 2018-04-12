i = 1


def flip(n,copy):
    if copy:
        return long(str(n) + str(n)[::-1])
    else:
        return long(str(n) + str(n)[:-1][::-1])


def is_palindrome(n):
    s = str(n)
    count = len(s)
    for i in range(0, count/2):
        if s[i] != s[count-i-1]:
            return False
    return True


def flip_with_two(n):
    return long(str(n) + '2' + str(n)[::-1])


count = 0
while i < 2**10:
    number = long(bin(i)[2:])
    flipped = flip(number,False)
    if is_palindrome(flipped*flipped) and str(flipped).count('1')==9:
        print flipped, len(str(flipped)), str(flipped).count('1')
        count = count + 1
    i = i + 1
print count
