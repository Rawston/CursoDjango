from django.shortcuts import render

def video(request, slug):
    video = {
        'motivacao':{'titulo': 'Video Aperitivo: Motivaçao', 'youtube_id': 695772},
        'instalacao-windows':{'titulo': 'Instalação do Windows', 'youtube_id': 251497668},
    }
    video = video[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
