def count_inversions(lst):
    return merge_count_inversion(lst)

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count

def main():
    cases = int(input().rstrip())
    buffer = input()
    for _ in range(cases):
        count = 0
        data =[]
        buffer = input().rstrip()
        while buffer != "":
            data.append(int(buffer))
            buffer = input()
        data = data[1:]
        
        print(count_inversions(data))

#main()
print(count_inversions([9,8,0,1,2,4,5,6,10,7]))