from django.shortcuts import render
from .models import Guide, Video, Test, Music,Books

def home(request):
    return render(request, 'home.html', {'home': 'home'})

def guides(request):
    guides = Guide.objects.all()
    return render(request, 'guides.html', {'guides': guides})

def videos(request):
    videos = Video.objects.all()
    return render(request, 'videos.html', {'videos': videos})

def tests(request):
    if request.method == 'POST':
        tests = Test.objects.all()
        score = 0
        total = len(tests)
        for test in tests:
            selected = request.POST.get(f'test_{test.id}')
            if selected == 'option1':  # Agar birinchi javob to‘g‘ri deb faraz qilsak
                score += 1
        compatibility = (score / total) * 100 if total > 0 else 0
        return render(request, 'test_result.html', {'compatibility': compatibility})
    tests = Test.objects.all()
    return render(request, 'tests.html', {'tests': tests})

def music(request):
    music_list = Music.objects.all()
    return render(request, 'music.html', {'music_list': music_list})

def guide_detail(request, pk):
    guide = Guide.objects.get(pk=pk)
    return render(request, 'guide_detail.html', {'guide': guide})

def books(request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})
