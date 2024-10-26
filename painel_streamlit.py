from moviepy.editor import *
import uuid

import streamlit as st


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

		st.text(mp3_filename)
