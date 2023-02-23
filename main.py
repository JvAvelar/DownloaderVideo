import pytube

link = input('Digite a URL do YouTube: ')

yt = pytube.YouTube(link)

yt.streams.first().download('D:\Downloads\Videos')

print(f'Download do vídeo: {yt.title} , realizado com sucesso.')