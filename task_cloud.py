# Libraries related to the cloud
import requests
from google.cloud import storage

# Libraries for for music and audio analysis
import librosa
from scipy.signal import butter, filtfilt

# Libraries for data collection and transformation
import glob
import pandas as pd
import numpy as np

from tqdm import tqdm

import warnings

warnings.filterwarnings("ignore")

# Download model file from cloud storage bucket
def download_data_file():

    from google.cloud import storage

    # Model Bucket details
    BUCKET_NAME = "BUCKET_NAME"
    PROJECT_ID = "PROJECT_ID"

    # Initialise a client
    client = storage.Client(PROJECT_ID)

    # Create a bucket object for our bucket
    bucket = client.bucket(BUCKET_NAME)

    # Iterate through the files in sounds/samples
    iterator = bucket.list_blobs(
        versions=True,
        prefix="sounds/samples/vi95kMQ65UeU7K1wae12D1GUeXd2/",
        delimiter="/",
    )
    subdirectories = iterator.prefixes
    objects = list(iterator)

    # Download the file to a destination
    folder = "/tmp/"
    for blob in objects:
        name = str(blob.name.lstrip("sounds/samples/vi95kMQ65UeU7K1wae12D1GUeXd2/"))
        blob.download_to_filename(folder + "sample" + name)


def detect_coughs(request):
    request_args = request.args
    download_data_file()
    if request_args and "filename" in request_args:
        x, sr = librosa.load("/tmp/" + str(request_args["filename"]))
    else:
        x, sr = librosa.load("/tmp/sample-1613658921823.m4a")

    # onset detection
    o_env = librosa.onset.onset_strength(x, sr=sr)
    onset_frames = librosa.util.peak_pick(o_env, 3, 3, 3, 3, 0.3, 100)
    peaks = librosa.frames_to_time(onset_frames)

    headers = {"Access-Control-Allow-Origin": "*"}
    return (str(peaks), 200, headers)
