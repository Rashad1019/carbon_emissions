import sys
try:
    import jupyter
    import pypdf
    print("Environment verification successful: jupyter and pypdf are importable.")
except ImportError as e:
    print(f"Environment verification failed: {e}")
    sys.exit(1)
