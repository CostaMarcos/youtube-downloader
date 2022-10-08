from pytube import YouTube
from pytube.cli import on_progress

link = input("Insira o link do vídeo: ")
yt = YouTube(link, on_progress_callback = on_progress)
print("Video: ", yt.title)
print("Iniciando o download, aguarde alguns instantes...")

ys = yt.streams.get_highest_resolution()
ys.download(output_path=".")
print("Download Finalizado com sucesso!")
input()