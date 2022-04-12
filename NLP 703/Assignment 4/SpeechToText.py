# https://colab.research.google.com/github/pytorch/tutorials/blob/gh-pages/_downloads/51ceef925146825bff7f3dcfd3da80b1/speech_recognition_pipeline_tutorial.ipynb#scrollTo=L8ocdml7UlvQ

import os
import re
import torch
import torchaudio
import numpy as np
from recordSpeech import Record


torch.random.manual_seed(0)
device = 'cpu'
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

voice = Record()
voice.run()

print("\n")

print('DECODE SPEECH') 
print('-'*15)

print('Loading Recorded File ...')
SPEECH_FILE = "_assets/File.wav"


bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H

# print("Sample Rate:", bundle.sample_rate)
# print("Labels:", bundle.get_labels())

print('Building Model ...')
model = bundle.get_model().to(device)
# print(model.__class__)


waveform, sample_rate = torchaudio.load(SPEECH_FILE)
waveform = waveform.to(device)

if sample_rate != bundle.sample_rate:
    waveform = torchaudio.functional.resample(waveform, sample_rate, bundle.sample_rate)

with torch.inference_mode():
    features, _ = model.extract_features(waveform)

with torch.inference_mode():
    emission, _ = model(waveform)


class GreedyCTCDecoder(torch.nn.Module):
    def __init__(self, labels, blank=0):
        super().__init__()
        self.labels = labels
        self.blank = blank

    def forward(self, emission: torch.Tensor):
        
        """
        Given a sequence emission over labels, get the best path string
        Args:
          emission (Tensor): Logit tensors. Shape `[num_seq, num_label]`.

        Returns:
          str: The resulting transcript
        """

        indices = torch.argmax(emission, dim=-1)  # [num_seq,]
        indices = torch.unique_consecutive(indices, dim=-1)
        indices = [i for i in indices if i != self.blank]
        return "".join([self.labels[i] for i in indices])

print('Converting Speech to Text ...')
decoder = GreedyCTCDecoder(labels=bundle.get_labels())
transcript = decoder(emission[0])
transcript = transcript.lower().capitalize()
transcript = re.sub(r'\|', ' ', transcript)
transcript = transcript.strip()
print('Transcript: {}'.format(transcript))