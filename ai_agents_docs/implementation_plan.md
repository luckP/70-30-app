# 70-30 Implementation Master Plan

This document outlines the high-level roadmap for the development of the **70-30** platform. The project is divided into **6 One-Week Sprints**.

**Status**: 
- Backend moved to `backend/` (Django + PostGIS).
- Client initialized in `client/` (React + Vite).
- Docker environment configured `docker-compose.yml`.

## Definition of Done (DoD)
All tasks and features implemented in this project must adhere to the following quality standards before being considered complete:
1.  **Documentation**:
    - Code must be commented where complex.
    - **API Endpoints**: Must be fully documented in Swagger/OpenAPI.
    - **Features**: Must be described in the relevant Sprint documentation.
2.  **Testing**:
    - **Backend**: Unit tests (Pytest/Django Test) must be created for models, views, and serializers.
    - **Frontend**: Basic component rendering tests (Vitest/Jest) where applicable.
3.  **review**: All code must follow the project's style guide and pass linting checks.


## Roadmap Overview

| Sprint | Dates | Focus Area | Key Deliverables |
| :--- | :--- | :--- | :--- |
| **Sprint 1** | Jan 05 - Jan 11 | **Foundation & Auth** | Docker Setup, Backend Auth (JWT, User Types: Mentor/Mentee/Admin), Frontend Login/Register UI. |
| **Sprint 2** | Jan 12 - Jan 18 | **Profiles & Location** | Profile CRUD, User Location (PostGIS), Frontend Dashboard & Profile Mgmt. |
| **Sprint 3** | Jan 19 - Jan 25 | **Skills & Discovery** | Skill Taxonomy, Discovery APIs, Map-based Mentor Search (Frontend). |
| **Sprint 4** | Jan 26 - Feb 01 | **Booking & Connections** | Booking Request Flow, Calendar Integration, Scheduling UI. |
| **Sprint 5** | Feb 02 - Feb 08 | **Trust & Social** | Reviews/Ratings System, Admin Moderation Tools, Social UI Components. |
| **Sprint 6** | Feb 09 - Feb 15 | **Polish & Launch Prep** | Performance Tuning (Redis), E2E Testing, CI/CD Scripts, Final Documentation. |

---

## Detailed Sprint Breakdown

### Sprint 1: Foundation & Infrastructure (Current)
**Goal**: Operational Stack with authenticated Frontend & Backend.
- **Backend (`grandpa-backend`)**:
  - Dockerize Django + PostGIS + Redis.
  - Implement Custom User Model with Types: `MENTOR`, `MENTEE`, `ADMIN`.
  - Auth Endpoints: Register, Login, Logout (JWT).
  - Swagger Documentation.
- **Frontend (`grandpa-client`)**:
  - Initialize Vite + React project.
  - Dockerize Frontend.
  - Setup React Router & Axios/Query.
  - Create Login & Registration Forms.

### Sprint 2: User Profiles & Geography
**Goal**: Define "Who" and "Where".
- **Backend**:
  - `Profile` model (1-to-1 with User).
  - `Location` handling with GeoDjango (PointField).
  - API: Get/Update Profile, Update Location.
- **Frontend**:
  - User Dashboard (Private Route).
  - Profile Edit Page (Upload Avatar, Bio).
  - Integration with Maps (e.g., Leaflet) to set "My Location".

### Sprint 3: Skills & Discovery Engine
**Goal**: Connect Demand with Supply.
- **Backend**:
  - `Skill` and `UserSkill` models.
  - Discovery API: Filter by Skill, Radius (Distance), and Availability.
  - Admin API: Manage Skill Categories.
- **Frontend**:
  - Homepage "Find a Mentor" Search Bar.
  - Search Results Page with Map View (Pins for Mentors).
  - Mentor Public Profile View.

### Sprint 4: Booking & Scheduling System
**Goal**: Facilitate the Meeting.
- **Backend**:
  - `Booking` model (Status: Pending, Accepted, Rejected, Completed).
  - Email Notifications (Console backend for dev).
- **Frontend**:
  - "Book Session" Modal on Mentor Profile.
  - "My Bookings" List (Incoming/Outgoing requests).
  - Status Management Actions (Accept/Decline buttons).

### Sprint 5: Trust & Social
**Goal**: Safety and Reputation.
- **Backend**:
  - `Review` model (Rating, Comment).
  - Admin Dashboard APIs (stats, user management).
- **Frontend**:
  - Rate User Component.
  - Profile Reviews Section.
  - **Admin Panel**: Specialized view for users with `ADMIN` role to manage users/content.

### Sprint 6: Polish, Performance & Launch
**Goal**: Production Readiness.
- **Backend**:
  - Redis Caching for Geo-searches.
  - Security Audit (Rate limiting, CORS).
- **Frontend**:
  - UI Polish (Animations, Responsive Design check).
  - Error Boundary & Loading State handling.
  - Optimistic UI updates.
