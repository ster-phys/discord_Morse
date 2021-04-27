#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

ROOTPATH = os.path.dirname(os.path.abspath(__file__))
PATH = "{}/Morse/assets/".format(ROOTPATH)

from synthesizer import Synthesizer, Waveform, Writer

UNIT = 0.1
osc1Volume = 1.0
FREQUENCY = 880.0

# dot
synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=osc1Volume, use_osc2=False)
wave = synth.generate_constant_wave(frequency=FREQUENCY, length=UNIT*1)
writer = Writer()
writer.write_wave("{}/1.wav".format(PATH), wave)

# dash
synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=osc1Volume, use_osc2=False)
wave = synth.generate_constant_wave(frequency=FREQUENCY, length=UNIT*3)
writer = Writer()
writer.write_wave("{}/3.wav".format(PATH), wave)

# space
synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=0.0, use_osc2=False)
wave = synth.generate_constant_wave(frequency=FREQUENCY, length=UNIT*1)
writer = Writer()
writer.write_wave("{}/_.wav".format(PATH), wave)
