from django.shortcuts import render

# Create your views here.
from .forms import SMSForm
from .models import SMSRecord
from .utils import send_sms

def send_sms_view(request):
    if request.method == "POST":
        form = SMSForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data["recipient"]
            message = form.cleaned_data["message"]

            # Send SMS
            response = send_sms(recipient, message)

            # Save SMS record
            SMSRecord.objects.create(
                recipient=recipient,
                message=message,
                status=response.get("status"),
            )

            return render(request, "sms/success.html", {"response": response})
    else:
        form = SMSForm()

    return render(request, "sms/send_sms.html", {"form": form})
