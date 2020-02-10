from django.shortcuts import render
from school.models import Pre_primary, Lower_primary, Upper_primary


def message(request):
    context = {
        "message": Pre_primary.objects.all(),
        "message_one": Lower_primary.objects.all(),
        "message_two": Upper_primary.objects.all()
    }
    context_one = {

    }
    return render(request, 'messaging/send_message.html', context)
