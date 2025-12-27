from .models import Category
from about.models import SocialLink
def get_categories(request):
    category=Category.objects.all().order_by('updated_at')
    return dict(category=category)

def get_sociallink(request):
    socialLink=SocialLink.objects.all()
    return dict(socialLink=socialLink)
