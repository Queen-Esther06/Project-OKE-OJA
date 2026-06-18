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


    def send(self):
        with open ("ledger", "r") as message:
            waveform = ggwave.encode(message.read().encode('utf-8'), protocolId = 1, volume = 20)

            print("Transmitting ledgers waveform...")
            stream = self.audio.open(format=pyaudio.paFloat32, channels=1, rate=48000, output=True, frames_per_buffer=1024)
            stream.write(waveform, len(waveform)//4)
            stream.stop_stream()
            stream.close()

            self.audio.terminate()


    def receive(self):
        stream = self.audio.open(format=pyaudio.paFloat32, channels=1, rate=48000, input=True, frames_per_buffer=1024)

        print('Listening ... Press Ctrl+C to stop')
        try:
            while True:
                waveform = stream.read(1024, exception_on_overflow=False)
                message = ggwave.decode(self.instance, waveform)
                if (not message is None):
                    try:
                        print('Received text: ' + message.decode("utf-8"))
                    except:
                        pass
        except KeyboardInterrupt:
            pass

        ggwave.free(self.instance)

        stream.stop_stream()
        stream.close()

        self.audio.terminate()
