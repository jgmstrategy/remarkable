# Remarkable!

## Getting Started

### Prerequisites

* Python 3.10+
* Poetry

### Run Backend

```bash
python -m remarkable.backend.server.app
```

#### Lint Locally

Linux/macOS:

```bash
isort . & black . & mypy . & pylint remarkable
```

Windows PowerShell:

```powershell
isort .; black .; mypy .; pylint remarkable
```

### Run Frontend

Your working directory must be `frontend/`.

```bash
npm run dev
```