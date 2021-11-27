from pydub import AudioSegment
import os
import json


RAW_DATA = '20200416/20200416'
CUT_DATA = 'audio_1s'


def cut_audio_1s(audio_path, metadata, audio_type):
    age = metadata['a']
    gender = metadata['g']
    id = metadata['id'][:4]

    song = AudioSegment.from_file(audio_path)
    time=int(len(song)/1000)
    for i in range(time):
        extract=song[i*1000:1000*(i+1)]
        save_path = f'audio_1s/{audio_type}_{age}_{gender}_{id}_{i}.wav'
        extract.export(save_path, format="wav")
        print('save to', save_path)


for folder in os.listdir(RAW_DATA):
    for file_name in os.listdir(os.path.join(RAW_DATA, folder)):
        if file_name == 'metadata.json':
            with open(os.path.join(RAW_DATA, folder, file_name), 'r') as f:
                metadata = json.load(f)
    
    for file_name in os.listdir(os.path.join(RAW_DATA, folder)):
        if file_name == 'breathing-deep.wav':
            cut_audio_1s(os.path.join(RAW_DATA, folder, file_name), metadata, 'bd')
        if file_name == 'breathing-shallow.wav':
            cut_audio_1s(os.path.join(RAW_DATA, folder, file_name), metadata, 'bs')

