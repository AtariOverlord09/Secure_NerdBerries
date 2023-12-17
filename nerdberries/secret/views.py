from os import replace
import subprocess

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from secret.forms import PingForm

@csrf_exempt
def ping_site(request):
    if request.method == 'POST':
        form = PingForm(request.POST)
        if form.is_valid():
            site_url = form.cleaned_data['site_url']
            try:
                # Use shlex.split to safely split the command into a list.
                command = ['ping', str(site_url)]
                result = subprocess.check_output(command, encoding='utf-8', errors='replace')
            except subprocess.CalledProcessError:
                result = 'Введите команду верно!'
        else:
            result = 'Форма содержит ошибки.'
    else:
        form = PingForm()
        result = None

    return render(request, 'secret/ping.html', {'form': form, 'result': result, 'error': result})
