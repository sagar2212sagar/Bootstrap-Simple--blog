from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import Posts
from django.db.models import Q
from .forms import PostForm
from django.contrib import messages


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form=PostForm(request.POST or None,request.FILES or None)
    if(form.is_valid()):
        form.save()
        messages.success(request,"Successfully created")
    else:
         messages.error(request,"Sorry")


    context={"form":form,}

    return render(request,'post_form.html',context)
def post_detail(request,id=None):
    instance=get_object_or_404(Posts,id=id)
    context={"title":instance.title,"instance":instance}

    return render(request,'post_details.html',context)
def post_list(request):
    queryset_list=Posts.objects.all()

    page = request.GET.get('page')
    query=request.GET.get("q")
    if query:
        queryset_list=queryset_list.filter(Q(title=query)|Q(content=query)).distinct()
    paginator = Paginator(queryset_list,2)
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:

        queryset=paginator.page(paginator.num_pages)

    context={ "object_list":queryset,
              "title":"list"}
    return render(request,"post_list.html",context)


def post_update(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Posts,id=id)
    form=PostForm(request.POST or None,request.FILES or None,instance=instance)
    if(form.is_valid()):
        form.save()
        return HttpResponseRedirect(instance.get_absolute_url())


    context={"form":form, "title":instance.title,"instance":instance}

    return render(request,'post_form.html',context)

def post_delete(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Posts,id=id)
    instance.delete()

    return redirect("blog1:list")

