import os
import shutil

# startTime=1000
# endTime=2000
# # Opening file and extracting segment
# song = AudioSegment.from_wav("trial_covid/0AWF9zOT8YY_ 150.000_ 160.000.wav")
# extract = song[startTime:endTime]
# print(extract)
# # Saving
# extract.export('extract.mp3', format="mp3")
RAW_DATA = '20200416/20200416'
i=1
for folder in os.listdir(RAW_DATA):
	for file in os.listdir(os.path.join(RAW_DATA, folder)):
		if file=="cough-heavy.wav" or file=="cough-shallow.wav":
			shutil.copyfile(os.path.join(RAW_DATA, folder, file), f"cough_data/cough_{i}.wav")
			i += 1
			
print(i)