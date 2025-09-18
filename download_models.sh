mkdir -p model
cd model

wget -nc https://essentia.upf.edu/models/feature-extractors/vggish/audioset-vggish-3.pb \
& wget -nc https://essentia.upf.edu/models/feature-extractors/discogs-effnet/discogs-effnet-bs64-1.pb \
& wget -nc https://essentia.upf.edu/models/classification-heads/genre_discogs400/genre_discogs400-discogs-effnet-1.pb \
& wget -nc https://essentia.upf.edu/models/feature-extractors/musicnn/msd-musicnn-1.pb \
& wget -nc https://essentia.upf.edu/models/classification-heads/genre_discogs400/genre_discogs400-discogs-effnet-1.json \
& wget -nc https://essentia.upf.edu/models/classification-heads/genre_discogs519/genre_discogs519-discogs-maest-30s-pw-519l-1.pb \
& wget -nc https://essentia.upf.edu/models/classification-heads/genre_discogs519/genre_discogs519-discogs-maest-30s-pw-519l-1.json \
& wget -nc https://essentia.upf.edu/models/feature-extractors/maest/discogs-maest-30s-pw-519l-2.pb \
& wget -nc https://essentia.upf.edu/models/feature-extractors/maest/discogs-maest-30s-pw-519l-2.pb \
& wget -nc https://essentia.upf.edu/models/feature-extractors/maest/discogs-maest-5s-pw-2.pb \
& wget -nc https://essentia.upf.edu/models/classification-heads/mtg_jamendo_genre/mtg_jamendo_genre-discogs_track_embeddings-effnet-1.pb \
& wget -nc https://essentia.upf.edu/models/classification-heads/mtg_jamendo_genre/mtg_jamendo_genre-discogs_track_embeddings-effnet-1.json \
& wget -nc https://essentia.upf.edu/models/feature-extractors/discogs-effnet/discogs_track_embeddings-effnet-bs64-1.pb \
& wget -nc https://essentia.upf.edu/models/classification-heads/danceability/danceability-msd-musicnn-1.pb \
& wget -nc https://essentia.upf.edu/models/feature-extractors/musicnn/msd-musicnn-1.pb

cd ..
