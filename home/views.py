from django.shortcuts import render,redirect,reverse
from .models import Gallery
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def getImages(request):
    images = Gallery.objects.all()

    paginator = Paginator(images, 9)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    context = {'images': images, 'page': page}
    return render(request, 'home/index.html', context)

def getImage(request, slug):
    image=Gallery.objects.filter(slug=slug).first()
    image.save()
    
    context={'image':image}
    return render(request, 'home/desc.html', context)

def createImage(request):
    if request.method == 'POST':
        imgName = request.POST['imgName']
        imgUrl = request.POST['imgUrl']
        imgDesc = request.POST['imgDesc']

        image = Gallery(imgName=imgName, imgUrl=imgUrl, imgDesc=imgDesc)
        image.save()
        return redirect(reverse('getImages'))
    return render(request, 'home/index.html')

def editImage(request, slug):
    image=Gallery.objects.filter(slug=slug).first()
    if request.method == 'POST':
        image.imgName = request.POST['imgName']
        image.imgUrl = request.POST['imgUrl']
        image.imgDesc = request.POST['imgDesc']

        image.save()
        return redirect(reverse('getImages'))
    return render(request, 'home/index.html', {'image': image})

def deleteImage(request, slug):
    image=Gallery.objects.filter(slug=slug).first()
    image.delete()
    return redirect(reverse('getImages'))

def search(request):
    query=request.GET['query']
    if len(query)>78:
        images=Gallery.objects.none()
    else:
        allImageName= Gallery.objects.filter(imgName__icontains=query)
        allImageDescription =Gallery.objects.filter(imgDesc__icontains=query)
        images=  allImageName.union(allImageDescription)
    if images.count()==0:
        pass
        # messages.warning(request, "No search results found. Please refine your query.")
    params={'images': images, 'query': query}
    
    return render(request, 'home/search.html', params)