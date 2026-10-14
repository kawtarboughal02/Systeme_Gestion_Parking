"""
Capture automatique des captures d'ecran des interfaces de l'application.
- Demarre le serveur Django de developpement.
- Utilise Playwright (Chromium) pour visiter les pages et les photographier.
- Arrete le serveur a la fin.

Usage : python capture_screenshots.py
"""
import os
import sys
import time
import subprocess
import socket

PROJ_DIR = os.path.dirname(os.path.abspath(__file__))
SHOT_DIR = os.path.join(PROJ_DIR, "docs", "screenshots")
os.makedirs(SHOT_DIR, exist_ok=True)

BASE = "http://127.0.0.1:8021"


def wait_for_port(host, port, timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((host, port)) == 0:
                return True
        time.sleep(0.5)
    return False


def main():
    from playwright.sync_api import sync_playwright

    env = dict(os.environ)
    env["DJANGO_SETTINGS_MODULE"] = "Systeme_Gestion_Parking.settings"

    # 1) Demarrer le serveur Django
    server = subprocess.Popen(
        [sys.executable, "manage.py", "runserver", "127.0.0.1:8021", "--noreload"],
        cwd=PROJ_DIR,
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print(f"Serveur Django demarre (PID {server.pid})")

    try:
        if not wait_for_port("127.0.0.1", 8021, timeout=30):
            print("ERREUR : le serveur n'a pas demarre a temps.")
            return
        print("Serveur en ecoute sur le port 8021.")

        # Pages publiques + pages du back-office (accessibles directement)
        pages = [
            ("/", "01_accueil.png"),
            ("/About", "02_about.png"),
            ("/Login", "03_login.png"),
            ("/Registration", "04_registration.png"),
            ("/Dashboard", "05_dashboard.png"),
            ("/ListeClients", "06_liste_clients.png"),
            ("/AjouterClient", "07_ajouter_client.png"),
            ("/ListeReservation", "08_liste_reservations.png"),
            ("/AjouterReservation", "09_ajouter_reservation.png"),
            ("/ListePlacesLibres", "10_liste_places.png"),
            ("/AjouterPlacesLibres", "11_ajouter_places.png"),
            ("/ListeAbonnement", "12_liste_abonnements.png"),
            ("/AjouterAbonnement", "13_ajouter_abonnement.png"),
        ]

        with sync_playwright() as pw:
            # Utilise le Chrome deja installe sur le systeme (pas de telechargement
            # supplementaire de Chromium). Repli sur le Chromium fourni par
            # Playwright si le Chrome systeme n'est pas disponible.
            try:
                browser = pw.chromium.launch(channel="chrome")
            except Exception:
                browser = pw.chromium.launch()
            context = browser.new_context(viewport={"width": 1366, "height": 950})
            page = context.new_page()
            for url, name in pages:
                full = BASE + url
                try:
                    page.goto(full, wait_until="networkidle", timeout=20000)
                    page.wait_for_timeout(700)
                    page.screenshot(path=os.path.join(SHOT_DIR, name), full_page=True)
                    print(f"Capture OK : {name}  ({url})")
                except Exception as e:
                    print(f"Capture ECHEC : {url} -> {e}")
            browser.close()
    finally:
        server.terminate()
        try:
            server.wait(timeout=10)
        except Exception:
            server.kill()
        print("Serveur Django arrete.")


if __name__ == "__main__":
    main()
