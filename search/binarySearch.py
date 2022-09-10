def binarySearch(arr, key):
    aLength = len(arr)
    arr.sort()
    print(arr)
    low = 0
    high = aLength
    while low < high:
        medium = (low + high) // 2
        if arr[medium] == key:
            return medium
        elif arr[medium] < key:
            low = medium
        else:
            high = medium
    return -1


if __name__ == "__main__":
    arr = [4, 2, 5, 3, 6, 1, 2, 3]
    key = 5
    idx = binarySearch(arr, key)
    if idx != -1:
        print(f"Key: {key} found at index: {idx}")
    else:
        print(f"Key: {key} doesn't exist in list")
