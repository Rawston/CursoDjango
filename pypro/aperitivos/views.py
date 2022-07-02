from django.shortcuts import render

def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivaçao', 'youtube_id': 695772}
    return render(request, 'aperitivos/video.html', context={'video': video})
