'''
Exercise 9: Assertion-Based Testing 
Implement Fahrenheit→Celsius converter and validate using assertions for known points 
(freezing, boiling). 
Example:  
Input: 32     Output: 0  
Input: 212  Output: 100  
'''

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def main():
    assert fahrenheit_to_celsius(32) == 0, "Freezing point failed"
    assert fahrenheit_to_celsius(212) == 100, "Boiling point failed"

if __name__ == '__main__':
    main()