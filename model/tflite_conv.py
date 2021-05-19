import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, TimeDistributed, Dense, RepeatVector, Activation, Bidirectional, Concatenate
from tensorflow.keras.optimizers import RMSprop

embedding_size = 300
max_len = 40
vocab_size = 8256

image_model = Sequential([
        Dense(embedding_size, input_shape=(2048,), activation='relu'),
        RepeatVector(max_len)
    ])

caption_model = Sequential([
        Embedding(vocab_size, embedding_size, input_length=max_len),
        LSTM(256, return_sequences=True),
        TimeDistributed(Dense(300))
    ])

final_model = Sequential([
        Concatenate()([image_model.output, caption_model.output]),
        Bidirectional(LSTM(256, return_sequences=False)),
        Dense(vocab_size),
        Activation('softmax')
    ])

final_model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])

final_model.summary()

final_model.load_weights('time_inceptionV3_1.5987_loss.h5')

# Convert the model
converter = tf.lite.TFLiteConverter.from_keras_model('time_inceptionV3_1.5987_loss.h5') # path to the SavedModel directory
tflite_model = converter.convert()

# Save the model.
with open('model.tflite', 'wb') as f:
  f.write(tflite_model)