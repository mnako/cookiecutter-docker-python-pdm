import os


os.system("make build-dev")
os.system("make install-dev-deps")
os.system("make format")
os.system("make test")
os.system("cat README.md")
