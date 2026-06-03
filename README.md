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
- Drag-and-drop interface via Streamlit dashboard

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
│                    AI INVOICE PROCESSING SYSTEM              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   👤 User / Client                                          │
│        │                                                    │
│        ▼                                                    │
│   ┌─────────────┐        ┌──────────────────┐              │
│   │  Streamlit  │◄──────►│   FastAPI REST   │              │
│   │  Dashboard  │        │     Backend      │              │
│   └─────────────┘        └────────┬─────────┘              │
│                                   │                         │
│              ┌────────────────────┘                         │
│              │                                              │
│              ▼                                              │
│   ┌──────────────────┐                                      │
│   │  Invoice Upload  │  (PDF / PNG / JPG / JPEG / BMP)      │
│   └────────┬─────────┘                                      │
│            │                                                │
│            ▼                                                │
│   ┌──────────────────────────────────────────┐             │
│   │             OCR Processing               │             │
│   │  ┌───────────────┐  ┌──────────────────┐ │             │
│   │  │  PyMuPDF      │  │  Tesseract OCR   │ │             │
│   │  │  (PDF files)  │  │  (Image files)   │ │             │
│   │  └───────────────┘  └──────────────────┘ │             │
│   └────────────────────┬─────────────────────┘             │
│                        │                                    │
│                        ▼                                    │
│   ┌──────────────────────────────────────────┐             │
│   │          AI Data Extraction              │             │
│   │  • Vendor Name    • Invoice Number       │             │
│   │  • Invoice Date   • Invoice Amount       │             │
│   │  • Confidence Score                      │             │
│   └────────────────────┬─────────────────────┘             │
│                        │                                    │
│                        ▼                                    │
│   ┌──────────────────────────────────────────┐             │
│   │          Validation Engine               │             │
│   │  ✔ Invoice Number  ✔ Amount              │             │
│   │  ✔ Vendor          ✔ Date                │             │
│   │  ✘ Reject Invalid Invoices               │             │
│   └────────────────────┬─────────────────────┘             │
│                        │                                    │
│                        ▼                                    │
│   ┌──────────────────────────────────────────┐             │
│   │         Database Storage (SQLite)        │             │
│   │         SQLAlchemy ORM Layer             │             │
│   └────────────────────┬─────────────────────┘             │
│                        │                                    │
│                        ▼                                    │
│   ┌──────────────────────────────────────────┐             │
│   │          Approval Workflow               │             │
│   │   PENDING ──► APPROVED / REJECTED        │             │
│   └────────────────────┬─────────────────────┘             │
│                        │                                    │
│                        ▼                                    │
│   ┌──────────────────────────────────────────┐             │
│   │        Dashboard Analytics               │             │
│   │  📊 Total | ⏳ Pending | ✅ Approved      │             │
│   │  ❌ Rejected | ⚠️ Errors                  │             │
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
| **Database** | SQLite | MVP | Lightweight embedded database |
| **OCR — PDF** | PyMuPDF (fitz) | 1.23+ | High-fidelity PDF text extraction |
| **OCR — Images** | Tesseract OCR | 5.x | Open-source image OCR engine |
| **OCR Wrapper** | pytesseract | 0.3+ | Python bindings for Tesseract |
| **Dashboard** | Streamlit | 1.32+ | Interactive analytics frontend |
| **Image Processing** | Pillow (PIL) | 10.x | Image pre-processing for OCR |
| **API Server** | Uvicorn | 0.27+ | ASGI server for FastAPI |
| **Validation** | Pydantic | 2.x | Request/response data validation |

---

## 📁 Project Structure

```
ai-invoice-processing/
│
├── 📂 app/
│   ├── 📂 api/
│   │   ├── __init__.py
│   │   └── routes.py              # FastAPI route definitions
│   │
│   ├── 📂 core/
│   │   ├── __init__.py
│   │   ├── ocr_engine.py          # PyMuPDF + Tesseract OCR logic
│   │   ├── extractor.py           # AI-based field extraction
│   │   └── validator.py           # Business rule validation engine
│   │
│   ├── 📂 models/
│   │   ├── __init__.py
│   │   └── invoice.py             # SQLAlchemy ORM models
│   │
│   ├── 📂 schemas/
│   │   ├── __init__.py
│   │   └── invoice.py             # Pydantic request/response schemas
│   │
│   ├── 📂 database/
│   │   ├── __init__.py
│   │   └── db.py                  # Database session & engine config
│   │
│   └── main.py                    # FastAPI application entry point
│
├── 📂 dashboard/
│   └── streamlit_app.py           # Streamlit dashboard application
│
├── 📂 uploads/                    # Temporary invoice upload storage
│
├── 📂 tests/
│   ├── test_ocr.py
│   ├── test_extractor.py
│   ├── test_validator.py
│   └── test_api.py
│
├── 📂 sample_invoices/            # Sample PDF/image invoices for testing
│
├── .env                           # Environment variables
├── .env.example                   # Environment variable template
├── .gitignore
├── requirements.txt               # Python dependencies
└── README.md
```

---

## 🚀 Installation Guide

### Prerequisites

Ensure the following are installed on your system:

- Python **3.10+**
- pip **23+**
- Tesseract OCR (see [Tesseract Installation](#-tesseract-installation))
- Git

### Step 1 — Clone the Repository

```bash
git clone https://github.com/yourusername/ai-invoice-processing.git
cd ai-invoice-processing
```

### Step 2 — Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate — Linux / macOS
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### Step 3 — Install Python Dependencies

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

### Step 4 — Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env`:

```env
DATABASE_URL=sqlite:///./invoices.db
UPLOAD_FOLDER=uploads/
TESSERACT_CMD=/usr/bin/tesseract
MAX_UPLOAD_SIZE_MB=10
CONFIDENCE_THRESHOLD=60
```

### Step 5 — Initialize the Database

```bash
python -c "from app.database.db import Base, engine; Base.metadata.create_all(bind=engine)"
```

---

## 🔡 Tesseract Installation

Tesseract must be installed at the OS level in addition to the Python `pytesseract` wrapper.

### 🐧 Linux (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install tesseract-ocr -y
sudo apt install libtesseract-dev -y

# Verify installation
tesseract --version
```

### 🍎 macOS

```bash
brew install tesseract

# Verify installation
tesseract --version
```

### 🪟 Windows

1. Download the installer from: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run the `.exe` installer and note the installation path (e.g., `C:\Program Files\Tesseract-OCR\`)
3. Add to System PATH or configure in `.env`:

```env
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
```

### Verify Tesseract in Python

```python
import pytesseract
print(pytesseract.get_tesseract_version())
```

---

## ▶️ Running FastAPI

### Development Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

The API will be available at:

| Interface | URL |
|-----------|-----|
| **API Base** | `http://localhost:8000` |
| **Swagger UI (Interactive Docs)** | `http://localhost:8000/docs` |
| **ReDoc Documentation** | `http://localhost:8000/redoc` |
| **OpenAPI JSON** | `http://localhost:8000/openapi.json` |

---

## 📊 Running Streamlit Dashboard

```bash
streamlit run dashboard/streamlit_app.py
```

The dashboard will open at: **`http://localhost:8501`**

> **Note:** Ensure the FastAPI backend is running before launching the Streamlit dashboard.

---

## 📖 API Documentation

### Base URL
```
http://localhost:8000
```

---

### `POST /invoice/upload`
Upload a new invoice (PDF or image) for OCR processing and data extraction.

**Request:**
```bash
curl -X POST "http://localhost:8000/invoice/upload" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@invoice_sample.pdf"
```

**Response `201 Created`:**
```json
{
  "id": 1,
  "vendor": "Acme Corp",
  "invoice_number": "INV-2024-0042",
  "invoice_date": "2024-03-15",
  "amount": 4250.00,
  "confidence_score": 87,
  "status": "pending",
  "message": "Invoice uploaded and processed successfully."
}
```

---

### `GET /invoice`
Retrieve all invoices in the system.

**Request:**
```bash
curl -X GET "http://localhost:8000/invoice" \
  -H "accept: application/json"
```

**Response `200 OK`:**
```json
[
  {
    "id": 1,
    "vendor": "Acme Corp",
    "invoice_number": "INV-2024-0042",
    "invoice_date": "2024-03-15",
    "amount": 4250.00,
    "confidence_score": 87,
    "status": "pending"
  },
  {
    "id": 2,
    "vendor": "Global Supplies Ltd",
    "invoice_number": "INV-2024-0051",
    "invoice_date": "2024-03-18",
    "amount": 12800.50,
    "confidence_score": 92,
    "status": "approved"
  }
]
```

---

### `GET /invoice/{id}`
Retrieve a single invoice by its ID.

**Request:**
```bash
curl -X GET "http://localhost:8000/invoice/1" \
  -H "accept: application/json"
```

**Response `200 OK`:**
```json
{
  "id": 1,
  "vendor": "Acme Corp",
  "invoice_number": "INV-2024-0042",
  "invoice_date": "2024-03-15",
  "amount": 4250.00,
  "confidence_score": 87,
  "status": "pending"
}
```

**Response `404 Not Found`:**
```json
{
  "detail": "Invoice with ID 1 not found."
}
```

---

### `PUT /invoice/{id}/approve`
Approve a pending invoice.

**Request:**
```bash
curl -X PUT "http://localhost:8000/invoice/1/approve" \
  -H "accept: application/json"
```

**Response `200 OK`:**
```json
{
  "id": 1,
  "status": "approved",
  "message": "Invoice INV-2024-0042 has been approved."
}
```

---

### `PUT /invoice/{id}/reject`
Reject a pending invoice.

**Request:**
```bash
curl -X PUT "http://localhost:8000/invoice/1/reject" \
  -H "accept: application/json"
```

**Response `200 OK`:**
```json
{
  "id": 1,
  "status": "rejected",
  "message": "Invoice INV-2024-0042 has been rejected."
}
```

---

### `GET /dashboard`
Retrieve aggregated invoice analytics for the dashboard.

**Request:**
```bash
curl -X GET "http://localhost:8000/dashboard" \
  -H "accept: application/json"
```

**Response `200 OK`:**
```json
{
  "total_invoices": 150,
  "pending": 23,
  "approved": 112,
  "rejected": 11,
  "error_count": 4
}
```

---

### API Endpoint Summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/invoice/upload` | Upload and process a new invoice |
| `GET` | `/invoice` | List all invoices |
| `GET` | `/invoice/{id}` | Get invoice by ID |
| `PUT` | `/invoice/{id}/approve` | Approve an invoice |
| `PUT` | `/invoice/{id}/reject` | Reject an invoice |
| `GET` | `/dashboard` | Get dashboard analytics |

---

## 🗄️ Database Schema

### Table: `invoices`

```sql
CREATE TABLE invoices (
    id              INTEGER     PRIMARY KEY AUTOINCREMENT,
    vendor          VARCHAR     NOT NULL,
    invoice_number  VARCHAR     UNIQUE NOT NULL,
    invoice_date    VARCHAR,
    amount          FLOAT,
    confidence_score INTEGER    DEFAULT 0,
    status          VARCHAR     DEFAULT 'pending'
);
```

### Schema Reference

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | `INTEGER` | `PRIMARY KEY`, `AUTOINCREMENT` | Unique invoice record identifier |
| `vendor` | `VARCHAR` | `NOT NULL` | Extracted vendor/supplier name |
| `invoice_number` | `VARCHAR` | `UNIQUE`, `NOT NULL` | Invoice document reference number |
| `invoice_date` | `VARCHAR` | — | Extracted invoice date (ISO format) |
| `amount` | `FLOAT` | — | Total invoice amount (numeric) |
| `confidence_score` | `INTEGER` | `DEFAULT 0` | OCR/AI extraction confidence (0–100) |
| `status` | `VARCHAR` | `DEFAULT 'pending'` | Workflow state: pending / approved / rejected |

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

Below is an example of a raw invoice document uploaded to the system:

```
═══════════════════════════════════════════
              ACME CORPORATION
          123 Business Park, Suite 500
             New York, NY 10001
          Phone: +1 (212) 555-0198
═══════════════════════════════════════════

INVOICE

Invoice Number : INV-2024-0042
Invoice Date   : March 15, 2024
Due Date       : April 15, 2024

Bill To:
  TechStart Inc.
  456 Innovation Drive
  San Francisco, CA 94102

───────────────────────────────────────────
DESCRIPTION               QTY    AMOUNT
───────────────────────────────────────────
Software Consulting        10    $250.00
Cloud Infrastructure        1   $1,500.00
Support & Maintenance       1   $2,500.00
───────────────────────────────────────────
                  TOTAL:         $4,250.00
═══════════════════════════════════════════
Payment Terms: Net 30
```

---

## 📤 Expected Output Example

After the system processes the above invoice, the extracted and validated output is:

```json
{
  "id": 1,
  "vendor": "Acme Corporation",
  "invoice_number": "INV-2024-0042",
  "invoice_date": "2024-03-15",
  "amount": 4250.00,
  "confidence_score": 91,
  "status": "pending"
}
```

| Field | Extracted Value | Confidence |
|-------|----------------|------------|
| Vendor Name | Acme Corporation | ✅ High |
| Invoice Number | INV-2024-0042 | ✅ High |
| Invoice Date | 2024-03-15 | ✅ High |
| Invoice Amount | 4250.00 | ✅ High |
| Overall Confidence Score | 91% | ✅ High |

---

## 🛡️ Validation Rules

The validation engine applies the following business rules to every extracted invoice. Invoices failing any critical rule are automatically set to `rejected` status.

| Rule | Field | Criteria | Failure Action |
|------|-------|----------|----------------|
| **VR-001** | Invoice Number | Must be non-empty and match pattern `[A-Z]{2,}-\d{4}-\d{3,}` | Auto-reject |
| **VR-002** | Invoice Number | Must be unique in the database | Auto-reject |
| **VR-003** | Amount | Must be a positive numeric value > 0 | Auto-reject |
| **VR-004** | Amount | Must not exceed configurable maximum threshold | Flag for review |
| **VR-005** | Vendor | Must be non-empty string, minimum 2 characters | Auto-reject |
| **VR-006** | Vendor | No special characters that indicate OCR garbage | Auto-reject |
| **VR-007** | Date | Must be a parseable date (ISO 8601 preferred) | Flag for review |
| **VR-008** | Date | Must not be a future date beyond 7 days | Flag for review |
| **VR-009** | Confidence Score | Score below threshold (default: 60%) | Flag for manual review |

### Validation Response Codes

| Code | Meaning |
|------|---------|
| `VALID` | All rules passed, invoice is accepted |
| `INVALID_INVOICE_NUMBER` | Invoice number is missing, malformed, or duplicate |
| `INVALID_AMOUNT` | Amount is zero, negative, or non-numeric |
| `INVALID_VENDOR` | Vendor name is missing or failed format check |
| `INVALID_DATE` | Date is unparseable or out of valid range |
| `LOW_CONFIDENCE` | OCR confidence below threshold, requires manual review |

---

## 📈 Dashboard Overview

The Streamlit Dashboard provides a real-time operational view of the invoice processing pipeline.

### Key Metrics (Top KPI Cards)

```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│   TOTAL     │ │   PENDING   │ │  APPROVED   │ │  REJECTED   │ │   ERRORS    │
│    150      │ │     23      │ │    112      │ │     11      │ │      4      │
│  Invoices   │ │  Invoices   │ │  Invoices   │ │  Invoices   │ │   Errors    │
└─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘
```

### Dashboard Panels

| Panel | Description |
|-------|-------------|
| **KPI Cards** | Live counts for Total, Pending, Approved, Rejected, and Errors |
| **Invoice Table** | Sortable, filterable list of all invoices with status indicators |
| **Status Distribution** | Pie/donut chart of invoice statuses |
| **Approval Actions** | One-click Approve / Reject buttons per invoice row |
| **Invoice Detail View** | Full extracted data view for any selected invoice |
| **Error Log** | Processing errors with timestamps and file references |

---

## 🔮 Future Enhancements

### Near-Term (v1.1 – v1.3)

- [ ] **PostgreSQL Migration** — Replace SQLite with production-grade PostgreSQL
- [ ] **JWT Authentication** — Role-based access control (Admin, Reviewer, Viewer)
- [ ] **Email Notifications** — Notify stakeholders on approval/rejection events
- [ ] **Bulk Upload** — Process multiple invoices in a single ZIP upload
- [ ] **Export to CSV/Excel** — Invoice data export for accounting integrations

### Medium-Term (v2.0)

- [ ] **LLM Integration** — GPT-4 / Claude API for improved extraction accuracy on complex layouts
- [ ] **Duplicate Detection** — Fuzzy matching to detect near-duplicate invoices
- [ ] **Multi-Language OCR** — Support for invoices in non-English languages
- [ ] **Document Classification** — Distinguish invoices from receipts, POs, and statements
- [ ] **Audit Trail** — Complete change history with user attribution

### Long-Term (v3.0+)

- [ ] **ERP Integration** — Connectors for SAP, Oracle, QuickBooks, and Xero
- [ ] **Vendor Master Database** — Centralized vendor registry with enrichment
- [ ] **PO Matching** — Three-way match: Invoice ↔ Purchase Order ↔ Receipt
- [ ] **Mobile App** — iOS/Android app for on-the-go approvals
- [ ] **Anomaly Detection** — ML model to flag unusual invoice patterns or fraud indicators

---

## 🗺️ Deployment Roadmap

```
Phase 1 — MVP (Current)
──────────────────────
✅ SQLite database
✅ FastAPI REST backend
✅ Tesseract + PyMuPDF OCR
✅ Streamlit dashboard
✅ Basic validation engine

Phase 2 — Production Hardening
───────────────────────────────
🔲 Migrate to PostgreSQL
🔲 Docker containerization
🔲 Docker Compose orchestration
🔲 JWT authentication & RBAC
🔲 Comprehensive test suite (>90% coverage)

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
🔲 SLA-based processing queues
🔲 Enterprise SSO (SAML / OAuth2)
```

### Docker Quick Start (Phase 2 Preview)

```bash
# Build image
docker build -t ai-invoice-processing .

# Run with Docker Compose
docker-compose up --build

# Services:
#   FastAPI  → http://localhost:8000
#   Streamlit → http://localhost:8501
```

---

## 🖼️ Screenshots

> Screenshots will be added upon first stable release. Contributions welcome!

### 📸 Upload Interface
```
[ Screenshot: Invoice Upload Page — Drag & Drop PDF/Image ]
```

### 📸 OCR Extraction Result
```
[ Screenshot: Extracted Fields — Vendor, Invoice No., Date, Amount, Confidence ]
```

### 📸 Invoice List View
```
[ Screenshot: All Invoices Table — Status badges, Approve/Reject actions ]
```

### 📸 Dashboard Analytics
```
[ Screenshot: KPI Cards + Status Distribution Chart ]
```

### 📸 API Swagger UI
```
[ Screenshot: FastAPI /docs — Interactive Swagger Documentation ]
```

> 📌 **Want to contribute screenshots?** Submit a PR with `docs/screenshots/` images and update the paths above.

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
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

⭐ **If this project helped you, please consider giving it a star!** ⭐

Made with ❤️ by [Your Name](https://github.com/prashantdarshanwar)

</div>