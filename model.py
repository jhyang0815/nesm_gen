import tensorflow as tf
import numpy as np
from pretty_midi import *
import pickle



lm_pkl_dir='nesmdb_nlm/'
midi_dir='nesmdb_midi/'

midi_data = pretty_midi.PrettyMIDI(midi_dir+'train/297_SkyKid_00_01StartMusicBGMIntroBGM.mid')

# If loading MIDI file fails, try
# pretty_midi.pretty_midi.MAX_TICK = 1e10

for instrument in midi_data.instruments:
  print('-' * 80)
  print(instrument.name.upper())
  print('# note events: {}'.format(len(instrument.notes)))
  print('# control change events: {}'.format(len(instrument.control_changes)))