"""
Advanced Hash Management System
"""
import hashlib
import bcrypt
import string
import secrets
from typing import Dict, Optional

class HashManager:
    """Professional hash management with multiple algorithms"""
    
    def __init__(self):
        self.algorithms = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1, 
            'sha256': hashlib.sha256,
            'sha512': hashlib.sha512,
            'sha3_256': hashlib.sha3_256,
            'sha3_512': hashlib.sha3_512,
            'blake2b': hashlib.blake2b,
            'blake2s': hashlib.blake2s
        }
        
        # Common password patterns database
        self.common_patterns = self._load_common_patterns()
    
    def hash_password(self, password: str, algorithm: str = 'sha256') -> str:
        """Hash password using specified algorithm"""
        if algorithm not in self.algorithms:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        
        hash_func = self.algorithms[algorithm]
        return hash_func(password.encode()).hexdigest()
    
    def hash_with_salt(self, password: str, algorithm: str = 'sha256') -> tuple:
        """Hash password with random salt"""
        salt = secrets.token_hex(16)
        salted_password = salt + password
        hash_value = self.hash_password(salted_password, algorithm)
        return hash_value, salt
    
    def verify_hash(self, password: str, hash_value: str, algorithm: str) -> bool:
        """Verify password against hash"""
        test_hash = self.hash_password(password, algorithm)
        return secrets.compare_digest(test_hash, hash_value)
    
    def detect_hash_type(self, hash_value: str) -> Dict[str, str]:
        """Intelligent hash type detection"""
        hash_length = len(hash_value)
        hash_types = {
            32: ('md5', 'MD5 (128-bit)'),
            40: ('sha1', 'SHA-1 (160-bit)'),
            64: ('sha256', 'SHA-256 (256-bit)'),
            128: ('sha512', 'SHA-512 (512-bit)'),
            56: ('sha224', 'SHA-224 (224-bit)'),
            96: ('sha384', 'SHA-384 (384-bit)')
        }
        
        algo, description = hash_types.get(hash_length, ('unknown', 'Unknown Hash Type'))
        
        return {
            'algorithm': algo,
            'description': description,
            'length': hash_length,
            'entropy': self._calculate_hash_entropy(hash_value)
        }
    
    def _calculate_hash_entropy(self, hash_value: str) -> float:
        """Calculate entropy of hash value"""
        from collections import Counter
        import math
        
        freq = Counter(hash_value)
        prob = [count/len(hash_value) for count in freq.values()]
        return -sum(p * math.log2(p) for p in prob if p > 0)
    
    def _load_common_patterns(self) -> list:
        """Load common password patterns"""
        return [
            # Basic patterns
            r'^[a-z]+$', r'^[A-Z]+$', r'^[0-9]+$', r'^[a-z0-9]+$',
            # Common sequences
            r'123', r'abc', r'qwerty', r'password', r'admin',
            # Date patterns
            r'19\d{2}', r'20\d{2}', r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',
            # Leet speak patterns
            r'[a4@]', r'[e3]', r'[i1!]', r'[o0]', r'[s5$]'
        ]
    
    def get_available_algorithms(self) -> list:
        """Get list of available hashing algorithms"""
        return list(self.algorithms.keys())
