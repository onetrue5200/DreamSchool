def count_subsequences(a, b):
    i, count = 0, 0
    while i < len(b):
        j, k = 0, i
        while j < len(a):
            if k < len(b) and a[j] == b[k]:
                k += 1
            j += 1
        if k == i:
            return -1
        count += 1
        i = k
    return count

def main():
    source = input()
    target = input()
    print(count_subsequences(source, target))

if __name__ == "__main__":
    main()
