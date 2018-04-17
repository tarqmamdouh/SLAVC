import numpy as np
from alexnet import alexnet
WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 400
MODEL_NAME = 'CarNaiveDrive-{}-{}-{}-epochs-100K-data.model'.format(LR, 'SV',EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

hm_data = 100
for i in range(EPOCHS):
    for i in range(1,hm_data):
        train_data = np.load('Balanced-Data\\Balanced-{}.npy'.format(i*1000))

        train = train_data[:-30]
        test = train_data[-30:]

        X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
        Y = [i[1] for i in train]

        test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
        test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}),
            snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

model.save(MODEL_NAME)