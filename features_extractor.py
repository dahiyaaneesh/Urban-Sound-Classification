from tqdm import tqdm
import os
import librosa
import numpy as np
import argparse
from multiprocessing import Pool
from p_tqdm import p_map
import pickle
BASE_PATH = "/media/aneesh/USB1000/Zurich_Urban_Sounds"
RECORDER = "TASCAM_RECORDER"
SEGMENT_DIR = "audio_segments"
def save_features(filename, base_path=BASE_PATH, recorder=RECORDER, segment_dir=SEGMENT_DIR):
    y, sr = librosa.load(os.path.join(base_path, recorder, segment_dir, filename))
    mfccs = np.mean(librosa.feature.mfcc(y, sr, n_mfcc=36).T, axis=0)
    melspectrogram = np.mean(
        librosa.feature.melspectrogram(y=y, sr=sr, n_mels=36, fmax=8000).T, axis=0
    )
    chroma_stft = np.mean(
        librosa.feature.chroma_stft(y=y, sr=sr, n_chroma=36).T, axis=0
    )
    chroma_cq = np.mean(librosa.feature.chroma_cqt(y=y, sr=sr, n_chroma=36).T, axis=0)
    chroma_cens = np.mean(
        librosa.feature.chroma_cens(y=y, sr=sr, n_chroma=36).T, axis=0
    )
    melspectrogram.shape, chroma_stft.shape, chroma_cq.shape, chroma_cens.shape, mfccs.shape
    features = np.reshape(
        np.vstack((mfccs, melspectrogram, chroma_stft, chroma_cq, chroma_cens)), (36, 5,1)
    )
    np.save(os.path.join(base_path, recorder,"features",filename[:-4] ), features)
    # return features


def main():

    filenames = sorted(
        [
            f
            for f in os.listdir(os.path.join(BASE_PATH, RECORDER, SEGMENT_DIR))
            if ".wav" in f
        ]
    )
    p_map(save_features,filenames[100:900] ,num_cpus=6)

main()

