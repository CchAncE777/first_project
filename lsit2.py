l = list(range(0, 10_000_000))
isk = 9_246_236
iskomoe = 3
index = 0
jump = 1
is_found = False

for i  in range(0, len(l), jump):
    jump *= 2
    if iskomoe < l[i]:
        start = i - jump 
        end =  i
        while is_found is False:
            mid = (end - (start)) // 2
            if mid == iskomoe:
                index = mid
                is_found = True
            elif l[mid] < iskomoe:
                end = mid
            else:
                start = mid
                break
    if is_found:
        break

start = i - jump 
end =  i
while is_found is False:
    mid = (end - (start)) // 2
    if mid == iskomoe:
        index = mid
        is_found = True
    elif l[mid] < iskomoe:
        end = mid
    else:
        start = mid
if is_found:
    print(index)
else:
    print("Not found")
            