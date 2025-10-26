# UltraPasswordCracker

An advanced, educational password auditing tool with a professional GUI, AI-assisted attacks, and real-time analytics.

> Educational and authorized-use only. Use this tool only on systems you own or have explicit permission to test.

## Features
- Multi-tab Tkinter GUI with progress logs and status bar
- Multiple attack methods: Smart Dictionary, AI Intelligence, Markov Chain, Brute Force, Hybrid, Parallel
- Hash analysis and detection (MD5, SHA-1, SHA-256, SHA-512, SHA3-256)
- AI engine with Markov chains, pattern analysis, smart password generation
- Real-time performance charts (hash rate, success rate, attempts)
- SQLite database for attack history and password strength analysis
- Exportable analytics and session reports

## Folder Structure
```
UltraPasswordCracker/
├── advanced_password_cracker.py   # Main GUI application
├── core/
│   ├── ai_engine.py               # AI/ML password analysis and generation
│   ├── attack_engine.py           # Dictionary/Brute/Hybrid/Markov/Parallel attacks
│   ├── hash_manager.py            # Hashing, detection, entropy
│   └── performance_monitor.py     # Metrics, charts, attack statistics
└── requirements.txt               # Python dependencies
```

## Installation (Source)
1. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the app:
```bash
python advanced_password_cracker.py
```

## Build Windows Executable (PyInstaller)
1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. From the project root, build the EXE:
```bash
pyinstaller --onefile --windowed --name UltraPasswordCracker \
  --hidden-import matplotlib.backends.backend_tkagg \
  --hidden-import matplotlib.animation \
  --hidden-import core.ai_engine \
  --hidden-import core.attack_engine \
  --hidden-import core.hash_manager \
  --hidden-import core.performance_monitor \
  advanced_password_cracker.py
```

3. The executable will be in the `dist/` folder.

## Usage
- Paste a target hash, select algorithm and strategy, then start an attack.
- Train the AI to improve Markov/Hybrid attacks.
- Use Quick Test to generate a target and practice.
- Review performance charts and export analytics as JSON.

## Database Storage
The application stores session data in `password_cracker.db` (SQLite). When packaged as EXE, the database is created next to the executable unless configured otherwise.

## Ethics & Legal
- This project is for cybersecurity education and research.
- Never target accounts or systems without explicit permission.
- The author and contributors are not responsible for misuse.

## License
MIT License. See `LICENSE`.

## Acknowledgements
- Python Tkinter and matplotlib communities
- Inspiration from classic tools (Hashcat, John the Ripper) for attack strategies
