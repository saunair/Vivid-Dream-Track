#		python code
#
#		script_name:vivid dream 
#
#		author:saurabh nair
#
#		description:code
#
#
#
# setup
from earsketch import * 

import random

init() 
setTempo(100) 

# variables
tom =OS_LOWTOM01
clap = OS_CLAP04
kick = OS_KICK05
snare= OS_SNARE01 
left_hat =OS_CLOSEDHAT01
right_hat =OS_CLOSEDHAT04
weird = ELECTRO_SFX_WHITENOISE_SCATTER_010
guitar = Y11_GUITAR_1 
bass = SAURABH.NK@GMAIL.COM_BASSS
bass_2 =SAURABH.NK@GMAIL.COM_BASS_2

hiphop_1=ELECTRO_ANALOGUE_LEAD_009
hiphop_2=ELECTRO_ANALOGUE_LEAD_008
hiphop_3=ELECTRO_ANALOGUE_LEAD_006
hiphop_4 =ELECTRO_ANALOGUE_LEAD_001
hiphop_5=ELECTRO_STARLEAD_003
hiphop_6=ELECTRO_ANALOGUE_LEAD_007


#beat strings
kick_beat=    "0------0-00--0-0"
kick_roll= "00--00--00--00--"
snare_roll= "--00--00--00--00"
snare_beat="----0-------0---"
left_hat_beat= "0-0-0-0-0-0-0-0-"
right_hat_beat="-0-0-0-0-0-0-0-0"
bass_pattern = "1+++0+++1+++1+++0+++0+++1+++0+++"
sequence =""
hip_str =""


# lists
beats = [ kick, snare, clap, tom, right_hat]
bass_string = [bass, bass_2]
hip_hop= [hiphop_1, hiphop_2, hiphop_3, hiphop_4, hiphop_5, hiphop_6]


def riff(start):
    fitMedia(guitar, 10, start, start+1)

	
	
for measure in range(1, 100):
	
	if measure%4 == 0:
		if measure%16 == 0:
			makeBeat(kick, 1, measure/4, shuffleString(kick_roll))
			makeBeat(snare, 2, measure/4, shuffleString(snare_roll))
		else:
			makeBeat(kick, 5, measure/4, kick_beat)
			makeBeat(snare, 6, measure/4, snare_beat) 
	
	if measure%8 == 0:
		makeBeat(bass_string, 11, measure/4, bass_pattern) 	
		
	if ( (measure%8 == 0) and (measure>8) ): 
		makeBeat(left_hat, 7, measure/4, left_hat_beat)
		makeBeat(right_hat, 8, measure/4, right_hat_beat)
		
	if ((measure%16 == 0) and measure>8 ):
		riff(measure/4) 
	
	


#pattern

for measure in range(8, 48):
	for length in range(1,4):
		sequence += str(random.randint(0, 4))
	
	if measure%16 == 0:
		makeBeat(beats, 3, measure/2, sequence)
	
for measure in range(12, 72):
	for length in range(0,4):
		hip_str += str(random.randint(0, 5))
	
	if measure%24== 0:
		makeBeat(hip_hop, 4, measure/3, hip_str)
# second

fitMedia(weird, 9, 1, 3)
fitMedia(weird, 9, 11, 13.5) 
fitMedia(weird, 9, 24, 26.5) 



# set volumes on tracks
#setEffect(12, VOLUME, GAIN, 0.1) # setting volumes on some tracks to help move toward a good mix of all sounds
setEffect(5, VOLUME, GAIN, -20)  # since the volume level of this track sounds good at 0, we don't need to call this (but we still could, with volume value 0 as shown)

setEffect(7, PAN, LEFT_RIGHT, -100)
setEffect(8, PAN, LEFT_RIGHT, 100)

#setEffect(6, DISTORTION, DISTO_GAIN, 12)

# add some delay 
setEffect(10, WAH, WAH_POSITION, 0.3) 
#setEffect(10,  DELAY, DELAY_TIME, 200)
setEffect(9,  DELAY, DELAY_TIME, 200)
#ENVELOPE
setEffect(10, VOLUME, GAIN, 0.01, 1,0.3, 8)
setEffect(10, VOLUME, GAIN, 0.3, 8,1.5, 10)
setEffect(10, VOLUME, GAIN, 1.5, 20,1.5, 22)
setEffect(10, VOLUME, GAIN, 1.5,23,10, 26)
# this delay time value (in ms) makes a dotted-4tr note pulse (for 115 bpm)
#setEffect(6,  DELAY, MIX, 0.38) # beatHit sound
#setEffect(6,  DELAY, DELAY_TIME, 391) # this delay time value (in ms) makes a dotted-8th note pulse (for 115 bpm)
#setEffect(8,  DELAY, MIX, 0.38) # intro scratch sound
#setEffect(8,  DELAY, DELAY_TIME, 391) # this delay time value (in ms) makes a dotted-8th note pulse (for 115 bpm)
#setEffect(9,  DELAY, MIX, 0.38) # intro synth sound
#setEffect(9,  DELAY, DELAY_TIME, 522) # this delay time value (in ms) makes a quarter note pulse (for 115 bpm)
#setEffect(10, DELAY, MIX, 0.38) # intro whoosh sound
#setEffect(10, DELAY, DELAY_TIME, 522) # this delay time value (in ms) makes a quarter note pulse (for 115 bpm)

finish() 
