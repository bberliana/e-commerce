from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Rania Berliana',
        'kelas' : 'PBP B',
        'name' : 'Jodie Handbag',
        'price': '30000000',
        'description': 'A beautiful handbag made from the finest leather',
        'size': 'S',
        'color': 'Beige'
    }

    return render(request, "main.html", context)