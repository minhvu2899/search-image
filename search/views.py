from django.http.response import HttpResponse
from django.shortcuts import render
from numpy.core.fromnumeric import ptp
from .form import FormSelect
import cv2
from .colordescriptor import ColorDescriptor
from .searcher import Searcher
import pathlib
import os
# Create your views here.
def index(request):
    context = {}
    if request.method == "POST":
        form = FormSelect(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get("image_query")
            path="static/images/"+str(img)
            # print(GeeksModel.objects.filter(img= path)!='')
            # if GeeksModel.objects.filter(img= path)=='':
            #     q=GeeksModel.objects.get(img= path)
            # else:
            #     obj = GeeksModel.objects.create(
            #                         title = name, 
            #                         img = img
            #                         )
            #     obj.save()
            context['filename']=str(img)
            cd = ColorDescriptor((8, 8, 8))
            query = cv2.imread(path)
            # print(query)
            features = cd.describe(query)
            # print(features)
            searcher = Searcher("static/index1.csv")
            results = searcher.search(features)
            # display the query
            print(results)
            urlImage=[]
            # loop over the result
            for (score, resultID) in results:
                # load the result image and display it
                name_image = resultID.split("\\")[-1]
                name_video = name_image.split("_")[0]
                # print(name_video)
                print(name_image)
                urlImage.append(name_image)
                context['url']=urlImage
              
    else:
        form = FormSelect()
    context['form']= FormSelect
    
    
    return render(request, "search/index.html", context)
   