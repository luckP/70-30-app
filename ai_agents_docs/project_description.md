# 70-30 Project Documentation

## 1. Executive Summary
**70-30** is a social impact platform designed to foster intergenerational connection and knowledge transfer. The core philosophy is to value the accumulated wisdom of senior citizens (70+)—who may be retired but still seek purpose—by connecting them with younger generations (30s and younger) eager to learn traditional trades and professional skills.

## 2. Quick Start Guide
**How to start the project locally:**

### Prerequisites
- Docker & Docker Compose installed.

### Steps
1. **Clone the repository**:
   ```bash
   git clone <repo_url>
   cd 70-30-app
   ```

2. **Run with Docker Compose**:
   ```bash
   docker compose up --build
   ```

3. **Access the Application**:
   - **Frontend (React)**: [http://localhost:5173](http://localhost:5173)
   - **Backend API (Django)**: [http://localhost:8001](http://localhost:8001)
     - **Swagger Docs**: [http://localhost:8001/swagger/](http://localhost:8001/swagger/)
     - **Admin Panel**: [http://localhost:8001/admin/](http://localhost:8001/admin/)

4. **Default Credentials**:
   - **Superuser**: `admin` / `admin`

## 3. Platform Mission & Vision
- **Mission**: To democratize access to experience-based knowledge.
- **Vision**: A world where professional and artisanal skills are preserved through direct mentorship.

## 4. Technical Architecture

### 4.1 Backend System (`grandpa-backend`)
- **Framework**: Django REST Framework.
- **Database**: PostgreSQL + PostGIS (Container: `grandpa-db`).
- **Cache**: Redis (Container: `grandpa-redis`).

### 4.2 Frontend System (`grandpa-client`)
- **Framework**: React (Vite).
- **Styling**: CSS / Tailwind (TBD).

### 4.3 Development Process
- **Methodology**: Scrum (Weekly Sprints).
- **Documentation**: Handled in `ai_agents_docs/`.

## 5. Core User Roles
1. **Mentor**: Senior experts sharing knowledge.
2. **Mentee**: Juniors seeking knowledge.
3. **Admin**: Platform moderators ensuring safety and quality.
