from pydub import AudioSegment

file_path = '../music_files/originals/'
file_name = 'pandit-hari-orig.mp3'
print(file_name[:-8])
out_path = '../music_files/samples/'

startMin = 1
startSec = 30

endMin = 2
endSec = 30

# Time to Milliseconds

startTime = startMin*60*1000 + startSec*1000
endTime = endMin*60*1000 + startSec*1000

# Opening file and extracting segment
song = AudioSegment.from_mp3(file_path+file_name)
extract = song[startTime:endTime]

# Save
extract.export(out_path+file_name[:-4]+'extract.mp3', format='mp3')
