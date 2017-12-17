from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages

from .models import *
from ..user.models import *



def show(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    else:
        content={'user':User.objects.get(id=request.session['user_id']),
                 'all_messages': Message.objects.all().order_by("-updated_at"),
                 'all_comments': Comment.objects.all().order_by("-updated_at")}
        return render(request,'message/process.html',content)

#==============================================================================
#                    messages add/modify/delete
#==============================================================================
def add_message(request):
    errors=Message.objects.message_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/wall')
    else:
        Message.objects.create(user_id=User.objects.get(id=request.session['user_id']),content=request.POST['des'])
        return redirect('/wall')

def udate_message(request):
    if Message.objects.get(id=request.POST['msg']).user_id.id != request.session['user_id']:
        messages.error(request,'Only author can edit the message!',extra_tags='edit error')
        return redirect('/wall')
    else:
        errors=Message.objects.message_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/wall')
        else:
            print request.POST['msg']
            message=Message.objects.get(id=request.POST['msg'])
            message.content=request.POST['des']
            message.save()
            return redirect('/wall')

def remove_message(request):
    if Message.objects.get(id=request.POST['msg']).user_id.id != request.session['user_id']:
        messages.error(request,'Only author can delete the message!',extra_tags='delete error')
        return redirect('/wall')
    else:
        Message.objects.get(id=request.POST['msg']).delete()
        return redirect('/wall')

#==============================================================================
#                    comments add/modify/delete
#==============================================================================

def add_comment(request):
    errors=Comment.objects.message_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/wall')
    else:
        Comment.objects.create(user_id=User.objects.get(id=request.session['user_id']),content=request.POST['des'],message_id=Message.objects.get(id=request.POST['msg_id']))
        return redirect('/wall')