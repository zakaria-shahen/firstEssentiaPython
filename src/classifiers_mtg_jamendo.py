from essentia.standard import MonoLoader, TensorflowPredictEffnetDiscogs, TensorflowPredict2D
import numpy as np
import json 

audio = MonoLoader(filename="../audio/stay_886449400515.aac", sampleRate=16000, resampleQuality=4)()
embedding_model = TensorflowPredictEffnetDiscogs(graphFilename="../model/discogs_track_embeddings-effnet-bs64-1.pb", output="PartitionedCall:1")

embeddings = embedding_model(audio)

model = TensorflowPredict2D(graphFilename="../model/mtg_jamendo_genre-discogs_track_embeddings-effnet-1.pb")

predictions = model(embeddings)


# The shape of the predictions matrix is [n_patches, n_labels]
# Take advantage of NumPy to average them over the time axis
averaged_predictions = np.mean(predictions, axis=0)

# Sort the predictions and get the top N
top_n = 3

with open('../model/mtg_jamendo_genre-discogs_track_embeddings-effnet-1.json', 'r') as json_file:
    metadata = json.load(json_file)
    msd_labels = metadata['classes']
    for i, l in enumerate(averaged_predictions.argsort()[-top_n:][::-1], 1):
        print('{}: {}'.format(i, msd_labels[l]))