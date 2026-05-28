# Data Integration Guides

Complete guides for integrating real vulnerability data from security scanning tools into the Security Governance Dashboard.

## 📚 Available Guides

### 1. **Fortify SSC Integration** 
📄 [`FORTIFY_DATA_INTEGRATION.txt`](FORTIFY_DATA_INTEGRATION.txt)

Extract vulnerability data from Fortify SSC (Static Application Security Testing)
- **Data Type:** Application vulnerabilities (SAST)
- **Frequency:** Weekly recommended
- **Methods:** Manual export or automated API extraction
- **Time to implement:** 30 minutes (manual) or 1 hour (API)

**Quick Start:**
```bash
# Option 1: Manual export from UI
1. Log into https://soft-security.vermeg.com/ssc/
2. Reports → Vulnerability Report
3. Export as CSV
4. Import to dashboard

# Option 2: Automated API extraction
python3 extract_fortify_data.py \
  --fortify-url https://soft-security.vermeg.com/ssc \
  --token YOUR_API_TOKEN \
  --output vulnerabilities.csv
```

---

### 2. **Sonatype Nexus IQ Integration**
📄 [`NEXUS_IQ_DATA_INTEGRATION.txt`](NEXUS_IQ_DATA_INTEGRATION.txt)

Extract vulnerability data from Sonatype Nexus IQ (Software Composition Analysis)
- **Data Type:** Dependency vulnerabilities (SCA)
- **Frequency:** Daily recommended
- **Methods:** Manual export, API extraction, or CLI scan
- **Time to implement:** 30 minutes (manual) or 1 hour (API)

**Quick Start:**
```bash
# Option 1: Manual export from UI
1. Log into https://soft-security.vermeg.com:8070/
2. Reports → Download report
3. Export as CSV
4. Import to dashboard

# Option 2: Automated API extraction
python3 extract_nexus_iq_data.py \
  --nexus-url https://soft-security.vermeg.com:8070 \
  --username YOUR_USERNAME \
  --password YOUR_PASSWORD \
  --output nexus_iq_data.csv
```

---

### 3. **DevOps-Sec Portal Integration**
📄 [`DEVOPS_SEC_DATA_INTEGRATION.txt`](DEVOPS_SEC_DATA_INTEGRATION.txt)

Extract aggregated vulnerability data from the devops-sec.vermeg.com security portal
- **Data Type:** Aggregated from all scanners
- **Frequency:** Real-time or daily
- **Methods:** API, export, or web scraping
- **Time to implement:** 45 minutes to 2 hours

**Quick Start:**
```bash
# Option 1: Check for export feature
1. Visit https://devops-sec.vermeg.com/
2. Vulnerabilities page
3. Click Export button
4. Import to dashboard

# Option 2: API extraction
curl "https://devops-sec.vermeg.com/api/vulnerabilities" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  > vulnerabilities.json

# Option 3: Web scraping
python3 extract_devops_sec_data.py \
  --output devops_sec_data.csv
```

---

### 4. **Master Integration Guide**
📄 [`MASTER_DATA_INTEGRATION.txt`](MASTER_DATA_INTEGRATION.txt)

Complete guide for combining all three data sources into one comprehensive dataset
- **Combines:** Fortify + Nexus IQ + DevOps-Sec
- **Includes:** Deduplication, validation, and automated pipeline
- **Frequency:** Daily automated
- **Time to implement:** 2 hours (setup) + 0 minutes per day

**Quick Start:**
```bash
# Set up automated daily pipeline
1. Create project structure (see guide)
2. Configure API credentials
3. Set up extraction scripts
4. Configure cron job for daily runs
5. Dashboard auto-updates every morning

# Daily result: Fresh vulnerability data!
6:00 AM  - Extract Fortify
6:15 AM  - Extract Nexus IQ
6:30 AM  - Extract DevOps-Sec
6:45 AM  - Combine & validate
7:00 AM  - Dashboard updated
```

---

## 🎯 Integration Levels

### **Level 1: Manual (Easiest)**
- ✅ No setup required
- ✅ No coding needed
- ✅ Perfect for: Testing, monthly reviews, small teams
- ⏱️ Time: 30 minutes per extraction
- 📖 See: Individual tool guides (1, 2, 3 above)

**Steps:**
1. Export CSV from tool UI
2. Open in Excel
3. Map fields to dashboard format
4. Save as CSV
5. Import to dashboard

---

### **Level 2: Semi-Automated (Recommended)**
- ✅ Repeatable weekly extractions
- ✅ Python scripts provided
- ✅ Perfect for: Growing teams, weekly reviews
- ⏱️ Time: 1 hour setup + 5 minutes per week
- 📖 See: Master Integration Guide

**Setup:**
1. Get API credentials
2. Download extraction scripts
3. Configure credentials
4. Run scripts weekly
5. Import latest CSV

---

### **Level 3: Fully Automated (Enterprise)**
- ✅ Daily automatic extractions
- ✅ Data deduplication built-in
- ✅ Perfect for: Large enterprises, governance committees
- ⏱️ Time: 2 hours setup + 0 minutes daily
- 📖 See: Master Integration Guide - Scheduled Pipeline

**Setup:**
1. Create project structure
2. Configure all three data sources
3. Set up Python pipeline scripts
4. Configure daily cron job
5. Dashboard auto-updates every morning

---

## 📊 Data Format

All guides standardize vulnerability data to this CSV format:

```csv
Vuln_ID,CVE,Severity,Product,Component,Discovery_Date,Days_Overdue,Owner,Status,Remediation_Plan
VUL-2024-001,CVE-2024-1234,Critical,Veggo,OpenSSL 1.1.1,2024-01-15,45,John Doe,Open,Upgrade to OpenSSL 3.0
VUL-2024-002,CVE-2024-5678,High,Megara,Log4j 2.14.1,2024-02-01,20,Jane Smith,Open,Patch to v2.17
```

**Required Columns:**
- `Vuln_ID` - Unique vulnerability identifier
- `CVE` - CVE number (if available)
- `Severity` - Critical/High/Medium/Low
- `Product` - Application/product name
- `Component` - Affected library/framework
- `Discovery_Date` - Date found (YYYY-MM-DD)
- `Days_Overdue` - Days beyond SLA (0 if on time)
- `Owner` - Responsible person
- `Status` - Open/In Progress/Closed
- `Remediation_Plan` - How to fix

---

## 🚀 Quick Comparison

| Feature | Fortify | Nexus IQ | DevOps-Sec | All Combined |
|---------|---------|----------|-----------|--------------|
| **Scan Type** | SAST (code) | SCA (deps) | All types | Complete |
| **Frequency** | Weekly | Daily | Real-time | Daily |
| **Setup Time** | 30 min | 30 min | 45 min | 2 hours |
| **Automation** | Yes | Yes | Yes | Full pipeline |
| **Data Volume** | ~250 vulns | ~150 vulns | ~400 vulns | ~450 unique |
| **Cost** | Included | Included | Included | Free |

---

## 📋 Data Source Details

### Fortify SSC
- **URL:** https://soft-security.vermeg.com/ssc/
- **Type:** Static Application Security Testing (SAST)
- **What it finds:** Code vulnerabilities in applications
- **Best for:** Application security assessment
- **API Available:** Yes (REST)
- **Authentication:** API Token

### Sonatype Nexus IQ
- **URL:** https://soft-security.vermeg.com:8070/
- **Type:** Software Composition Analysis (SCA)
- **What it finds:** Vulnerable dependencies/libraries
- **Best for:** Supply chain security
- **API Available:** Yes (REST)
- **Authentication:** Username/Password or token

### DevOps-Sec Portal
- **URL:** https://devops-sec.vermeg.com/
- **Type:** Aggregated security data
- **What it finds:** All vulnerabilities from all scanners
- **Best for:** Holistic security view
- **API Available:** Possibly (check site)
- **Authentication:** May vary

---

## 🔧 Troubleshooting

### "Authentication failed"
**Solution:** Verify credentials/tokens are correct and haven't expired

See:
- Fortify: [FORTIFY_DATA_INTEGRATION.txt](FORTIFY_DATA_INTEGRATION.txt#troubleshooting)
- Nexus IQ: [NEXUS_IQ_DATA_INTEGRATION.txt](NEXUS_IQ_DATA_INTEGRATION.txt#troubleshooting)

### "CSV import fails"
**Solution:** Verify column names match exactly and data is valid

See: Any guide → "Data Quality Checks" section

### "No vulnerabilities found"
**Solution:** Check if tools have been scanned and user has permissions

See: Specific tool guide → "Troubleshooting" section

### "Data looks wrong in dashboard"
**Solution:** Validate data format before importing

```bash
# Check data quality
python3 validate_data.py dashboard_vulnerabilities.csv
```

---

## 📚 Implementation Roadmap

### Week 1: Manual Testing
- [ ] Day 1: Read guide overview
- [ ] Day 2: Export Fortify data manually
- [ ] Day 3: Import to dashboard
- [ ] Day 4: Export Nexus IQ data manually
- [ ] Day 5: Import to dashboard

### Week 2: Automation Setup
- [ ] Day 1: Set up API credentials
- [ ] Day 2: Test extraction scripts
- [ ] Day 3: Configure automation
- [ ] Day 4: Run first automated extraction
- [ ] Day 5: Validate automated data

### Week 3: Production Deployment
- [ ] Day 1: Set up cron jobs
- [ ] Day 2: Configure monitoring/alerts
- [ ] Day 3: Train team on dashboard
- [ ] Day 4: Go live with automated pipeline
- [ ] Day 5: Monitor and refine

---

## ✅ Checklist Before Going Live

- [ ] All three data sources configured
- [ ] API credentials securely stored
- [ ] Extraction scripts tested
- [ ] CSV format validated
- [ ] Deduplication working
- [ ] Dashboard imports data successfully
- [ ] Cron job scheduled
- [ ] Logging configured
- [ ] Monitoring/alerts set up
- [ ] Team trained on process
- [ ] Backup process established

---

## 📞 Support & Questions

**For Fortify SSC questions:**
→ See [FORTIFY_DATA_INTEGRATION.txt](FORTIFY_DATA_INTEGRATION.txt)

**For Nexus IQ questions:**
→ See [NEXUS_IQ_DATA_INTEGRATION.txt](NEXUS_IQ_DATA_INTEGRATION.txt)

**For DevOps-Sec questions:**
→ See [DEVOPS_SEC_DATA_INTEGRATION.txt](DEVOPS_SEC_DATA_INTEGRATION.txt)

**For combining all sources:**
→ See [MASTER_DATA_INTEGRATION.txt](MASTER_DATA_INTEGRATION.txt)

**For GitHub project issues:**
→ Open [GitHub Issue](https://github.com/fayeztekitek/SecurityDashboard/issues)

---

## 🎓 Learning Resources

- **CSV Format Specification:** See any guide → "Data Format" section
- **API Documentation:** Each guide includes API reference section
- **Troubleshooting:** Each guide includes troubleshooting section
- **Python Scripts:** Each guide includes working code examples
- **Cron Job Examples:** Master Integration Guide → "Scheduled Pipeline"

---

## 🚀 Next Steps

1. **Choose your integration level** (Manual/Semi-auto/Fully-auto)
2. **Read the relevant guide(s)**
3. **Set up credentials** for your data sources
4. **Test with sample data** first
5. **Import into dashboard**
6. **Set up automation** (if desired)
7. **Monitor and refine**

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | May 2024 | Initial release with all 4 guides |

---

**Start with the guide for your first data source, then expand!** 🚀

---

*For the latest information, check the main [README.md](../../README.md) and [GitHub repository](https://github.com/fayeztekitek/SecurityDashboard)*
