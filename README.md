# Instructions

Do not spend more than 1-2 hours on any task.

## Task 1

#### Fork this repo  

#### Read the instructions in `task.py`

#### Modify the `detect_coughs` function
  - For this event detection task, I use the library called Librosa, a python package for music and audio processing.
  - librosa.load loads an audio file into a audio array
  - butter_highpass function filters low-frequency noise using a high-pass filter
  - librosa.util.peak_pick uses a flexible heuristic to pick peaks in a signal.
  - finally, I return these peaks as detected coughs
  - I tweak the parameters of peak_pick to get an optimal precision/recall score

#### Libraries used:
  - pandas==1.1.3
  - scipy==1.5.2
  - numpy==1.19.2
  - tqdm==4.50.2
  - librosa==0.8.0


## Task 2

#### Build a simple cloud function to deploy `detect_coughs` (what you built in task 1). Use the Google Cloud platform.
    - Enable Clould Build API
    - Create a function called hyfe-cough-detection
    - Script task_cloud.py is running on Google cloud
    - requirements.txt installs all dependencies on cloud

#### Write a basic script in python or bash for sending the files in `sounds` to your endpoint and receiving the outputs
  - copy paste https to try it yourself: https://us-central1-hyfe-cloud-function.cloudfunctions.net/hyfe-cough-detection?filename=sample-1613659553295.m4a

####  Add this script to your forked repo.

When finished, email the URL of your forked repo to joe@hyfe.ai.
