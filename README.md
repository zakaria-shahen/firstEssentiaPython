### Starter app to use Essentia library with Python


### What is Essentia?

- ML models ready to use for music audio analysis.
- applications include music classification, mood detection, genre detection, etc.

#### Installation

- install pyenv in WSL, or unix environment.

```bash
sudo apt update
sudo apt upgrade
sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git libncursesw5-dev \
xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
curl https://pyenv.run | bash
## there are some additional steps to add pyenv to your shell profile
## follow the instructions after running the above commands
```
- install python 3.11

```bash
pyenv install 3.11
pyenv global 3.11
```

- install dependencies

```bash
pip install -r requirements.txt
```


- run the app

```bash
python3 main.py
```

#### Download models


- just run next command to download the models

```bash
sh download_models.sh
```
- you can visit [Essentia models](https://essentia.upf.edu/models.html) page for more models.
