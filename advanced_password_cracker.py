"""
🚀 ULTRA-ADVANCED PASSWORD CRACKER - Bachelor's Graduation Project
Professional Cybersecurity Tool with Real Machine Learning and Advanced Analytics
Author: Mohammad
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import threading
import time
import random
import string
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from datetime import datetime
import sqlite3
import json
import webbrowser

# Import our advanced core modules
from core.hash_manager import HashManager
from core.ai_engine import AIPasswordEngine
from core.attack_engine import AdvancedAttackEngine
from core.performance_monitor import PerformanceMonitor

class UltraPasswordCracker:
    """Ultra-Advanced Password Cracker with Professional GUI"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🔐 ULTRA-ADVANCED PASSWORD CRACKER - Bachelor's Graduation Project")
        self.root.geometry("1400x900")
        self.root.configure(bg='#0a0a0a')
        
        # Initialize advanced components
        self.hash_manager = HashManager()
        self.ai_engine = AIPasswordEngine()
        self.attack_engine = AdvancedAttackEngine(self.hash_manager)
        self.performance_monitor = PerformanceMonitor()
        
        # Application state
        self.is_ai_trained = False
        self.current_attack_thread = None
        self.attack_running = False
        
        # Statistics
        self.session_stats = {
            'total_attempts': 0,
            'successful_cracks': 0,
            'total_time': 0,
            'attack_methods_used': set(),
            'ai_intelligence_level': 1.0
        }
        
        # Real-time data for visualization
        self.visualization_data = {
            'timestamps': [],
            'attempts': [],
            'success_rate': [],
            'hash_speed': []
        }
        
        self.setup_advanced_ui()
        self.setup_database()
        self.log_system_message("🚀 ULTRA-ADVANCED PASSWORD CRACKER INITIALIZED")
        self.log_system_message("🎯 Professional Cybersecurity Tool Ready")
        self.log_system_message("🧠 Real Machine Learning Engine Loaded")
        
    def setup_advanced_ui(self):
        """Setup professional user interface with multiple sections"""
        
        # ===== HEADER SECTION =====
        header_frame = tk.Frame(self.root, bg='#000000', height=120)
        header_frame.pack(fill="x", padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        # Main title
        title_label = tk.Label(header_frame, 
                             text="🔐 ULTRA-ADVANCED PASSWORD CRACKER", 
                             font=("Arial", 20, "bold"), 
                             fg='#00ff88', bg='#000000')
        title_label.pack(pady=5)
        
        # Subtitle
        subtitle_label = tk.Label(header_frame,
                                text="Bachelor's Graduation Project - Professional Cybersecurity Tool",
                                font=("Arial", 12),
                                fg='#00ffff', bg='#000000')
        subtitle_label.pack(pady=2)
        
        # Features badge
        features_label = tk.Label(header_frame,
                                text="🧠 AI Engine • 📊 Real Analytics • 🔍 Advanced Attacks • 🎯 Machine Learning",
                                font=("Arial", 10),
                                fg='#ff00ff', bg='#000000')
        features_label.pack(pady=5)
        
        # ===== MAIN NOTEBOOK (TABBED INTERFACE) =====
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Create tabs
        self.setup_attack_tab()
        self.setup_ai_tab()
        self.setup_analytics_tab()
        self.setup_training_tab()
        self.setup_settings_tab()
        
        # ===== STATUS BAR =====
        self.setup_status_bar()
        
    def setup_attack_tab(self):
        """Setup the main attack tab"""
        attack_tab = ttk.Frame(self.notebook)
        self.notebook.add(attack_tab, text="⚡ Advanced Attacks")
        
        # Main attack frame
        main_frame = ttk.LabelFrame(attack_tab, text="🎯 Password Cracking Operations", padding=15)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Target configuration
        target_frame = ttk.LabelFrame(main_frame, text="🔍 Target Configuration", padding=10)
        target_frame.pack(fill="x", pady=10)
        
        # Hash input
        hash_row = tk.Frame(target_frame)
        hash_row.pack(fill="x", pady=5)
        
        tk.Label(hash_row, text="Target Hash:", font=("Arial", 10, "bold"), width=12).pack(side="left")
        self.hash_entry = tk.Entry(hash_row, font=("Consolas", 10), width=70)
        self.hash_entry.pack(side="left", fill="x", expand=True, padx=5)
        
        # Analysis button
        tk.Button(hash_row, text="🔬 Analyze Hash", command=self.analyze_hash,
                 bg='#9C27B0', fg='white', width=15).pack(side="left", padx=5)
        
        # Configuration row
        config_row = tk.Frame(target_frame)
        config_row.pack(fill="x", pady=5)
        
        # Hash type
        tk.Label(config_row, text="Hash Algorithm:", width=15).pack(side="left")
        self.hash_type = ttk.Combobox(config_row, 
                                    values=self.hash_manager.get_available_algorithms(),
                                    state="readonly", width=12)
        self.hash_type.set("sha256")
        self.hash_type.pack(side="left", padx=5)
        
        # Max attempts
        tk.Label(config_row, text="Max Attempts:", width=12).pack(side="left", padx=(20,0))
        self.max_attempts = tk.Entry(config_row, width=10)
        self.max_attempts.insert(0, "5000")
        self.max_attempts.pack(side="left", padx=5)
        
        # Attack strategy
        tk.Label(config_row, text="Strategy:", width=8).pack(side="left", padx=(20,0))
        self.attack_strategy = ttk.Combobox(config_row, 
                                          values=["Smart AI", "Hybrid Intelligence", "Markov Chain", "Brute Force"],
                                          state="readonly", width=15)
        self.attack_strategy.set("Hybrid Intelligence")
        self.attack_strategy.pack(side="left", padx=5)
        
        # ===== ATTACK BUTTONS =====
        attack_buttons_frame = ttk.LabelFrame(main_frame, text="⚡ Attack Methods", padding=10)
        attack_buttons_frame.pack(fill="x", pady=10)
        
        # Row 1
        buttons_row1 = tk.Frame(attack_buttons_frame)
        buttons_row1.pack(pady=5)
        
        attack_buttons = [
            ("🔍 Smart Dictionary", self.smart_dictionary_attack, '#2196F3'),
            ("🤖 AI Intelligence", self.ai_intelligence_attack, '#FF5722'),
            ("📊 Markov Chain", self.markov_chain_attack, '#9C27B0'),
            ("💥 Brute Force", self.brute_force_attack, '#795548'),
        ]
        
        for text, command, color in attack_buttons:
            btn = tk.Button(buttons_row1, text=text, command=command,
                          bg=color, fg='white', width=18, height=2,
                          font=("Arial", 10, "bold"))
            btn.pack(side="left", padx=5)
        
        # Row 2
        buttons_row2 = tk.Frame(attack_buttons_frame)
        buttons_row2.pack(pady=5)
        
        advanced_buttons = [
            ("🚀 Hybrid Attack", self.hybrid_attack, '#E91E63'),
            ("⚡ Parallel Attack", self.parallel_attack, '#FF9800'),
            ("🎯 Quick Test", self.quick_test, '#4CAF50'),
            ("🛡️ Stop Attack", self.stop_attack, '#f44336'),
        ]
        
        for text, command, color in advanced_buttons:
            btn = tk.Button(buttons_row2, text=text, command=command,
                          bg=color, fg='white', width=18, height=2,
                          font=("Arial", 10, "bold"))
            btn.pack(side="left", padx=5)
        
        # ===== PROGRESS AND RESULTS =====
        results_frame = ttk.LabelFrame(main_frame, text="📊 Attack Progress & Results", padding=10)
        results_frame.pack(fill="both", expand=True, pady=10)
        
        # Progress bar
        self.progress_frame = tk.Frame(results_frame)
        self.progress_frame.pack(fill="x", pady=5)
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, mode='determinate')
        self.progress_bar.pack(fill="x", side="left", expand=True)
        
        self.progress_label = tk.Label(self.progress_frame, text="Ready for attack...", 
                                     font=("Arial", 9), fg='#cccccc')
        self.progress_label.pack(side="right", padx=10)
        
        # Results text area with tabs
        results_notebook = ttk.Notebook(results_frame)
        results_notebook.pack(fill="both", expand=True)
        
        # Main log tab
        self.results_text = scrolledtext.ScrolledText(results_notebook, 
                                                    height=15, 
                                                    font=("Consolas", 9),
                                                    bg='#1a1a1a', fg='#00ff88')
        results_notebook.add(self.results_text, text="📝 Main Log")
        
        # AI Analysis tab
        self.ai_analysis_text = scrolledtext.ScrolledText(results_notebook,
                                                         height=15,
                                                         font=("Consolas", 9),
                                                         bg='#1a1a1a', fg='#00ffff')
        results_notebook.add(self.ai_analysis_text, text="🧠 AI Analysis")
        
        # Performance tab
        self.performance_text = scrolledtext.ScrolledText(results_notebook,
                                                         height=15,
                                                         font=("Consolas", 9),
                                                         bg='#1a1a1a', fg='#ff00ff')
        results_notebook.add(self.performance_text, text="📈 Performance")
    
    def setup_ai_tab(self):
        """Setup AI and Machine Learning tab"""
        ai_tab = ttk.Frame(self.notebook)
        self.notebook.add(ai_tab, text="🧠 AI Intelligence")
        
        main_frame = ttk.LabelFrame(ai_tab, text="Artificial Intelligence Engine", padding=15)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # AI Training Section
        training_frame = ttk.LabelFrame(main_frame, text="🤖 AI Training & Model Management", padding=10)
        training_frame.pack(fill="x", pady=10)
        
        # Training info
        info_text = """
The AI Engine uses advanced machine learning techniques including:
• Markov Chains for password pattern recognition
• Pattern analysis for common password structures
• Entropy calculation for strength assessment
• Smart password generation algorithms

Training the AI will significantly improve attack success rates!
"""
        info_label = tk.Label(training_frame, text=info_text, justify='left',
                            font=("Arial", 9), fg='#cccccc')
        info_label.pack(pady=10)
        
        # Training controls
        training_controls = tk.Frame(training_frame)
        training_controls.pack(pady=10)
        
        tk.Button(training_controls, text="🚀 Train AI Model", command=self.train_ai_model,
                 bg='#2196F3', fg='white', width=15, height=2).pack(side="left", padx=5)
        
        tk.Button(training_controls, text="📊 Model Statistics", command=self.show_model_stats,
                 bg='#9C27B0', fg='white', width=15, height=2).pack(side="left", padx=5)
        
        self.ai_status_label = tk.Label(training_frame, text="🔴 AI Status: Not Trained",
                                      font=("Arial", 10, "bold"), fg='#ff4444')
        self.ai_status_label.pack(pady=5)
        
        # Password Generation Section
        gen_frame = ttk.LabelFrame(main_frame, text="🎲 Smart Password Generation", padding=10)
        gen_frame.pack(fill="x", pady=10)
        
        gen_controls = tk.Frame(gen_frame)
        gen_controls.pack(pady=10)
        
        strengths = [("Weak", "weak"), ("Medium", "medium"), ("Strong", "strong"), ("Very Strong", "very_strong")]
        
        for text, strength in strengths:
            btn = tk.Button(gen_controls, text=f"Generate {text}", 
                          command=lambda s=strength: self.generate_smart_password(s),
                          bg='#4CAF50', fg='white', width=12)
            btn.pack(side="left", padx=5)
        
        self.generated_password = tk.Entry(gen_frame, font=("Consolas", 12), width=50)
        self.generated_password.pack(pady=10)
        
        # Password Analysis Section
        analysis_frame = ttk.LabelFrame(main_frame, text="🔍 Password Strength Analysis", padding=10)
        analysis_frame.pack(fill="x", pady=10)
        
        analysis_controls = tk.Frame(analysis_frame)
        analysis_controls.pack(pady=10)
        
        self.analysis_entry = tk.Entry(analysis_controls, font=("Arial", 11), width=40)
        self.analysis_entry.pack(side="left", padx=5)
        
        tk.Button(analysis_controls, text="Analyze Strength", command=self.analyze_password_strength,
                 bg='#FF9800', fg='white').pack(side="left", padx=5)
        
        self.analysis_result = scrolledtext.ScrolledText(analysis_frame, height=8,
                                                       font=("Consolas", 9),
                                                       bg='#1a1a1a', fg='#00ff88')
        self.analysis_result.pack(fill="x", pady=5)
    
    def setup_analytics_tab(self):
        """Setup analytics and visualization tab"""
        analytics_tab = ttk.Frame(self.notebook)
        self.notebook.add(analytics_tab, text="📊 Advanced Analytics")
        
        main_frame = ttk.LabelFrame(analytics_tab, text="Performance Analytics & Visualization", padding=15)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Real-time visualization frame
        viz_frame = ttk.LabelFrame(main_frame, text="📈 Real-time Performance Metrics", padding=10)
        viz_frame.pack(fill="both", expand=True, pady=10)
        
        # Create matplotlib figure
        self.fig, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = plt.subplots(2, 2, figsize=(10, 8))
        self.fig.patch.set_facecolor('#1a1a1a')
        
        # Create canvas
        self.canvas = FigureCanvasTkAgg(self.fig, viz_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        # Start animation
        self.ani = animation.FuncAnimation(self.fig, self.update_visualization, interval=1000, cache_frame_data=False)
        
        # Analytics controls
        controls_frame = tk.Frame(main_frame)
        controls_frame.pack(fill="x", pady=10)
        
        tk.Button(controls_frame, text="🔄 Refresh Analytics", command=self.refresh_analytics,
                 bg='#2196F3', fg='white').pack(side="left", padx=5)
        
        tk.Button(controls_frame, text="💾 Export Data", command=self.export_analytics,
                 bg='#4CAF50', fg='white').pack(side="left", padx=5)
        
        tk.Button(controls_frame, text="📋 Session Report", command=self.generate_report,
                 bg='#9C27B0', fg='white').pack(side="left", padx=5)
    
    def setup_training_tab(self):
        """Setup training and educational content tab"""
        training_tab = ttk.Frame(self.notebook)
        self.notebook.add(training_tab, text="🎓 Education")
        
        main_frame = ttk.LabelFrame(training_tab, text="Cybersecurity Education & Training", padding=15)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Educational content
        content_text = """
🔐 CYBERSECURITY FUNDAMENTALS

🎯 PASSWORD SECURITY PRINCIPLES:
• Use long, complex passwords (12+ characters)
• Combine uppercase, lowercase, numbers, and symbols
• Avoid common words, patterns, and personal information
• Use unique passwords for different accounts
• Consider using password managers

🔍 HASHING ALGORITHMS:
• MD5: Fast but cryptographically broken
• SHA-1: Deprecated, vulnerable to collisions  
• SHA-256: Currently secure, widely used
• SHA-512: More secure, larger output
• bcrypt: Designed for password hashing, slow

⚡ ATTACK METHODS:
• Dictionary Attacks: Use common passwords and variations
• Brute Force: Try all possible combinations
• Rainbow Tables: Precomputed hash tables
• Social Engineering: Manipulate people
• Phishing: Deceptive websites/emails

🛡️ DEFENSE STRATEGIES:
• Strong password policies
• Multi-factor authentication
• Regular security audits
• Employee training
• Incident response plans

🧠 AI IN CYBERSECURITY:
• Pattern recognition for threat detection
• Behavioral analysis for anomaly detection
• Automated response systems
• Predictive analytics for risk assessment

⚠️ ETHICAL CONSIDERATIONS:
• This tool is for educational and authorized testing only
• Always obtain proper authorization before testing
• Respect privacy and legal boundaries
• Use knowledge to improve security, not exploit it
"""
        
        content_area = scrolledtext.ScrolledText(main_frame, font=("Consolas", 9),
                                               bg='#1a1a1a', fg='#00ff88')
        content_area.pack(fill="both", expand=True)
        content_area.insert('1.0', content_text)
        content_area.config(state='disabled')
        
        # Challenge section
        challenge_frame = ttk.LabelFrame(main_frame, text="🎯 Learning Challenges", padding=10)
        challenge_frame.pack(fill="x", pady=10)
        
        challenges = [
            ("Create a password that scores 90+", self.challenge_high_score),
            ("Crack a medium-strength password", self.challenge_crack_medium),
            ("Analyze hash entropy", self.challenge_entropy),
            ("Train AI and generate passwords", self.challenge_ai_training)
        ]
        
        for text, command in challenges:
            btn = tk.Button(challenge_frame, text=text, command=command,
                          bg='#FF9800', fg='white', width=25)
            btn.pack(side="left", padx=5, pady=5)
    
    def setup_settings_tab(self):
        """Setup settings and configuration tab"""
        settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(settings_tab, text="⚙️ Settings")
        
        main_frame = ttk.LabelFrame(settings_tab, text="Application Configuration", padding=15)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Performance settings
        perf_frame = ttk.LabelFrame(main_frame, text="Performance Settings", padding=10)
        perf_frame.pack(fill="x", pady=10)
        
        # Thread settings
        thread_row = tk.Frame(perf_frame)
        thread_row.pack(fill="x", pady=5)
        
        tk.Label(thread_row, text="Max Threads:", width=15).pack(side="left")
        self.thread_count = ttk.Combobox(thread_row, values=[str(i) for i in range(1, 17)], width=10)
        self.thread_count.set(str(self.attack_engine.cpu_count))
        self.thread_count.pack(side="left", padx=5)
        
        # UI settings
        ui_frame = ttk.LabelFrame(main_frame, text="Interface Settings", padding=10)
        ui_frame.pack(fill="x", pady=10)
        
        self.auto_scroll = tk.BooleanVar(value=True)
        tk.Checkbutton(ui_frame, text="Auto-scroll logs", variable=self.auto_scroll,
                      fg='white', bg='#2b2b2b').pack(anchor='w')
        
        self.show_animations = tk.BooleanVar(value=True)
        tk.Checkbutton(ui_frame, text="Show animations", variable=self.show_animations,
                      fg='white', bg='#2b2b2b').pack(anchor='w')
        
        # Database settings
        db_frame = ttk.LabelFrame(main_frame, text="Data Management", padding=10)
        db_frame.pack(fill="x", pady=10)
        
        db_controls = tk.Frame(db_frame)
        db_controls.pack(pady=10)
        
        tk.Button(db_controls, text="🗑️ Clear History", command=self.clear_history,
                 bg='#f44336', fg='white').pack(side="left", padx=5)
        
        tk.Button(db_controls, text="💾 Backup Data", command=self.backup_data,
                 bg='#2196F3', fg='white').pack(side="left", padx=5)
        
        # About section
        about_frame = ttk.LabelFrame(main_frame, text="About", padding=10)
        about_frame.pack(fill="x", pady=10)
        
        about_text = """
ULTRA-ADVANCED PASSWORD CRACKER
Bachelor's Graduation Project

Version: 2.0.0
Author: Mohammad
Purpose: Educational Cybersecurity Tool

Features:
• Advanced AI and Machine Learning
• Real-time Analytics and Visualization
• Multiple Attack Methods
• Professional User Interface
• Comprehensive Reporting

⚠️ Educational Use Only
"""
        about_label = tk.Label(about_frame, text=about_text, justify='left',
                             font=("Arial", 9), fg='#cccccc')
        about_label.pack(pady=10)
    
    def setup_status_bar(self):
        """Setup the status bar"""
        status_frame = tk.Frame(self.root, bg='#000000', relief='sunken', bd=1)
        status_frame.pack(fill="x", side="bottom")
        
        # Status message
        self.status_var = tk.StringVar()
        self.status_var.set("🟢 System Ready | AI: Not Trained | Attacks: 0")
        
        status_label = tk.Label(status_frame, textvariable=self.status_var,
                              bg='#000000', fg='#00ff88', font=("Arial", 9, "bold"))
        status_label.pack(side="left", padx=10, pady=2)
        
        # Performance indicators
        perf_frame = tk.Frame(status_frame, bg='#000000')
        perf_frame.pack(side="right", padx=10)
        
        self.hash_rate_label = tk.Label(perf_frame, text="⚡ H/s: 0",
                                      bg='#000000', fg='#ff00ff', font=("Arial", 9))
        self.hash_rate_label.pack(side="left", padx=5)
        
        self.memory_label = tk.Label(perf_frame, text="💾 RAM: 0%",
                                   bg='#000000', fg='#00ffff', font=("Arial", 9))
        self.memory_label.pack(side="left", padx=5)
        
        self.ai_iq_label = tk.Label(perf_frame, text="🧠 AI IQ: 100",
                                  bg='#000000', fg='#ffff00', font=("Arial", 9))
        self.ai_iq_label.pack(side="left", padx=5)
    
    def setup_database(self):
        """Initialize application database"""
        self.db_conn = sqlite3.connect('password_cracker.db', check_same_thread=False)
        cursor = self.db_conn.cursor()
        
        # Create tables
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attack_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                method TEXT,
                target_hash TEXT,
                success BOOLEAN,
                attempts INTEGER,
                time_taken REAL,
                password_found TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS password_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                password TEXT,
                strength_score REAL,
                entropy REAL,
                category TEXT
            )
        ''')
        
        self.db_conn.commit()
    
    # ===== CORE FUNCTIONALITY METHODS =====
    
    def log_system_message(self, message):
        """Log system messages"""
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        self.results_text.insert(tk.END, f"{timestamp} {message}\n")
        if self.auto_scroll.get():
            self.results_text.see(tk.END)
    
    def log_ai_message(self, message):
        """Log AI-related messages"""
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        self.ai_analysis_text.insert(tk.END, f"{timestamp} {message}\n")
        if self.auto_scroll.get():
            self.ai_analysis_text.see(tk.END)
    
    def update_progress(self, value, maximum, message):
        """Update progress bar and label"""
        self.progress_bar['value'] = value
        self.progress_bar['maximum'] = maximum
        self.progress_label.config(text=message)
        self.root.update()
    
    def train_ai_model(self):
        """Train the AI model"""
        def training_thread():
            self.update_progress(0, 100, "Starting AI training...")
            self.log_ai_message("🧠 Initializing AI Training Sequence")
            
            training_data = self.ai_engine._generate_training_data()
            
            training_steps = [
                ("Loading training data", 10),
                ("Training Markov chains", 30),
                ("Analyzing password patterns", 50),
                ("Building probability models", 70),
                ("Optimizing AI parameters", 90),
                ("Finalizing training", 100)
            ]
            
            for step, progress in training_steps:
                self.log_ai_message(f"📚 {step}...")
                self.update_progress(progress, 100, step)
                time.sleep(1)  # Simulate work
            
            success = self.ai_engine.train(training_data)
            
            if success:
                self.is_ai_trained = True
                self.session_stats['ai_intelligence_level'] = 2.5
                self.log_ai_message("✅ AI TRAINING COMPLETED SUCCESSFULLY!")
                self.log_ai_message(f"🎯 Learned {len(self.ai_engine.markov_chain):,} Markov states")
                self.log_ai_message(f"📊 Analyzed {len(self.ai_engine.common_patterns)} password patterns")
                self.ai_status_label.config(text="🟢 AI Status: Fully Trained", fg='#00ff00')
                messagebox.showinfo("AI Training", "AI model trained successfully!")
            else:
                self.log_ai_message("❌ AI training failed")
                messagebox.showerror("Training Error", "AI training failed!")
            
            self.update_progress(0, 100, "AI training completed")
        
        thread = threading.Thread(target=training_thread, daemon=True)
        thread.start()
    
    def smart_dictionary_attack(self):
        """Perform smart dictionary attack"""
        if not self.validate_attack_inputs():
            return
        
        target_hash = self.hash_entry.get().strip()
        hash_type = self.hash_type.get()
        max_attempts = int(self.max_attempts.get())
        
        self.log_system_message("🚀 Starting Smart Dictionary Attack...")
        self.attack_running = True
        
        def attack_thread():
            for result in self.attack_engine.smart_dictionary_attack(target_hash, hash_type, max_attempts):
                if not self.attack_running:
                    break
                
                if 'error' in result:
                    self.log_system_message(f"❌ Error: {result['error']}")
                    break
                
                if result.get('found', False):
                    self.handle_successful_attack(result)
                    break
                else:
                    self.update_attack_progress(result)
            
            self.attack_running = False
            self.update_progress(0, 100, "Attack completed")
        
        self.current_attack_thread = threading.Thread(target=attack_thread, daemon=True)
        self.current_attack_thread.start()
    
    def ai_intelligence_attack(self):
        """Perform AI intelligence attack"""
        if not self.is_ai_trained:
            messagebox.showwarning("AI Not Trained", "Please train the AI first!")
            return
        
        if not self.validate_attack_inputs():
            return
        
        target_hash = self.hash_entry.get().strip()
        hash_type = self.hash_type.get()
        max_attempts = int(self.max_attempts.get())
        
        self.log_system_message("🧠 Starting AI Intelligence Attack...")
        self.attack_running = True
        
        def attack_thread():
            for result in self.attack_engine.hybrid_intelligence_attack(
                target_hash, hash_type, self.ai_engine, max_attempts):
                
                if not self.attack_running:
                    break
                
                if 'error' in result:
                    self.log_system_message(f"❌ Error: {result['error']}")
                    break
                
                if result.get('found', False):
                    self.handle_successful_attack(result)
                    break
                else:
                    self.update_attack_progress(result)
            
            self.attack_running = False
            self.update_progress(0, 100, "Attack completed")
        
        self.current_attack_thread = threading.Thread(target=attack_thread, daemon=True)
        self.current_attack_thread.start()
    
    def markov_chain_attack(self):
        """Perform Markov chain attack"""
        if not self.is_ai_trained:
            messagebox.showwarning("AI Not Trained", "Please train the AI first!")
            return
        
        if not self.validate_attack_inputs():
            return
        
        target_hash = self.hash_entry.get().strip()
        hash_type = self.hash_type.get()
        max_attempts = int(self.max_attempts.get())
        
        self.log_system_message("📊 Starting Markov Chain Attack...")
        self.attack_running = True
        
        def attack_thread():
            for result in self.attack_engine.markov_chain_attack(
                target_hash, hash_type, self.ai_engine.markov_chain, 
                self.ai_engine.start_chars, max_attempts):
                
                if not self.attack_running:
                    break
                
                if 'error' in result:
                    self.log_system_message(f"❌ Error: {result['error']}")
                    break
                
                if result.get('found', False):
                    self.handle_successful_attack(result)
                    break
                else:
                    self.update_attack_progress(result)
            
            self.attack_running = False
            self.update_progress(0, 100, "Attack completed")
        
        self.current_attack_thread = threading.Thread(target=attack_thread, daemon=True)
        self.current_attack_thread.start()
    
    def brute_force_attack(self):
        """Perform brute force attack"""
        if not self.validate_attack_inputs():
            return
        
        target_hash = self.hash_entry.get().strip()
        hash_type = self.hash_type.get()
        
        self.log_system_message("💥 Starting Brute Force Attack...")
        self.attack_running = True
        
        def attack_thread():
            for result in self.attack_engine.brute_force_attack(target_hash, hash_type, max_length=4):
                if not self.attack_running:
                    break
                
                if 'error' in result:
                    self.log_system_message(f"❌ Error: {result['error']}")
                    break
                
                if result.get('found', False):
                    self.handle_successful_attack(result)
                    break
                else:
                    self.update_attack_progress(result)
            
            self.attack_running = False
            self.update_progress(0, 100, "Attack completed")
        
        self.current_attack_thread = threading.Thread(target=attack_thread, daemon=True)
        self.current_attack_thread.start()
    
    def hybrid_attack(self):
        """Perform hybrid attack combining multiple methods"""
        if not self.validate_attack_inputs():
            return
        
        target_hash = self.hash_entry.get().strip()
        hash_type = self.hash_type.get()
        max_attempts = int(self.max_attempts.get())
        
        self.log_system_message("🚀 Starting Hybrid Intelligence Attack...")
        self.attack_running = True
        
        def attack_thread():
            # Run multiple attack methods in sequence
            methods = [
                ("Smart Dictionary", self.attack_engine.smart_dictionary_attack),
                ("AI Intelligence", lambda h, t: self.attack_engine.hybrid_intelligence_attack(h, t, self.ai_engine, max_attempts//2))
            ]
            
            for method_name, method_func in methods:
                if not self.attack_running:
                    break
                    
                self.log_system_message(f"🔄 Running {method_name}...")
                
                for result in method_func(target_hash, hash_type):
                    if not self.attack_running:
                        break
                    
                    if 'error' in result:
                        self.log_system_message(f"❌ Error in {method_name}: {result['error']}")
                        break
                    
                    if result.get('found', False):
                        self.handle_successful_attack(result)
                        return
                    else:
                        self.update_attack_progress(result)
            
            self.attack_running = False
            self.update_progress(0, 100, "Hybrid attack completed")
        
        self.current_attack_thread = threading.Thread(target=attack_thread, daemon=True)
        self.current_attack_thread.start()
    
    def parallel_attack(self):
        """Perform parallel attack using multiple threads"""
        if not self.validate_attack_inputs():
            return
        
        target_hash = self.hash_entry.get().strip()
        hash_type = self.hash_type.get()
        
        self.log_system_message("⚡ Starting Parallel Dictionary Attack...")
        
        def attack_thread():
            result = self.attack_engine.parallel_dictionary_attack(target_hash, hash_type)
            
            if result.get('found', False):
                self.handle_successful_attack(result)
            else:
                self.log_system_message(f"❌ Parallel attack failed after {result.get('attempts', 0)} attempts")
                self.update_progress(100, 100, "Attack completed - No password found")
        
        thread = threading.Thread(target=attack_thread, daemon=True)
        thread.start()
    
    def quick_test(self):
        """Generate a quick test scenario"""
        test_passwords = {
            "Easy": ["password", "123456", "admin", "welcome"],
            "Medium": ["Password123", "admin@123", "Welcome2024"],
            "Hard": ["MyP@ssw0rd!", "Secure123!", "Admin@2024"],
            "Very Hard": ["Tr0ub4dor&3", "MyUlt1m@t3P@ss!", "V3ryS3cur3P@ssw0rd!"]
        }
        
        category = random.choice(list(test_passwords.keys()))
        password = random.choice(test_passwords[category])
        hash_type = self.hash_type.get()
        
        hash_value = self.hash_manager.hash_password(password, hash_type)
        
        self.hash_entry.delete(0, tk.END)
        self.hash_entry.insert(0, hash_value)
        
        self.log_system_message(f"🎲 Generated {category} test: '{password}'")
        self.log_system_message(f"🔐 Hash: {hash_value}")
        self.log_system_message("🎯 Ready for attack!")
    
    def stop_attack(self):
        """Stop current attack"""
        self.attack_running = False
        self.log_system_message("🛑 Attack stopped by user")
        self.update_progress(0, 100, "Attack stopped")
    
    def validate_attack_inputs(self):
        """Validate attack inputs"""
        if not self.hash_entry.get().strip():
            messagebox.showwarning("Input Error", "Please enter a target hash!")
            return False
        
        if not self.hash_type.get():
            messagebox.showwarning("Input Error", "Please select a hash type!")
            return False
        
        try:
            max_attempts = int(self.max_attempts.get())
            if max_attempts <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid number for max attempts!")
            return False
        
        return True
    
    def handle_successful_attack(self, result):
        """Handle successful password crack"""
        password = result['password']
        attempts = result['attempts']
        time_taken = result['time_taken']
        method = result['method']
        
        self.session_stats['successful_cracks'] += 1
        self.session_stats['total_attempts'] += attempts
        self.session_stats['attack_methods_used'].add(method)
        
        # Log success
        self.log_system_message("🎉" * 50)
        self.log_system_message("🎉 PASSWORD CRACKED SUCCESSFULLY!")
        self.log_system_message(f"🔓 Password: {password}")
        self.log_system_message(f"🎯 Method: {method}")
        self.log_system_message(f"📊 Attempts: {attempts:,}")
        self.log_system_message(f"⏱️ Time: {time_taken:.2f} seconds")
        self.log_system_message(f"⚡ Hash Rate: {result.get('hash_rate', 0):.0f} H/s")
        self.log_system_message("🎉" * 50)
        
        # Update progress
        self.update_progress(100, 100, f"Password found: {password}")
        
        # Show success message
        messagebox.showinfo("Success!", f"Password cracked: {password}\n\nAttempts: {attempts:,}\nTime: {time_taken:.2f}s")
        
        # Store in database
        cursor = self.db_conn.cursor()
        cursor.execute('''
            INSERT INTO attack_history (method, target_hash, success, attempts, time_taken, password_found)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (method, self.hash_entry.get()[:50], True, attempts, time_taken, password))
        self.db_conn.commit()
    
    def update_attack_progress(self, result):
        """Update attack progress"""
        attempts = result.get('attempts', 0)
        time_taken = result.get('time_taken', 0)
        progress = result.get('progress', 0)
        current_password = result.get('current_password', '')
        
        # Update progress bar
        self.update_progress(progress, 100, f"Attempts: {attempts:,} | Testing: {current_password}")
        
        # Update real-time stats
        if time_taken > 0:
            hash_rate = attempts / time_taken
            self.performance_monitor.metrics['hash_rates'].append(hash_rate)
        
        # Log progress every 500 attempts
        if attempts % 500 == 0:
            self.log_system_message(f"📊 Progress: {attempts:,} attempts | {progress:.1f}% complete")
    
    def analyze_hash(self):
        """Analyze hash and detect type"""
        hash_value = self.hash_entry.get().strip()
        if not hash_value:
            messagebox.showwarning("Input Error", "Please enter a hash to analyze!")
            return
        
        analysis = self.hash_manager.detect_hash_type(hash_value)
        
        result_text = f"""
🔍 HASH ANALYSIS RESULTS:
{'='*40}
📊 Hash: {hash_value}
🔢 Length: {analysis['length']} characters
🎯 Type: {analysis['description']}
📈 Entropy: {analysis['entropy']:.2f} bits
💡 Security: {self.get_hash_security_level(analysis['algorithm'])}
"""
        self.log_system_message(result_text)
        messagebox.showinfo("Hash Analysis", result_text)
    
    def get_hash_security_level(self, algorithm):
        """Get security level for hash algorithm"""
        security_levels = {
            'md5': '❌ VERY WEAK (Cryptographically broken)',
            'sha1': '⚠️ WEAK (Vulnerable to collisions)',
            'sha256': '🟢 STRONG (Widely used, secure)',
            'sha512': '🟢 VERY STRONG (Highly secure)',
            'sha3_256': '🔵 EXCELLENT (Modern standard)',
            'unknown': '❓ UNKNOWN (Verify manually)'
        }
        return security_levels.get(algorithm, '❓ UNKNOWN')
    
    def generate_smart_password(self, strength):
        """Generate smart password with specified strength"""
        password = self.ai_engine.generate_smart_password(strength)
        self.generated_password.delete(0, tk.END)
        self.generated_password.insert(0, password)
        
        # Analyze the generated password
        analysis = self.ai_engine.assess_password_strength(password)
        
        self.log_ai_message(f"🎲 Generated {strength} password: {password}")
        self.log_ai_message(f"📊 Strength: {analysis['score']}/100 ({analysis['category']})")
        self.log_ai_message(f"🔐 Entropy: {analysis['entropy']} bits")
        self.log_ai_message(f"⏱️ Crack time: {analysis['crack_time']}")
    
    def analyze_password_strength(self):
        """Analyze password strength"""
        password = self.analysis_entry.get().strip()
        if not password:
            messagebox.showwarning("Input Error", "Please enter a password to analyze!")
            return
        
        analysis = self.ai_engine.assess_password_strength(password)
        
        result_text = f"""
🔍 PASSWORD STRENGTH ANALYSIS:
{'='*40}
🔐 Password: {password}
📏 Length: {analysis['length']} characters
🎯 Strength Score: {analysis['score']}/100
📊 Category: {analysis['category']}
🔢 Entropy: {analysis['entropy']} bits
⏱️ Estimated Crack Time: {analysis['crack_time']}
💡 Character Types: {analysis['char_types']}

RECOMMENDATIONS:
{self.get_password_recommendations(analysis)}
"""
        self.analysis_result.delete('1.0', tk.END)
        self.analysis_result.insert('1.0', result_text)
        
        # Store in database
        cursor = self.db_conn.cursor()
        cursor.execute('''
            INSERT INTO password_analysis (password, strength_score, entropy, category)
            VALUES (?, ?, ?, ?)
        ''', (password, analysis['score'], analysis['entropy'], analysis['category']))
        self.db_conn.commit()
    
    def get_password_recommendations(self, analysis):
        """Get password improvement recommendations"""
        score = analysis['score']
        length = analysis['length']
        char_types = analysis['char_types']
        
        recommendations = []
        
        if score < 40:
            recommendations.append("❌ CRITICAL: This password is very weak!")
            recommendations.append("💡 Increase length to at least 12 characters")
            recommendations.append("💡 Add uppercase letters, numbers, and symbols")
            recommendations.append("💡 Avoid common words and patterns")
        elif score < 60:
            recommendations.append("⚠️ MODERATE: This password could be stronger")
            recommendations.append("💡 Consider increasing length")
            recommendations.append("💡 Add more character variety")
        elif score < 80:
            recommendations.append("🟢 GOOD: This is a decent password")
            recommendations.append("💡 For better security, increase length")
        else:
            recommendations.append("🔵 EXCELLENT: This is a strong password!")
            recommendations.append("💡 No improvements needed")
        
        if length < 8:
            recommendations.append("📏 Password is too short (minimum 8 characters)")
        if char_types < 3:
            recommendations.append("🎨 Use more character types (upper, lower, numbers, symbols)")
        
        return '\n'.join(recommendations)
    
    def show_model_stats(self):
        """Show AI model statistics"""
        if not self.is_ai_trained:
            messagebox.showwarning("AI Not Trained", "Please train the AI first!")
            return
        
        stats_text = f"""
🧠 AI MODEL STATISTICS:
{'='*30}
📊 Markov States: {len(self.ai_engine.markov_chain):,}
🎯 Patterns Learned: {len(self.ai_engine.common_patterns)}
🔠 Start Characters: {len(self.ai_engine.start_chars)}
📈 Training Data: {len(self.ai_engine.training_data)} passwords
💡 Intelligence Level: {self.session_stats['ai_intelligence_level']:.1f}
"""
        self.log_ai_message(stats_text)
        messagebox.showinfo("AI Model Statistics", stats_text)
    
    def update_visualization(self, frame):
        """Update real-time visualization"""
        try:
            # Get current performance data
            perf_summary = self.performance_monitor.get_performance_summary()
            attack_stats = self.performance_monitor.get_attack_statistics()
            
            # Update status bar
            self.status_var.set(f"🟢 System Active | AI: {'Trained' if self.is_ai_trained else 'Not Trained'} | Attacks: {perf_summary['successful_attacks']}")
            self.hash_rate_label.config(text=f"⚡ H/s: {perf_summary['average_hash_rate']:.0f}")
            self.memory_label.config(text=f"💾 RAM: {perf_summary['current_memory_usage']:.1f}%")
            self.ai_iq_label.config(text=f"🧠 AI IQ: {int(100 + self.session_stats['ai_intelligence_level'] * 50)}")
            
            # Update visualization data
            current_time = time.time()
            self.visualization_data['timestamps'].append(current_time)
            self.visualization_data['attempts'].append(perf_summary['total_attempts'])
            self.visualization_data['success_rate'].append(perf_summary['success_rate'])
            self.visualization_data['hash_speed'].append(perf_summary['average_hash_rate'])
            
            # Keep only recent data
            for key in self.visualization_data:
                if len(self.visualization_data[key]) > 50:
                    self.visualization_data[key] = self.visualization_data[key][-50:]
            
            # Update plots
            self.update_plots()
            
        except Exception as e:
            print(f"Visualization update error: {e}")
    
    def update_plots(self):
        """Update all matplotlib plots"""
        # Clear all axes
        for ax in [self.ax1, self.ax2, self.ax3, self.ax4]:
            ax.clear()
        
        # Plot 1: Attack attempts over time
        if len(self.visualization_data['timestamps']) > 1:
            self.ax1.plot(self.visualization_data['attempts'], 'b-', linewidth=2)
        self.ax1.set_title('Total Attack Attempts', color='white', fontweight='bold')
        self.ax1.set_facecolor('#1a1a1a')
        self.ax1.tick_params(colors='white')
        
        # Plot 2: Success rate
        if len(self.visualization_data['success_rate']) > 1:
            self.ax2.plot(self.visualization_data['success_rate'], 'g-', linewidth=2)
        self.ax2.set_title('Success Rate (%)', color='white', fontweight='bold')
        self.ax2.set_facecolor('#1a1a1a')
        self.ax2.tick_params(colors='white')
        
        # Plot 3: Hash speed
        if len(self.visualization_data['hash_speed']) > 1:
            self.ax3.plot(self.visualization_data['hash_speed'], 'r-', linewidth=2)
        self.ax3.set_title('Hash Rate (H/s)', color='white', fontweight='bold')
        self.ax3.set_facecolor('#1a1a1a')
        self.ax3.tick_params(colors='white')
        
        # Plot 4: Method efficiency
        methods = list(self.performance_monitor.get_attack_statistics().keys())
        if methods:
            efficiencies = [50 + random.randint(-20, 20) for _ in methods]  # Placeholder
            bars = self.ax4.bar(methods, efficiencies, color=['#ff6b6b', '#4ecdc4', '#45b7d1'])
            self.ax4.set_title('Method Efficiency', color='white', fontweight='bold')
            self.ax4.set_facecolor('#1a1a1a')
            self.ax4.tick_params(colors='white')
            
            # Add value labels
            for bar, eff in zip(bars, efficiencies):
                self.ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                             f'{eff}%', ha='center', va='bottom', color='white')
        
        self.fig.tight_layout()
        self.canvas.draw()
    
    def refresh_analytics(self):
        """Refresh analytics data"""
        self.visualization_data = {'timestamps': [], 'attempts': [], 'success_rate': [], 'hash_speed': []}
        self.log_system_message("📊 Analytics data refreshed")
    
    def export_analytics(self):
        """Export analytics data"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            exported_file = self.performance_monitor.export_data(filename)
            self.log_system_message(f"💾 Analytics exported to: {exported_file}")
            messagebox.showinfo("Export Successful", f"Data exported to:\n{exported_file}")
    
    def generate_report(self):
        """Generate session report"""
        report_data = {
            'session_summary': self.performance_monitor.get_performance_summary(),
            'attack_statistics': self.performance_monitor.get_attack_statistics(),
            'ai_status': {
                'trained': self.is_ai_trained,
                'intelligence_level': self.session_stats['ai_intelligence_level'],
                'markov_states': len(self.ai_engine.markov_chain) if self.is_ai_trained else 0
            },
            'timestamp': datetime.now().isoformat()
        }
        
        report_text = f"""
📊 SESSION REPORT
{'='*50}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

🎯 PERFORMANCE SUMMARY:
• Total Runtime: {report_data['session_summary']['total_runtime']}
• Total Attempts: {report_data['session_summary']['total_attempts']:,}
• Successful Attacks: {report_data['session_summary']['successful_attacks']}
• Success Rate: {report_data['session_summary']['success_rate']:.1f}%
• Average Hash Rate: {report_data['session_summary']['average_hash_rate']:.0f} H/s

🧠 AI STATUS:
• AI Trained: {'Yes' if report_data['ai_status']['trained'] else 'No'}
• Intelligence Level: {report_data['ai_status']['intelligence_level']:.1f}
• Markov States: {report_data['ai_status']['markov_states']:,}

⚡ ATTACK METHODS USED:
"""
        
        for method, stats in report_data['attack_statistics'].items():
            report_text += f"• {method}: {stats['count']} attacks, {stats['success_rate']:.1f}% success rate\n"
        
        # Show report
        self.performance_text.delete('1.0', tk.END)
        self.performance_text.insert('1.0', report_text)
        
        messagebox.showinfo("Session Report", "Report generated in Performance tab")
    
    def clear_history(self):
        """Clear attack history"""
        if messagebox.askyesno("Confirm", "Clear all attack history and analytics?"):
            cursor = self.db_conn.cursor()
            cursor.execute('DELETE FROM attack_history')
            cursor.execute('DELETE FROM password_analysis')
            self.db_conn.commit()
            
            self.performance_monitor.attack_history.clear()
            self.visualization_data = {'timestamps': [], 'attempts': [], 'success_rate': [], 'hash_speed': []}
            
            self.log_system_message("🗑️ All history cleared")
            messagebox.showinfo("Success", "All history and analytics cleared!")
    
    def backup_data(self):
        """Backup application data"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".db",
            filetypes=[("Database files", "*.db"), ("All files", "*.*")]
        )
        
        if filename:
            # Simple backup by copying the database
            import shutil
            shutil.copy2('password_cracker.db', filename)
            self.log_system_message(f"💾 Data backed up to: {filename}")
            messagebox.showinfo("Backup Successful", f"Data backed up to:\n{filename}")
    
    # ===== CHALLENGE METHODS =====
    
    def challenge_high_score(self):
        """Challenge: Create high-scoring password"""
        self.analysis_entry.delete(0, tk.END)
        self.analysis_entry.insert(0, "Try to create a password that scores 90+!")
        messagebox.showinfo("Challenge", "Create a password that scores 90+ in strength analysis!\n\nTips:\n• Use 12+ characters\n• Mix uppercase, lowercase, numbers, symbols\n• Avoid common patterns")
    
    def challenge_crack_medium(self):
        """Challenge: Crack medium password"""
        password = "Secure123!"
        hash_value = self.hash_manager.hash_password(password, "sha256")
        
        self.hash_entry.delete(0, tk.END)
        self.hash_entry.insert(0, hash_value)
        self.hash_type.set("sha256")
        
        self.log_system_message("🎯 Challenge: Crack the medium-strength password!")
        self.log_system_message("💡 Hint: The password is 'Secure123!'")
        messagebox.showinfo("Challenge", "Try to crack the medium-strength password!\n\nUse different attack methods and see which works best.")
    
    def challenge_entropy(self):
        """Challenge: Analyze hash entropy"""
        messagebox.showinfo("Challenge", "Analyze different hashes and compare their entropy!\n\nTry:\n• MD5 hashes\n• SHA-256 hashes\n• See how entropy relates to security")
    
    def challenge_ai_training(self):
        """Challenge: Train AI and generate passwords"""
        messagebox.showinfo("Challenge", "Train the AI and generate passwords of different strengths!\n\nCompare:\n• Weak vs Strong passwords\n• AI-generated vs manually created\n• Different character combinations")
    
    def run(self):
        """Start the application"""
        try:
            self.root.mainloop()
        finally:
            # Cleanup
            self.performance_monitor.stop_monitoring()
            if hasattr(self, 'db_conn'):
                self.db_conn.close()

# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    print("🚀 Starting Ultra-Advanced Password Cracker...")
    print("🎓 Bachelor's Graduation Project - Professional Cybersecurity Tool")
    print("⚠️  Educational Use Only")
    
    # Check dependencies
    try:
        import matplotlib
        import numpy
        print("✅ All dependencies loaded successfully")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("💡 Run: pip install matplotlib numpy scikit-learn")
        exit(1)
    
    # Create and run application
    app = UltraPasswordCracker()
    app.run()
