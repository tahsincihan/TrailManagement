# **Trail Management App**

## **Overview**
The Trail Management App is a microservice designed to manage trails, features, and routes while providing secure user authentication and role-based access control. This application allows administrators to create, update, and delete trails, while users can view trail details. The app is built using Flask and follows RESTful API principles.

---

## **Features**
- **Authentication**: Secure login using JWT for role-based access control.
- **CRUD Operations**: Manage trails, routes, and features.
- **Role-Based Access**:
  - Admin: Full access to manage trails.
  - Users: View-only access to trails.
- **Interactive API Documentation**: Swagger UI for testing endpoints.
- **Database Design**: Normalized database schema for scalability and efficiency.

---

## **Technologies Used**
- **Backend**: Python, Flask, Flask-RESTful, Flask-Cors
- **Database**: Microsoft SQL Server
- **Documentation**: Swagger (Flasgger)
- **Authentication**: JSON Web Tokens (JWT)
- **Containerization**: Docker (optional)

---

## **Prerequisites**
- Python 3.9 or higher
- Microsoft SQL Server with appropriate drivers
- Docker (optional)
- Python packages listed in `requirements.txt`

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/trail-management-app.git
cd trail-management-app
