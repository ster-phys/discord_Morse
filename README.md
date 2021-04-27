# discord_Morse

This converts the input characters into Morse code and transmits them on the voice channel.

Japanese is supported.

## Steps
1. Clone this repository.
1. Add `DISCORD_TOKEN` of Discord bot to the `.env` file.
1. Add the [Necessary libraries](#necessary-libraries).
1. Execute `$ python main.py`.
1. (Recommended) Delete the `userID.wav` file from the tmp file.

## Usage
### `?morse join`
Connects to the voice channel to which the executor is connected.

### `?morse leave`
Leave the voice channel.

### `?morse send something-you-send`
By placing a text in `something-you-send`, the string is converted into Morse code and played to the voice channel.
Please pay attention to the volume.

## Necessary libraries
### `$ pip install`
```
discord.py[voice]
python-dotenv
pykakasi
synthesizer
pydub
```

### `$ pip freeze`
```
aiohttp==3.7.4.post0
async-timeout==3.0.1
attrs==20.3.0
cffi==1.14.5
chardet==4.0.0
dill==0.3.3
discord.py==1.7.1
enum34==1.1.10
idna==3.1
klepto==0.2.0
multidict==5.1.0
numpy==1.20.2
pkg-resources==0.0.0
pox==0.2.9
pycparser==2.20
pydub==0.25.1
pykakasi==2.0.6
PyNaCl==1.4.0
python-dotenv==0.17.0
scipy==1.6.3
six==1.15.0
synthesizer==0.2.0
typing-extensions==3.7.4.3
yarl==1.6.3
```
