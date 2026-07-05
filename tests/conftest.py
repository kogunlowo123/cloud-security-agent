"""Test configuration for Cloud Security Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "cloud-security-agent", "category": "Security AI"}
