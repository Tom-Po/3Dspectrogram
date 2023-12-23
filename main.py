import numpy as np
from matplotlib import mlab, pyplot as plt
import soundfile as sf

ELEVATION_RATIO = 15

# Ici on extrait les données et le samplerate du fichier audio

# data, samplerate = sf.read('beat.wav')
data, samplerate = sf.read('synth.wav')

# Puisqu'il est en stereo pour le moment j'ai isolé un seul channel
# Sinon on obtient un tableau en 2 dimensions qui n'est pas digeste pour mlab.specgram

left = data[:, 0]
# right = data[:, 1]


def specgram3d(y, srate=44100, ax=None):
    if not ax:
        ax = plt.axes(projection='3d')

    # On transforme le tableau de données du sample en spectre
    spec, freqs, t = mlab.specgram(y, Fs=srate)
    # On transforme le spectre en tableaux 2 dimensions
    X, Y, Z = t[None, :], freqs[:, None],  ELEVATION_RATIO * np.log10(spec)
    ax.plot_surface(X, Y, Z, cmap='viridis')
    # On désactive la grille et les labels/legendes
    ax.grid(False)
    ax.axis('off')
    # On offset la vue pour être centré
    ax.set_zlim(-220, 0)
    return X, Y, Z


fig2, ax2 = plt.subplots(subplot_kw={'projection': '3d'})

# Appel à la fonction définie plus haut
# En paramètre y = les données audio en tableau, srate = le samplerate
specgram3d(left, srate=samplerate, ax=ax2)

# On affiche le spectrogram
plt.show()
