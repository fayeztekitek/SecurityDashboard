#!/usr/bin/env python3
"""
Security Governance Dashboard - Fortify Data Extraction Script
Extracts vulnerability data from Fortify SSC and converts to dashboard CSV format

Usage:
    python3 extract_fortify_data.py --fortify-url https://soft-security.vermeg.com/ssc \
                                     --token YOUR_API_TOKEN \
                                     --output dashboard_data.csv

Requirements:
    pip install requests python-dateutil
"""

import requests
import csv
import json
import argparse
from datetime import datetime, timedelta
from typing import List, Dict, Any
import sys

class FortifyExtractor:
    """Extract vulnerability data from Fortify SSC"""
    
    def __init__(self, base_url: str, token: str = None, username: str = None, password: str = None):
        self.base_url = base_url.rstrip('/')
        self.token = token
        self.username = username
        self.password = password
        self.session = requests.Session()
        
        if token:
            self.session.headers.update({'X-API-Token': token})
        elif username and password:
            self.session.auth = (username, password)
    
    def get_issues(self, days: int = 90) -> List[Dict[str, Any]]:
        """
        Fetch all issues from Fortify SSC
        Args:
            days: Only return issues from last N days
        Returns:
            List of issue dictionaries
        """
        issues = []
        start_date = (datetime.now() - timedelta(days=days)).isoformat()
        
        try:
            # Get all projects first
            projects_url = f"{self.base_url}/api/v1/projects"
            projects_resp = self.session.get(projects_url, verify=False)
            projects_resp.raise_for_status()
            projects = projects_resp.json().get('data', [])
            
            print(f"[*] Found {len(projects)} projects")
            
            for project in projects:
                project_id = project['id']
                project_name = project['name']
                
                # Get issues for this project
                issues_url = f"{self.base_url}/api/v1/projects/{project_id}/issues"
                params = {
                    'onlyIfSuppressed': False,
                    'filter': f'foundDate:[{start_date} TO *]',
                    'limit': 500
                }
                
                try:
                    resp = self.session.get(issues_url, params=params, verify=False)
                    resp.raise_for_status()
                    project_issues = resp.json().get('data', [])
                    
                    print(f"[+] {project_name}: {len(project_issues)} issues")
                    
                    for issue in project_issues:
                        issue['project_name'] = project_name
                        issue['project_id'] = project_id
                        issues.append(issue)
                
                except Exception as e:
                    print(f"[-] Error fetching issues for {project_name}: {e}")
                    continue
            
            return issues
        
        except Exception as e:
            print(f"[-] Error connecting to Fortify: {e}")
            print("[!] Make sure to use:")
            print("    - Valid token via --token parameter, OR")
            print("    - Valid credentials via --username and --password")
            return []
    
    def extract_artifacts(self, issues: List[Dict]) -> List[Dict]:
        """
        Extract issue artifacts (components) for each issue
        """
        for issue in issues:
            try:
                issue_id = issue['id']
                project_id = issue['project_id']
                
                artifacts_url = f"{self.base_url}/api/v1/projects/{project_id}/issues/{issue_id}/artifacts"
                resp = self.session.get(artifacts_url, verify=False)
                resp.raise_for_status()
                
                artifacts = resp.json().get('data', [])
                components = []
                for artifact in artifacts:
                    if 'componentName' in artifact:
                        components.append(artifact['componentName'])
                
                issue['components'] = ', '.join(components) if components else 'Unknown'
            
            except Exception as e:
                issue['components'] = 'Unknown'
        
        return issues
    
    def convert_to_dashboard_format(self, issues: List[Dict]) -> List[Dict]:
        """
        Convert Fortify issues to dashboard CSV format
        """
        dashboard_issues = []
        
        for issue in issues:
            # Calculate days overdue
            due_date = self._calculate_due_date(issue.get('priority', 'Medium'))
            found_date = issue.get('foundDate', datetime.now().isoformat())
            days_overdue = self._calculate_days_overdue(found_date, due_date)
            
            # Map severity levels
            severity_map = {
                'Critical': 'Critical',
                'High': 'High',
                'Medium': 'Medium',
                'Low': 'Low'
            }
            
            status_map = {
                'Unreviewed': 'Open',
                'Reviewed': 'Open',
                'Remediated': 'Closed',
                'Mitigated': 'Open',
                'Suppressed': 'Closed'
            }
            
            dashboard_issue = {
                'Vuln_ID': f"VUL-{issue.get('id', 'UNKNOWN')}",
                'CVE': self._extract_cve(issue),
                'Severity': severity_map.get(issue.get('priority', 'Medium'), 'Medium'),
                'Product': issue.get('project_name', 'Unknown'),
                'Component': issue.get('components', 'Unknown'),
                'Discovery_Date': self._format_date(found_date),
                'Days_Overdue': str(max(0, days_overdue)),
                'Owner': issue.get('assignedUser', 'Unassigned'),
                'Status': status_map.get(issue.get('issueStatus', 'Unreviewed'), 'Open'),
                'Remediation_Plan': issue.get('comment', 'No plan defined')
            }
            
            dashboard_issues.append(dashboard_issue)
        
        return dashboard_issues
    
    @staticmethod
    def _extract_cve(issue: Dict) -> str:
        """Extract CVE number from issue"""
        # Look for CVE in various fields
        for field in ['issueName', 'comment', 'description']:
            if field in issue:
                import re
                cve_match = re.search(r'CVE-\d{4}-\d{4,}', str(issue[field]))
                if cve_match:
                    return cve_match.group()
        return ''
    
    @staticmethod
    def _calculate_due_date(severity: str) -> datetime:
        """Calculate due date based on severity"""
        sla_days = {
            'Critical': 30,
            'High': 60,
            'Medium': 90,
            'Low': 180
        }
        days = sla_days.get(severity, 90)
        return datetime.now() - timedelta(days=days)
    
    @staticmethod
    def _calculate_days_overdue(found_date_str: str, due_date: datetime) -> int:
        """Calculate days overdue"""
        try:
            found_date = datetime.fromisoformat(found_date_str.replace('Z', '+00:00'))
            due_date_calc = found_date + (due_date - datetime.now())
            days_overdue = (datetime.now() - due_date_calc).days
            return max(0, days_overdue)
        except:
            return 0
    
    @staticmethod
    def _format_date(date_str: str) -> str:
        """Format date as YYYY-MM-DD"""
        try:
            date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return date_obj.strftime('%Y-%m-%d')
        except:
            return datetime.now().strftime('%Y-%m-%d')


def write_csv(data: List[Dict], output_file: str):
    """Write data to CSV file"""
    if not data:
        print("[-] No data to write")
        return
    
    fieldnames = [
        'Vuln_ID', 'CVE', 'Severity', 'Product', 'Component',
        'Discovery_Date', 'Days_Overdue', 'Owner', 'Status', 'Remediation_Plan'
    ]
    
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"[+] Successfully wrote {len(data)} vulnerabilities to {output_file}")
        return True
    
    except Exception as e:
        print(f"[-] Error writing CSV: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Extract vulnerability data from Fortify SSC for Security Governance Dashboard'
    )
    
    parser.add_argument('--fortify-url', required=True,
                       help='Fortify SSC URL (e.g., https://soft-security.vermeg.com/ssc)')
    
    # Auth options
    auth_group = parser.add_mutually_exclusive_group(required=True)
    auth_group.add_argument('--token', help='Fortify API token')
    auth_group.add_argument('--username', help='Fortify username (with --password)')
    
    parser.add_argument('--password', help='Fortify password (with --username)')
    parser.add_argument('--output', default='extracted_vulnerabilities.csv',
                       help='Output CSV file (default: extracted_vulnerabilities.csv)')
    parser.add_argument('--days', type=int, default=90,
                       help='Only export vulnerabilities from last N days (default: 90)')
    parser.add_argument('--no-verify-ssl', action='store_true',
                       help='Disable SSL verification (not recommended)')
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.username and not args.password:
        print("[-] Error: --password required with --username")
        sys.exit(1)
    
    print("[*] Security Governance Dashboard - Fortify Data Extractor")
    print(f"[*] Target: {args.fortify_url}")
    print(f"[*] Days: {args.days}")
    print(f"[*] Output: {args.output}")
    print()
    
    # Create extractor
    extractor = FortifyExtractor(
        base_url=args.fortify_url,
        token=args.token,
        username=args.username,
        password=args.password
    )
    
    # Extract data
    print("[*] Fetching issues from Fortify...")
    issues = extractor.get_issues(days=args.days)
    
    if not issues:
        print("[-] No issues found")
        sys.exit(1)
    
    print(f"[*] Total issues: {len(issues)}")
    print("[*] Extracting artifacts...")
    issues = extractor.extract_artifacts(issues)
    
    print("[*] Converting to dashboard format...")
    dashboard_data = extractor.convert_to_dashboard_format(issues)
    
    print("[*] Writing to CSV...")
    if write_csv(dashboard_data, args.output):
        print()
        print("[✓] Extraction complete!")
        print(f"[✓] File ready: {args.output}")
        print("[✓] Next step: Open consolidated_dashboard.html and import this CSV")
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
