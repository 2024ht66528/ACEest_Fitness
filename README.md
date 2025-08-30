# ACEest Fitness & Gym - DevOps Assignment

## 🚀 Project Overview
A simple Flask-based API for managing workouts, containerized with Docker, tested with Pytest, and automated with GitHub Actions CI/CD.

---

## 🛠️ Setup & Run Locally

```bash
# Clone repo
git clone https://github.com/<your-username>/ACEest_Fitness.git
cd ACEest_Fitness

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Run Tests

```bash
pytest
```

---

## 🐳 Run with Docker

```bash
docker build -t aceest_fitness .
docker run -p 5000:5000 aceest_fitness
```

---

## ⚙️ CI/CD (GitHub Actions)

- Runs tests automatically on push.
- Builds Docker image if tests pass.
