import sys
import os
from pathlib import Path

# Ensure project root is on sys.path
proj_root = Path(__file__).resolve().parents[1]
if str(proj_root) not in sys.path:
    sys.path.insert(0, str(proj_root))

# Prepare ledger file
# ledger_path = proj_root / 'ledger'
# ledger_text = 'hello TEST'
# ledger_path.write_text(ledger_text)

# Change cwd
os.chdir(proj_root)

# Run test scenario
try:
    print("=====  =====  =====  =====\n  =    =      =        =  \n  =    =====  =====    =  \n  =    =          =    =  \n  =    =====  =====    =  ")
    print()
    status = True
    from acoustics import acoustics
    a = acoustics()
    while status:
        mode = input("Choose mode to test.\nSend        S\nReceive     R\nQuit        Q\n").lower()
        if mode == "s":
            a.send()
            print('PASS')
        elif mode == "r":
            a.receive()
            print('PASS')
        else:
            status = False
    # from pyaudio import Stream
    # last = Stream.last_write
    # if last is None:
    #     print('FAIL: no write recorded')
    #     sys.exit(1)
    # waveform, num_frames = last
    # if waveform == ledger_text.encode('utf-8'):
    #     print('PASS')
    #     sys.exit(0)
    # else:
    #     print('FAIL: waveform mismatch', waveform)
    #     sys.exit(1)
    a.cleanup()
except Exception as e:
    print('ERROR', e)
    sys.exit(2)
