import yt_dlp
import os

def baixar_video(url):
    try:
        pasta_destino = 'C:/Users/User/Desktop/Downloads Py'  # Altere para o caminho desejado

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        # Opções para baixar o vídeo
        ydl_opts = {
            'format': 'best',  # Baixar o melhor formato
            'outtmpl': os.path.join(pasta_destino, '%(title)s.%(ext)s'),  
        }

        # Instanciando o downloader
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Baixando vídeo de: {url}")
            ydl.download([url])  # Baixa o vídeo
            print("Download concluído!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")
    baixar_video(url)
