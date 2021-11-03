while True:
    values=str(input())
    if values == 'done' or values=='Done' or values=='d':
        break
    print(values[::-1])

