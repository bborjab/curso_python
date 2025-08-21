import pandas as pd
from playwright.sync_api import sync_playwright
import time
import { test, expect } from '@playwright/test';

# Ruta del archivo Excel
archivo_excel = "datos.xlsx"

# Leemos el Excel
df = pd.read_excel(archivo_excel)

with sync_playwright() as p:
    # Abrimos el navegador con la sesión guardada
    contexto = p.chromium.launch_persistent_context(
        user_data_dir="sesion_guardada",
        headless=False
    )
    pagina = contexto.new_page()

    # Vamos a la página donde se llenan los datos
    for _, fila in df.iterrows():
        pagina.goto("https://web.budgetbakers.com/")

        pagina.get_by_role("button", name="＋ Record").click()
        # Llenar campos (ajusta los selectores según tu HTML real)
        pagina.fill('input[name="nombre"]', str(fila["nombre"]))
        pagina.fill('input[name="email"]', str(fila["email"]))

        # Enviar el formulario
        pagina.click('button[type="submit"]')
        pagina.wait_for_load_state("networkidle")

        print(f"Registro enviado: {fila['nombre']}")
        time.sleep(1)  # Pequeña pausa para evitar bloqueos

    contexto.close()
