"""
Advanced AI Engine for Password Analysis and Generation
"""
import random
import string
import numpy as np
from collections import defaultdict, Counter
import math
from typing import List, Tuple, Dict
import re

class AIPasswordEngine:
    """Advanced AI engine with machine learning capabilities"""
    
    def __init__(self):
        # Markov Chain for password generation
        self.markov_chain = defaultdict(lambda: defaultdict(int))
        self.start_chars = defaultdict(int)
        
        # Pattern database
        self.common_patterns = []
        self.password_weights = {}
        
        # Training data
        self.training_data = []
        self.is_trained = False
        
        # Advanced metrics
        self.entropy_thresholds = {
            'very_weak': 28,
            'weak': 35,
            'moderate': 59,
            'strong': 79,
            'very_strong': 120
        }
    
    def train(self, password_list: List[str]) -> bool:
        """Train AI model on password dataset"""
        try:
            if not password_list:
                password_list = self._generate_training_data()
            
            self.training_data = password_list
            
            # Train Markov Chain
            self._train_markov_chain(password_list)
            
            # Extract patterns
            self._extract_advanced_patterns(password_list)
            
            # Calculate weights
            self._calculate_password_weights(password_list)
            
            self.is_trained = True
            return True
            
        except Exception as e:
            print(f"AI Training Error: {e}")
            return False
    
    def _train_markov_chain(self, passwords: List[str]):
        """Train Markov chain on password dataset"""
        for password in passwords:
            if len(password) < 2:
                continue
                
            # Track starting characters
            self.start_chars[password[0]] += 1
            
            # Build transition probabilities
            for i in range(len(password) - 1):
                current_char = password[i]
                next_char = password[i + 1]
                self.markov_chain[current_char][next_char] += 1
    
    def _extract_advanced_patterns(self, passwords: List[str]):
        """Extract advanced password patterns"""
        pattern_counter = Counter()
        length_distribution = Counter()
        char_type_distribution = Counter()
        
        for password in passwords:
            # Length patterns
            length_distribution[len(password)] += 1
            
            # Character type patterns
            pattern = self._password_to_pattern(password)
            pattern_counter[pattern] += 1
            
            # Character type distribution
            char_types = self._get_char_types(password)
            char_type_distribution[char_types] += 1
        
        # Store most common patterns
        self.common_patterns = [
            pattern for pattern, count in pattern_counter.most_common(50)
        ]
        
        self.length_distribution = length_distribution
        self.char_type_distribution = char_type_distribution
    
    def _password_to_pattern(self, password: str) -> str:
        """Convert password to pattern representation"""
        pattern = []
        for char in password:
            if char.islower():
                pattern.append('L')
            elif char.isupper():
                pattern.append('U')
            elif char.isdigit():
                pattern.append('D')
            else:
                pattern.append('S')
        return ''.join(pattern)
    
    def _get_char_types(self, password: str) -> str:
        """Get character types used in password"""
        types = set()
        if any(c.islower() for c in password):
            types.add('lower')
        if any(c.isupper() for c in password):
            types.add('upper')
        if any(c.isdigit() for c in password):
            types.add('digit')
        if any(not c.isalnum() for c in password):
            types.add('special')
        return ''.join(sorted(types))
    
    def _calculate_password_weights(self, passwords: List[str]):
        """Calculate password weights based on frequency"""
        password_freq = Counter(passwords)
        total = len(passwords)
        
        for password, freq in password_freq.items():
            # Lower weight for more common passwords
            self.password_weights[password] = 1 - (freq / total)
    
    def generate_markov_password(self, min_length: int = 8, max_length: int = 16) -> str:
        """Generate password using Markov chain"""
        if not self.start_chars:
            return self._generate_random_password()
        
        # Select starting character based on frequency
        start_chars = list(self.start_chars.keys())
        weights = list(self.start_chars.values())
        
        current_char = random.choices(start_chars, weights=weights)[0]
        password = [current_char]
        
        # Generate using Markov chain
        while len(password) < max_length:
            next_chars = list(self.markov_chain[current_char].keys())
            next_weights = list(self.markov_chain[current_char].values())
            
            if not next_chars or (len(password) >= min_length and random.random() < 0.2):
                break
                
            next_char = random.choices(next_chars, weights=next_weights)[0]
            password.append(next_char)
            current_char = next_char
        
        return ''.join(password)
    
    def generate_smart_password(self, strength: str = 'strong') -> str:
        """Generate password with specified strength"""
        strength_params = {
            'weak': {'length': (6, 8), 'types': 2},
            'medium': {'length': (8, 12), 'types': 3},
            'strong': {'length': (12, 16), 'types': 4},
            'very_strong': {'length': (16, 20), 'types': 4}
        }
        
        params = strength_params.get(strength, strength_params['strong'])
        min_len, max_len = params['length']
        required_types = params['types']
        
        while True:
            if self.is_trained and random.random() < 0.7:
                password = self.generate_markov_password(min_len, max_len)
            else:
                password = self._generate_structured_password(min_len, max_len, required_types)
            
            if self.assess_password_strength(password)['score'] >= self._get_min_score(strength):
                return password
    
    def _generate_structured_password(self, min_len: int, max_len: int, required_types: int) -> str:
        """Generate structured password with required character types"""
        length = random.randint(min_len, max_len)
        
        # Define character pools
        pools = {
            'lower': string.ascii_lowercase,
            'upper': string.ascii_uppercase,
            'digit': string.digits,
            'special': '!@#$%^&*()_+-=[]{}|;:,.<>?'
        }
        
        # Select required character types
        selected_types = random.sample(list(pools.keys()), required_types)
        
        password = []
        # Ensure at least one of each selected type
        for char_type in selected_types:
            password.append(random.choice(pools[char_type]))
        
        # Fill remaining length
        all_chars = ''.join(pools[ctype] for ctype in selected_types)
        while len(password) < length:
            password.append(random.choice(all_chars))
        
        # Shuffle the password
        random.shuffle(password)
        return ''.join(password)
    
    def _generate_random_password(self, length: int = 12) -> str:
        """Generate random password as fallback"""
        chars = string.ascii_letters + string.digits + '!@#$%^&*'
        return ''.join(random.choice(chars) for _ in range(length))
    
    def assess_password_strength(self, password: str) -> Dict:
        """Comprehensive password strength assessment"""
        if not password:
            return {'score': 0, 'category': 'Empty', 'entropy': 0}
        
        # Calculate entropy
        entropy = self._calculate_entropy(password)
        
        # Base score from entropy
        score = min(entropy * 2, 100)
        
        # Bonus for length
        score += min(len(password) * 2, 20)
        
        # Bonus for character variety
        char_types = self._count_char_types(password)
        score += (char_types - 1) * 10
        
        # Penalty for common patterns
        pattern_penalty = self._check_common_patterns(password)
        score -= pattern_penalty
        
        # Penalty for sequential characters
        seq_penalty = self._check_sequential_chars(password)
        score -= seq_penalty
        
        # Final score adjustment
        score = max(0, min(100, score))
        
        # Categorize
        category = self._categorize_strength(score, entropy)
        
        return {
            'score': round(score, 1),
            'category': category,
            'entropy': round(entropy, 2),
            'length': len(password),
            'char_types': char_types,
            'crack_time': self._estimate_crack_time(entropy)
        }
    
    def _calculate_entropy(self, password: str) -> float:
        """Calculate password entropy"""
        if not password:
            return 0
        
        # Character pool size estimation
        pool_size = 0
        if any(c.islower() for c in password): pool_size += 26
        if any(c.isupper() for c in password): pool_size += 26
        if any(c.isdigit() for c in password): pool_size += 10
        if any(not c.isalnum() for c in password): pool_size += 20
        
        if pool_size == 0:
            return 0
        
        # Calculate entropy
        return len(password) * math.log2(pool_size)
    
    def _count_char_types(self, password: str) -> int:
        """Count different character types in password"""
        types = 0
        if any(c.islower() for c in password): types += 1
        if any(c.isupper() for c in password): types += 1
        if any(c.isdigit() for c in password): types += 1
        if any(not c.isalnum() for c in password): types += 1
        return types
    
    def _check_common_patterns(self, password: str) -> float:
        """Check for common patterns and apply penalty"""
        penalty = 0
        password_lower = password.lower()
        
        common_patterns = [
            ('123', 5), ('abc', 5), ('qwerty', 10), ('password', 15),
            ('admin', 10), ('test', 5), ('welcome', 8), ('login', 8)
        ]
        
        for pattern, weight in common_patterns:
            if pattern in password_lower:
                penalty += weight
        
        # Check for repeated characters
        if len(set(password)) < len(password) * 0.6:
            penalty += 10
        
        return penalty
    
    def _check_sequential_chars(self, password: str) -> float:
        """Check for sequential characters"""
        penalty = 0
        sequential_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        
        for i in range(len(password) - 2):
            seq = password[i:i+3].lower()
            if seq in sequential_chars or seq in sequential_chars[::-1]:
                penalty += 3
        
        return penalty
    
    def _categorize_strength(self, score: float, entropy: float) -> str:
        """Categorize password strength"""
        if score >= 90:
            return 'Very Strong'
        elif score >= 75:
            return 'Strong'
        elif score >= 60:
            return 'Good'
        elif score >= 40:
            return 'Weak'
        else:
            return 'Very Weak'
    
    def _estimate_crack_time(self, entropy: float) -> str:
        """Estimate cracking time based on entropy"""
        # Assuming 1 trillion hashes per second
        hashes_per_second = 1e12
        combinations = 2 ** entropy
        seconds = combinations / hashes_per_second
        
        if seconds < 1:
            return 'Instant'
        elif seconds < 60:
            return f'{seconds:.1f} seconds'
        elif seconds < 3600:
            return f'{seconds/60:.1f} minutes'
        elif seconds < 86400:
            return f'{seconds/3600:.1f} hours'
        elif seconds < 31536000:
            return f'{seconds/86400:.1f} days'
        elif seconds < 3153600000:
            return f'{seconds/31536000:.1f} years'
        else:
            return f'{seconds/31536000:.0f} years'
    
    def _get_min_score(self, strength: str) -> float:
        """Get minimum score for strength category"""
        return {
            'weak': 30,
            'medium': 50,
            'strong': 70,
            'very_strong': 85
        }.get(strength, 50)
    
    def _generate_training_data(self) -> List[str]:
        """Generate comprehensive training data"""
        base_words = [
            'password', 'admin', 'test', 'user', 'welcome', 'login',
            'secret', 'key', 'master', 'system', 'default', 'guest'
        ]
        
        training_data = []
        
        # Basic variations
        for word in base_words:
            variations = [
                word,
                word + '123',
                word.capitalize(),
                word.upper(),
                word + '!',
                word + '@123',
                word + '2024',
                word + '2025',
                word + '!@#',
            ]
            training_data.extend(variations)
        
        # Leet speak variations
        leet_replacements = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '5'}
        for word in base_words[:6]:  # Use first 6 words for leet
            leet_word = ''.join(leet_replacements.get(c, c) for c in word)
            training_data.extend([
                leet_word,
                leet_word.capitalize(),
                leet_word + '123'
            ])
        
        # Strong password examples
        strong_passwords = [
            'MyP@ssw0rd!', 'Secure123!', 'Admin@2024', 'P@ssw0rd2024',
            'Welcome123!', 'Test@1234', 'UserSecure1', 'KeyMaster2024',
            'Tr0ub4dor&3', 'C0mpl3x!Pass', 'Ultr@S3cur3!', 'Sup3rS3cur3#'
        ]
        training_data.extend(strong_passwords)
        
        return list(set(training_data))  # Remove duplicates
