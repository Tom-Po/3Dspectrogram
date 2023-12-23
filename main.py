import numpy as np
from matplotlib import mlab
import soundfile as sf
from mayavi import mlab as mayavilab

ELEVATION_RATIO = 15

# Ici on extrait les données et le samplerate du fichier audio
# data, samplerate = sf.read('synth.wav')
data, samplerate = sf.read('beat.wav')

# Puisqu'il est en stereo pour le moment j'ai isolé un seul channel
# Sinon on obtient un tableau en 2 dimensions qui n'est pas digeste pour mlab.specgram

left = data[:, 0]
# right = data[:, 1]


def Mayaspecgram3d(y, srate=44100):
    spec, freqs, t = mlab.specgram(y, Fs=srate)
    X, Y, Z = t[None, :], freqs[:, None],  ELEVATION_RATIO * np.log10(spec)
    mayavilab.surf(Z)
    mayavilab.show()


Mayaspecgram3d(left, samplerate)
