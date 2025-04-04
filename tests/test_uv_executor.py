import shutil

import pytest


@pytest.mark.skipif(not shutil.which("uv"), reason="No uv available")
def test_uv_package_script_task(run_poe_subproc, projects):
    result = run_poe_subproc("-q", "script-task", project="uv")

    assert result.capture == ""
    assert result.stderr == ""
    assert result.stdout == "Hello from uv-project 0.0.99\n"


@pytest.mark.skipif(not shutil.which("uv"), reason="No uv available")
def test_uv_executor_env(run_poe_subproc, projects):
    result = run_poe_subproc("show-env", project="uv")

    assert result.capture == "Poe => poe_test_env\n"
    assert result.stderr == ""

    assert f"VIRTUAL_ENV={projects['uv']}/.venv" in result.stdout
    assert "POE_ACTIVE=uv" in result.stdout
