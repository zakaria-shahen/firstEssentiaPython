from essentia.standard import MonoLoader, TensorflowPredictVGGish, TensorflowPredictEffnetDiscogs


def main():
    test()


def test():
    audio = MonoLoader(filename="audio/stay_886449400515.aac", sampleRate=16000, resampleQuality=4)()
    # model = TensorflowPredictVGGish(graphFilename="model/audioset-vggish-3.pb", output="model/vggish/embeddings")
    model = TensorflowPredictEffnetDiscogs(graphFilename="model/discogs-effnet-bs64-1.pb", output="PartitionedCall:1")
    embeddings = model(audio)
    print(embeddings)


if __name__ == "__main__":
    main()

