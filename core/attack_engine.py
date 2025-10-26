"""
Advanced Password Attack Engine
"""
import itertools
import string
import random
import time
import hashlib
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing
from typing import Dict, List, Optional, Generator
from collections import defaultdict
import re

class AdvancedAttackEngine:
    """Professional password attack engine with multiple algorithms"""
    
    def __init__(self, hash_manager):
        self.hash_manager = hash_manager
        self.cpu_count = multiprocessing.cpu_count()
        self.attack_stats = defaultdict(int)
        
        # Advanced wordlists
        self.advanced_wordlists = self._build_advanced_wordlists()
        
    def smart_dictionary_attack(self, target_hash: str, hash_type: str, max_attempts: int = 5000) -> Generator[Dict, None, None]:
        """Advanced dictionary attack with intelligent pattern matching"""
        start_time = time.time()
        attempts = 0
        
        # Generate comprehensive wordlist
        wordlist = self._generate_comprehensive_wordlist()[:max_attempts]
        
        hash_func = self.hash_manager.algorithms.get(hash_type)
        if not hash_func:
            yield {'error': f"Unsupported hash type: {hash_type}"}
            return
        
        self.log_attack_start("Smart Dictionary", len(wordlist))
        
        for i, password in enumerate(wordlist):
            attempts = i + 1
            
            # Test password
            test_hash = hash_func(password.encode()).hexdigest()
            
            if test_hash == target_hash:
                yield {
                    'found': True,
                    'password': password,
                    'attempts': attempts,
                    'time_taken': time.time() - start_time,
                    'method': 'Smart Dictionary',
                    'hash_rate': attempts / (time.time() - start_time)
                }
                return
            
            # Yield progress every 100 attempts
            if attempts % 100 == 0:
                yield {
                    'found': False,
                    'attempts': attempts,
                    'time_taken': time.time() - start_time,
                    'current_password': password,
                    'progress': (attempts / len(wordlist)) * 100
                }
        
        yield {
            'found': False,
            'attempts': attempts,
            'time_taken': time.time() - start_time,
            'method': 'Smart Dictionary'
        }
    
    def markov_chain_attack(self, target_hash: str, hash_type: str, markov_chain: dict, 
                          start_chars: dict, max_attempts: int = 3000) -> Generator[Dict, None, None]:
        """Markov chain based password attack"""
        start_time = time.time()
        attempts = 0
        
        hash_func = self.hash_manager.algorithms.get(hash_type)
        if not hash_func:
            yield {'error': f"Unsupported hash type: {hash_type}"}
            return
        
        self.log_attack_start("Markov Chain", max_attempts)
        
        for i in range(max_attempts):
            attempts = i + 1
            
            # Generate password using Markov chain
            password = self._generate_markov_password(markov_chain, start_chars)
            
            # Test password
            test_hash = hash_func(password.encode()).hexdigest()
            
            if test_hash == target_hash:
                yield {
                    'found': True,
                    'password': password,
                    'attempts': attempts,
                    'time_taken': time.time() - start_time,
                    'method': 'Markov Chain',
                    'hash_rate': attempts / (time.time() - start_time)
                }
                return
            
            # Yield progress every 50 attempts
            if attempts % 50 == 0:
                yield {
                    'found': False,
                    'attempts': attempts,
                    'time_taken': time.time() - start_time,
                    'current_password': password,
                    'progress': (attempts / max_attempts) * 100
                }
        
        yield {
            'found': False,
            'attempts': attempts,
            'time_taken': time.time() - start_time,
            'method': 'Markov Chain'
        }
    
    def hybrid_intelligence_attack(self, target_hash: str, hash_type: str, 
                                 ai_engine, max_attempts: int = 4000) -> Generator[Dict, None, None]:
        """Hybrid AI attack combining multiple methods"""
        start_time = time.time()
        attempts = 0
        
        hash_func = self.hash_manager.algorithms.get(hash_type)
        if not hash_func:
            yield {'error': f"Unsupported hash type: {hash_type}"}
            return
        
        self.log_attack_start("Hybrid AI", max_attempts)
        
        # Multiple generation methods
        methods = [
            lambda: ai_engine.generate_markov_password(6, 12),
            lambda: ai_engine.generate_smart_password('medium'),
            lambda: ai_engine.generate_smart_password('strong'),
            lambda: self._generate_pattern_based_password(),
            lambda: self._generate_leet_password()
        ]
        
        for i in range(max_attempts):
            attempts = i + 1
            
            # Rotate through different methods
            method_index = i % len(methods)
            password = methods[method_index]()
            
            # Test password
            test_hash = hash_func(password.encode()).hexdigest()
            
            if test_hash == target_hash:
                yield {
                    'found': True,
                    'password': password,
                    'attempts': attempts,
                    'time_taken': time.time() - start_time,
                    'method': 'Hybrid AI',
                    'hash_rate': attempts / (time.time() - start_time)
                }
                return
            
            # Yield progress every 50 attempts
            if attempts % 50 == 0:
                yield {
                    'found': False,
                    'attempts': attempts,
                    'time_taken': time.time() - start_time,
                    'current_password': password,
                    'progress': (attempts / max_attempts) * 100,
                    'method': f'Hybrid AI (Method {method_index + 1})'
                }
        
        yield {
            'found': False,
            'attempts': attempts,
            'time_taken': time.time() - start_time,
            'method': 'Hybrid AI'
        }
    
    def brute_force_attack(self, target_hash: str, hash_type: str, 
                          max_length: int = 6, charset: str = None) -> Generator[Dict, None, None]:
        """Configurable brute force attack"""
        start_time = time.time()
        attempts = 0
        
        if charset is None:
            charset = string.ascii_letters + string.digits + '!@#$%^&*'
        
        hash_func = self.hash_manager.algorithms.get(hash_type)
        if not hash_func:
            yield {'error': f"Unsupported hash type: {hash_type}"}
            return
        
        self.log_attack_start("Brute Force", sum(len(charset)**i for i in range(1, max_length + 1)))
        
        for length in range(1, max_length + 1):
            for candidate in itertools.product(charset, repeat=length):
                attempts += 1
                candidate_str = ''.join(candidate)
                
                test_hash = hash_func(candidate_str.encode()).hexdigest()
                
                if test_hash == target_hash:
                    yield {
                        'found': True,
                        'password': candidate_str,
                        'attempts': attempts,
                        'time_taken': time.time() - start_time,
                        'method': 'Brute Force',
                        'hash_rate': attempts / (time.time() - start_time)
                    }
                    return
                
                # Yield progress every 1000 attempts
                if attempts % 1000 == 0:
                    yield {
                        'found': False,
                        'attempts': attempts,
                        'time_taken': time.time() - start_time,
                        'current_length': length,
                        'progress': (length / max_length) * 100
                    }
        
        yield {
            'found': False,
            'attempts': attempts,
            'time_taken': time.time() - start_time,
            'method': 'Brute Force'
        }
    
    def parallel_dictionary_attack(self, target_hash: str, hash_type: str, 
                                 max_workers: int = None) -> Dict:
        """Parallel dictionary attack using multiple threads"""
        if max_workers is None:
            max_workers = self.cpu_count
        
        hash_func = self.hash_manager.algorithms.get(hash_type)
        if not hash_func:
            return {'error': f"Unsupported hash type: {hash_type}"}
        
        wordlist = self._generate_comprehensive_wordlist()
        chunk_size = len(wordlist) // max_workers
        
        def check_chunk(chunk):
            for password in chunk:
                if hash_func(password.encode()).hexdigest() == target_hash:
                    return password
            return None
        
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            chunks = [wordlist[i:i + chunk_size] for i in range(0, len(wordlist), chunk_size)]
            futures = [executor.submit(check_chunk, chunk) for chunk in chunks]
            
            for future in as_completed(futures):
                result = future.result()
                if result:
                    return {
                        'found': True,
                        'password': result,
                        'time_taken': time.time() - start_time,
                        'method': 'Parallel Dictionary',
                        'workers': max_workers
                    }
        
        return {
            'found': False,
            'time_taken': time.time() - start_time,
            'method': 'Parallel Dictionary',
            'attempts': len(wordlist)
        }
    
    def _generate_markov_password(self, markov_chain: dict, start_chars: dict, 
                                min_length: int = 4, max_length: int = 12) -> str:
        """Generate password using Markov chain"""
        if not start_chars:
            return self._generate_random_password()
        
        # Choose starting character based on frequency
        start_chars_list = list(start_chars.keys())
        start_weights = list(start_chars.values())
        
        current_char = random.choices(start_chars_list, weights=start_weights)[0]
        password = [current_char]
        
        while len(password) < max_length:
            next_chars = list(markov_chain[current_char].keys())
            next_weights = list(markov_chain[current_char].values())
            
            if not next_chars:
                break
                
            next_char = random.choices(next_chars, weights=next_weights)[0]
            password.append(next_char)
            current_char = next_char
            
            if len(password) >= min_length and random.random() < 0.3:
                break
        
        return ''.join(password)
    
    def _generate_comprehensive_wordlist(self) -> List[str]:
        """Generate comprehensive password wordlist"""
        base_words = [
            'password', '123456', 'admin', 'test', 'welcome', 'qwerty', 
            'letmein', 'monkey', 'dragon', 'master', 'hello', 'freedom',
            'whatever', 'computer', 'internet', 'access', 'control', 'login',
            'secret', 'key', 'system', 'default', 'guest', 'user', 'service'
        ]
        
        wordlist = []
        
        # Base words with common variations
        for word in base_words:
            variations = [
                # Basic variations
                word, word + '123', word + '!', word.capitalize(), word.upper(),
                word + '2024', word + '2025', word + '@123', word + '!@#',
                
                # Advanced variations
                word.replace('a', '@').replace('o', '0').replace('i', '1'),
                word.replace('a', '4').replace('e', '3').replace('s', '5'),
                word.capitalize() + '123', word.capitalize() + '!',
                word.upper() + '123', word.upper() + '!',
                
                # Year variations
                word + '2023', word + '2022', word + '2021', word + '2020',
                word + '2019', word + '2018', word + '2017',
                
                # Special character variations
                word + '#', word + '$', word + '%', word + '&', word + '*',
                '!' + word, '@' + word, '#' + word, '$' + word,
            ]
            wordlist.extend(variations)
        
        # Common patterns
        common_patterns = [
            'admin123', 'test123', 'welcome123', 'password123', 'login123',
            'Admin123', 'Test123', 'Welcome123', 'Password123', 'Login123',
            'admin@123', 'test@123', 'welcome@123', 'password@123',
            'P@ssw0rd', 'Adm1n', 'T3st', 'W3lc0me', 'L0g1n', 'S3cr3t',
            'Pass@123', 'Admin@2024', 'Welcome@2024', 'Test@2024'
        ]
        wordlist.extend(common_patterns)
        
        # Remove duplicates and return
        return list(set(wordlist))
    
    def _generate_pattern_based_password(self) -> str:
        """Generate password based on common patterns"""
        patterns = [
            # Letter patterns
            lambda: ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 8))),
            lambda: ''.join(random.choices(string.ascii_uppercase, k=random.randint(4, 8))),
            lambda: ''.join(random.choices(string.ascii_letters, k=random.randint(6, 10))),
            
            # Mixed patterns
            lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=8)),
            lambda: ''.join(random.choices(string.ascii_lowercase, k=4)) + 
                    ''.join(random.choices(string.digits, k=4)),
            lambda: ''.join(random.choices(string.ascii_uppercase, k=3)) +
                    ''.join(random.choices(string.ascii_lowercase, k=3)) +
                    ''.join(random.choices(string.digits, k=2)),
        ]
        
        return random.choice(patterns)()
    
    def _generate_leet_password(self) -> str:
        """Generate leet speak password"""
        base_words = ['password', 'admin', 'test', 'user', 'login', 'secret']
        word = random.choice(base_words)
        
        leet_map = {
            'a': ['@', '4'],
            'e': ['3'],
            'i': ['1', '!'],
            'o': ['0'],
            's': ['5', '$'],
            't': ['7']
        }
        
        leet_word = ''
        for char in word:
            if char.lower() in leet_map and random.random() < 0.7:
                leet_word += random.choice(leet_map[char.lower()])
            else:
                leet_word += char
        
        # Add random suffix
        suffixes = ['', '123', '!', '@123', '!@#', '2024']
        return leet_word + random.choice(suffixes)
    
    def _generate_random_password(self, length: int = 10) -> str:
        """Generate random password"""
        chars = string.ascii_letters + string.digits + '!@#$%^&*'
        return ''.join(random.choice(chars) for _ in range(length))
    
    def _build_advanced_wordlists(self) -> Dict[str, List[str]]:
        """Build advanced wordlists for different attack types"""
        return {
            'common': self._generate_comprehensive_wordlist(),
            'admin': ['admin', 'Admin', 'ADMIN', 'administrator', 'Administrator'],
            'test': ['test', 'Test', 'TEST', 'testing', 'Testing'],
            'default': ['default', 'Default', 'DEFAULT', 'password', 'Password'],
            'user': ['user', 'User', 'USER', 'username', 'Username']
        }
    
    def log_attack_start(self, method: str, total_attempts: int):
        """Log attack start"""
        print(f"🚀 Starting {method} attack with {total_attempts:,} potential attempts")
        self.attack_stats[method] += 1
    
    def get_attack_statistics(self) -> Dict:
        """Get attack statistics"""
        return dict(self.attack_stats)
