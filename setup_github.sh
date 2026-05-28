#!/bin/bash
# Initialize GitHub repository for Security Governance Dashboard
# Run this in your project directory after cloning from GitHub

set -e

echo "🔧 Security Governance Dashboard - GitHub Setup"
echo "=================================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install git first:"
    echo "   MacOS: brew install git"
    echo "   Ubuntu: sudo apt-get install git"
    echo "   Windows: https://git-scm.com/download/win"
    exit 1
fi

echo "✅ Git is installed"
echo ""

# Initialize git repository (if not already initialized)
if [ ! -d .git ]; then
    echo "📦 Initializing git repository..."
    git init
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

echo ""
echo "📝 Configuring git..."

# Set local git config
git config user.name "Security Governance Team" || echo "Note: Set user.name manually: git config user.name 'Your Name'"
git config user.email "security@vermeg.com" || echo "Note: Set user.email manually: git config user.email 'your.email@vermeg.com'"

echo "✅ Git configured locally"
echo ""

# Add files to git
echo "📂 Staging files..."
git add .
echo "✅ Files staged"
echo ""

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Security Governance Dashboard v1.0

- Interactive vulnerability governance dashboard
- CSV data import capability
- KPI calculations and RAG status
- Executive summary generation
- Support for Fortify SSC integration" || echo "Note: Commit may have failed if repository already has commits"

echo ""
echo "✅ Setup complete!"
echo ""
echo "📌 Next steps:"
echo "1. Create a new repository on GitHub: https://github.com/new"
echo "2. Repository name: security-governance-dashboard"
echo "3. Description: Security Governance Dashboard - Vulnerability Management"
echo "4. Do NOT initialize with README (we have one)"
echo "5. Copy the HTTPS URL from GitHub"
echo "6. Run: git remote add origin <PASTE_YOUR_GITHUB_URL>"
echo "7. Run: git branch -M main"
echo "8. Run: git push -u origin main"
echo ""
echo "For SSH setup:"
echo "   git remote add origin git@github.com:YourUsername/security-governance-dashboard.git"
echo ""
