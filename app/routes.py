from flask import Blueprint, render_template, jsonify
import psutil
import platform
import datetime

bp = Blueprint("main", __name__)

@bp.route('/')
def index():
    return render_template("index.html")

@bp.route('/status')
def status():
    # Simulated service statuses
    services = {
        "PostgreSQL": "Running",
        "Redis": "Running",
        "RabbitMQ": "Stopped",
        "API Gateway": "Running"
    }
    return jsonify(services)

@bp.route('/healthz')
def healthz():
    return jsonify({"status": "healthy"}), 200

@bp.route('/metrics')
def metrics():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    return jsonify({
        "cpu_usage_percent": cpu,
        "memory_used_mb": round(memory.used / (1024 * 1024), 2),
        "memory_total_mb": round(memory.total / (1024 * 1024), 2),
        "os": platform.system(),
        "uptime": str(datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time()))
    })
