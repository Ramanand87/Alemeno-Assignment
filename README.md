# 💳 Credit Approval System

This project provides a Dockerized Django-based backend for managing customer loans, checking eligibility, and computing credit scores based on financial behavior.


## 🔧 Clone the Repository

```bash
git clone https://github.com/yourusername/credit-approval-system.git
cd credit-approval-system
```
## 🚀 Build and Start All Services

```bash
docker-compose up -d --build
```
## 👤 Create a Superuser (Optional)

```bash
docker-compose exec web python manage.py createsuperuser
```
## 🛑 Shut Down All Containers
```bash
docker-compose down
```
---

## 📄 Project Highlights

  📊 Loan approval logic based on credit score, income, and loan history
  
  🔁 Fully automated ingestion on startup (or run manually)
  
  🐳 Zero-setup development with Docker
  
  🧪 Easy testing with pytest

