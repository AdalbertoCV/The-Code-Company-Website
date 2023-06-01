from django.shortcuts import render

def mision(request):
    return render(request, 'mision.html')

def vision(request):
    puntos = [
        {
            'descripcion': 'Ser un líder mundial en el desarrollo de soluciones de software innovadoras.',
        },
        {
            'descripcion': 'Proporcionar soluciones de software que mejoren la calidad de vida de las personas.',
        },
        {
            'descripcion': 'Ser una empresa cuyos servicios puedan ser fácilmente accesibles a la mayoría de los clientes.',
        },
        {
            'descripcion': 'Crear software de calidad y original.',
        },

    ]

    return render(request, 'vision.html', {'puntos': puntos})

def valores(request):
    valores = [
        {
            'nombre': 'Innovación',
            'descripcion': 'Nos comprometemos a tener una dedicación constante a la búsqueda de nuevas ideas y soluciones de software para el mundo.',
        },
        {
            'nombre': 'Excelencia',
            'descripcion': 'Nos comprometemos a tener responsabilidad con la calidad y la excelencia en todos los aspectos de la empresa, desde el desarrollo de software hasta el servicio al cliente.',
        },
        {
            'nombre': 'Integridad',
            'descripcion': 'Nos comprometemos a tener una conducta ética y transparente en todas las interacciones con los clientes, empleados, accionistas y la sociedad en general.',
        },
        {
            'nombre': 'Colaboración',
            'descripcion': 'Nos comprometemos a tener una cultura de trabajo en equipo y apoyo mutuo para alcanzar objetivos comunes.',
        },
        {
            'nombre': 'Responsabilidad social',
            'descripcion': 'Nos comprometemos a involucrarnos con el desarrollo sostenible y la contribución positiva a la sociedad y el medio ambiente.',
        },
        {
            'nombre': 'Diversidad e inclusión',
            'descripcion': 'Nos comprometemos a tener una valoración y apreciación de la diversidad en todas sus formas y con la creación de un entorno inclusivo.',
        },
        {
            'nombre': 'Calidad',
            'descripcion': 'la empresa se compromete a entregar productos que cumplan las expectativas de los clientes.',
        }
    ]

    return render(request, 'valores.html', {'valores': valores})
