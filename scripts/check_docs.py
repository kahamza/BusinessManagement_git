#!/usr/bin/env python3
"""
Documentation Linter for Business Management App

This script checks markdown documentation files against our documentation standards.
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple
import sys

# Configuration
ROOT_DIR = Path(__file__).parent.parent
DOCS_DIR = ROOT_DIR / 'docs'
TEMPLATE_FILE = ROOT_DIR / 'docs' / 'templates' / 'DOCUMENTATION_TEMPLATE.md'

# Required sections with their English and Arabic headers
REQUIRED_SECTIONS = [
    (r'## 📝 Overview', r'## 📝 Overview \| نظرة عامة'),
    (r'## 🎯 Purpose', r'## 🎯 Purpose \| الغرض'),
    (r'## 🏗️ Architecture', r'## 🏗️ Architecture \| الهندسة المعمارية'),
    (r'## 🛠️ Implementation', r'## 🛠️ Implementation \| التنفيذ'),
    (r'## 🔐 Security Considerations', r'## 🔐 Security Considerations \| اعتبارات الأمان'),
    (r'## 🧪 Testing', r'## 🧪 Testing \| الاختبار'),
]

class DocLinter:
    def __init__(self):
        self.errors: List[Dict] = []
        self.warnings: List[Dict] = []
        self.files_checked = 0
        self.files_with_issues = 0
        
    def check_file(self, file_path: Path) -> None:
        """Check a single markdown file against documentation standards."""
        self.files_checked += 1
        rel_path = file_path.relative_to(ROOT_DIR)
        
        try:
            content = file_path.read_text(encoding='utf-8')
            lines = content.split('\n')
            
            # Check for required sections
            self._check_required_sections(rel_path, content)
            
            # Check for bilingual content
            self._check_bilingual(rel_path, content)
            
            # Check for proper RTL formatting
            self._check_rtl_formatting(rel_path, lines)
            
            # Check for code blocks
            self._check_code_blocks(rel_path, content)
            
        except UnicodeDecodeError:
            self._add_error(rel_path, 0, "File is not UTF-8 encoded")
        except Exception as e:
            self._add_error(rel_path, 0, f"Error processing file: {str(e)}")
    
    def _check_required_sections(self, file_path: Path, content: str) -> None:
        """Check if all required sections are present."""
        for eng_pattern, ar_pattern in REQUIRED_SECTIONS:
            has_eng = re.search(eng_pattern, content) is not None
            has_ar = re.search(ar_pattern, content) is not None
            
            if not has_eng and not has_ar:
                self._add_error(file_path, 0, f"Missing section: {eng_pattern}")
            elif not has_eng:
                self._add_error(file_path, 0, f"Missing English section: {eng_pattern}")
            elif not has_ar:
                self._add_warning(file_path, 0, f"Missing Arabic translation for section: {eng_pattern}")
    
    def _check_bilingual(self, file_path: Path, content: str) -> None:
        """Check if content has both English and Arabic translations."""
        # Simple check for RTL content (Arabic text)
        has_rtl = any('\u0600' <= c <= '\u06FF' for c in content)
        has_ltr = bool(re.search(r'[a-zA-Z]', content))
        
        if not has_rtl and has_ltr:
            self._add_warning(file_path, 0, "Document is missing Arabic translations")
        elif has_rtl and not has_ltr:
            self._add_warning(file_path, 0, "Document is missing English content")
    
    def _check_rtl_formatting(self, file_path: Path, lines: List[str]) -> None:
        """Check for proper RTL formatting."""
        for i, line in enumerate(lines, 1):
            # Check for unmarked RTL text
            if any('\u0600' <= c <= '\u06FF' for c in line) and not line.strip().startswith('<div dir="rtl">'):
                self._add_warning(file_path, i, "RTL text should be wrapped in <div dir=\"rtl\">")
    
    def _check_code_blocks(self, file_path: Path, content: str) -> None:
        """Check for properly formatted code blocks."""n        code_blocks = re.findall(r'```(\w*)\n(.*?)```', content, re.DOTALL)
        for lang, code in code_blocks:
            if not lang and '```' not in code:  # Only check non-empty code blocks with language specified
                self._add_warning(file_path, 0, f"Code block missing language specification")
    
    def _add_error(self, file_path: Path, line: int, message: str) -> None:
        """Add an error to the error list."""
        self.errors.append({
            'file': str(file_path),
            'line': line,
            'type': 'ERROR',
            'message': message
        })
        self.files_with_issues += 1
    
    def _add_warning(self, file_path: Path, line: int, message: str) -> None:
        """Add a warning to the warning list."""
        self.warnings.append({
            'file': str(file_path),
            'line': line,
            'type': 'WARNING',
            'message': message
        })
    
    def print_report(self) -> None:
        """Print a summary of the linting results."""
        print(f"\n📝 Documentation Linter Report")
        print("=" * 80)
        
        # Print errors
        if self.errors:
            print("\n❌ Errors:")
            for error in self.errors:
                print(f"{error['file']}:{error['line']} - {error['type']}: {error['message']}")
        
        # Print warnings
        if self.warnings:
            print("\n⚠️  Warnings:")
            for warning in self.warnings:
                print(f"{warning['file']}:{warning['line']} - {warning['type']}: {warning['message']}")
        
        # Print summary
        print("\n" + "=" * 80)
        print(f"📊 Summary:")
        print(f"  Files checked: {self.files_checked}")
        print(f"  Files with issues: {self.files_with_issues}")
        print(f"  Total errors: {len(self.errors)}")
        print(f"  Total warnings: {len(self.warnings)}")
        print("=" * 80)
        
        if self.errors:
            sys.exit(1)

def find_markdown_files(directory: Path) -> List[Path]:
    """Find all markdown files in the given directory."""
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and not file.startswith('.'):
                md_files.append(Path(root) / file)
    return md_files

def main():
    """Main function to run the linter."""
    linter = DocLinter()
    
    # Find all markdown files in the docs directory
    md_files = find_markdown_files(DOCS_DIR)
    
    # Skip template files
    md_files = [f for f in md_files if 'templates' not in str(f)]
    
    if not md_files:
        print("No markdown files found in the docs directory.")
        return
    
    # Check each file
    for md_file in md_files:
        linter.check_file(md_file)
    
    # Print the report
    linter.print_report()

if __name__ == "__main__":
    main()
