from pydub import AudioSegment
import os
from tqdm import tqdm
def audio_splitter(base_path, recorder, audio_files):
    desired_split = 4
    for m in tqdm(range(len(audio_files))):
        filename = audio_files[m]
        audio_file = AudioSegment.from_wav(os.path.join(base_path,recorder,filename))
        audio_length = audio_file.duration_seconds
        PATH_TO_SPLITTED_AUDIO = os.path.join(base_path,recorder,"audio_segments")
        k = 0
        for i in tqdm(range(0,int(audio_length), desired_split)):
            audio_file[i*1000:(i+4)*1000].export(os.path.join(PATH_TO_SPLITTED_AUDIO,f"{m}_{k}.wav"),format="wav")
            k+=1  

def main():
    BASE_PATH = "/media/aneesh/USB1000/Zurich_Urban_Sounds"
    RECORDER = "TASCAM_RECORDER"
    audio_files = sorted([f for f in os.listdir(os.path.join(BASE_PATH,RECORDER)) if ".wav" in f])
    audio_splitter(BASE_PATH, RECORDER, audio_files)

if __name__== '__main__':
    main()
    