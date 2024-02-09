from django.shortcuts import render, redirect
from .forms import ConfirmDeleteForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


# resource
# https://docs.djangoproject.com/en/4.2/topics/forms/#:~:text=,and%20Form%20and%20field%20validation
# https://docs.djangoproject.com/en/4.2/ref/forms/
# https://docs.djangoproject.com/en/4.2/ref/forms/api/#:~:text=,set%20of%20data%2C%20or%20unbound
# https://docs.djangoproject.com/en/4.2/ref/forms/fields/

@login_required
def confirm_delete_account(request):
    if request.method == 'POST':
        form = ConfirmDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            request.user.delete()
            messages.success(request, 'Account successfully deleted.')
            return redirect('home')
    else:
        form = ConfirmDeleteForm()

    return render(request, 'includes/confirm_delete.html', {'form': form})
