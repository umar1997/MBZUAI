import pyaudio
import wave
import keyboard

# https://stackoverflow.com/questions/48653745/continuesly-streaming-audio-signal-real-time-infinitely-python

print('RECORD SPEECH') 
print('-'*15)

FORMAT = pyaudio.paInt16
CHANNELS = 1 # Or keep as 2 (1 is working better)
RATE = 44100
WAVE_OUTPUT_FILENAME = "_assets/File.wav"
RECORD_SECONDS = 60
CHUNK = 1024

 
class Record:
	def __init__(self,):
		pass

	def run(self,):

		audio = pyaudio.PyAudio()
		 
		# Start Recording
		stream = audio.open(
						format=FORMAT, 
						channels=CHANNELS,
						rate=RATE, 
						input=True,
						frames_per_buffer=CHUNK)

		print('Press R To Start Recording!')
		while True:
			if keyboard.read_key() == "R":
				print("Recording Started. . .")
				print("Press q To Stop Recording!")
				break

		frames = []
		# stream.start_stream()
		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)
			if keyboard.is_pressed("q"):
				print("Recording Finished!")
				break
		# while True:
		# 	data = stream.read(CHUNK)
		# 	frames.append(data)
		# 	if keyboard.is_pressed("q"):
		# 		print("Recording Finished!")
		# 		break
		 
		 
		# Stop Recording
		stream.stop_stream()
		stream.close()
		audio.terminate()
		 
		waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		waveFile.setnchannels(CHANNELS)
		waveFile.setsampwidth(audio.get_sample_size(FORMAT))
		waveFile.setframerate(RATE)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()

if __name__ == '__main__':
	voice = Record()
	voice.run()