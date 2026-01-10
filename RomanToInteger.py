class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary mapping Roman numerals to their integer values
        roman_to_int = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        
        result = 0  # Initialize the result to 0
        
        for i in range(len(s)):  # Loop through each character in the string
            # Check if the current numeral is smaller than the next one (for subtraction cases)
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[s[i]]  # Subtract the current value
            else:
                result += roman_to_int[s[i]]   # Otherwise, add the current value
        
        return result  # Return the final integer