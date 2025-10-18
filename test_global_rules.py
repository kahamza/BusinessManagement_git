"""
Unit tests for Windsurf Global Rules and Configuration document.

This module contains tests to validate the structure, completeness, and
format of the Windsurf Global Rules and Configuration markdown document.
"""

import unittest
import re
import os
from pathlib import Path
from typing import List, Set


class TestWindsurfGlobalRules(unittest.TestCase):
    """Test cases for Windsurf Global Rules and Configuration document."""

    def setUp(self):
        """Set up test fixtures."""
        self.rules_file_path = Path(r"c:/Users/k_ham/.codeium/windsurf/memories/global_rules.md")

        # Read the rules file
        if not self.rules_file_path.exists():
            self.fail(f"Rules file not found at: {self.rules_file_path}")

        with open(self.rules_file_path, 'r', encoding='utf-8') as f:
            self.content = f.read()

        # Split content into lines for easier processing
        self.lines = self.content.split('\n')

    def test_file_exists(self):
        """Test that the rules file exists."""
        self.assertTrue(self.rules_file_path.exists(), "Global rules file should exist")
        self.assertTrue(self.rules_file_path.is_file(), "Global rules should be a file")

    def test_file_not_empty(self):
        """Test that the rules file is not empty."""
        self.assertGreater(len(self.content.strip()), 0, "Global rules file should not be empty")

    def test_main_title_exists(self):
        """Test that the main title exists and is properly formatted."""
        self.assertTrue(self.content.startswith('# Windsurf Global Rules and Configuration'),
                       "File should start with main title")

    def test_required_sections_exist(self):
        """Test that all required main sections exist."""
        required_sections = [
            '## Overview',
            '## Core Principles',
            '## Application Architecture',
            '## Development Workflow',
            '## Security Policies',
            '## Monitoring and Analytics',
            '## API Documentation Standards',
            '## Testing Strategy',
            '## Future Enhancements',
            '## Compliance and Legal',
            '## Getting Started'
        ]

        for section in required_sections:
            with self.subTest(section=section):
                self.assertIn(section, self.content, f"Required section '{section}' should exist")

    def test_core_principles_content(self):
        """Test that core principles section contains expected principles."""
        core_principles = [
            'Modularity',
            'Security First',
            'Scalability',
            'User-Centric',
            'Maintainability'
        ]

        # Find the core principles section
        core_principles_start = self.content.find('## Core Principles')
        self.assertNotEqual(core_principles_start, -1, "Core Principles section should exist")

        # Extract the core principles section (until next main section)
        next_section_match = re.search(r'\n## ', self.content[core_principles_start + 1:])
        if next_section_match:
            core_section_end = core_principles_start + 1 + next_section_match.start()
            core_section = self.content[core_principles_start:core_section_end]
        else:
            core_section = self.content[core_principles_start:]

        for principle in core_principles:
            with self.subTest(principle=principle):
                self.assertIn(principle, core_section,
                            f"Core principle '{principle}' should be documented")

    def test_architecture_guidelines_exist(self):
        """Test that architecture sections contain expected guidelines."""
        # Check for frontend guidelines
        self.assertIn('React for interactive UI components', self.content)
        self.assertIn('responsive design for mobile and desktop', self.content)
        self.assertIn('WCAG 2.1', self.content)

        # Check for backend guidelines
        self.assertIn('microservices architecture', self.content)
        self.assertIn('RESTful APIs', self.content)
        self.assertIn('error handling and logging', self.content)

    def test_security_policies_exist(self):
        """Test that security policies section contains expected policies."""
        security_policies = [
            'Encrypt sensitive data in transit and at rest',
            'rate limiting on API endpoints',
            'OAuth 2.0',
            'JWT',
            'Regularly update dependencies'
        ]

        for policy in security_policies:
            with self.subTest(policy=policy):
                self.assertIn(policy, self.content,
                            f"Security policy '{policy}' should be documented")

    def test_testing_strategy_exists(self):
        """Test that testing strategy section contains expected test types."""
        testing_types = [
            'Unit tests for individual functions',
            'Integration tests for component interactions',
            'End-to-end tests for complete user journeys',
            'Performance tests for high-load scenarios'
        ]

        for test_type in testing_types:
            with self.subTest(test_type=test_type):
                self.assertIn(test_type, self.content,
                            f"Testing type '{test_type}' should be documented")

    def test_development_workflow_exists(self):
        """Test that development workflow section contains expected practices."""
        workflow_items = [
            'ESLint/Prettier configurations',
            'unit and integration tests for all new features',
            'version control with clear commit messages',
            'code reviews before merging',
            'blue-green deployment'
        ]

        for item in workflow_items:
            with self.subTest(item=item):
                self.assertIn(item, self.content,
                            f"Development workflow item '{item}' should be documented")

    def test_markdown_formatting_is_valid(self):
        """Test that markdown formatting follows expected patterns."""
        # Check that all main sections use ## headers
        main_sections = re.findall(r'^## [^\n]+', self.content, re.MULTILINE)
        self.assertGreater(len(main_sections), 0, "Should have main sections with ## headers")

        # Check that subsections use ### headers where expected
        subsections = re.findall(r'^### [^\n]+', self.content, re.MULTILINE)
        self.assertGreater(len(subsections), 0, "Should have subsections with ### headers")

    def test_getting_started_steps_are_numbered(self):
        """Test that getting started steps are properly numbered."""
        getting_started_start = self.content.find('## Getting Started')
        self.assertNotEqual(getting_started_start, -1, "Getting Started section should exist")

        # Find the numbered steps
        steps_pattern = r'\d+\.\s+[^\n]+'
        steps_section = self.content[getting_started_start:]

        steps = re.findall(steps_pattern, steps_section)
        self.assertGreaterEqual(len(steps), 3, "Should have at least 3 numbered steps")

        # Check that steps start with proper numbering
        for i, step in enumerate(steps[:4], 1):  # Check first 4 steps
            expected_start = f"{i}."
            with self.subTest(step_number=i):
                self.assertTrue(step.strip().startswith(expected_start),
                              f"Step {i} should start with '{expected_start}'")

    def test_document_ends_with_contact_info(self):
        """Test that document ends with contact information."""
        self.assertTrue(self.content.strip().endswith('For questions or updates to these rules, contact the development team.'),
                       "Document should end with contact information")

    def test_no_broken_links_in_examples(self):
        """Test that example URLs or references are properly formatted."""
        # Check for common URL patterns that should be valid
        url_pattern = r'https?://[^\s)]+'
        urls = re.findall(url_pattern, self.content)

        # This is a basic check - in a real scenario you might want to validate URLs
        for url in urls:
            with self.subTest(url=url):
                self.assertTrue(url.startswith(('http://', 'https://')),
                              f"URL should use http/https protocol: {url}")

    def test_code_examples_are_consistent(self):
        """Test that code examples and technology references are consistent."""
        # Check for consistent technology mentions
        tech_references = [
            'React',
            'ESLint',
            'Prettier',
            'OAuth 2.0',
            'JWT',
            'OpenAPI',
            'Swagger'
        ]

        for tech in tech_references:
            with self.subTest(tech=tech):
                # Should appear at least once (could be case-sensitive or not)
                self.assertTrue(tech in self.content or tech.lower() in self.content.lower(),
                              f"Technology reference '{tech}' should be mentioned")


if __name__ == '__main__':
    unittest.main()
