from os import listdir
from pickle import dump
import tensorflow as tf 
import tensorflow.keras.applications.inception_v3 as inception_v3
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Model

def extract_features(directory):
	incep_model = inception_v3.InceptionV3(weights='imagenet')
	model = Model(inputs=incep_model.inputs, outputs=incep_model.layers[-2].output)
	print(model.summary())
	features = dict()
	for name in listdir(directory):
		filename = directory + '/' + name
		image = load_img(filename, target_size=(299, 299))
		image = img_to_array(image)
		image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
		image = preprocess_input(image)
		feature = model.predict(image, verbose=0)
		image_id = name.split('.')[0]
		features[image_id] = feature
		print('>%s' % name)
	return features

directory = '/mnt/f/Projects/OcuHelp/data/Images/'
features = extract_features(directory)
print('Extracted Features: %d' % len(features))
dump(features, open('/mnt/f/Projects/OcuHelp/data/img_features.pkl', 'wb'))