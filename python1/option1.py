for i in range(30, 60):
    if True in [i % j == 0 for j in range(2, i)]:
        print(i)
    else:
        print('Prime')