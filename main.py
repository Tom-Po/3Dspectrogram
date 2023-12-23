import numpy as np
from matplotlib import mlab
import soundfile as sf
from mayavi import mlab as mayavilab

ELEVATION_RATIO = 15
data, samplerate = sf.read('beat.wav')
left = data[:, 0]
# right = data[:, 1]


def Spectrogram3D(y, srate=44100):
    spec, freqs, t = mlab.specgram(y, Fs=srate)
    X, Y, Z = t[None, :], freqs[:, None],  ELEVATION_RATIO * np.log10(spec)
    mayavilab.surf(Z)
    mayavilab.show()


Spectrogram3D(left, samplerate)
