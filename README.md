# Real-Time Container and Host Monitoring Dashboard

**Course:** Cloud Resource Management  
**Project:** Lab 1 - 2025/26  
**Group:** 5
**Members:** Endrit Gjoka, Bleron Morina, Rukije Morina

---

## 1. Project Overview

This project provides a sophisticated, real-time dashboard for monitoring the resource utilization (CPU, Memory, Network, Disk I/O) of Docker containers and their underlying host machine. Built on a powerful open-source stack, the system automatically discovers and monitors all running containers, offering deep insights into application performance and system health.

The primary goal is to deliver a professional-grade, visual tool for administrators and developers to diagnose performance issues, optimize resource allocation, and ensure system stability in a containerized environment. This enhanced version integrates all components into a single, easy-to-deploy stack.

## 2. System Architecture

The architecture uses a set of containerized services, orchestrated by Docker Compose, to provide a seamless monitoring experience.

```
+------------------------+      +--------------------------+      +---------------------------+
|   User (Web Browser)   |----->|  Monitoring UI (Flask)   |----->|   Grafana Dashboard       |
| http://localhost:5000  |      |      (Port 5000)         |      |   (embedded, Port 3000)   |
+------------------------+      +--------------------------+      +---------------------------+
                                                                             | (queries data via PromQL)
                                                                             v
+-------------------------------------------------------------+      +---------------------------+
| Docker Host (Windows w/ Docker Desktop)                     |      |  Prometheus Server        |
|                                                             |----->|   (scrapes & stores       |
| +-------------------------+  +-------------------------+    |      |    metrics, Port 9090)    |
| | cAdvisor                |  | windows_exporter        |    |      +---------------------------+
| | (container metrics)     |  | (host OS metrics)       |    |                 ^
| +-------------------------+  +-------------------------+    |                 | (scrapes metrics from)
|                                                             |-----------------+
| +-------------------------+  +-------------------------+    |
| | Container 1 (test-app)  |  | Container 2 (e.g. db)   |    |
| +-------------------------+  +-------------------------+    |
+-------------------------------------------------------------+

```

### Technology Stack:

- **Docker & Docker Compose:** For containerizing and orchestrating all services.
- **Prometheus:** A powerful time-series database for collecting and storing metrics. It scrapes data from cAdvisor, the Windows Exporter, and other instrumented applications.
- **Grafana:** The industry standard for visualizing time-series data. It queries Prometheus to generate the rich, interactive dashboards.
- **cAdvisor:** Deployed as a container, it automatically collects detailed performance metrics from every other container running on the host.
- **Windows Exporter:** A Prometheus exporter that provides extensive metrics about the Windows host OS, including CPU, memory, disk, and network statistics.
- **Flask:** A Python web framework used to build a professional frontend for the dashboard and to create a sample test application for generating load.

## 3. How to Run the Project

**Prerequisites:**

- Docker Desktop for Windows installed and running.

**Steps:**

1.  **Clone the repository.**
2.  **Launch the entire monitoring stack with a single command:**
    From the root directory of the project, run:

    ```bash
    docker-compose up -d
    ```

    This command will build the necessary images and start all services (Prometheus, Grafana, cAdvisor, Windows Exporter, the UI, and the test app) in the background.

3.  **Access the Main Dashboard:**

    - Open your web browser and navigate to **`http://localhost:5000`**.

4.  **Generate Load and Observe:**
    - In a separate browser tab, open the test application at **`http://localhost:5001`**.
    - Use the buttons on the test app to generate CPU, memory, and other types of load.
    - Observe the real-time changes on the main monitoring dashboard. The dashboard will automatically detect the `test-app` container.

## 4. Cleaning Up

To stop and remove all containers, networks, and volumes created by the project, run:

```bash
docker-compose down
```
