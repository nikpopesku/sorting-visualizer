from django.shortcuts import render


def homepage(request):
    """Render homepage."""
    return render(request, "homepage.html")
