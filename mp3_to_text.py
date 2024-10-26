import assemblyai as aai

aai.settings.api_key = "b8a3ef6ed06e4ec2a8cff577afaf3d30"
transcriber = aai.Transcriber()

mp3_filename = r'C:\Users\cadup\Desktop\automacao_de_atas\bcf824becd634f6dbe7200560eb7f10f.mp3'

config = aii.TranscriptionConfig(speaker_labels = True, speakers_expected = 2, langague_code = 'pt')

trasncriber = aai.Trascriber()
trasncricao = trasncriber.transcribe(mp3_filename, config = config)

for sentenca in transcricao.utterances:
  print(f"Pessoa {sentenca.speaker}: {sentenca.text})
