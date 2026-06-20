import time
import runpy

try:
    import ggwave
    import pyaudio
except ImportError:
    runpy.run_path("setup_local_deps.py")

class acoustics():
    def __init__(self):
        print("Initializing pyaudio")
        self.audio = pyaudio.PyAudio()
        print("Intitializing ggwave")
        self.instance = ggwave.init()
        self.MAX_PAYLOAD = 120 # To leave space for header

    
    def chunk_bytes(self, data: bytes):
        chunk_size = self.MAX_PAYLOAD
        for i in range(0, len(data), chunk_size):
            yield data[i:i+chunk_size]


    def make_packet(self, chunk_index, total_chunks, chunk_data):
        header = f"{chunk_index}/{total_chunks}|".encode("utf-8")
        return header + chunk_data


    def send(self):
        with open ("ledger", "r") as message:
            stream = self.audio.open(format=pyaudio.paFloat32, channels=2, rate=378000, output=True, frames_per_buffer=4096)
            print("Chunking message...")
            payload = message.read().encode("utf-8")
            chunks = list(self.chunk_bytes(payload))
            total = len(chunks)
            
            print("Converting byte chunks to waveform packets...")
            for idx, chunk in enumerate(chunks, start=1):
                packet = self.make_packet(idx, total, chunk)
                waveform = ggwave.encode(packet, protocolId=5, volume=100)
                print("Transmitting ledger's waveform...")
                stream.write(waveform)
                time.sleep(0.1)  # Short delay between packets

            stream.stop_stream()
            stream.close()


    def receive(self):
        stream = self.audio.open(format=pyaudio.paFloat32, channels=2, rate=378000, input=True, frames_per_buffer=4096)

        print('Listening... Press Ctrl+C to stop')
        try:
            received_chunks = {}
            while True:
                waveform = stream.read(4096, exception_on_overflow=False)
                message = ggwave.decode(self.instance, waveform)
                if (not message is None):
                    print("Cleaning up message...")
                    try:
                        header, body = message.split(b"|", 1)
                        idx, total = map(int, header.split(b"/"))
                    except ValueError:
                        continue

                    received_chunks[idx] = body
                    if len(received_chunks) == total:
                        full_message = b"".join(received_chunks[i] for i in range(1, total + 1))
                        print(full_message.decode("utf-8"))
                        received_chunks.clear()
        except KeyboardInterrupt:
            pass

        stream.stop_stream()
        stream.close()


    def cleanup(self):
        ggwave.free(self.instance)
        self.audio.terminate()