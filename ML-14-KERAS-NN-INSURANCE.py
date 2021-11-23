from sklearn.model_selection import train_test_split
import pandas as pd
import keras

df = pd.read_csv('Datasets/dataset6.csv')
#print(df.head())

x_train, x_test, y_train, y_test = train_test_split(df[['age', 'affordibility']],df.bought_insurance, test_size=0.2)

x_train_scaled = x_train.copy()
x_train_scaled['age'] = x_train_scaled['age'] / 100 # scaling ages

x_test_scaled = x_test.copy()
x_test_scaled = x_test_scaled['age'] / 100

#Build simple neural network

model = keras.Sequential([
                                                                            # Weights are 1                 # Bias 0
    keras.layers.Dense(1, input_shape=(2,), activation='sigmoid', kernel_initializer='ones', bias_initializer='zeros')
])
# compile the network with x params
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the network
model.fit(x_train_scaled, y_train, epochs=5000)
#model.evaluate(x_test_scaled, y_test) # doesnt work?