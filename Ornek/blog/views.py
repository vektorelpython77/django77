from django.shortcuts import render
from .models import BlogModel
# apikey 3CWVwRQkq1aTesIyx3aKKQ:1JjiM4Er0w4fGVhglvPH4f
def listele(request):

    data = apiGet()
    bloglar = BlogModel.objects.all() #ORM
    ########### apiden gelen veriyi ayıkla

    ################
    return render(request,"blog/listele.html",{"postlar":bloglar,"data":data})

def apiGet():
    import http.client

    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 3CWVwRQkq1aTesIyx3aKKQ:1JjiM4Er0w4fGVhglvPH4f"
        }

    conn.request("GET", "/economy/currencyToAll?int=10&base=USD", headers=headers)

    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")
    print(data.decode("utf-8"))