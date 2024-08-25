from django.shortcuts import render, get_object_or_404, redirect
from .models import EspacoCoworking, Reserva
from .forms import ReservaForm
from django.contrib import messages


# reservas/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import EspacoCoworking, Reserva
from .forms import ReservaForm
from django.contrib import messages


def detalhe_espaco(request, espaco_id):
    espaco = get_object_or_404(EspacoCoworking, id=espaco_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, espaco=espaco)

        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.espaco = espaco  # Associa a reserva ao espaço de coworking correto
            reserva.usuario = request.user
            print(f"Reserva: {reserva}, Espaço: {
                  reserva.espaco}, Usuário: {reserva.usuario}")  # Debug
            reserva.save()
            messages.success(request, 'Reserva feita com sucesso!')
            return redirect('lista_espacos')
    else:
        form = ReservaForm()
    return render(request, 'reservas/detalhe_espaco.html', {'espaco': espaco, 'form': form})


def lista_espacos(request):
    espacos = EspacoCoworking.objects.all()
    return render(request, 'reservas/lista_espacos.html', {'espacos': espacos})
