import json
import os
import socket
import subprocess
import sys
from urllib.error import URLError
from urllib.request import urlopen


HOST = "127.0.0.1"
PORT = 8000
HEALTH_URL = f"http://{HOST}:{PORT}/api/health"


def port_is_open() -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        return sock.connect_ex((HOST, PORT)) == 0


def backend_is_healthy() -> bool:
    try:
        with urlopen(HEALTH_URL, timeout=1) as response:
            data = json.loads(response.read().decode("utf-8"))
            return response.status == 200 and data.get("status") == "ok"
    except (OSError, URLError, json.JSONDecodeError):
        return False


def uvicorn_command() -> list[str]:
    local_uvicorn = os.path.join(".venv", "bin", "uvicorn")
    if os.path.exists(local_uvicorn):
        return [local_uvicorn]
    return [sys.executable, "-m", "uvicorn"]


if port_is_open():
    if backend_is_healthy():
        print(f"Backend already running at {HEALTH_URL}")
        sys.exit(0)

    print(f"Port {PORT} is already in use, but {HEALTH_URL} is not responding as this backend.", file=sys.stderr)
    print("Stop the process using port 8000, then run `npm run dev:backend` again.", file=sys.stderr)
    sys.exit(1)


command = [
    *uvicorn_command(),
    "app.main:app",
    "--reload",
    "--host",
    HOST,
    "--port",
    str(PORT),
    "--env-file",
    ".env",
]

raise SystemExit(subprocess.call(command))
