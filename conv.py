from __future__ import division
import math
import struct
import sys
import re

def Parse_Tone(Note):
	Note = Note.upper()
	if Note.find("-") == -1:
		try:
			(Duration, Octave) = re.findall(r"[0-9]+", Note)
		except:
			pass
	else:
		Duration = re.findall(r"[0-9]+", Note)[0]
		Octave = 1
	Tone = re.findall(r"[A-Z,#,-]+", Note)[0]
	Duration = int(Duration)
	Octave = int(Octave)
	if Note.find(".") != -1:
		Duration = Duration/1.5
	return (32/Duration, Tone, Octave)

Frames = []
Notes = {"-" : 0 ,"C" : 261.626, "#C" : 277.183, "D" : 293.665, "#D" : 311.127, "E": 329.628, "#E" : 349.228, "F" : 349.228, "#F" : 369.994, "G" : 391.995, "#G" : 415.305, "A" : 440.000, "#A" : 466.164, "B" : 493.883, "#B" : 523.251}

def Append_Note(VOL, TIME, NOTE, OCTAVE):
    FREQ = Notes[NOTE]*OCTAVE
    if FREQ != 0:
        print('tone(9, ' + str(FREQ) + ', ' + str(TIME) + ');' + '\ndelay(' + str(TIME) + ');\n')
        f = open(OutFile, 'a')
        f.write('tone(9, ' + str(FREQ) + ', ' + str(TIME) + ');' + '\ndelay(' + str(TIME) + ');\n')
        f.close

def Append_Notes(VOL, LIST, BPM):
	for Each in LIST:
		(Duration, Tone, Octave) = Parse_Tone(Each)
		try:
			Append_Note(VOL, int(Duration*1000*7.5/BPM), Tone, Octave)
		except:
			print ("Error! ne mogu obrabotat %s" %Each)
		Append_Note(0, int(250*7.5/BPM), "-", 1)

if __name__ == "__main__":
    if len (sys.argv) != 4:
        print ('ERROR!\n	USAGE:\n	conv.py "Notes" BMP FileName\nExample:\n	conv.py "16c2 16#a1 4c2 2f1 16#c2 16c2 8#c2 8c2 2#a1 16#c2 16c2 4#c2 2f1 16#a1 16#g1 8#a1 8#g1 8g1 8#a1 2#g1 16g1 16#g1 2#a1 16#g1 16#a1 8c2 8#a1 8#g1 8g1 4f1 4#c2 1c2 16c2 16#c2 16c2 16#a1 1c2" 120 Music.txt')
    List = sys.argv[1].split(' ')
    BPM = int(sys.argv[2])
    OutFile = sys.argv[3]
    print ("\nFile information:\n\n	Note number: %s\n	Tempo: %s BPM\n\nGeneration of amplitude..." % (len(List), BPM))

Append_Notes(1, List, BPM)
