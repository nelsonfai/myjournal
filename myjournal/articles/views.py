from django.shortcuts import render,redirect
from .models import Articles,Prompts
from .forms import ArticleForm,UpdateForm,WriteupForm,CommentForm
from accounts.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def articles(request):
    articles = Articles.objects.filter(status ='publish').order_by('-date')
    context={
        'pagetitle':'My Feed',
        'articles':articles
    }
    return render (request,'articles/feed.html', context)
def article(request,pk,slug):
    if request.method =='POST':
        form = CommentForm(request.POST)
        articleid=request.POST.get("articleid")
        article = Articles.objects.get(id=articleid)

        if form.is_valid:
            comment= form.save(commit=False)
            article = Articles.objects.get(id=articleid)
            print(article)
            profile= Profile.objects.get(user=request.user) 
            comment.author=profile
            comment.article =article
            comment.save()
            return redirect (request.path)
        else:
            return redirect (request.path)
    else:        
        article = Articles.objects.get(pk=pk)
        form = CommentForm()

        context={
            'article':article,
            'form':form
        }
        return render (request,'articles/details.html', context)
def tagfilter(request,slug):
    articles =Articles.objects.filter(tags=slug,status='publish')
    context={
        'articles':articles
    }

    return render (request,'articles/feed.html', context)
@login_required(login_url='login')
def createpost(request):
    myprofile= Profile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            newpost= form.save(commit=False)
            newpost.author = myprofile
            newpost.save()
            return redirect('allarticles')
        else:
            context={
                'pagetitle':'Write article',
                'form':form,
            }
            return render (request,"articles/createpost.html",context) 
    else:
            initial_data={
                'author':myprofile
            }
            form = ArticleForm(initial=initial_data)
            context={
                'pagetitle':'Write article',
                'form':form,
            } 
            return render (request,"articles/createpost.html",context) 
@login_required(login_url='login')
def edit_post(request,slug):
    post =Articles.objects.get(id=slug)
    if post.author.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST,instance=post)
            
            if form.is_valid():
                print('valid')
                form.save()
                return redirect ('profile',request.user.username)
            else:
                form =  ArticleForm(instance=post)
                context={
                     'pagetitle':'Edit post',
                    'form':form,
                }
                return render (request,"articles/edit.html",context)
        else:
            form =  ArticleForm(instance=post)
            context={
                 'pagetitle':'Edit post',
                        'form':form,
                    } 
            return render (request,"articles/editpost.html",context) 
    else:
        return redirect ('profile',post.author.user.username)
@login_required(login_url='login')
def delete_post(request,slug):
    post =Articles.objects.get(id=slug)
    if post.author.user == request.user:
       post.delete()
       return redirect ('profile',request.user.username)
         
    else:
        return redirect ('profile',post.author.user.username)

def prompts(request):
    prompts = Prompts.objects.all()
    context={              'pagetitle':'Daily Prompts',
                        'prompts':prompts,
                    } 
    return render (request,"articles/prompts.html",context)
def prompt_details(request,slug):
    print(' promp details  ...............................')
    prompt = Prompts.objects.get(id=slug)
    profile = Profile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = WriteupForm(request.POST)
       
        
        if form.is_valid():
            print('valid promp...............................')
            write= form.save(commit=False)
            write.author = profile
            write.prompt = prompt
            write.save()
            return redirect('prompt_details', prompt.id)
        else:
            print('INvalid promp...............................')
            form = WriteupForm()
            context={       'pagetitle':'Daily Prompt',
                            'prompt':prompt,
                            'form':form
                        } 
        return render (request,"articles/prompt_details.html",context)
    else:
        print(' promp  else   ...............................')
        form = WriteupForm()
        context={            'pagetitle':'Daily Prompt',
                            'prompt':prompt,
                            'form':form
                        } 
        return render (request,"articles/prompt_details.html",context)

@login_required(login_url='login')
def comment(request):
    if request.method =='POST':
        form = CommentForm(request.POST)
        articleid=request.POST.get("articleid")
        article = Articles.objects.get(id=articleid)

        
        if form.is_valid:
            comment= form.save(commit=False)
            article = Articles.objects.get(id=articleid)
            print(article)
            profile= Profile.objects.get(user=request.user) 
            comment.author=profile
            comment.article =article
            comment.save()
            return redirect (request.path)
        
        return redirect ('article_details', int=articleid ,slug=article.slug)
    


