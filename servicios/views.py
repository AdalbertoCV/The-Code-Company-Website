from django.shortcuts import render

def servicios(request):
    servicios = [
        {
            'nombre': 'Desarrollo web',
            'descripcion': 'Creamos sitios web personalizados y escalables utilizando el framework más conocido "Django". Nuestro equipo de expertos altamente calificado en desarrollo web se encargará de crear una presencia en línea efectiva para tu negocio, brindando una experiencia de usuario excepcional y funcionalidades muy avanzadas.',
        },
        {
            'nombre': 'Análisis de datos',
            'descripcion': 'Recolectamos, procesamos y visualizamos datos para obtener información valiosa. Utilizamos técnicas y herramientas de análisis de datos para descubrir patrones, tendencias y conocimientos ocultos en tus conjuntos de datos, lo que te ayudará a tomar decisiones informadas y estratégicas.',
        },
        {
            'nombre': 'Videojuegos',
            'descripcion': 'Desarrollamos emocionantes y excelentes videojuegos para diversas plataformas. Nuestro equipo de desarrollo de videojuegos crea experiencias interactivas, originales y envolventes, desde juegos para dispositivos móviles hasta juegos en consola como Playstation y Xbox, brindando entretenimiento y diversión a los usuarios.',
        },
        {
            'nombre': 'Aplicaciones empresariales',
            'descripcion': 'Creamos aplicaciones a medida para diferentes áreas empresariales. Nuestras soluciones de software personalizadas ayudan a optimizar los procesos empresariales, mejorar la eficiencia y potenciar el crecimiento de tu empresa, en el cual está se adapta a tus necesidades y requisitos específicos que se tengan.',
        },
        {
            'nombre': 'Diseño gráfico',
            'descripcion': 'Ofrecemos servicios de diseño gráfico para logotipos, etiquetas, infografías y más. Nuestro equipo de diseñadores gráficos los cuales son altamente creativos y talentosos, transformarán tu idea que tienes en cabeza en diseños atractivos y profesionales en el cual llamarán la atención de tu audiencia.',
        },
        {
            'nombre': 'Marketing digital',
            'descripcion': 'Ayudamos a impulsar tu presencia en línea y a alcanzar a tu audiencia objetivo. Nuestros servicios de marketing digital incluyen estrategias de SEO, publicidad en línea, gestión de redes sociales y más, todo diseñado para aumentar tus vistas y mejorar tu presencia digital.',
        },
        {
            'nombre': 'Desarrollo de aplicaciones móviles',
            'descripcion': 'Creamos aplicaciones móviles de calidad para el sistema de iOS y Android, si necesitas una aplicación para tu negocio o una idea innovadora que llego a tu cabeza, nuestro equipo de desarrollo de aplicaciones móviles te dará soluciones personalizadas y funcionales que brillarán en el mercado.',
        },
        {
            'nombre': 'Consultoría tecnológica',
            'descripcion': 'Proporcionamos servicios de consultoría tecnológica para ayudarte a tomar decisiones estratégicas y aprovechar al máximo la tecnología. Nuestros altamente expertos analizarán tus necesidades, evaluarán tus sistemas y procesos actuales, y te ayudarán sobre las soluciones tecnológicas más correctas y adecuadas para tu negocio.',
        },
        {
            'nombre': 'Desarrollo de comercio electrónico',
            'descripcion': 'Creamos tiendas en línea atractivas y funcionales para impulsar tus ventas en línea. Nuestro equipo de desarrollo altamente especializados en comercio electrónico se encargará de crear una plataforma de comercio electrónico personalizada que cumpla con tus requerimientos específicos y le brinde una experiencia de compra excepcional a tus clientes que usaran tu sitio Web.',
        }
    ]

    return render(request, 'servicios.html', {'servicios': servicios})
