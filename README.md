# Ops-Dashboard Documentation

## Overview
The Ops Dashboard is a modern, real-time monitoring solution built with Flask and deployed on Kubernetes. It provides system metrics, Kubernetes cluster status, and application health monitoring with a responsive UI.

## Tech Stack
- Frontend: HTML5, TailwindCSS, Chart.js, Moment.js
- Backend: Python/Flask
- Container: Docker
- Orchestration: Kubernetes
- CI/CD: GitHub Actions

## Features
1. System Monitoring
   - CPU Usage
   - Memory Usage
   - Storage Metrics
   - Real-time Updates

2. Kubernetes Integration
   - Pod Status
   - Node Health
   - Deployment Status
   - Cluster Events

3. Application Health
   - Response Time
   - Error Rate
   - System Uptime
   - Live Performance Charts

## Setup Instructions

### Local Development
1. Clone the repository
```bash
git clone https://github.com/srikxcipher/ops-dash.git
cd ops-dash
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run locally
```bash
python -m app.main
```
Access at http://localhost:5000/

### Docker Build
1. Pull the image
```bash
docker pull srikant25/ops-dashboard:latest
```

2. Build the image
```bash
docker build -t srikant25/ops-dashboard:latest .
```

3. Run container
```bash
docker run -p 5000:5000 srikant25/ops-dashboard:latest
```

### Kubernetes Deployment (Minikube)

1. Start Minikube
```bash
minikube start
```

2. Apply RBAC (Required for Kubernetes metrics)
```bash
kubectl apply -f k8s/rbac.yaml
```

3. Deploy application
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

4. Verify deployment
```bash
kubectl get pods -l app=ops-dashboard
kubectl get svc ops-dashboard
```

5. Access the dashboard
```bash
minikube service ops-dashboard --url
```

### CI/CD Pipeline

- Configuration needed to be done on your GitHub Repository, goto Settings -> Security -> Secrets and Variables -> Actions | Here store your secrets.

1. Set up GitHub Secrets:
   - DOCKER_USERNAME: Your Docker Hub username
   - DOCKER_PASSWORD: Your Docker Hub password/token

2. Pipeline automatically:
   - Builds Docker image
   - Pushes to Docker Hub on main branch changes

## Application Architecture

1. Frontend Components:
   - Real-time metrics display
   - Interactive charts
   - Event logging
   - Health status indicators

2. Backend Routes:
   - /metrics - System metrics
   - /health - Application health
   - /k8s/status - Kubernetes status
   - /events - System events

3. Kubernetes Resources:
   - Deployment: 2 replicas for high availability
   - Service: NodePort for Minikube access
   - RBAC: Required permissions for metrics

## Monitoring Features

1. System Metrics:
   - CPU utilization percentage
   - Memory usage tracking
   - Storage capacity monitoring
   - Performance trends

2. Kubernetes Monitoring:
   - Pod status and health
   - Node conditions
   - Deployment status
   - Resource utilization

3. Application Metrics:
   - Response time tracking
   - Error rate monitoring
   - System uptime
   - Performance graphs

## Best Practices Implemented

1. Container Best Practices:
   - Multi-stage builds
   - Non-root user
   - Resource limits
   - Health checks

2. Kubernetes Best Practices:
   - Readiness/Liveness probes
   - Resource quotas
   - RBAC security
   - High availability setup

3. Monitoring Best Practices:
   - Real-time updates
   - Performance metrics
   - Error tracking
   - Event logging

## Troubleshooting

1. Container Issues:
```bash
# Check container logs
docker logs <container-id>

# Check container status
docker ps -a
```

2. Kubernetes Issues:
```bash
# Check pod logs
kubectl logs -l app=ops-dashboard

# Check pod status
kubectl describe pod -l app=ops-dashboard

# Check service
kubectl describe svc ops-dashboard
```

3. Application Issues:
   - Check browser console for frontend errors
   - Verify API endpoints are responding
   - Check Flask logs in container
   - Verify metrics collection

## References

1. Documentation:
   - Flask: https://flask.palletsprojects.com/
   - Kubernetes: https://kubernetes.io/docs/
   - Chart.js: https://www.chartjs.org/docs/
   - TailwindCSS: https://tailwindcss.com/docs

2. Tools:
   - Docker: https://docs.docker.com/
   - Minikube: https://minikube.sigs.k8s.io/docs/
   - GitHub Actions: https://docs.github.com/en/actions

## Security Considerations

1. Container Security:
   - Non-root user
   - Minimal base image
   - Updated dependencies
   - Resource limitations

2. Kubernetes Security:
   - RBAC implementation
   - Resource quotas
   - Network policies
   - Secure configurations

3. Application Security:
   - Environment variables
   - Error handling
   - Input validation
   - Secure communications
