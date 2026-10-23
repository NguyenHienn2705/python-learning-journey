try:
    n = int(input())
    nums = list(map(int, input().split()))

    print(max(nums))
except:
    print(0)