# 💼 Reimbursement Management System

### (Odoo x VIT Pune Hackathon 2026)

A full-stack **Reimbursement Management System** developed as part of the
**Odoo x VIT Pune Hackathon 2026**, addressing real-world challenges in expense tracking, approval workflows, and reimbursement management.


## 🎥 Demo Video

🔗 (https://drive.google.com/drive/folders/1WBpf3R_PVzev-wLqiugwBV9qqzYq5j53?usp=sharing)

---
## 👥 Team Members

* Aarya Deshpande
* Aashana Sonarkar
* Arya Manve
* Jineshwari Bagul

---

## 📄 Problem Statement

As described in the hackathon:

> Companies often struggle with manual expense reimbursement processes that are time-consuming, error-prone, and lack transparency. 

### Key challenges addressed:

* Multi-level approval flows
* Role-based expense management
* Conditional approval rules
* Transparency in approval lifecycle

---

## ✨ Features

---

### 🔐 Authentication & User Management

* Company + Admin auto-created on first signup
* JWT-based authentication
* Role-based system:

  * **Admin**
  * **Manager**
  * **Employee**
* Admin can:

  * Create users
  * Assign roles
  * Define manager relationships

---

### 💰 Expense Submission (Employee)

* Submit reimbursement requests:

  * Amount
  * Category
  * Description
  * Date
* View personal expense history
* Track approval status

---

### 🔄 Multi-Level Approval Workflow

* Sequential approval system:

  * Step 1 → Manager
  * Step 2 → Admin

* Approval moves to next step only after previous approval

* Supports multiple approvers

---

### 👨‍💼 Manager Features

* View team expenses
* Approve / Reject requests
* Add comments during approval

---

### 👨‍💼 Admin Features

* Manage all users
* Configure approval hierarchy
* Override approvals
* View all expenses across company

---
### 🔮 Enhancements

* OCR-based receipt scanning (as per problem statement)
* Currency conversion APIs
* Conditional approval engine

---

### 🏢 Multi-Tenant Architecture

* Company-based data isolation
* Separate users and workflows per company

---

## 🧰 Tech Stack

### 🎨 Frontend

* Next.js (React Framework)
* TypeScript
* Tailwind CSS
* Axios
* Lucide Icons

---

### ⚙️ Backend

* Node.js + Express
* MySQL
* JWT Authentication
* REST APIs

---

## 🏗️ Project Structure

```bash id="proj-structure"
project-root/
│
├── backend/
│   ├── src/
│   │   ├── controllers/
│   │   ├── services/
│   │   ├── models/
│   │   ├── routes/
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│
└── README.md
```

---

## ⚙️ Installation

### Backend

```bash id="backend-install"
cd backend
npm install
```

Create `.env`:

```env id="backend-env"
PORT=5000
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=yourdb
JWT_SECRET=secret
```

Run:

```bash id="backend-run"
npm run dev
```

---

### Frontend

```bash id="frontend-install"
cd frontend
npm install
npm run dev
```

---

## 🔌 API Endpoints

### Auth

* `POST /api/auth/login`

---

### Expenses

* `POST /api/expenses`
* `GET /api/expenses/my`
* `GET /api/expenses/pending`

---

### Approval

* `PUT /api/expenses/:id/approve`
* `PUT /api/expenses/:id/reject`

---

### Timeline

* `GET /api/expenses/:id/timeline`

---

## 🏁 Conclusion

This project demonstrates a scalable and real-world implementation of a
**Reimbursement Management System**, aligned with enterprise requirements and the official hackathon problem statement.

---


