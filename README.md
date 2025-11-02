# FILE: README.md

# Resource Monitoring Dashboard for Cloud Applications

**Course:** Menaxhimi i Burimeve në Cloud Computing (Cloud Resource Management)  
**Project:** Lab 1 - 2025/26  
**Group:** 5  
**Members:** Endrit Gjoka, Bleron Morina, Rukije Morina

---

## 1. Project Description

This project implements a real-time, web-based dashboard for monitoring the resource utilization (CPU, Memory, Network I/O) of Docker containers. The system is designed to be dynamic and scalable, automatically discovering and monitoring any new containers that are launched on the host system.

The primary goal is to provide a clear, visual tool for administrators and developers to observe the performance and health of their containerized applications, enabling them to diagnose issues, optimize resource allocation, and ensure system stability.

## 2. Architecture

The system is built on a modern, cloud-native monitoring stack, with each component running as a separate Docker container for portability and easy management.

```
+------------------------+      +--------------------------+      +-------------------------+
|   User (Web Browser)   |----->|   Flask Web UI (Port 5000) |----->|  Grafana UI (Port 3000) |
+------------------------+      +--------------------------+      +-------------------------+
                                          (embeds)                           | (queries data)
                                                                             |
                                                                             v
+------------------------+      +--------------------------+      +--------------------------+
| Docker Host (Windows)  |      | cAdvisor (collects metrics)|<-----|  Prometheus (Port 9090)  |
| +--------------------+ |      +--------------------------+      | (scrapes & stores metrics)|
| | Container 1 (App)  | |                                        +--------------------------+
| | Container 2 (DB)   | |<-- watches Docker socket                 ^          ^
| | ...                | |                                          |          | (discovers)
| +--------------------+ |      +--------------------------+         |          |
+------------------------+      |  Docker-SD-Adapter       |---------+          +-------------+
                                +--------------------------+                    | windows_exporter |
                               (provides container list)                      (host metrics)
                                                                                +-------------+
```

### Technology Stack:

- **Docker & Docker Compose:** For containerizing and orchestrating all services.
- **Prometheus:** The core time-series database for collecting and storing metrics.
- **Grafana:** For querying Prometheus and visualizing the data in a rich, interactive dashboard.
- **cAdvisor:** A service that collects performance metrics from every running container on the host.
- **Docker-SD-Adapter:** A helper service that enables Prometheus to automatically discover new containers.
- **Flask:** A Python web framework used to build a professional, user-friendly frontend to present the dashboard.
- **windows_exporter:** To collect performance metrics from the Windows host machine.

## 3. How to Run the Project

**Prerequisites:**

- Docker Desktop for Windows
- Windows Exporter installed and running on the host.

**Steps:**

1.  **Clone the repository.**
2.  **Build the test application container:**
    ```bash
    cd sample-apps/flask-test-app
    docker build -t test-app .
    cd ../..
    ```
3.  **Launch the entire monitoring stack:**
    ```bash
    docker-compose up -d
    ```
4.  **Launch the test application container:**
    ```bash
    docker run --name my-test-app -p 5001:5000 -d test-app
    ```
5.  **Access the Dashboard:**

    - Open your browser to **`http://localhost:5000`**.

6.  **Generate Load:**
    - Access the test application at `http://localhost:5001` and click the links to generate CPU and Memory load, then observe the changes on the main dashboard.

## 4. Cleaning Up

To stop and remove all containers, run:

```bash
docker-compose down
```
