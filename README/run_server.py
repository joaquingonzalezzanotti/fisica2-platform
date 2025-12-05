"""
Servidor local para Fisica II.
Arranca http.server en el puerto 5500 y abre el navegador en index.html.
Pensado para compilarse a .exe con PyInstaller o ejecutarse con Python.
"""

from __future__ import annotations

import http.server
import os
import socket
import socketserver
import sys
import threading
import webbrowser
from pathlib import Path


PORT = 5500

# Cuando es un exe (PyInstaller), __file__ apunta al bundle; usamos sys.executable.
if getattr(sys, "frozen", False):
    ROOT = Path(sys.executable).resolve().parent
else:
    ROOT = Path(__file__).resolve().parent


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    """Sirve archivos estaticos desde ROOT sin log en stdout."""

    def log_message(self, format: str, *args) -> None:  # noqa: A003
        # Silencia el log para una ejecucion mas limpia
        return


def run_server() -> socketserver.TCPServer:
    handler = QuietHandler
    handler.directory = str(ROOT)
    # Allow address reuse to relanzar sin esperar
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    return httpd


def hide_console_window() -> None:
    """Oculta la ventana de consola en Windows cuando corre como exe."""
    if os.name != "nt":
        return
    try:
        import ctypes

        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 0)  # SW_HIDE
    except Exception:
        # Si falla no es grave; dejamos la consola visible.
        return


def start():
    httpd = run_server()
    url = f"http://127.0.0.1:{PORT}/index.html"

    def serve():
        with httpd:
            httpd.serve_forever()

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()
    webbrowser.open(url)
    print(f"Servidor listo en {url} (Ctrl+C para detener)")

    try:
        while thread.is_alive():
            thread.join(0.5)
    except KeyboardInterrupt:
        print("\nDeteniendo servidor...")
        httpd.shutdown()


if __name__ == "__main__":
    # Ajusta cwd al ROOT para rutas relativas
    os.chdir(ROOT)
    if getattr(sys, "frozen", False):
        hide_console_window()
    start()
