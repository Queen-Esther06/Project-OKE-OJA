# Oke Oja - Acoustics & ggwave Integration

This directory implements a simple acoustic data transmitter/receiver using the vendored `ggwave` library and `pyaudio`.

## Quick Start

### 1. Install Python dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Build the vendored ggwave extension
```bash
python setup_local_deps.py
```

This script will:
- install required build tools and Python packaging support
- compile the vendored `ggwave` C++ library with Python bindings
- make the extension available to the local Python environment

### 3. Run the manual test runner
```bash
python tests/run_manual_test.py
```

When the runner starts, choose:
- `S` to invoke `send()`
- `R` to invoke `receive()`
- `Q` to quit and clean up resources

## Current implementation

- `acoustics.py` contains the `acoustics` class.
- `send()` reads `ledger` from the project root, chunks it, encodes each chunk with `ggwave`, and writes it to the output audio stream.
- `receive()` opens an input audio stream, decodes incoming audio with `ggwave.decode()`, reassembles numbered packets, and prints the reconstructed message.
- `cleanup()` frees the `ggwave` instance and terminates the shared `pyaudio.PyAudio()` session.

### Message chunking

Because the current `ggwave` receiver has a payload-size limit, `send()` splits the ledger into smaller packets before transmission.
Each packet is prefixed with a header like `1/5|` so the receiver can reconstruct the full message.

## Project structure

```
Prototype & Testing/Acoustics/
  acoustics.py
  ledger
  README.md
  requirements.txt
  setup_local_deps.py
  tests/
    run_manual_test.py
  vendor/
    ggwave/
    pyaudio/
```

## Notes

- `tests/run_manual_test.py` creates one `acoustics` instance and calls `cleanup()` once at the end.
- `acoustics.send()` and `acoustics.receive()` both open and close audio streams, but they keep the shared `PyAudio` context and `ggwave` instance alive until cleanup.
- If you see device errors after switching between send and receive, ensure the script is not terminating `pyaudio` or `ggwave` before the final cleanup.

## Troubleshooting

**`ImportError` for `ggwave` or `pyaudio`**
- Run `python setup_local_deps.py` to build the local extension and install the vendored dependencies.

**`Invalid input device` / `Invalid output device` errors**
- Make sure the runner is not repeatedly terminating the `PyAudio` session before the test script ends.
- Use the manual runner and quit cleanly via `Q` so `cleanup()` is called.

**Need to rebuild**
- Remove build artifacts from `vendor/ggwave/bindings/python/build`
- Re-run `python setup_local_deps.py`
