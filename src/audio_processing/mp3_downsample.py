import os
from pydub import AudioSegment

cwd = os.getcwd()
print(cwd)
file_path = '/Users/rchatter/Desktop/DS/Python/Senior-Thesis/music_files/originals/'
file_name="pandit-hari-todi-orig.mp3"
print(file_name[:-8])
out_path = '/Users/rchatter/Desktop/DS/Python/Senior-Thesis/music_files/samples'

startMin = 1
startSec = 00

endMin = 2
endSec = 00

# Time to Milliseconds

startTime = startMin*60*1000 + startSec*1000
endTime = endMin*60*1000 + startSec*1000

# Opening file and extracting segment
song = AudioSegment.from_mp3(file_path+file_name)
extract = song[startTime:endTime]

# Save
extract.export(out_path+file_name[:-8]+'extract.mp3', format='mp3')
