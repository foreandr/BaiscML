import keras
(X_train, y_train) , (X_test, y_test) = keras.datasets.mnist.load_data()
#len(X_train)
#len(X_test)
#X_train[0].shape
#X_train[0]

#plt.matshow(X_train[0])
#plt.show()

X_train = X_train / 255 # SOMEHTING TO DO WITH COLORS # cHANGES to between0 and 1
X_test = X_test / 255

X_train_flattened = X_train.reshape(len(X_train), 28*28)
X_test_flattened = X_test.reshape(len(X_test), 28*28)

#X_train_flattened.shape
#X_train_flattened[0]

model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train_flattened, y_train, epochs=5)

model.evaluate(X_test_flattened, y_test)
model.predict(X_test_flattened)