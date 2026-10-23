try:
    n = int(input())
    nums = list(map(int, input().split()))

    chan = 0
    le = 0

    for x in nums:
        if x % 2 == 0:
            chan += 1
        else:
            le += 1
    print(f"Chẵn: {chan}, Lẻ: {le}")
except:
    print(f"Chẵn: 0, Lẻ: 0")