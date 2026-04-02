import whisper, json, os
import time

audios = os.listdir('Dataset_Audios')
print('Loading model turbo...')
model = whisper.load_model("turbo")
print('Model loaded Successfully, Now processing the audio files...')

start_time = time.time()
total_files = len(audios)

for idx, aud in enumerate(audios):#aud is the name of the audio file in the format "chapter_title.mp3"
   file_start_time = time.time()
   chapter=aud[0]
   title=aud.split('_')[1].split('.')[0]
   print("\n\nProcessing Chapter "+chapter+" - "+title)
   #transcribe the audio file and get the segments with timestamps
   result = model.transcribe(f"Dataset_Audios/{aud}") 
   # result = model.transcribe(f"Dataset_Audios/SampleAudio_20sec.wav")
   chunks=[]
   for segment in result['segments']:
      chunks.append({'chapter':chapter,'title':title,'text':segment['text'],'start':segment['start'],'end':segment['end']}) #append the chapter, title, text, start and end time of each segment to the chunks list
      print('processing chunk: '+segment['text'])
   chunks_metadata={'chunks':chunks,'text':result['text']} #create a dictionary with the chunks and the full text of the chapter
   with open(f"jsons/{aud}.json",'w') as f:
      json.dump(chunks_metadata,f)
   print('Dumped the json for chapter '+chapter+' - '+title) 
   
   file_end_time = time.time()
   file_time = file_end_time - file_start_time

   elapsed_time = file_end_time - start_time
   avg_time_per_file = elapsed_time / (idx + 1)
   remaining_files = total_files - (idx + 1)
   eta = avg_time_per_file * remaining_files

   print(f"Time for this file: {file_time:.2f} sec")
   print(f"Processed {idx+1}/{total_files} files")
   print(f"Estimated time remaining: {eta/60:.2f} minutes")     