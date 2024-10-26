from moviepy.editor import AudioFileClip
import uuid

import streamlit as st
import assemblyai as aai


aai.settings.api_key = "b8a3ef6ed06e4ec2a8cff577afaf3d30"






def mp4_to_mp3(mp4_filename, mp3_filename):

	arquivo_a_ser_convertido = AudioFileClip(mp4_filename)
	arquivo_a_ser_convertido.write_audiofile(mp3_filename)
	arquivo_a_ser_convertido.close()





st.title('Automação de atas')

st.write('Criando uma ferramenta de automação de atas de reunião com tecnologia de IA com Python')


uploaded_file = st.file_uploader("Selecione o seu arquivo", accept_multiple_files=False, type = ['mp4'])

if uploaded_file:

	with st.spinner('Convertendo de mp4 para mp3'):
	
		mp4_filename = uploaded_file.name
		mp3_filename = '{nome_arquivo}.mp3'.format(nome_arquivo = uuid.uuid4().hex)

		tempfile = open(mp4_filename, 'wb')
		tempfile.write(uploaded_file.read())

		mp4_to_mp3(mp4_filename, mp3_filename)

	st.success("Conversão de MP4 para MP3 realizada!")



	with st.spinner('Convertendo de mp3 para texto'):

		transcriber = aai.Transcriber()

		config = aai.TranscriptionConfig( speaker_labels = True, speakers_expected = 2, language_code = 'pt' )

		transcriber = aai.Transcriber()
		transcricao = transcriber.transcribe(mp3_filename, config = config)


		texto_transcrito = ''
		for sentenca in transcricao.utterances:
			texto_transcrito = f"Pessoa {sentenca.speaker}: {sentenca.text}"
			texto_transcrito = texto_transcrito + '\n'

		st.text_area('Transcrição', texto_transcrito)

	st.success("Transcrição realizada!")

