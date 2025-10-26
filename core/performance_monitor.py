"""
Advanced Performance Monitoring and Analytics
"""
import time
import psutil
import threading
from datetime import datetime, timedelta
import json
import sqlite3
from typing import Dict, List
import statistics

class PerformanceMonitor:
    """Real-time performance monitoring and analytics"""
    
    def __init__(self):
        self.metrics = {
            'start_time': time.time(),
            'total_attempts': 0,
            'successful_attacks': 0,
            'failed_attacks': 0,
            'hash_rates': [],
            'memory_usage': [],
            'cpu_usage': []
        }
        
        self.attack_history = []
        self.real_time_data = {
            'timestamps': [],
            'attempts_per_second': [],
            'success_rate': []
        }
        
        # Database for persistent storage
        self.db_connection = sqlite3.connect('performance_metrics.db', check_same_thread=False)
        self._init_database()
        
        # Start monitoring thread
        self.monitoring = True
        self.monitor_thread = threading.Thread(target=self._monitor_system, daemon=True)
        self.monitor_thread.start()
    
    def _init_database(self):
        """Initialize performance database"""
        cursor = self.db_connection.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attack_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_method TEXT,
                target_hash TEXT,
                success BOOLEAN,
                attempts INTEGER,
                time_taken REAL,
                hash_rate REAL,
                password_found TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_usage REAL,
                memory_usage REAL,
                hash_rate REAL,
                active_attacks INTEGER
            )
        ''')
        
        self.db_connection.commit()
    
    def record_attack(self, attack_result: Dict):
        """Record attack results"""
        self.metrics['total_attempts'] += attack_result.get('attempts', 0)
        
        if attack_result.get('found', False):
            self.metrics['successful_attacks'] += 1
        else:
            self.metrics['failed_attacks'] += 1
        
        # Store in history
        self.attack_history.append({
            'timestamp': datetime.now(),
            'result': attack_result
        })
        
        # Store in database
        cursor = self.db_connection.cursor()
        cursor.execute('''
            INSERT INTO attack_sessions 
            (attack_method, target_hash, success, attempts, time_taken, hash_rate, password_found)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            attack_result.get('method', 'Unknown'),
            attack_result.get('target_hash', '')[:50],
            attack_result.get('found', False),
            attack_result.get('attempts', 0),
            attack_result.get('time_taken', 0),
            attack_result.get('hash_rate', 0),
            attack_result.get('password', '')[:100] if attack_result.get('found') else None
        ))
        
        self.db_connection.commit()
    
    def update_real_time_metrics(self, current_attempts: int, current_success: int):
        """Update real-time performance metrics"""
        current_time = time.time()
        
        # Calculate attempts per second
        if len(self.real_time_data['timestamps']) > 0:
            time_diff = current_time - self.real_time_data['timestamps'][-1]
            attempts_diff = current_attempts - self.metrics['total_attempts']
            if time_diff > 0:
                aps = attempts_diff / time_diff
                self.real_time_data['attempts_per_second'].append(aps)
        
        # Calculate success rate
        total_attacks = self.metrics['successful_attacks'] + self.metrics['failed_attacks']
        success_rate = (self.metrics['successful_attacks'] / total_attacks * 100) if total_attacks > 0 else 0
        self.real_time_data['success_rate'].append(success_rate)
        self.real_time_data['timestamps'].append(current_time)
        
        # Keep only last 100 data points
        for key in self.real_time_data:
            if len(self.real_time_data[key]) > 100:
                self.real_time_data[key] = self.real_time_data[key][-100:]
    
    def _monitor_system(self):
        """Monitor system resources in background"""
        while self.monitoring:
            try:
                # CPU usage
                cpu_percent = psutil.cpu_percent(interval=1)
                self.metrics['cpu_usage'].append(cpu_percent)
                
                # Memory usage
                memory = psutil.virtual_memory()
                self.metrics['memory_usage'].append(memory.percent)
                
                # Store in database
                cursor = self.db_connection.cursor()
                cursor.execute('''
                    INSERT INTO performance_metrics (cpu_usage, memory_usage, hash_rate, active_attacks)
                    VALUES (?, ?, ?, ?)
                ''', (
                    cpu_percent,
                    memory.percent,
                    self.get_current_hash_rate(),
                    len(self.attack_history)
                ))
                self.db_connection.commit()
                
                # Keep only recent data
                for key in ['cpu_usage', 'memory_usage', 'hash_rates']:
                    if len(self.metrics[key]) > 50:
                        self.metrics[key] = self.metrics[key][-50:]
                
                time.sleep(2)  # Update every 2 seconds
                
            except Exception as e:
                print(f"Performance monitoring error: {e}")
                time.sleep(5)
    
    def get_performance_summary(self) -> Dict:
        """Get comprehensive performance summary"""
        total_time = time.time() - self.metrics['start_time']
        
        return {
            'total_runtime': str(timedelta(seconds=int(total_time))),
            'total_attempts': self.metrics['total_attempts'],
            'successful_attacks': self.metrics['successful_attacks'],
            'success_rate': (self.metrics['successful_attacks'] / max(self.metrics['total_attempts'], 1)) * 100,
            'average_hash_rate': statistics.mean(self.metrics['hash_rates']) if self.metrics['hash_rates'] else 0,
            'current_cpu_usage': self.metrics['cpu_usage'][-1] if self.metrics['cpu_usage'] else 0,
            'current_memory_usage': self.metrics['memory_usage'][-1] if self.metrics['memory_usage'] else 0,
            'total_attack_sessions': len(self.attack_history)
        }
    
    def get_current_hash_rate(self) -> float:
        """Get current hash rate"""
        if len(self.metrics['hash_rates']) > 0:
            return statistics.mean(self.metrics['hash_rates'][-10:])  # Average of last 10
        return 0
    
    def get_attack_statistics(self) -> Dict:
        """Get detailed attack statistics"""
        methods = {}
        for attack in self.attack_history:
            method = attack['result'].get('method', 'Unknown')
            if method not in methods:
                methods[method] = {'count': 0, 'success': 0, 'total_attempts': 0}
            
            methods[method]['count'] += 1
            methods[method]['total_attempts'] += attack['result'].get('attempts', 0)
            if attack['result'].get('found', False):
                methods[method]['success'] += 1
        
        # Calculate success rates
        for method in methods:
            methods[method]['success_rate'] = (methods[method]['success'] / methods[method]['count']) * 100
        
        return methods
    
    def export_data(self, filename: str = 'performance_export.json'):
        """Export performance data to JSON"""
        export_data = {
            'summary': self.get_performance_summary(),
            'attack_statistics': self.get_attack_statistics(),
            'recent_attacks': self.attack_history[-20:],  # Last 20 attacks
            'system_metrics': {
                'cpu_usage': self.metrics['cpu_usage'][-50:],
                'memory_usage': self.metrics['memory_usage'][-50:],
                'hash_rates': self.metrics['hash_rates'][-50:]
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        return filename
    
    def stop_monitoring(self):
        """Stop performance monitoring"""
        self.monitoring = False
        if self.monitor_thread.is_alive():
            self.monitor_thread.join(timeout=5)
        self.db_connection.close()
