# Create your views here.

# downloader/views.py

# from django.shortcuts import render
# from pytube import YouTube
# import requests

# # def download(request):
# #     if request.method == 'POST':
# #         url = request.POST.get('url')
# #         yt = YouTube(url)
# #         stream = yt.streams.first()
# #         stream.download()
# #         return render(request, 'download.html', {'message': 'Download successful!'})
# #     return render(request, 'download.html')
# downloader/views.py

# from django.shortcuts import render
# from pytube import YouTube

# def download(request):
#     message = None
#     if request.method == 'POST':
#         url = request.POST.get('url')
#         try:
#             yt = YouTube(url)
#             stream = yt.streams.first()
#             stream.download()
#             message = 'Download successful!'
#         except Exception as e:
#             message = f'Error downloading video: {str(e)}'
#     return render(request, 'download.html', {'message': message})
import os
from django.conf import settings
from django.shortcuts import render
from pytube import YouTube

def download(request):
    message = None
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            yt = YouTube(url)
            stream = yt.streams.first()
            download_path = os.path.join(settings.BASE_DIR, 'downloads')
            if not os.path.exists(download_path):
                os.makedirs(download_path)
            file_path = os.path.join(download_path, stream.default_filename)
            stream.download(output_path=download_path, filename=stream.default_filename)
            message = 'Download successful!'
        except Exception as e:
            message = f'Error downloading video: {str(e)}'
    return render(request, 'download.html', {'message': message})


# # from django.shortcuts import render
# # from pytube import YouTube
# # from pytube.exceptions import RegexMatchError, VideoUnavailable

# # def download(request):
# #     message = None
# #     if request.method == 'POST':
# #         url = request.POST.get('url')
# #         try:
# #             yt = YouTube(url)
# #             stream = yt.streams.first()
# #             stream.download()
# #             message = 'Download successful!'
# #         except (RegexMatchError, VideoUnavailable) as e:
# #             message = f'Error: {str(e)}'
# #     return render(request, 'download.html', {'message': message})
# # downloader/views.py

# # downloader/views.py

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from pytube import YouTube
# from pytube.exceptions import RegexMatchError, VideoUnavailable

# def download(request):
#     if request.method == 'POST':
#         url = request.POST.get('url')
#         try:
#             yt = YouTube(url)
#             stream = yt.streams.first()
#             stream.download()
#             messages.success(request, 'Download successful!')
#         except (RegexMatchError, VideoUnavailable) as e:
#             messages.error(request, f'Error: {str(e)}')
#         return redirect('download')  # Redirect to clear POST data and display message
#     return render(request, 'download.html')












