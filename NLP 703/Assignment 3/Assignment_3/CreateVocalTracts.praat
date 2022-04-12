#
# CreateVocalTracts.praat Copyright (C) 2012  NKI-AVL, Amsterdam and R.J.J.H. van Son
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
form Convert speech recordings to VocalTract
	sentence Speech_files ./*.wav
	sentence Target_directory .
	comment Give the position in the recording to determine
	comment the vocal tract area function in percent of duration
	positive Position_of_slice_(perc) 25
	natural Number_of_segments 40
	positive Vocal_tract_length_(m) 0.20
endform

.directory$ = replace_regex$(speech_files$, "/?[^/]*$", "", 0)
target_directory$ = replace_regex$(target_directory$, "/$", "", 0)

.list = Create Strings as file list... List 'speech_files$'
.numFiles = Get number of strings

for .i to .numFiles
	select .list
	.currentFile$ = Get string... .i
	# a sound
	.a_sound = Read from file... '.directory$'/'.currentFile$'
	.fullname$ = selected$()
	.type$ = extractWord$(.fullname$, "")
	.name$ = extractWord$(.fullname$, " ")
	if .type$ = "Sound"
		# Create a vocal tract, slice at Position_of_slice*duration seconds
		select .a_sound
		.duration = Get total duration
		.slice_point = .duration * position_of_slice / 100
		.tmp = To LPC (autocorrelation)... number_of_segments 0.025 0.005 50
		.vocal_tract = To VocalTract (slice)... .slice_point vocal_tract_length
 		
		select .vocal_tract
		Save as short text file... '.name$'.VocalTract
		
		# Clean up
		select .tmp 
		plus .vocal_tract
		Remove
	endif
	select .a_sound
	Remove
endfor
select .list
Remove