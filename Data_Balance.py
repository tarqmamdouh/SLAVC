import numpy as np
from random import shuffle

def Balance(offset):
    train_data = np.load('Naive-Data\\Coordinates' + '-' + str(offset) + '.npy')

    # df = pd.DataFrame(train_data)
    # print(df.head())
    # print(Counter(df[1].apply(str)))

    lefts = []
    rights = []
    forwards = []

    shuffle(train_data)

    for data in train_data:
        img = data[0]
        choice = data[1]

        if choice == [1,0,0]:
            lefts.append([img,choice])
        elif choice == [0,1,0]:
            forwards.append([img,choice])
        elif choice == [0,0,1]:
            rights.append([img,choice])
        else:
            print('no matches')


    forwards = forwards[:len(lefts)][:len(rights)]
    lefts = lefts[:len(forwards)]
    rights = rights[:len(forwards)]

    final_data = forwards + lefts + rights
    shuffle(final_data)

    np.save('Balanced-Data\\Balanced' + '-' + str(offset) + '.npy', final_data)


if __name__ == '__main__':

    i = 1000
    while i <= 100000:
        Balance(i)
        i = i + 1000
