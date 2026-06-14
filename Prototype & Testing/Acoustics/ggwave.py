"""
ggwave import shim
Tries to import the built C++ ggwave module first.
Runs the local dependency setup script if the module is not available.
"""

from pathlib import Path
# import subprocess
# import sys
import runpy

try:
    # Try to import the real built ggwave C++ extension
    from ggwave import init, encode, decode, free
except ImportError:
    # Fall back to the mock vendor shim for testing
    # (Use if ggwave has not been built/installed yet)
    try:
        from vendor.ggwave import init, encode, decode, free
    except ImportError as e:
        raise ImportError(
            "Could not import ggwave. Trying to run: python setup_local_deps.py"
        ) from e
        proj_root = Path(__file__).parent

        setup_script = proj_root / "setup_local_deps.py"
        runpy.run_path(setup_script, run_name="__main__") # For automated setup of local dependencies