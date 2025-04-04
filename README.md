# 🏛️ My Lawyer - Digitalized Law System

### 📜 Transforming the Indian legal system by digitalizing legal services.

---

## 📌 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Scope](#project-scope)
- [System Requirements](#system-requirements)

---

## 📖 Introduction

The Indian legal system is complex, and most citizens struggle with legal procedures such as **filing petitions, applying for licenses, and accessing legal documents**.

**My Lawyer** is a **web-based application** designed to **simplify and digitalize legal processes**. The system allows users to:
- **Search for legal information** and obtain relevant legal templates.
- **File applications and petitions** online.
- **Connect with legal professionals** for expert guidance.
- **Access government-approved legal documents** for various procedures.

Our **goal** is to provide a **simplified and user-friendly solution** for common legal processes, reducing the need for in-person visits to government offices.

---

## ✨ Features

✅ **Online Licensing System** – Users can apply for licenses online.  
✅ **Legal Document Generation** – Provides access to legal templates.  
✅ **Fuzzy String Matching for Search** – Helps users find relevant legal content even if they make spelling mistakes.  
✅ **Virtual Legal Advisor (Keyword-Based Search)** – Users can find relevant cases and documents based on keywords.  
✅ **User & Admin Management** – Secure login system for different user roles.  
✅ **Responsive Web UI** – Easy-to-use interface for all users.  
✅ **Secure Data Storage** – Ensures sensitive user data is protected.  

---

## 🏗 System Architecture

The **system is a web-based platform** built with modern **frontend and backend technologies**.

- **Frontend (ReactJS)** – Provides an interactive and responsive user interface.
- **Backend (Django 3.0.5, Django REST Framework)** – Handles user authentication, legal data, and API management.
- **Database (MongoDB via Djongo)** – Stores user data, legal templates, and application records.
- **Fuzzy String Matching (FuzzyWuzzy)** – Improves search accuracy for legal queries.
- **NLP Support (Spacy)** – Helps process legal text and user queries.


---

## 🚀 Installation

### Prerequisites
Ensure you have the following installed:
- **Python (3.8+)**
- **Django (3.0.5+)**
- **MongoDB (for Djongo)**
- **Node.js (14+)**
- **ReactJS**
- **Git**

### Setup Instructions

1️⃣ **Clone the Repository**
```sh
git clone https://github.com/yourusername/My-Lawyer.git
cd My-Lawyer
```

2️⃣ **Set Up the Backend (Django)**
```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

3️⃣ **Apply Migrations**
```sh
python manage.py migrate
```

4️⃣ **Create a Superuser (Admin)**
```sh
python manage.py createsuperuser
```
Follow the prompts to set up your admin credentials.

5️⃣ **Start the Django Server**
```sh
python manage.py runserver
```

---

## 📌 Usage

- **Sign Up/Login** using email authentication.
- **Search for legal templates** using keywords.
- **Apply for legal licenses and petitions** online.
- **Download official legal forms and documents**.
- **Find legal professionals** through the platform.

---

## 📋 Project Scope

- **Simplify legal processes** for common users.
- **Provide legal document templates** without requiring legal knowledge.
- **Improve search functionality** with **fuzzy matching**.
- **Ensure user security** with robust authentication.

---

## 💻 System Requirements

### Hardware
- **Processor:** Intel Core i3 (2.2 GHz) or higher  
- **RAM:** 4GB+  
- **Storage:** 500MB free space  

### Software
- **Operating System:** Windows/Linux/Mac  
- **Browser:** Chrome, Firefox, Edge  
- **Python 3.8+**  
- **Django 3.0.5+**  
- **MongoDB (via Djongo)**  
- **Node.js 14+**  
