import json
import numpy as np
from essentia import Pool
from essentia.standard import MonoLoader, TensorflowPredictMAEST, TensorflowPredict

audio = MonoLoader(filename="../audio/stay_886449400515.aac", sampleRate=16000, resampleQuality=4)()
embedding_model = TensorflowPredictMAEST(graphFilename="../model/discogs-maest-30s-pw-519l-2.pb", output="PartitionedCall/Identity_12")
embeddings = embedding_model(audio)

pool = Pool()
pool.set("embeddings", embeddings)

model = TensorflowPredict(graphFilename="../model/genre_discogs519-discogs-maest-30s-pw-519l-1.pb", inputs=["embeddings"], outputs=["PartitionedCall/Identity_1"])
predictions = model(pool)["PartitionedCall/Identity_1"]

# TODO: how to map predictions to labels?

# The shape of the predictions matrix is [n_patches, n_labels]
# Take advantage of NumPy to average them over the time axis
averaged_predictions = np.mean(predictions, axis=0)

# Sort the predictions and get the top N
top_n = 3

with open('../model/genre_discogs519-discogs-maest-30s-pw-519l-1.json', 'r') as json_file:
    metadata = json.load(json_file)
    msd_labels = metadata['classes']
    for i, l in enumerate(averaged_predictions.argsort()[-top_n:][::-1], 1):
        print(l)
        print('{}: {}'.format(i, msd_labels[l]))