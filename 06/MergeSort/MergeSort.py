# Code from the lecture

def merge(a, temp, zacatek, stred, konec):
    i,j,k = zacatek, stred + 1, zacatek
    while i <= stred and j <= konec:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1

    while i <= stred:
        temp[k] = a[i]
        i,k = i + 1,k + 1

    while j <= konec:
        temp[k] = a[j]
        j,k = j + 1,k + 1

    print("Merge run:", zacatek, stred, konec)
    print(a[zacatek:konec + 1], a)
    print(temp[zacatek:konec + 1], temp)

    a[zacatek:konec + 1] = temp[zacatek:konec + 1]

def mergeSort(a):
    n = len(a)
    temp = [None] * n
    beh = 1
    while beh < n:
        for zacatek in range(0, n - beh, 2 * beh):
            stred = zacatek + beh - 1
            konec = min(stred + beh, n - 1)
            merge(a, temp, zacatek, stred, konec)
        beh *= 2
    return a

print(mergeSort([3, 5, 12, 2, 1, 60, 44, 13]))

# Problem: how to get rid of a[zacatek:konec+1]= temp[zacatek:konec+1] ?

def merge_without_copy(a, temp, zacatek, stred, konec):
    i,j,k = zacatek, stred + 1, zacatek
    while i <= stred and j <= konec:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1

    while i <= stred:
        temp[k] = a[i]
        i,k = i + 1,k + 1

    while j <= konec:
        temp[k] = a[j]
        j,k = j + 1,k + 1

    print("Merge run without copy:", zacatek, stred, konec)
    print(a[zacatek:konec + 1], a)
    print(temp[zacatek:konec + 1], temp)

def mergeSort_without_copy(a):
    n = len(a)
    temp = [None] * n
    beh = 1
    use_temp = False
    while beh < n:
        for zacatek in range(0, n - beh, 2 * beh):
            stred = zacatek + beh - 1
            konec = min(stred + beh, n - 1)
            merge_without_copy(temp if use_temp else a, a if use_temp else temp, zacatek, stred, konec)
        beh *= 2
        use_temp = not use_temp
    return temp if use_temp else a

print(mergeSort_without_copy([3, 5, 12, 2, 1, 60, 44, 13]))