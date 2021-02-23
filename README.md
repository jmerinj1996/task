# Instructions

Do not spend more than 1-2 hours on any task.

## Task 1

#### Fork this repo  

#### Read the instructions in `task.py`

#### Modify the `detect_coughs` function
  1. For this event detection task, I use a library called Librosa, a python package for music and audio processing.
  2. librosa.load loads an audio file into a audio array
  3. butter_highpass function filters low-frequency noise using a high-pass filter
  4. librosa.util.peak_pick uses a flexible heuristic to pick peaks in a signal.
  5. Finally, I return these peaks as detected coughs
  6. I tweak the parameters of peak_pick to get an optimal precision/recall score

#### Libraries used:
    - pandas==1.1.3
    - scipy==1.5.2
    - numpy==1.19.2
    - tqdm==4.50.2
    - librosa==0.8.0


## Task 2

#### Build a simple cloud function to deploy `detect_coughs` (what you built in task 1). Use the Google Cloud platform.
  1. First, I enable Clould Build API on Google Cloud
  2. I create a function called `hyfe-cough-detection`
  3. The file `task_cloud.py` is what is running on Google cloud
  4. `requirements.txt` installs all dependencies on the cloud
  5. Sending the files in `sounds` and receiving the output is as simple as writing a http request

#### Write a basic script in python or bash for sending the files in `sounds` to your endpoint and receiving the outputs
  - copy paste https to try it yourself:
 https://us-central1-hyfe-cloud-function.cloudfunctions.net/hyfe-cough-detection?filename=sample-1613659553295.m4a

####  Add this script to your forked repo.

When finished, email the URL of your forked repo to joe@hyfe.ai.
