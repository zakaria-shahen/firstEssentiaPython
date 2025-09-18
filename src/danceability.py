from essentia.standard import MonoLoader, TensorflowPredictMusiCNN, TensorflowPredict2D
import numpy as np

# see: https://acousticbrainz.org/datasets/accuracy

audio = MonoLoader(filename="../audio/stay_886449400515.aac", sampleRate=16000, resampleQuality=4)()
embedding_model = TensorflowPredictMusiCNN(graphFilename="../model/msd-musicnn-1.pb", output="model/dense/BiasAdd")
embeddings = embedding_model(audio)

model = TensorflowPredict2D(graphFilename="../model/danceability-msd-musicnn-1.pb", output="model/Softmax")
predictions = model(embeddings)

mean_prediction = np.mean(predictions, axis=0)

# maybe can use median instead of mean for delete outliers
# mean_prediction = np.median(predictions, axis=0) 

# Get the percentage for the positive class (class 1)
danceability_percent = mean_prediction[1] * 100

print(f"Danceability: {danceability_percent:.2f}%")
