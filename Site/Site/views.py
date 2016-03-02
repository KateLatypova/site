from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from visits.models import Visit


def index_page(request):
    return render(request, 'index.html', {})


def check_autorizovanem(request):  # Недоработанное место, нет перекида на РЕФЕРЕР в случае чего (смотри JS)
    if request.method == 'GET':
        if request.is_ajax():
            return HttpResponse(request.user.is_authenticated())
    return HttpResponse(request.META['HTTP_REFERER'])

# Terrible function
def hits_page(request):
    hits_by_ip = {}
    final_list_by_ip = []
    all_hits = Visit.objects.all()
    ip_addrs = set([visitor.ip_address for visitor in all_hits])
    for ip_addr in ip_addrs:
        visits_by_ip = Visit.objects.filter(ip_address=ip_addr)
        num_hits = 0
        for visit_by_ip in visits_by_ip:
            num_hits += visit_by_ip.visits
        last_visit = timezone.localtime(visits_by_ip.order_by('-last_visit')[0].last_visit)
        hits_by_ip[ip_addr] = [last_visit, num_hits]
    for key in sorted(hits_by_ip, key=lambda k: hits_by_ip[k][0], reverse=True):
        final_list_by_ip.append([key, hits_by_ip[key][0], hits_by_ip[key][1]])
    return render(request, 'hitsPage.html', {'hits_by_ip': final_list_by_ip})


def visits_page(request, ip_address):
    all_visits_by_ip = Visit.objects.filter(ip_address=ip_address).order_by('-last_visit')
    for visit_by_ip in all_visits_by_ip:
        if visit_by_ip.last_visit:
            visit_by_ip.last_visit = timezone.localtime(visit_by_ip.last_visit)
    return render(request, 'visitsPage.html', {'all_visits_by_ip': all_visits_by_ip})