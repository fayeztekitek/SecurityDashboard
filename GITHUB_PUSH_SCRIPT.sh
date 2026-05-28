#!/bin/bash
# ==============================================================================
# Security Governance Dashboard - GitHub Push Script
# ==============================================================================
# This script initializes the local repository and pushes to GitHub
# Run this on YOUR machine after cloning your empty GitHub repository
# ==============================================================================

set -e

echo "🚀 Security Governance Dashboard - GitHub Push Script"
echo "======================================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git is not installed${NC}"
    echo "Please install git first:"
    echo "  MacOS: brew install git"
    echo "  Ubuntu: sudo apt-get install git"
    echo "  Windows: https://git-scm.com/download/win"
    exit 1
fi

echo -e "${GREEN}✅ Git is installed${NC}"
echo ""

# Get repository URL from user
echo -e "${BLUE}📋 STEP 1: GitHub Repository URL${NC}"
echo ""
read -p "Enter your GitHub repository URL (HTTPS format): " REPO_URL

if [ -z "$REPO_URL" ]; then
    echo -e "${RED}❌ Repository URL cannot be empty${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Repository URL: $REPO_URL${NC}"
echo ""

# Configure git user
echo -e "${BLUE}📋 STEP 2: Configure Git User${NC}"
echo ""

read -p "Enter your name (for commits): " GIT_NAME
read -p "Enter your email (for commits): " GIT_EMAIL

git config --global user.name "$GIT_NAME"
git config --global user.email "$GIT_EMAIL"

echo -e "${GREEN}✅ Git configured:${NC}"
echo "   Name: $GIT_NAME"
echo "   Email: $GIT_EMAIL"
echo ""

# Initialize repository
echo -e "${BLUE}📋 STEP 3: Initialize Git Repository${NC}"
echo ""

if [ -d .git ]; then
    echo -e "${YELLOW}⚠️  Git repository already exists${NC}"
    read -p "Remove existing .git directory? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf .git
        echo -e "${GREEN}✅ Removed existing .git${NC}"
    else
        echo -e "${YELLOW}⚠️  Using existing git repository${NC}"
    fi
fi

git init
echo -e "${GREEN}✅ Git repository initialized${NC}"
echo ""

# Add remote
echo -e "${BLUE}📋 STEP 4: Add GitHub Remote${NC}"
echo ""

if git remote get-url origin &>/dev/null; then
    echo -e "${YELLOW}⚠️  Remote 'origin' already exists${NC}"
    git remote remove origin
    echo -e "${GREEN}✅ Removed existing remote${NC}"
fi

git remote add origin "$REPO_URL"
echo -e "${GREEN}✅ Remote added: origin${NC}"
echo ""

# Stage files
echo -e "${BLUE}📋 STEP 5: Stage Files${NC}"
echo ""

git add .
echo -e "${GREEN}✅ All files staged${NC}"

# Show what will be committed
echo ""
echo -e "${YELLOW}📂 Files to be committed:${NC}"
git diff --cached --name-only | head -20
echo ""

FILE_COUNT=$(git diff --cached --name-only | wc -l)
echo -e "${GREEN}Total: $FILE_COUNT files${NC}"
echo ""

# Create initial commit
echo -e "${BLUE}📋 STEP 6: Create Initial Commit${NC}"
echo ""

git commit -m "Initial commit: Security Governance Dashboard v1.0

📊 Interactive vulnerability governance dashboard

✨ Features:
- Real-time KPI calculations and RAG status
- CSV data import with validation
- Executive summary generation
- Product risk assessment
- Client exposure analysis
- SLA compliance tracking
- Risk acceptance management
- Trend analysis and visualizations
- Fortify SSC integration support
- Responsive design (desktop/mobile)

📦 Components:
- consolidated_dashboard.html - Main interactive dashboard
- extract_fortify_data.py - Automated Fortify data extraction
- sample_vulnerabilities.csv - Sample data for testing
- Complete documentation (5 guides)
- GitHub configuration (issue templates, contributing guide)

🔐 Security:
- READONLY mode (no data modifications)
- All processing local to browser
- No external API calls
- No database required
- Suitable for confidential data

📚 Documentation:
- README.txt - Complete getting started guide
- DATA_EXTRACTION_GUIDE.txt - Fortify export instructions
- GOVERNANCE_SUMMARY_TEMPLATE.txt - Executive briefing format
- GITHUB_SETUP_INSTRUCTIONS.txt - Repository setup guide

🚀 Ready for immediate deployment!"

echo -e "${GREEN}✅ Commit created${NC}"
echo ""

# Set main branch
echo -e "${BLUE}📋 STEP 7: Set Main Branch${NC}"
echo ""

git branch -M main
echo -e "${GREEN}✅ Branch set to 'main'${NC}"
echo ""

# Push to GitHub
echo -e "${BLUE}📋 STEP 8: Push to GitHub${NC}"
echo ""
echo -e "${YELLOW}⚠️  You will be prompted for authentication...${NC}"
echo "   For HTTPS: Use your Personal Access Token (not password)"
echo "   For SSH: Ensure SSH key is configured"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅✅✅ SUCCESS! Project pushed to GitHub! ✅✅✅${NC}"
    echo ""
    echo -e "${BLUE}📌 Next Steps:${NC}"
    echo "   1. Go to: $REPO_URL"
    echo "   2. Verify all files are present"
    echo "   3. Configure branch protection (Settings > Branches)"
    echo "   4. Add team members (Settings > Collaborators)"
    echo "   5. Start tracking changes!"
    echo ""
    echo -e "${GREEN}Dashboard is ready for team use!${NC}"
else
    echo ""
    echo -e "${RED}❌ Push failed${NC}"
    echo "Troubleshooting:"
    echo "  1. Verify repository URL is correct"
    echo "  2. Check authentication (Personal Access Token or SSH key)"
    echo "  3. Ensure repository is empty (not initialized with README)"
    echo "  4. Try again: git push -u origin main"
    exit 1
fi

echo ""
