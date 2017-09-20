import os
from magenta.models.performance_rnn import performance_sequence_generator
from magenta.protobuf import generator_pb2
from magenta.protobuf import music_pb2

import magenta.music as mm

import numpy as np
from scipy.io.wavfile import write

import time

def ns_performance(temperature, output_path):
	# Constants.
	t1 = time.time()
	BUNDLE_DIR = './bundles'
	MODEL_NAME = 'performance_with_dynamics'
	BUNDLE_NAME = MODEL_NAME + '.mag'

	BUNDLE_ABS_PATH = '/Users/bregy/PycharmProjects/neurospace/bundles/performance_with_dynamics.mag'

	#mm.notebook_utils.download_bundle(BUNDLE_NAME, BUNDLE_DIR)
	bundle = mm.sequence_generator_bundle.read_bundle_file(BUNDLE_ABS_PATH)
	#bundle = mm.sequence_generator_bundle.read_bundle_file(os.path.join(BUNDLE_DIR, BUNDLE_NAME))
	generator_map = performance_sequence_generator.get_generator_map()
	generator = generator_map[MODEL_NAME](checkpoint=None, bundle=bundle)
	generator.initialize()
	generator_options = generator_pb2.GeneratorOptions()
	generator_options.args['temperature'].float_value = temperature
	generate_section = generator_options.generate_sections.add(start_time=0, end_time=120)
	sequence = generator.generate(music_pb2.NoteSequence(), generator_options)

	# Play this masterpiece.

	t2 = time.time()

	midi = mm.sequence_proto_to_pretty_midi(sequence)

	a = midi.fluidsynth()
	write(output_path, 44100, a)

