"""
pyaudio import shim
Tries to import the built pyaudio library first.
Runs the local dependency setup script if the module is not available.
"""

from pathlib import Path
# import subprocess
# import sys
import runpy

try:
    # Try to import the real built pyaudio extension
    from pyaudio import paFloat32
except ImportError:
    # Fall back to the mock vendor shim for testing
    # (Use if pyaudio has not been built/installed yet)
    try:
        from vendor.pyaudio import paFloat32
    except ImportError as e:
        raise ImportError(
            "Could not import pyaudio. Trying to run: python setup_local_deps.py"
        ) from e
        proj_root = Path(__file__).parent

        setup_script = proj_root / "setup_local_deps.py"
        runpy.run_path(setup_script, run_name="__main__") # For automated setup of local dependencies