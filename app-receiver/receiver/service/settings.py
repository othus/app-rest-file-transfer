import os
"""
This file contains configurations for receiver service.
If these enviromental variable exists, they will override the values.
"""
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "/usr/src/app-receiver/output")
DECRYPTION_KEY = os.getenv("DECRYPTION_KEY", "/tmp/decryption_key")
