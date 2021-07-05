from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.


def home(request):
    if request.method == 'POST':
        f = request.FILES['file']
        fs = FileSystemStorage()
        filename, ext = str(f).split('.')
        file = fs.save(str(f), f)
        fileurl = fs.url(file)
        size = fs.size(file)
        return render(request, 'home.html', {'fileurl': fileurl, 'filename': filename, 'ext': ext, 'size': size})
    else:
        return render(request, 'home.html', {})
