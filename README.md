# Cloud Security Agent

[![CI](https://github.com/kogunlowo123/cloud-security-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/cloud-security-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Security AI | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Cloud security posture agent that scans multi-cloud environments for misconfigurations, enforces security baselines, monitors for policy violations, and auto-remediates common security issues.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `analyze` | Primary analysis function for Cloud Security Agent |
| `scan` | Scan target for issues relevant to Cloud Security Agent |
| `report` | Generate report for Cloud Security Agent |
| `remediate` | Execute remediation action |
| `monitor` | Monitor for ongoing issues |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/cloud-security/analyze` | Run analysis |
| `POST` | `/api/v1/cloud-security/scan` | Scan target |
| `POST` | `/api/v1/cloud-security/report` | Generate report |
| `POST` | `/api/v1/cloud-security/remediate` | Execute remediation |
| `GET` | `/api/v1/cloud-security/status` | Get status |

## Features

- Cloud
- Security
- Reporting
- Monitoring

## Integrations

- Siem Connector
- Edr Connector
- Threat Intel
- Ticketing System

## Architecture

```
cloud-security-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── cloud_security_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Security Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
