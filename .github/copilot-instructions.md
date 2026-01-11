# Kinexon Handball API - AI Coding Instructions

## Project Overview
This is a Python wrapper for the Kinexon Handball API. It provides a user-friendly abstraction over a raw, auto-generated OpenAPI client.

## Architectural Structure
*   **Wrapper Core (`src/kinexon_handball_api/`):** Contains the manual logic, authentication handling, and high-level helper methods. New features should be added here.
    *   `api.py`: Handles the complex two-step authentication and `httpx` client initialization.
    *   `handball.py`: The main entry point for end-users. Adds convenience methods for specific API operations.
    *   `fetchers.py`: Static data loading (e.g., team IDs).
*   **Generated Client (`src/_vendor/kinexon_client/`):** An auto-generated OpenAPI client using `openapi-python-client`.
    *   **CRITICAL:** Do NOT edit files in `src/_vendor/` manually. They will be overwritten.
    *   If API definitions change, regenerate the client using `scripts/codegen.sh` (or `.ps1`).

## Development Workflows

### 1. Adding New API Features
1.  **Check Generated Client:** Verify if the endpoint already exists in `src/_vendor/kinexon_client/api/`. Note that generated names may be verbose (e.g., `get_public_v_1_events...`).
2.  **Implement Wrapper:** Add a method to `HandballAPI` in `src/kinexon_handball_api/handball.py`.
3.  **Pattern:** Use the `sync_detailed` method of the generated function to get access to status codes and parsed data.
    ```python
    # Example pattern
    from kinexon_client.api.some_module import some_generated_function

    def my_wrapper_method(self, param):
        resp = some_generated_function.sync_detailed(client=self.client, arg=param)
        if resp.status_code != 200:
            raise RuntimeError(f"Error: {resp.content}")
        return resp.parsed
    ```

### 2. Updating the Client
If the upstream API spec changes:
*   Run `./scripts/codegen.sh` (Linux/Mac) or `./scripts/codegen.ps1` (Windows).
*   This downloads the latest spec to `openapi/sports_app.json` and regenerates `src/_vendor`.

### 3. Dependencies
*   Use `uv` for package management.
*   Install: `uv pip install -e .`

## Conventions & Patterns
*   **Authentication:** The `KinexonAPI` class handles auth automatically. Do not manually pass generic headers unless necessary; the client injects the `api-key`.
*   **Imports:** Import generated classes/functions from `kinexon_client...`. The build system treats `src/_vendor` as a package source.
*   **Type Hints:** Use standard Python typing (`List`, `Dict`, `Optional`) and Pydantic models from `kinexon_client.models`.
*   **Structure:** Keep configuration (like team IDs) in `config/` or `fetchers.py`, not hardcoded in logic.

## Key Files
*   `src/kinexon_handball_api/handball.py`: Main wrapper class.
*   `src/kinexon_handball_api/api.py`: Auth implementation.
*   `pyproject.toml`: Dependencies (check `[project]`).
