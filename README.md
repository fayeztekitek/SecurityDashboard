# Security Governance Dashboard

**Interactive vulnerability management and governance dashboard for executive briefings and compliance tracking.**

[![Version](https://img.shields.io/badge/version-1.0-blue.svg)](https://github.com/vermeg/security-governance-dashboard/releases)
[![License](https://img.shields.io/badge/license-Internal-red.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active-green.svg)](https://github.com/vermeg/security-governance-dashboard)

---

## 🎯 Overview

The **Security Governance Dashboard** is a web-based vulnerability management system designed for security leaders and vulnerability committees. It provides real-time visibility into:

- **Vulnerability Posture** - Open/overdue issues by severity
- **SLA Compliance** - Remediation timeline adherence
- **Product Risk** - Risk assessment per application
- **Client Exposure** - Customer impact analysis
- **Risk Acceptances** - Waiver tracking and expiration monitoring
- **Trend Analysis** - Historical vulnerability trends

### Key Features

✅ **Interactive HTML Dashboard** - No installation required, runs in any browser
✅ **CSV Data Import** - Load vulnerability data from Fortify, Nexus IQ, or any security tool
✅ **Real-time KPIs** - Auto-calculated metrics with RAG status indicators
✅ **Executive Summaries** - Pre-formatted briefing materials for committees
✅ **Responsive Design** - Works on desktop, tablet, and mobile
✅ **Privacy-First** - All data processing local to browser, no external servers
✅ **Print/Export** - Generate PDF reports directly from browser

---

## 🚀 Quick Start

### Option 1: Direct Use (No Installation)

1. **Download** `consolidated_dashboard.html`
2. **Open** in any web browser
3. **Click** "Import Data" → "Load Sample Data"
4. **Explore** the dashboard

### Option 2: With Your Data

1. **Export** vulnerability CSV from Fortify SSC (see [Data Extraction Guide](DATA_EXTRACTION_GUIDE.txt))
2. **Open** `consolidated_dashboard.html`
3. **Click** "Import Data" → "Import CSV File"
4. **Select** your CSV file
5. **Review** populated dashboard

### Option 3: Automated Extraction (Python)

```bash
# Install dependencies
pip install requests python-dateutil

# Run extraction script
python3 extract_fortify_data.py \
    --fortify-url https://soft-security.vermeg.com/ssc \
    --token YOUR_API_TOKEN \
    --output vulnerabilities.csv

# Import to dashboard
# Then open consolidated_dashboard.html and import the CSV
```

---

## 📦 Package Contents

```
security-governance-dashboard/
├── consolidated_dashboard.html      # Main interactive dashboard
├── extract_fortify_data.py          # Automated data extraction script
├── setup_github.sh                  # GitHub repository setup
├── sample_vulnerabilities.csv       # Sample data for testing
├── README.md                        # This file (GitHub)
├── README.txt                       # Detailed getting started guide
├── DATA_EXTRACTION_GUIDE.txt        # How to export from Fortify SSC
├── GOVERNANCE_SUMMARY_TEMPLATE.txt  # Executive briefing template
├── .gitignore                       # Git configuration
├── .github/                         # GitHub specific files
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       ├── feature_request.md
│       └── data_extraction.md
└── LICENSE                          # Internal use license
```

---

## 📊 Dashboard Sections

### 1. **Overview**
   - Global security posture at a glance
   - KPI cards for Critical/High/Medium/Low vulnerabilities
   - SLA compliance percentage
   - RAG status indicator (Red/Amber/Green)
   - Severity distribution chart

### 2. **Vulnerabilities**
   - Detailed list of Critical issues
   - Detailed list of High severity issues
   - CVE mapping and component information
   - Days overdue tracking
   - Assigned owner for accountability

### 3. **Products**
   - Risk assessment by product
   - Critical/High counts per application
   - Overdue issues by product
   - Product-level RAG status
   - Stacked severity comparison chart

### 4. **SLA & Compliance**
   - Compliance percentage vs target
   - Overdue vulnerabilities by severity
   - Mean Time to Remediation (MTTR)
   - Vulnerability age analysis
   - SLA trend chart

### 5. **Risk Acceptance**
   - Active waivers/Risk Acceptances
   - Expiring acceptances (30-day warning)
   - Expired acceptances requiring action
   - Risk justification tracking
   - Compensating controls documentation

### 6. **Client Exposure**
   - Customer impact assessment
   - Critical vulnerabilities per client
   - Deployment version tracking
   - Notification status
   - Corrective release dates

### 7. **Trends**
   - 30-day vulnerability trend
   - Remediation progress tracking
   - Improving/deteriorating products
   - MTTR trend analysis

### 8. **Executive Summary**
   - One-page governance status
   - Committee decision framework
   - Critical action items
   - Risk recommendations
   - Key metrics for C-level briefing

---

## 📋 Data Format

### Required CSV Columns

| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `Vuln_ID` | String | Unique vulnerability ID | `VUL-2024-001` |
| `CVE` | String | CVE number (optional) | `CVE-2024-1234` |
| `Severity` | String | Critical/High/Medium/Low | `Critical` |
| `Product` | String | Product/Application name | `Veggo` |
| `Component` | String | Affected library/framework | `OpenSSL 1.1.1` |
| `Discovery_Date` | Date | Date found (YYYY-MM-DD) | `2024-01-15` |
| `Days_Overdue` | Integer | Days beyond SLA (0 if on time) | `45` |
| `Owner` | String | Responsible person | `John Doe` |
| `Status` | String | Open/In Progress/Closed | `Open` |
| `Remediation_Plan` | String | How to fix | `Upgrade to v3.0` |

### Sample CSV

```csv
Vuln_ID,CVE,Severity,Product,Component,Discovery_Date,Days_Overdue,Owner,Status,Remediation_Plan
VUL-2024-001,CVE-2024-1234,Critical,Veggo,OpenSSL 1.1.1,2024-01-15,45,John Doe,Open,Upgrade to OpenSSL 3.0
VUL-2024-002,CVE-2024-5678,High,Megara,Log4j 2.14.1,2024-02-01,20,Jane Smith,Open,Patch to v2.17
VUL-2024-003,CVE-2024-9012,Medium,Colline,jQuery 3.5,2024-02-10,5,Bob Johnson,Closed,Updated to v3.6
```

For detailed export instructions, see [DATA_EXTRACTION_GUIDE.txt](DATA_EXTRACTION_GUIDE.txt)

---

## 🔐 Security & Privacy

✅ **READONLY Mode** - Dashboard only reads data, never modifies anything
✅ **Local Processing** - All calculations happen in your browser
✅ **No External Calls** - No data sent to external servers
✅ **No Database** - Data stays in memory, cleared on page close
✅ **Browser-Based** - Suitable for confidential/internal data

---

## 🛠️ Technical Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Charts**: Chart.js 3.9.1 (CDN)
- **Data**: CSV import via FileReader API
- **Compatibility**: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- **Performance**: <2s load time, handles 10,000+ vulnerabilities

### Browser Compatibility

| Browser | Desktop | Mobile |
|---------|---------|--------|
| Chrome | ✅ 90+ | ✅ Latest |
| Firefox | ✅ 88+ | ✅ Latest |
| Safari | ✅ 14+ | ✅ Latest |
| Edge | ✅ 90+ | ✅ Latest |

---

## 📥 Real Data Integration

Inject real vulnerability data from your security scanning tools directly into the dashboard!

### Supported Data Sources

| Tool | Type | Integration |
|------|------|-------------|
| **Fortify SSC** | Application vulnerabilities (SAST) | [Guide](docs/integration/FORTIFY_DATA_INTEGRATION.txt) |
| **Nexus IQ** | Dependency vulnerabilities (SCA) | [Guide](docs/integration/NEXUS_IQ_DATA_INTEGRATION.txt) |
| **DevOps-Sec** | Aggregated security data | [Guide](docs/integration/DEVOPS_SEC_DATA_INTEGRATION.txt) |
| **All Combined** | Complete vulnerability picture | [Master Guide](docs/integration/MASTER_DATA_INTEGRATION.txt) |

### Quick Start (5 minutes)

**Option 1: Manual Export (Easiest)**
```bash
# 1. Export CSV from Fortify/Nexus/DevOps-Sec
# 2. Open dashboard_live_demo.html in browser
# 3. Click "Import CSV File"
# 4. Select your file
# 5. Done! Dashboard updates with real data
```

**Option 2: Automated API (Recommended)**
```bash
# Extract from Fortify
python3 extract_fortify_data.py \
    --fortify-url https://soft-security.vermeg.com/ssc \
    --token YOUR_FORTIFY_API_TOKEN \
    --output vulnerabilities.csv

# Extract from Nexus IQ
python3 extract_nexus_iq_data.py \
    --nexus-url https://soft-security.vermeg.com:8070 \
    --username YOUR_USERNAME \
    --password YOUR_PASSWORD \
    --output nexus_vulnerabilities.csv

# Import to dashboard
# Open dashboard in browser → Import CSV File
```

**Option 3: Fully Automated Daily Pipeline (Enterprise)**
```bash
# See Master Integration Guide for complete setup
# Results: Fresh data every morning at 7 AM
```

### Integration Guides

Complete step-by-step guides are available in `/docs/integration/`:

1. **[FORTIFY_DATA_INTEGRATION.txt](docs/integration/FORTIFY_DATA_INTEGRATION.txt)** (14 KB)
   - Manual export from Fortify SSC UI
   - Automated API extraction with Python
   - Scheduled daily exports
   - Troubleshooting guide

2. **[NEXUS_IQ_DATA_INTEGRATION.txt](docs/integration/NEXUS_IQ_DATA_INTEGRATION.txt)** (16 KB)
   - Manual export from Nexus IQ
   - API-based extraction
   - CLI scanning and parsing
   - Integration with Fortify data

3. **[DEVOPS_SEC_DATA_INTEGRATION.txt](docs/integration/DEVOPS_SEC_DATA_INTEGRATION.txt)** (16 KB)
   - Extract from devops-sec.vermeg.com
   - API integration
   - Web scraping fallback
   - Data aggregation

4. **[MASTER_DATA_INTEGRATION.txt](docs/integration/MASTER_DATA_INTEGRATION.txt)** (18 KB)
   - Combine all three data sources
   - Deduplication and validation
   - Automated daily pipeline
   - Production deployment

See [docs/integration/README.md](docs/integration/README.md) for complete index and comparison.

---

## 📈 Usage Examples

### Executive Committee Briefing
1. Import latest vulnerability data
2. Navigate to "Executive Summary" section
3. Print or export to PDF
4. Share with committee 24 hours before meeting

### Product Risk Assessment
1. Go to "Products" section
2. Review product-by-product RAG status
3. Identify products requiring escalation
4. Assign remediation owners

### Client Impact Analysis
1. Visit "Client Exposure" section
2. Identify critical vulnerabilities per customer
3. Generate corrective release date
4. Send notification with remediation ETA

### SLA Compliance Monitoring
1. Check "SLA & Overdue" section daily
2. Escalate any RED items within 24 hours
3. Track MTTR improvement trend
4. Report weekly to security leadership

---

## 🔧 Customization

### Change Colors
Edit CSS variables in `consolidated_dashboard.html`:
```javascript
:root {
    --color-critical: #ef4444;  /* Red */
    --color-high: #f97316;      /* Orange */
    --color-medium: #eab308;    /* Yellow */
    --color-low: #22c55e;       /* Green */
}
```

### Add New KPI Cards
1. Add HTML card in dashboard section
2. Calculate value in `calculateKPIs()` function
3. Update card value in `updateKPIs()` function

### Add New Charts
1. Add `<canvas>` element
2. Create Chart.js initialization function
3. Call from `updateDashboard()` or `switchSection()`

For more customization, see README.txt

---

## 📚 Documentation

- [README.txt](README.txt) - Comprehensive getting started guide
- [DATA_EXTRACTION_GUIDE.txt](DATA_EXTRACTION_GUIDE.txt) - How to export from security tools
- [GOVERNANCE_SUMMARY_TEMPLATE.txt](GOVERNANCE_SUMMARY_TEMPLATE.txt) - Executive briefing format
- [extract_fortify_data.py](extract_fortify_data.py) - Automated extraction script

---

## 🤝 Contributing

### Reporting Issues
- Use GitHub Issues with appropriate template
- Include your use case and environment details
- Attach sample data (anonymized) if applicable

### Suggesting Features
- Describe the feature and why it's needed
- Provide use case examples
- Reference executive/committee decision points

### Development Setup
1. Clone repository: `git clone <repository-url>`
2. Edit `consolidated_dashboard.html`
3. Test in browser (F12 for dev tools)
4. Commit with descriptive messages
5. Push to GitHub

---

## 📊 Sample Products

This dashboard is configured for monitoring these Vermeg products:

- **Veggo** - Digital banking platform
- **Megara** - Core banking system
- **Colline** - Insurance platform
- **Digital Collateral** - Collateral management
- **Digital Insurance** - Insurance management

Easily customizable for your specific product portfolio.

---

## 📞 Support

### Common Issues

**Q: Data won't import**
A: Verify CSV format matches requirement. Try `sample_vulnerabilities.csv` as template.

**Q: Charts not displaying**
A: Need minimum 5 vulnerabilities. Use "Load Sample Data" to test.

**Q: Where is my data saved?**
A: Data stays in browser memory. Use browser print/export to save. No database involved.

### Getting Help
1. Check [README.txt](README.txt) troubleshooting section
2. Review [DATA_EXTRACTION_GUIDE.txt](DATA_EXTRACTION_GUIDE.txt) for data issues
3. Open GitHub Issue with details
4. Contact Security Tools Administrator for Fortify access issues

---

## 📋 Roadmap

### v1.0 (Current)
✅ Interactive dashboard
✅ CSV import
✅ KPI calculations
✅ Executive summary
✅ RAG status indicators

### v1.1 (Planned)
- [ ] Direct Fortify API integration
- [ ] Automated scheduled imports
- [ ] Drill-down detail views
- [ ] Export to PDF with branding
- [ ] Email alerts for overdue items

### v1.2 (Future)
- [ ] Real-time dashboard updates
- [ ] Workflow automation
- [ ] Advanced filtering/search
- [ ] Custom KPI builder
- [ ] Multi-tenant support

---

## 📄 License

**INTERNAL USE ONLY**

This dashboard is for internal Vermeg use only. Unauthorized distribution, modification, or commercial use is prohibited.

See [LICENSE](LICENSE) for details.

---

## 👥 Team

**Maintained by:** Security Governance Team

**Key Contributors:**
- Security Architecture
- Vulnerability Management
- DevSecOps
- Application Security

---

## 📞 Contact

For questions or feedback:
- **Email**: security-governance@vermeg.com
- **Slack**: #security-governance-dashboard
- **GitHub Issues**: [Report Issue](https://github.com/vermeg/security-governance-dashboard/issues)

---

## 🔗 Related Resources

- [Fortify SSC](https://soft-security.vermeg.com/ssc/) - Main security scanning tool
- [Sonatype Nexus IQ](https://soft-security.vermeg.com:8070/) - Dependency scanning
- [Security Policies](https://wiki.vermeg.com/security) - Internal security standards
- [Vulnerability Management Process](https://wiki.vermeg.com/vuln-process) - Process documentation

---

**Last Updated:** February 2024 | Version 1.0

⭐ **Star this repository** if you find it useful!
🐛 **Found a bug?** [Report it here](https://github.com/vermeg/security-governance-dashboard/issues/new?template=bug_report.md)
💡 **Have an idea?** [Suggest a feature](https://github.com/vermeg/security-governance-dashboard/issues/new?template=feature_request.md)
