import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from pickle import load
 

 # map an integer to a word
def word_for_id(integer, tokenizer):
    return tokenizer.index_word.get(integer)

# generate a description for an image
def generate_desc(model, tokenizer, photo, max_length):
    # seed the generation process
    in_text = 'startseq'
    # iterate over the whole length of the sequence
    for i in range(max_length):
        # integer encode input sequence
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        #print("sequence after tok: ", sequence)
        # pad input
        sequence = pad_sequences([sequence], maxlen=max_length)
        # predict next word
        if i==0:
            photo = np.expand_dims(photo, axis=0)
        #print("photo: ", photo)
        #print("sequence: ", sequence)
        yhat = model.predict([photo, sequence], verbose=0)
        # convert probability to integer
        yhat = np.argmax(yhat)
        # map integer to word
        word = word_for_id(yhat, tokenizer)
        # stop if we cannot map the word
        if word is None:
            break
        # append as input for generating the next word
        in_text += ' ' + word
        # stop if we predict the end of the sequence
        if word == 'endseq':
            break
    return in_text

def image_to_feat_vec(imagePath):
    img1 = image.load_img(imagePath, target_size=(224, 224))
    x = image.img_to_array(img1)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    resnet = tf.keras.models.load_model('/mnt/f/Projects/OcuHelp/backend/resnet50.h5')
    fea_x = resnet.predict(x)
    fea_x1 = np.reshape(fea_x , fea_x.shape[1])
    return fea_x1

def generate_captions(photo_path):
	tokenizer = load(open('/mnt/f/Projects/OcuHelp/backend/tokenizer.pkl', 'rb'))
	max_length = 34
	model = tf.keras.models.load_model('/mnt/f/Projects/OcuHelp/backend/model.h5')
	photo = image_to_feat_vec(photo_path)
	description = generate_desc(model, tokenizer, photo, max_length)
	description = description[9:-6]
	return description

# print(generate_captions("/home/jkt/Downloads/image-captioning-app/backend/IMG-20210502-WA0003 (1).jpg"))
