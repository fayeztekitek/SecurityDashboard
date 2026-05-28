---
name: 📥 Data Extraction Issue
about: Report issues with importing data or integrating with Fortify SSC
title: "[DATA] "
labels: data-import
assignees: ''

---

## 📥 Data Import Issue

**What system are you exporting from?**
- [ ] Fortify SSC
- [ ] Sonatype Nexus IQ
- [ ] Manual CSV
- [ ] Other: _______________

**Describe the issue**
A clear description of the data import problem.

---

## 📋 Data Details

**File Information:**
- File size: [e.g., 500 KB]
- Number of rows: [e.g., 250 vulnerabilities]
- File format: [CSV / JSON / Excel]
- Number of columns: [e.g., 10]

**Data Sample (anonymized):**
Paste 2-3 rows of your data to help debug:
```
Vuln_ID,CVE,Severity,Product,Component,Discovery_Date,Days_Overdue,Owner,Status,Remediation_Plan
VUL-001,CVE-2024-XXX,Critical,ProductA,Component1,2024-01-15,45,Person A,Open,Fix description
```

---

## 🔧 Steps to Reproduce

1. Export from [system]
2. Open dashboard
3. Click "Import Data"
4. Select CSV file
5. Error occurs...

---

## ❌ Error Message

**Exact error shown:**
```
[Paste error message here]
```

**Browser console errors (F12 → Console):**
```
[Paste any console errors]
```

---

## 📊 Data Validation Checklist

- [ ] All required columns present
- [ ] No empty Vuln_ID cells
- [ ] Severity values are exactly: Critical, High, Medium, Low
- [ ] Product names are consistent (no typos/variations)
- [ ] Dates are YYYY-MM-DD format
- [ ] Days_Overdue is numeric (0, 1, 2, etc.)
- [ ] File is UTF-8 encoded (not Latin-1)
- [ ] No duplicate Vuln_IDs
- [ ] Less than 10,000 rows
- [ ] No special characters breaking CSV format

---

## 🔍 Troubleshooting Attempted

- [ ] Validated CSV format using DATA_EXTRACTION_GUIDE.txt
- [ ] Tested with sample_vulnerabilities.csv (works: Yes / No)
- [ ] Tried different browser (still fails: Yes / No)
- [ ] Checked file encoding (UTF-8: Yes / No)
- [ ] Verified column names match exactly
- [ ] Tested with smaller dataset (rows/columns)

---

## 📝 Field Mapping (if converting from another tool)

**Source System Fields → Dashboard Fields:**

| Source Field | Dashboard Field | Status |
|--------------|-----------------|--------|
| [Source] | Vuln_ID | ✓ |
| [Source] | CVE | ✓ |
| [Source] | Severity | ? |
| [Source] | Product | ✓ |

---

## 🔗 Related Documentation

- [DATA_EXTRACTION_GUIDE.txt](https://github.com/vermeg/security-governance-dashboard/blob/main/DATA_EXTRACTION_GUIDE.txt)
- [sample_vulnerabilities.csv](https://github.com/vermeg/security-governance-dashboard/blob/main/sample_vulnerabilities.csv)
- [README.txt - Troubleshooting](https://github.com/vermeg/security-governance-dashboard/blob/main/README.txt)

---

## 💡 System Information

**Fortify SSC Details (if applicable):**
- Fortify Version: [e.g., 22.2]
- Report Type: [e.g., "Vulnerability Report"]
- Number of Applications: [e.g., 5]
- API Access: Yes / No

**Export Method:**
- [ ] Manual export via UI
- [ ] API export (extract_fortify_data.py)
- [ ] Scheduled email report
- [ ] Other: ______________

---

## 📎 Attachments

- [ ] Sample CSV file (anonymized, first 5 rows)
- [ ] Screenshot of error
- [ ] CSV file header row with all column names

---

## ✅ Checklist

- [ ] I have read DATA_EXTRACTION_GUIDE.txt
- [ ] I have validated my CSV format
- [ ] I have tested with sample data
- [ ] I can share anonymized sample (important for debugging)
- [ ] I understand the CSV format requirements

