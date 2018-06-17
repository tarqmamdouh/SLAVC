from keras import Sequential
import numpy as np
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.optimizers import Adam
from collections import deque
import random

class DrivingAgent:
    def __init__(self):
        self.stateSize = (360, 120, 3)
        self.actionSize = 5*5*9
        self.memory = deque(maxlen=5000)
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilonMin = 0.01
        self.epsilonDecay = 0.995
        self.learningRate = 0.001
        self.model = self.buildModel()


    def buildModel(self):
        model = Sequential()

        model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=self.stateSize))
        model.add(Convolution2D(32, 3, 3, activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.actionSize, activation='linear'))

        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learningRate))
        return model

    def saveToMemory(self, state, action, reward, next_state):
        self.memory.append((state, action, reward, next_state))

    def chooseBestNextAction(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.actionSize)

        actionScores = self.model.predict(state)
        return np.argmax(actionScores[0])

    def learnFromPastExperience(self, batchSize):
        currentBatch = random.sample(self.memory, batchSize)

        for state, action, reward, nextState in currentBatch:

            target = reward + (self.gamma * np.amax(self.model.predict(nextState)[0]))

            targetDash = self.model.predict(state)
            targetDash[0][action] = target

            self.model.fit(state, targetDash, epochs=1, verbose=0)

            if self.epsilon > self.epsilonMin:
                self.epsilon *= self.epsilonDecay
