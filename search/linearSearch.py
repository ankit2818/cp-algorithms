def linearSearch(arr, key):
    aLength = len(arr)
    for idx in range(aLength):
        if arr[idx] == key:
            return idx
    return -1


if __name__ == "__main__":
    arr = [4, 2, 5, 3, 6, 1, 2, 3]
    key = 1
    idx = linearSearch(arr, key)
    if idx != -1:
        print(f"Key: {key} found at index: {idx}")
    else:
        print(f"Key: {key} doesn't exist in list")
