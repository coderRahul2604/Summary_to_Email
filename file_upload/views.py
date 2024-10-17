from django.shortcuts import render
from django.core.mail import send_mail
from file_upload.forms import UploadFileForm
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)  # Adjust according to the file format

            # Generate summary report
            summary = data.describe().to_string()

            # Send summary via email
            send_mail(
                subject=f'Python Assignment - {request.user.username}',
                message=summary,
                from_email='rahulvthorat777@gmail.com',
                recipient_list=['rahulvthorat777@gmail.com']
            )

            return render(request, 'file_upload/success.html', {'summary': summary})
    else:
        form = UploadFileForm()
    return render(request, 'file_upload/upload.html', {'form': form})
