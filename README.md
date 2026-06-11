\# Archive Migration DevOps Lab



A small DevOps learning project that simulates the basic operation of an archive migration service.



The project is built to practice core infrastructure topics such as web application operation, Docker containerization, health checks, automated testing and later database integration, CI/CD, backup and orchestration basics.



\## Project Goal



This project demonstrates how a small web application can be developed, tested and operated in a containerized environment.



The application currently provides a simple FastAPI service with basic endpoints for health monitoring and example archive migration data. It is intended as a practical learning lab for DevOps and system administration fundamentals.



\## Current Features



\* FastAPI web application

\* Basic API root endpoint

\* Health check endpoint

\* Example endpoint for archive document metadata

\* Automated test with pytest

\* Dockerfile for containerizing the application

\* Docker Compose setup for running the web service

\* Project structure prepared for future database, CI/CD, Kubernetes and Ansible extensions



\## Tech Stack



\* Python 3.12

\* FastAPI

\* Uvicorn

\* Pytest

\* Docker

\* Docker Compose

\* Git / GitHub



\## Project Structure



```text

archive-migration-devops-lab/

│

├── app/

│   ├── \_\_init\_\_.py

│   ├── main.py

│   ├── database.py

│   ├── models.py

│   ├── schemas.py

│   └── crud.py

│

├── tests/

│   └── test\_health.py

│

├── docs/

│   ├── architecture.md

│   └── migration\_process.md

│

├── scripts/

│   └── backup\_postgres.ps1

│

├── .github/

│   └── workflows/

│       └── ci.yml

│

├── k8s/

│   ├── deployment.yaml

│   └── service.yaml

│

├── ansible/

│   ├── inventory.ini

│   └── setup.yml

│

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── pytest.ini

├── .gitignore

└── README.md

```



\## API Endpoints



| Method | Endpoint     | Description                                             |

| ------ | ------------ | ------------------------------------------------------- |

| GET    | `/`          | Returns a basic service status message                  |

| GET    | `/health`    | Returns the health status of the application            |

| GET    | `/documents` | Returns example archive migration document metadata     |

| GET    | `/docs`      | Opens the automatically generated FastAPI documentation |



\## Example Response



\### `GET /health`



```json

{

&#x20; "status": "ok"

}

```



\### `GET /documents`



```json

\[

&#x20; {

&#x20;   "document\_id": "DOC-1001",

&#x20;   "source\_system": "old\_archive",

&#x20;   "target\_system": "new\_archive",

&#x20;   "file\_name": "invoice\_2024\_001.pdf",

&#x20;   "status": "pending"

&#x20; },

&#x20; {

&#x20;   "document\_id": "DOC-1002",

&#x20;   "source\_system": "old\_archive",

&#x20;   "target\_system": "new\_archive",

&#x20;   "file\_name": "contract\_2024\_002.pdf",

&#x20;   "status": "success"

&#x20; }

]

```



\## Run Locally Without Docker



Create and activate a virtual environment:



```powershell

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

```



Install dependencies:



```powershell

pip install -r requirements.txt

```



Start the FastAPI application:



```powershell

uvicorn app.main:app --reload

```



Open the application:



```text

http://127.0.0.1:8000

```



Open the API documentation:



```text

http://127.0.0.1:8000/docs

```



\## Run With Docker Compose



Build and start the container:



```powershell

docker compose up --build

```



Open the application:



```text

http://localhost:8000

```



Open the health check:



```text

http://localhost:8000/health

```



Open the API documentation:



```text

http://localhost:8000/docs

```



Stop the running service:



```powershell

CTRL + C

docker compose down

```



\## Run Tests



```powershell

pytest

```



Expected result:



```text

1 passed

```



\## Docker Setup



The project contains a Dockerfile that builds a Python-based image and starts the FastAPI application with Uvicorn.



The Docker Compose setup currently starts one service:



| Service | Description                              |

| ------- | ---------------------------------------- |

| `web`   | FastAPI application running on port 8000 |



Current port mapping:



```text

localhost:8000 -> container:8000

```



\## Current Development Status



Completed:



\* FastAPI project setup

\* Health check endpoint

\* Example document metadata endpoint

\* Pytest health check test

\* Dockerfile

\* Docker Compose setup

\* Successful container startup



Planned next steps:



\* Add PostgreSQL database service

\* Store document metadata in PostgreSQL

\* Add CRUD endpoints for migration records

\* Add GitHub Actions CI workflow

\* Add basic database backup script

\* Add environment variable configuration

\* Add Kubernetes manifests for local Minikube testing

\* Add basic Ansible playbook for automation practice



\## Learning Focus



This project is used to practice and document the following topics:



\* Web and application server basics

\* API development with FastAPI

\* Containerization with Docker

\* Multi-service setup with Docker Compose

\* Health checks and basic monitoring concepts

\* Automated testing with pytest

\* Git and GitHub workflow

\* Database integration with PostgreSQL

\* CI/CD basics with GitHub Actions

\* Backup and infrastructure automation basics



\## Notes



This is a learning and portfolio project.

It does not use real customer data.

All document data is sample data only.



