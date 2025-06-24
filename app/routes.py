from flask import Blueprint, render_template, jsonify
import psutil
import platform
import datetime
import time
import os

bp = Blueprint("main", __name__)

start_time = time.time()

def get_system_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return {
        "system": {
            "cpu": round(cpu_percent, 1),
            "memory": round(memory.percent, 1),
            "storage": round(disk.percent, 1)
        },
        "performance": {
            "cpu": round(cpu_percent, 1),
            "memory": round(memory.percent, 1)
        }
    }

def get_uptime():
    uptime_seconds = time.time() - start_time
    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(days)}d {int(hours)}h {int(minutes)}m"

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
    return jsonify(get_system_metrics())

@bp.route('/health')
def health():
    # Get real response time by measuring CPU usage briefly
    response_time = round(psutil.cpu_percent(interval=0.1), 1)
    error_rate = round(psutil.virtual_memory().percent / 100, 2)  # Using memory % as simulated error rate
    
    return jsonify({
        "status": "healthy",
        "responseTime": response_time,
        "errorRate": error_rate,
        "uptime": get_uptime()
    })

@bp.route('/k8s/status')
def k8s_status():
    # Simulated K8s data using system metrics
    return jsonify({
        "pods": f"{psutil.cpu_count()} / {psutil.cpu_count()}",
        "nodes": "Healthy",
        "deployments": str(len(psutil.Process().children()))
    })

@bp.route('/events')
def events():
    # Real system events based on metrics
    cpu_percent = psutil.cpu_percent(interval=0.1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    events = []
    
    if cpu_percent > 80:
        events.append({
            "type": "Warning",
            "message": f"High CPU usage detected: {cpu_percent}%",
            "timestamp": datetime.datetime.now().isoformat()
        })
        
    if memory.percent > 80:
        events.append({
            "type": "Warning",
            "message": f"High memory usage detected: {memory.percent}%",
            "timestamp": datetime.datetime.now().isoformat()
        })
        
    if disk.percent > 80:
        events.append({
            "type": "Warning",
            "message": f"High disk usage detected: {disk.percent}%",
            "timestamp": datetime.datetime.now().isoformat()
        })
        
    if not events:
        events.append({
            "type": "Info",
            "message": "All systems operating normally",
            "timestamp": datetime.datetime.now().isoformat()
        })
        
    return jsonify(events)
