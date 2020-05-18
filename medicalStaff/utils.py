from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa
import os
from django.conf import settings
from django.conf.urls.static import static


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
def fetch_resources(uri, rel):
    path = join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    return path
