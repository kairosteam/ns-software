#!usr/bin/env python  
#coding=utf-8  

import subprocess
audio_file = "/Users/bregy/PycharmProjects/neurospace/test1.wav"


def playWav(music_path):
	return_code = subprocess.call(["afplay", music_path])
	return return_code

print playWav(audio_file)