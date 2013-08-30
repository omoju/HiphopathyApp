# Create your views here.

from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.forms.models import modelformset_factory
from django.core.mail import send_mail


from models import Artist
from models import Song
from models import Snippet
from models import SnippetForm
from contactform import ContactForm
import list_cmp





def index(request):
    artist_list = Artist.objects.all().order_by('artist')
    return render_to_response('index.html', {'artist_list': artist_list})
    
def search_form(request):
    return render_to_response('search_form.html')
    
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        snippet_list = Snippet.objects.filter(songid = q)
        return render_to_response('search_results.html',
        {'snippet_list': snippet_list, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

    
def song_view(request, artistid):
    artist = Artist.objects.filter(artistid=artistid)
    song_list = Song.objects.filter(artistid=artistid)
    return render_to_response('song_index.html', {'song_list': song_list, 'artist': artist})
    
    
def snippet_view(request, songid):
    song = Song.objects.filter(songid=songid)
    artist = song[0].artistid
    chunk_list = Snippet.objects.filter(songid = songid)
    return render_to_response('snippet_index.html', {'chunk_list': chunk_list, 'song': song, 'artist': artist})
    

def post(request):
	if 'user_supplied_answer' in request.GET and request.GET['user_supplied_answer']:
		a = request.GET['user_supplied_answer']
		return render_to_response('snippet_post.html', {'answer': user_supplied_answer})
	else:
		return HttpResponse('Bye')

def about(request):
    return render_to_response('about.html')

def tutorial_1(request):
    return render_to_response('tutorial_1.html')

def visual_score(request):
    return render_to_response('visual_score.html', context_instance=RequestContext(request))

def tutorial_2(request):
    artist_list = Artist.objects.all().order_by('artist')
    return render_to_response('tutorial_2.html', {'artist_list': artist_list})

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            topic = form.clean_data['topic']
            message = form.clean_data['message']
            sender = form.clean_data.get('sender', 'noreply@example.com')
            send_mail(
                       'Feedback from your site, topic: %s' % topic,
                       message, sender,
                       ['administrator@example.com']
            )
        return render(request,'index.html')
    else:
        form = ContactForm()
        return render(request,'contact.html',{'form':form})

def manage_snippets(request, snippetid):
    mymodel = get_object_or_404(Snippet, snippetid =snippetid )
    form = SnippetForm(request.POST or None, instance= mymodel)
    if form.is_valid():
        mymodel = form.save()
        mymodel.save()
        artist_list = Artist.objects.all().order_by('artist')
        return render_to_response('tutorial_2.html', {'artist_list': artist_list})
    return render(request, "manage_snippets.html", {'form': form, 'mymodel':mymodel})

# What I need to do is get the first 4 snippets, assess them and then turn in into json and visualize it.
# Snippet.objects.all()[:4]