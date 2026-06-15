#!/usr/bin/env python
"""
Build and install ggwave C++ extension locally for this project.
Cross-OS for Windows, macOS, and Linux.
Usage: python setup_local_deps.py
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(cmd, description="", cwd=None):
    """Run a shell command and exit on failure."""
    if cwd:
        os.chdir(cwd)
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"\nERROR: Command failed with exit code {result.returncode}")
        sys.exit(1)


def source_exists(path):
    if not path.exists():
        print(f"ERROR: Source not found at {path}")
        print("Please ensure you have properly cloned the repository and try again.")
        sys.exit(1)


def setup_ggwave(proj_root=None):
    ggwave_dir = proj_root / "vendor" / "ggwave" / "bindings" / "python"
    
    print("\n" + "="*60)
    print("Building ggwave C++ extension")
    print("="*60)
    print(f"Project root: {proj_root}")
    print(f"ggwave source: {ggwave_dir}")
    print()
    
    # Check if ggwave source exists
    source_exists(ggwave_dir)
    
    # Check for Python
    result = subprocess.run([sys.executable, "--version"], capture_output=True)
    if result.returncode != 0:
        print("ERROR: Python not found in PATH")
        print("Please ensure Python is installed and in your PATH")
        sys.exit(1)
    
    # Step 1: Install build dependencies
    print("\nStep 1: Installing build dependencies (Cython, wheel, setuptools)")
    print()
    cmd = [sys.executable, "-m", "pip", "install", "--quiet", "--upgrade", 
           "pip", "setuptools", "wheel", "Cython"]
    run_command(cmd)
    
    # Step 2: Build ggwave C++ extension
    print("\nStep 2: Building ggwave C++ extension (this may take a minute)")
    print()
    env = os.environ.copy()
    env["GGWAVE_USE_CYTHON"] = "1" # Use Cython to build the extension
    env["GGWAVE_OMIT_README_RST"] = "1" # Omit README.rst from the build (not needed for local install without make implementation)

    import shutil
    
    # create local ggwave/ folder expected by the binding build (like `make ggwave`)
    local_ggwave = ggwave_dir / "ggwave"
    if local_ggwave.exists():
        shutil.rmtree(local_ggwave)
    local_ggwave.mkdir(parents=True, exist_ok=True)
    
    src_root = proj_root / "vendor" / "ggwave"
    shutil.copytree(src_root / "include", local_ggwave / "include")
    shutil.copytree(src_root / "src", local_ggwave / "src")

    cmd = [sys.executable, "setup.py", "build_ext", "--inplace"]
    result = subprocess.run(cmd, cwd=ggwave_dir, env=env)
    if result.returncode != 0:
        print("ERROR: Build failed. Check output above for details.")
        print("Common issues:")
        print("  - Missing C++ compiler (Visual Studio Build Tools / MSVC on Windows)")
        print("  - Missing Python development headers")
        sys.exit(1)
    
    # Step 3: Install ggwave locally
    print("\nStep 3: Installing ggwave locally for this project")
    print()
    cmd = [sys.executable, "setup.py", "install"]
    result = subprocess.run(cmd, cwd=ggwave_dir, env=env)
    if result.returncode != 0:
        print("ERROR: Install failed. Trying pip install instead...")
        cmd = [sys.executable, "-m", "pip", "install", "."]
        result = subprocess.run(cmd, cwd=ggwave_dir, env=env)
        if result.returncode != 0:
            print("ERROR: Installation failed")
            sys.exit(1)


def main():
    """Main entry point."""
    
    # Get project root
    proj_root = Path(__file__).parent
    
    try:
        from ggwave import init, encode, decode, free
        print("ggwave is already available. No need to build.")
    except ImportError:
        setup_ggwave(proj_root)
    
    try:
        from pyaudio import Stream, PyAudio, paFloat32
        print("pyaudio is already available. No need to build.")
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "pyaudio"], check=True)
    
    # Success
    os.chdir(proj_root)
    print("\n" + "="*60)
    print("Build successful!")
    print("="*60)
    
    # Success
    os.chdir(proj_root)
    print("\n" + "="*60)
    print("Build successful!")
    print("="*60)
    print()
    print("You can now import ggwave in Python:")
    print("  python -c \"import ggwave; print(ggwave.__version__ if hasattr(ggwave, '__version__') else 'ggwave loaded')\"")
    print()


if __name__ == "__main__":
    main()
