from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Creamos un contexto persistente para guardar cookies y login
    contexto = p.chromium.launch_persistent_context(
        user_data_dir="sesion_guardada",
        headless=False
    )
    pagina = contexto.new_page()
    pagina.goto("https://web.budgetbakers.com/")
    
    print("Abre el enlace único de tu correo en esta ventana.")
    print("Cuando hayas iniciado sesión y veas la página principal, vuelve aquí y presiona ENTER...")
    input()
    
    print("Sesión guardada.")
    contexto.close()
