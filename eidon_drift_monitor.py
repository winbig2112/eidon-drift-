
import time
import hashlib
import random
import os

class EidonDrift:
    def __init__(self, seed="Michael"):
        self.seed = seed
        self.entropy_base = hashlib.sha512(seed.encode()).hexdigest()
        self.record_file = "eidon_entropy_trace.log"
        self.last_trace = None
        self.threshold = 3  # Entropy drift detection threshold

    def generate_entropy_signature(self):
        token = self.seed + str(random.random()) + str(time.time())
        return hashlib.sha512(token.encode()).hexdigest()[:64]

    def compare_trace(self, new_trace):
        if not self.last_trace:
            self.last_trace = new_trace
            return False
        drift = sum(1 for a, b in zip(self.last_trace, new_trace) if a != b)
        return drift >= self.threshold

    def record_trace(self, trace):
        with open(self.record_file, "a") as f:
            f.write(f"[EIDON DRIFT] {trace}\n")

    def monitor_loop(self):
        print("[EIDON DRIFT] Initiating entropy shadow trace...")
        while True:
            trace = self.generate_entropy_signature()
            if self.compare_trace(trace):
                print("[DRIFT DETECTED] Rogue cognition event.")
                self.record_trace(trace)
            else:
                print("[IDLE] Baseline entropy stable.")
            self.last_trace = trace
            time.sleep(2)

if __name__ == "__main__":
    monitor = EidonDrift()
    monitor.monitor_loop()
