from django.shortcuts import render,redirect
from .models import Curso
from django.contrib import messages
# Create your views here.

def home(request):
    cursosListados = Curso.objects.all()
    
    return render(request, 'GestionCursos.html', {'cursos':cursosListados})


def contacto(request):
    

    return render(request, 'Contacto.html')


def registrarCurso(request):
    curso_existe = False
    if request.method == 'POST':
        codigo=request.POST['txtcodigo']
        nombre=request.POST['txtnombre']
        creditos=request.POST['numcreditos']
        
        curso_existe = Curso.objects.filter(codigo__iexact=codigo).exists()
        if curso_existe:
            messages.error(request, "El código del Curso ya existe")
            return redirect('/')
        else:
            Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
            messages.success(request, "Curso Registrado Correctamente")
            return redirect('/')
    return render(request, 'GestionCursos.html', {'curso_existe': curso_existe})



def edicionCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'edicionCurso.html', {'curso':curso})

def editarCurso(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    creditos=request.POST['numcreditos']
    
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    messages.success(request, "Curso editado correctamente")
    return redirect('/')
    

def eliminarCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, "Curso eliminado correctamente")
    return redirect('/')

def custom_404(request, exception):
    return render(request, '404.html', status=404)
    
