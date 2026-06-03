# 🧾 AI Invoice Processing System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%2B-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Tesseract](https://img.shields.io/badge/Tesseract_OCR-5.x-4285F4?style=for-the-badge&logo=google&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-MVP-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-blue?style=for-the-badge)

<br/>

> **Enterprise-grade AI-powered invoice processing pipeline with OCR, intelligent data extraction, business rule validation, approval workflows, and real-time analytics dashboard.**

[📖 Documentation](#-api-documentation) · [🚀 Quick Start](#-installation-guide) · [🐛 Report Bug](https://github.com/yourusername/ai-invoice-processing/issues) · [✨ Request Feature](https://github.com/yourusername/ai-invoice-processing/issues)

</div>

---

## 📋 Table of Contents

- [Project Description](#-project-description)
- [Key Features](#-key-features)
- [Architecture Diagram](#-architecture-diagram)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation Guide](#-installation-guide)
- [Tesseract Installation](#-tesseract-installation)
- [Running FastAPI](#-running-fastapi)
- [Running Streamlit Dashboard](#-running-streamlit-dashboard)
- [API Documentation](#-api-documentation)
- [Database Schema](#-database-schema)
- [Sample Invoice Example](#-sample-invoice-example)
- [Expected Output Example](#-expected-output-example)
- [Validation Rules](#-validation-rules)
- [Dashboard Overview](#-dashboard-overview)
- [Future Enhancements](#-future-enhancements)
- [Deployment Roadmap](#-deployment-roadmap)
- [Screenshots](#-screenshots)
- [Author](#-author)
- [License](#-license)

---

## 📌 Project Description

The **AI Invoice Processing System** is a production-ready, end-to-end automation platform designed to eliminate manual invoice handling in enterprise environments. It combines the power of **Optical Character Recognition (OCR)** with **AI-driven data extraction** to intelligently parse, validate, and manage invoices at scale.

Organizations processing hundreds or thousands of invoices per month can leverage this system to:

- **Reduce manual data entry** by automating extraction of key invoice fields
- **Enforce business rules** through a configurable validation engine
- **Streamline approval workflows** with a Pending → Approved / Rejected lifecycle
- **Gain real-time visibility** into invoice pipeline health via an analytics dashboard
- **Scale confidently** from SQLite MVP to PostgreSQL production deployment

Built with a clean **REST API backend (FastAPI)** and an intuitive **Streamlit frontend**, the system is designed for both developer extensibility and business-user accessibility.

---

## ✨ Key Features

### 📤 Invoice Upload
- Upload **PDF invoices** with multi-page support via PyMuPDF
- Upload **image invoices** in PNG, JPG, JPEG, and BMP formats
- Files stored in the `uploads/` directory for processing

### 🔍 OCR Engine
- Extract text from PDFs using **PyMuPDF (fitz)** — fast, accurate, no quality loss
- Extract text from images using **Tesseract OCR** — industry-standard open-source OCR
- Automatic format detection and routing to the correct extraction engine

### 🤖 Invoice Data Extraction
- Intelligently extracts structured fields:
  - **Vendor Name** — supplier/company identification
  - **Invoice Number** — unique document identifier
  - **Invoice Date** — transaction date parsing
  - **Invoice Amount** — monetary value with currency handling
  - **Confidence Score** — AI extraction reliability metric (0–100%)

### ✅ Validation Engine
- Validates **Invoice Number** format and uniqueness
- Validates **Amount** range, format, and non-zero requirement
- Validates **Vendor** name presence and format
- Validates **Date** format and business-logic constraints
- Automatically **rejects invalid invoices** with descriptive error reasons

### 🔄 Workflow Management

| Status | Description |
|--------|-------------|
| 🟡 **Pending** | Newly uploaded, awaiting review |
| ✅ **Approved** | Validated and approved for payment |
| ❌ **Rejected** | Failed validation or manually rejected |

### 📊 Dashboard Analytics
- **Total Invoices** processed in the system
- **Pending** invoices awaiting review
- **Approved** invoices ready for payment
- **Rejected** invoices with failure reasons
- **Error Count** for system-level processing failures

---

## 🏗️ Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                  AI INVOICE PROCESSING SYSTEM                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   👤 User / Client                                          │
│        │                                                    │
│        ▼                                                    │
│   ┌─────────────┐        ┌──────────────────┐              │
│   │  Streamlit  │◄──────►│   FastAPI REST   │              │
│   │  dashboard/ │        │   app/main.py    │              │
│   │   app.py    │        └────────┬─────────┘              │
│   └─────────────┘                 │                         │
│                                   │                         │
│              ┌────────────────────┘                         │
│              ▼                                              │
│   ┌──────────────────┐                                      │
│   │  Invoice Upload  │  uploads/ (PDF / Images)             │
│   └────────┬─────────┘                                      │
│            │                                                │
│            ▼                                                │
│   ┌──────────────────────────────────────────┐             │
│   │         app/services/                    │             │
│   │  ┌──────────────┐  ┌──────────────────┐  │             │
│   │  │  ocr_service │  │ extract_service  │  │             │
│   │  │  PyMuPDF PDF │  │  Tesseract OCR   │  │             │
│   │  └──────────────┘  └──────────────────┘  │             │
│   └────────────────────┬─────────────────────┘             │
│                        │                                    │
│                        ▼                                    │
│   ┌──────────────────────────────────────────┐             │
│   │   app/services/validation_service.py     │             │
│   │  ✔ Invoice Number  ✔ Amount              │             │
│   │  ✔ Vendor          ✔ Date                │             │
│   └────────────────────┬─────────────────────┘             │
│                        │                                    │
│                        ▼                                    │
│   ┌──────────────────────────────────────────┐             │
│   │   app/database.py + app/model.py         │             │
│   │   SQLAlchemy ORM → invoice_ai.db         │             │
│   └────────────────────┬─────────────────────┘             │
│                        │                                    │
│                        ▼                                    │
│   ┌──────────────────────────────────────────┐             │
│   │         app/routes/ (FastAPI)            │             │
│   │   PENDING ──► APPROVED / REJECTED        │             │
│   └────────────────────┬─────────────────────┘             │
│                        │                                    │
│                        ▼                                    │
│   ┌──────────────────────────────────────────┐             │
│   │     dashboard/app.py (Streamlit)         │             │
│   │  📊 Total | ⏳ Pending | ✅ Approved      │             │
│   │  ❌ Rejected | ⚠️  Errors                 │             │
│   └──────────────────────────────────────────┘             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Backend** | Python | 3.10+ | Core application language |
| **API Framework** | FastAPI | 0.110+ | REST API with automatic OpenAPI docs |
| **ORM** | SQLAlchemy | 2.0+ | Database abstraction layer |
| **Database** | SQLite (`invoice_ai.db`) | MVP | Lightweight embedded database |
| **OCR — PDF** | PyMuPDF (fitz) | 1.23+ | High-fidelity PDF text extraction |
| **OCR — Images** | Tesseract OCR | 5.x | Open-source image OCR engine |
| **OCR Wrapper** | pytesseract | 0.3+ | Python bindings for Tesseract |
| **Dashboard** | Streamlit | 1.32+ | Interactive analytics frontend |
| **Image Processing** | Pillow (PIL) | 10.x | Image pre-processing for OCR |
| **API Server** | Uvicorn | 0.27+ | ASGI server for FastAPI |
| **Validation** | Pydantic | 2.x | Request/response data validation |

---

## 📁 Project Structure

Exact structure matching the current codebase:

```
AI INVOICE PROCESSING/
│
├── 📂 app/                          # FastAPI backend application
│   ├── 📂 __pycache__/              # Python bytecode cache (auto-generated)
│   ├── 📂 routes/                   # API route handlers
│   │   └── invoice_routes.py        # Invoice CRUD + workflow endpoints
│   ├── 📂 services/                 # Business logic layer
│   │   ├── ocr_service.py           # PyMuPDF + Tesseract OCR processing
│   │   ├── extraction_service.py    # AI field extraction from raw OCR text
│   │   └── validation_service.py    # Business rule validation engine
│   ├── 📂 utils/                    # Shared utility functions
│   │   └── helpers.py               # Date parsers, formatters, etc.
│   ├── __init__.py                  # App package initializer
│   ├── database.py                  # SQLAlchemy engine & SessionLocal setup
│   ├── main.py                      # FastAPI app entry point & router registry
│   ├── model.py                     # SQLAlchemy ORM Invoice table definition
│   └── schemas.py                   # Pydantic request/response schemas
│
├── 📂 dashboard/                    # Streamlit frontend
│   └── app.py                       # Dashboard UI — KPIs, table, actions
│
├── 📂 uploads/                      # Invoice file storage directory
│   ├── invoce.pdf                   # Uploaded real-world test invoice
│   └── sample_invoice.pdf           # Generated test invoice for OCR pipeline
│
├── 📂 venv/                         # Python virtual environment (excluded from git)
│
├── .gitignore                       # Git ignore rules
├── AI Invoice Processing.png        # Project banner image
├── invoice_ai.db                    # SQLite database (auto-created on first run)
├── README.md                        # Project documentation
└── requirements.txt                 # Python dependencies
```

### Module Responsibilities

| Module | File | Responsibility |
|--------|------|----------------|
| **Entry Point** | `app/main.py` | FastAPI app init, router registration, CORS config |
| **Routes** | `app/routes/` | HTTP endpoints — upload, list, get, approve, reject |
| **OCR** | `app/services/ocr_service.py` | PDF (PyMuPDF) and image (Tesseract) text extraction |
| **Extraction** | `app/services/extraction_service.py` | Regex/NLP field parsing from raw OCR text |
| **Validation** | `app/services/validation_service.py` | Business rule enforcement before DB write |
| **Database** | `app/database.py` | SQLAlchemy engine, `SessionLocal`, `Base` |
| **Model** | `app/model.py` | `Invoice` ORM table mapped to `invoice_ai.db` |
| **Schemas** | `app/schemas.py` | Pydantic I/O models for type-safe API contracts |
| **Dashboard** | `dashboard/app.py` | Streamlit UI consuming FastAPI REST endpoints |

---

## 🚀 Installation Guide

### Prerequisites

- Python **3.10+**
- pip **23+**
- Tesseract OCR (see [Tesseract Installation](#-tesseract-installation))
- Git

### Step 1 — Clone the Repository

```bash
git clone https://github.com/yourusername/ai-invoice-processing.git
cd ai-invoice-processing
```

### Step 2 — Create & Activate Virtual Environment

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Step 3 — Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**`requirements.txt`:**

```txt
fastapi==0.110.0
uvicorn==0.27.1
sqlalchemy==2.0.28
pydantic==2.6.3
pymupdf==1.23.26
pytesseract==0.3.10
Pillow==10.2.0
streamlit==1.32.0
python-multipart==0.0.9
requests==2.31.0
python-dotenv==1.0.1
```

### Step 4 — Initialize the Database

`invoice_ai.db` is auto-created on first run. To initialize manually:

```bash
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

> The `invoice_ai.db` file will appear in the project root after this command.

---

## 🔡 Tesseract Installation

### 🐧 Linux (Ubuntu / Debian)

```bash
sudo apt update && sudo apt install tesseract-ocr -y
tesseract --version
```

### 🍎 macOS

```bash
brew install tesseract
tesseract --version
```

### 🪟 Windows

1. Download from: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
2. Install and note the path (e.g. `C:\Program Files\Tesseract-OCR\`)
3. Set path in `app/services/ocr_service.py`:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### Verify

```python
import pytesseract
print(pytesseract.get_tesseract_version())
```

---

## ▶️ Running FastAPI

```bash
# Development (with auto-reload)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

| Interface | URL |
|-----------|-----|
| **API Base** | `http://localhost:8000` |
| **Swagger UI** | `http://localhost:8000/docs` |
| **ReDoc** | `http://localhost:8000/redoc` |
| **OpenAPI JSON** | `http://localhost:8000/openapi.json` |

---

## 📊 Running Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

Opens at: **`http://localhost:8501`**

> Ensure the FastAPI backend is running on port `8000` first — `dashboard/app.py` fetches data from the REST API.

---

## 📖 API Documentation

### Base URL: `http://localhost:8000`

### Endpoint Summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/invoice/upload` | Upload and process a new invoice |
| `GET` | `/invoice` | List all invoices from `invoice_ai.db` |
| `GET` | `/invoice/{id}` | Get a single invoice by ID |
| `PUT` | `/invoice/{id}/approve` | Approve a pending invoice |
| `PUT` | `/invoice/{id}/reject` | Reject a pending invoice |
| `GET` | `/dashboard` | Get aggregated analytics |

---

### `POST /invoice/upload`

```bash
curl -X POST "http://localhost:8000/invoice/upload" \
  -F "file=@uploads/sample_invoice.pdf"
```

**Response `201 Created`:**
```json
{
  "id": 1,
  "vendor": "Acme Corporation",
  "invoice_number": "INV-2024-0042",
  "invoice_date": "2024-03-15",
  "amount": 8843.78,
  "confidence_score": 91,
  "status": "pending"
}
```

---

### `GET /invoice`

```bash
curl "http://localhost:8000/invoice"
```

Returns an array of all invoice objects stored in `invoice_ai.db`.

---

### `GET /invoice/{id}`

```bash
curl "http://localhost:8000/invoice/1"
```

**Response `404`:**
```json
{ "detail": "Invoice with ID 99 not found." }
```

---

### `PUT /invoice/{id}/approve`

```bash
curl -X PUT "http://localhost:8000/invoice/1/approve"
```

**Response:**
```json
{ "id": 1, "status": "approved", "message": "Invoice INV-2024-0042 has been approved." }
```

---

### `PUT /invoice/{id}/reject`

```bash
curl -X PUT "http://localhost:8000/invoice/1/reject"
```

**Response:**
```json
{ "id": 1, "status": "rejected", "message": "Invoice INV-2024-0042 has been rejected." }
```

---

### `GET /dashboard`

```bash
curl "http://localhost:8000/dashboard"
```

**Response:**
```json
{
  "total_invoices": 12,
  "pending": 4,
  "approved": 7,
  "rejected": 1,
  "error_count": 0
}
```

---

## 🗄️ Database Schema

Database file: **`invoice_ai.db`** (SQLite, project root)
Defined in: `app/model.py` | Configured in: `app/database.py`

```python
# app/model.py
from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id               = Column(Integer, primary_key=True, index=True, autoincrement=True)
    vendor           = Column(String)
    invoice_number   = Column(String, unique=True)
    invoice_date     = Column(String)
    amount           = Column(Float)
    confidence_score = Column(Integer, default=0)
    status           = Column(String, default="pending")
```

### Column Reference

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | `INTEGER` | `PK`, `AUTOINCREMENT` | Unique record identifier |
| `vendor` | `VARCHAR` | — | Extracted vendor/supplier name |
| `invoice_number` | `VARCHAR` | `UNIQUE` | Invoice document reference |
| `invoice_date` | `VARCHAR` | — | Extracted date (ISO 8601 format) |
| `amount` | `FLOAT` | — | Total invoice amount |
| `confidence_score` | `INTEGER` | `DEFAULT 0` | OCR confidence 0–100% |
| `status` | `VARCHAR` | `DEFAULT 'pending'` | pending / approved / rejected |

### Status State Machine

```
              ┌─────────┐
    UPLOAD ──►│ PENDING │
              └────┬────┘
                   │
         ┌─────────┴──────────┐
         ▼                    ▼
    ┌──────────┐         ┌──────────┐
    │ APPROVED │         │ REJECTED │
    └──────────┘         └──────────┘
```

---

## 📄 Sample Invoice Example

Test invoices are stored in `uploads/`:

```
uploads/
├── invoce.pdf           ← Real-world test invoice
└── sample_invoice.pdf   ← Generated test invoice
```

**Raw OCR text extracted from `uploads/sample_invoice.pdf`:**

```
ACME CORPORATION
123 Business Park, Suite 500, New York, NY 10001

INVOICE
Invoice Number : INV-2024-0042
Invoice Date   : March 15, 2024
Due Date       : April 14, 2024

Bill To: TechStart Inc.
456 Innovation Drive, San Francisco, CA 94102

DESCRIPTION                            QTY    AMOUNT
Software Consulting Services            10    $2,500.00
Cloud Infrastructure Setup               1    $1,500.00
Support & Maintenance Package            1    $2,500.00
Custom API Integration                   1    $1,200.00
Security Audit & Penetration Testing     1      $850.00

Subtotal:      $8,550.00
Discount (5%): - $427.50
Tax (8.875%):    $721.28
TOTAL DUE:     $8,843.78
```

---

## 📤 Expected Output Example

After OCR → Extraction → Validation, the record written to `invoice_ai.db`:

```json
{
  "id": 1,
  "vendor": "Acme Corporation",
  "invoice_number": "INV-2024-0042",
  "invoice_date": "2024-03-15",
  "amount": 8843.78,
  "confidence_score": 91,
  "status": "pending"
}
```

| Field | Extracted Value | Confidence |
|-------|----------------|------------|
| Vendor Name | Acme Corporation | ✅ High |
| Invoice Number | INV-2024-0042 | ✅ High |
| Invoice Date | 2024-03-15 | ✅ High |
| Invoice Amount | 8843.78 | ✅ High |
| Overall Confidence | 91% | ✅ High |

---

## 🛡️ Validation Rules

Implemented in `app/services/validation_service.py`:

| Rule | Field | Criteria | Failure Action |
|------|-------|----------|----------------|
| **VR-001** | Invoice Number | Must be non-empty | Auto-reject |
| **VR-002** | Invoice Number | Must be unique in `invoice_ai.db` | Auto-reject |
| **VR-003** | Amount | Must be positive numeric value > 0 | Auto-reject |
| **VR-004** | Amount | Must not exceed configurable maximum | Flag for review |
| **VR-005** | Vendor | Non-empty, minimum 2 characters | Auto-reject |
| **VR-006** | Vendor | No OCR garbage/special characters | Auto-reject |
| **VR-007** | Date | Must be parseable date format | Flag for review |
| **VR-008** | Date | Must not exceed 7 days in future | Flag for review |
| **VR-009** | Confidence Score | Below 60% threshold → manual review | Flag for review |

---

## 📈 Dashboard Overview

`dashboard/app.py` — Streamlit app consuming FastAPI endpoints.

### KPI Cards

```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│   TOTAL     │ │   PENDING   │ │  APPROVED   │ │  REJECTED   │ │   ERRORS    │
│    12       │ │      4      │ │      7      │ │      1      │ │      0      │
│  Invoices   │ │  Invoices   │ │  Invoices   │ │  Invoices   │ │   Errors    │
└─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘
```

### Dashboard Panels

| Panel | API Called | Description |
|-------|------------|-------------|
| **KPI Cards** | `GET /dashboard` | Live counts for all statuses |
| **Invoice Table** | `GET /invoice` | Sortable list with status badges |
| **Status Chart** | `GET /dashboard` | Pie chart — pending/approved/rejected |
| **Approve Action** | `PUT /invoice/{id}/approve` | One-click approval button |
| **Reject Action** | `PUT /invoice/{id}/reject` | One-click rejection button |
| **Invoice Detail** | `GET /invoice/{id}` | Expanded view of all extracted fields |

---

## 🔮 Future Enhancements

### Near-Term (v1.1 – v1.3)

- [ ] **PostgreSQL Migration** — Replace `invoice_ai.db` with production PostgreSQL
- [ ] **JWT Authentication** — Role-based access: Admin, Reviewer, Viewer
- [ ] **Email Notifications** — Notify stakeholders on approval/rejection
- [ ] **Bulk Upload** — Process multiple invoices from a ZIP file
- [ ] **Export to CSV/Excel** — Accounting integration exports

### Medium-Term (v2.0)

- [ ] **LLM Integration** — GPT-4 / Claude API for complex invoice layouts
- [ ] **Duplicate Detection** — Fuzzy matching for near-duplicate invoices
- [ ] **Multi-Language OCR** — Non-English invoice support
- [ ] **Document Classification** — Distinguish invoices from POs, receipts
- [ ] **Audit Trail** — Full change history with user attribution

### Long-Term (v3.0+)

- [ ] **ERP Integration** — SAP, Oracle, QuickBooks, Xero connectors
- [ ] **PO Matching** — Three-way match: Invoice ↔ Purchase Order ↔ Receipt
- [ ] **Mobile App** — iOS/Android on-the-go approvals
- [ ] **Anomaly Detection** — ML model flagging fraud indicators

---

## 🗺️ Deployment Roadmap

```
Phase 1 — MVP (Current)
──────────────────────
✅ SQLite database  →  invoice_ai.db
✅ FastAPI backend  →  app/
✅ OCR pipeline     →  app/services/
✅ Streamlit UI     →  dashboard/app.py
✅ Sample invoices  →  uploads/
✅ ORM models       →  app/model.py + app/schemas.py

Phase 2 — Production Hardening
───────────────────────────────
🔲 Migrate to PostgreSQL
🔲 Docker + Docker Compose
🔲 JWT authentication & RBAC
🔲 Unit + integration test suite
🔲 Environment config via .env

Phase 3 — Cloud Deployment
──────────────────────────
🔲 AWS / Azure / GCP deployment
🔲 CI/CD pipeline (GitHub Actions)
🔲 Kubernetes (K8s) manifests
🔲 Monitoring (Prometheus + Grafana)
🔲 Centralized logging (ELK Stack)

Phase 4 — Enterprise Scale
──────────────────────────
🔲 LLM-powered extraction
🔲 ERP integrations
🔲 Multi-tenant architecture
🔲 Enterprise SSO (SAML / OAuth2)
```

### Docker Quick Start (Phase 2 Preview)

```bash
docker build -t ai-invoice-processing .
docker-compose up --build
# FastAPI  → http://localhost:8000
# Streamlit → http://localhost:8501
```

---

## 🖼️ Screenshots

### 📸 Project Banner
![AI Invoice Processing](AI%20Invoice%20Processing.png)

### 📸 Swagger UI — Interactive API Docs
```
Visit → http://localhost:8000/docs
```

### 📸 Streamlit Dashboard
```
Visit → http://localhost:8501
```

> 📌 Add screenshots to `docs/screenshots/` and submit a PR to update this section.

---

## 👤 Author

<div align="center">

**Your Name**

[![GitHub](https://img.shields.io/badge/GitHub-yourusername-181717?style=flat-square&logo=github)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-yourprofile-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/yourprofile)
[![Email](https://img.shields.io/badge/Email-you@example.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:you@example.com)

*Senior Software Engineer · Solution Architect · AI/ML Enthusiast*

</div>

---

## 📝 License

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

<div align="center">

⭐ **If this project helped you, please consider giving it a star!** ⭐

Made with ❤️ by [Your Name](https://github.com/yourusername)

</div>