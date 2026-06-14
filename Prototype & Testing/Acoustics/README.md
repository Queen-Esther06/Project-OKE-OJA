# Oke Oja - Acoustics & ggwave Integration

This project includes the ggwave C++ library (for acoustic data transmission) vendored in `vendor/ggwave` so that anyone cloning this repo can build and test without needing to install ggwave system-wide.

## Quick Start

### 1. Install test dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Build ggwave (cross-OS: Windows, macOS, Linux)
```bash
python setup_local_deps.py
```

This script will:
- Install build tools (wheel, setuptools, Cython)
- Compile the ggwave C++ library with Python bindings
- Install it into your Python environment

### 3. Run tests
```bash
pytest -q
```

Or use the manual test runner:
```bash
python tests/run_manual_test.py
```

## How It Works

- **Vendored source**: The ggwave repository is cloned into `vendor/ggwave` (as a git submodule or full copy).
- **Python build helper**: `setup_local_deps.py` automates building the C++ extension for your platform.
- **No system install required**: Cloning the project and running the setup script is all you need.
- **Test shims**: `vendor/ggwave/__init__.py` and `vendor/pyaudio/__init__.py` provide minimal shims for unit tests.

## Project Structure

```
Prototype & Testing/
  acoustics.py              # Main module using ggwave
  ggwave.py                 # Shim to import ggwave
  pyaudio.py                # Shim to import pyaudio
  setup_local_deps.py       # Cross-OS build helper
  requirements.txt          # Test dependencies (pytest)
  tests/
    test_acoustics.py       # Unit tests (pytest)
    run_manual_test.py      # Manual test runner
  vendor/
    ggwave/                 # ggwave C++ source (cloned)
      bindings/python/      # Python bindings (Cython)
    pyaudio/                # Minimal pyaudio shim
```

## Troubleshooting

**Build fails with "Cython not found"**
- Run `python setup_local_deps.py` again; it installs Cython automatically.

**Tests fail with "module not found"**
- Ensure you've run `python setup_local_deps.py` to build ggwave.
- Check that the ggwave source is present in `vendor/ggwave`.

**Need to rebuild**
- Delete the build artifacts: `rm -rf vendor/ggwave/bindings/python/build`
- Re-run: `python setup_local_deps.py`
