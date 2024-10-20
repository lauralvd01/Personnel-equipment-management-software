from django.shortcuts import redirect

class RestrictViewMiddleware:
    def init(self, get_response):
        self.get_response = get_response

    def call(self, request):
        restricted_paths = [
            '/vistaMecanico/', 
            '/vistaJefeMotores/',    # Agrega aquí las otras rutas que deseas restringir
        ]

        if request.path in restricted_paths:
            return redirect('/')  # 'home' debe ser el nombre de tu vista home en urls.py

        response = self.get_response(request)
        return response