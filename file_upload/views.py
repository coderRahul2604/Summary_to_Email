from django.shortcuts import render
from django.core.mail import send_mail
from file_upload.forms import UploadFileForm
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            file = request.FILES['file']
            recipient_email = form.cleaned_data['email']

            # Read the file and generate a summary report
            data = pd.read_excel(file)
            summary = data.describe().to_string()

            
            send_mail(
                subject=f'Summary Report - {request.user.username}',
                message=summary,
                from_email='dypef2024@gmail.com',
                recipient_list=[recipient_email], 
            )

            return render(request, 'file_upload/success.html', {'summary': summary})
    else:
        form = UploadFileForm()

    return render(request, 'file_upload/upload.html', {'form': form})

