
answer = 0

n = 0
while n < 1000:
    mod3 = n % 3
    mod5 = n % 5
    if mod3 == 0 and mod5 == 0:
        answer += n
    elif mod3 == 0:
        answer += n
    elif mod5 == 0:
        answer += n
    n += 1
print answer

