#!/usr/bin/env python
# coding: utf-8

import argparse
import re
from collections import defaultdict

def main():
  # Parse command-line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('bibtex_file', help='Path to the bibtex file')
  args = parser.parse_args()

  # Read the bibtex file
  with open(args.bibtex_file, 'r') as f:
    bibtex_text = f.read()

  # Extract the entries from the bibtex file
  entries = extract_entries(bibtex_text)

  # Sort the entries by date in decreasing order
  sorted_entries = sorted(entries, key=lambda x: x['year'], reverse=True)

  # Generate the list of citation references
  citation_list = generate_citation_list(sorted_entries)

  # Print the citation list
  for i, citation in enumerate(citation_list, start=1):
    print(f'{i}. {citation}')

def extract_entries(text):
  """Extracts the entries from a bibtex file"""
  entries = []
  entry_texts = re.findall(r'@\w+\s*\{(.+?)\}', text, flags=re.DOTALL)
  for entry_text in entry_texts:
    entry = defaultdict(str)
    lines = entry_text.strip().split('\n')
    for line in lines:
      if '=' in line:
        key, value = line.split('=')
        entry[key.strip()] = value.strip()
    entries.append(entry)
  return entries


def generate_citation_list(entries):
  """Generates a list of human-readable citation references"""
  citation_list = []
  for entry in entries:
    citation = f'{entry["author"]}, {entry["title"]}, {entry["journal"]}, {entry["year"]}'
    citation_list.append(citation)
  return citation_list

if __name__ == '__main__':
  main()
