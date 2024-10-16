# -*- coding: utf-8 -*-
"""Malware_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G1SJKJz4w-Rke8ddQKpBBVf4jW62AWF0

ANALYSING SAMPLE LOG DATA
"""

import re

# Sample log data
log_data = '''
User accessed http://malicious-site.com/payload.exe
Connection established with IP: 192.168.1.1
MD5: d41d8cd98f00b204e9800998ecf8427e
Registry Key: HKCU\Software\MaliciousKey
SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
'''

# Regex patterns for IOCs
patterns = {
    'IP Address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
    'MD5 Hash': r'\b[a-fA-F0-9]{32}\b',
    'SHA-256 Hash': r'\b[a-fA-F0-9]{64}\b',
    'URL': r'\b(?:https?|ftp):\/\/[^\s/$.?#].[^\s]*\b',
    'Registry Key': r'(HKLM|HKCU|HKCR|HKU|HKCC)\\[a-zA-Z0-9_\\]+'

}

# Function to extract IOCs from log data
def extract_iocs(log, patterns):
    extracted_iocs = {}
    for ioc_type, pattern in patterns.items():
        extracted_iocs[ioc_type] = re.findall(pattern, log)
    return extracted_iocs

# Extracting IOCs from sample data
iocs = extract_iocs(log_data, patterns)

# Printing the extracted IOCs
for ioc_type, matches in iocs.items():
    print(f"{ioc_type}: {matches}")

"""ANALYSING sample.exe FILE"""

import re

exe_file_name = 'sample.exe'

def read_binary_file(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

#Extracting readable strings from the binary file
def extract_strings_from_binary(data, min_length=4):

    ascii_strings = re.findall(rb"[A-Za-z0-9/\-:.,_$%()#!'\"\\]+", data)
    filtered_strings = [s.decode('utf-8', 'ignore') for s in ascii_strings if len(s) >= min_length]

    return filtered_strings

#Defining regex patterns to extract them
def extract_patterns(strings):
    patterns = {
        'IP Address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        'MD5 Hash': r'\b[a-fA-F0-9]{32}\b',
        'SHA-256 Hash': r'\b[a-fA-F0-9]{64}\b',
        'URL': r'\b(?:https?|ftp):\/\/[^\s/$.?#].[^\s]*\b',
        'Registry Key': r'(HKLM|HKCU|HKCR|HKU|HKCC)\\[a-zA-Z0-9_\\]+'
    }

    extracted_data = {key: [] for key in patterns.keys()}

    for string in strings:
        for key, pattern in patterns.items():
            matches = re.findall(pattern, string)
            extracted_data[key].extend(matches)

    return extracted_data


try:

    binary_data = read_binary_file(exe_file_name)

    extracted_strings = extract_strings_from_binary(binary_data)

    print("\n=== Extracted Strings ===")
    if extracted_strings:
        for string in extracted_strings:
            print(string)
    else:
        print("No readable strings found.")


    extracted_data = extract_patterns(extracted_strings)


    for category, items in extracted_data.items():
        print(f"\n=== Extracted {category} ===")
        if items:
            for item in items:
                print(item)
        else:
            print(f"No {category.lower()} found.")

except Exception as e:
    print("Error analyzing the EXE file:", e)