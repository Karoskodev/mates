from django.shortcuts import render, reverse, redirect
from .forms import GiveawayForm
from django.contrib import messages


def giveaway_form(request):
    """ giveaway form view """

    template = 'giveaway/giveaway.html'
    form = GiveawayForm()

    if request.method == 'POST':
        form = GiveawayForm(request.POST)
        if form.is_valid():
            giveaway = form.save(commit=False)
            giveaway.user = request.user
            giveaway.save()
            messages.success(request, "Answer submited.")
            return redirect(reverse("giveaway_form"))
        else:
            messages.error(request, "Failed to submit the answer!")

    context = {
        "form": form,
    }
    return render(request, template, context)
