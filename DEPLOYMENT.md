# GitHub Pages Deployment

## 🚀 Deployment Status

The GitHub Pages deployment is now **ACTIVATED** and configured to automatically deploy the FHIR Implementation Guide.

## 📋 Deployment Configuration

### Triggers

- **Manual workflow dispatch ONLY**: Can only be triggered manually through GitHub Actions interface
- **No automatic deployment**: Changes pushed to main branch will NOT trigger deployment

### Deployment Target

- **Source branch**: `main` (where workflow runs and source code lives)
- **Deployment method**: GitHub Pages artifact upload (official GitHub Pages deployment)
- **Environment**: `github-pages` environment with proper protection rules

### Deployment URL
The FHIR IG will be available at: **https://rockphotog.github.io/nlk-test/**

## 🔧 Workflow Features

- ✅ Automated FHIR IG building with SUSHI and IG Publisher
- ✅ Caching for faster builds
- ✅ Security verification (only input directory used)
- ✅ Complete dependency management
- ✅ Jekyll-ready output for GitHub Pages
- ✅ Force rebuild option available

## 🎯 Next Steps

1. **Manually trigger workflow** - Use GitHub Actions interface to start deployment
2. **Monitor the workflow** - Check GitHub Actions tab for build status  
3. **Access the deployed IG** - Visit <https://rockphotog.github.io/nlk-test/> once deployment completes

## 🛠️ Manual Deployment

To manually trigger a deployment:
1. Go to **Actions** tab in GitHub
2. Select **"Build and Deploy FHIR IG to GitHub Pages"**
3. Click **"Run workflow"**
4. Optionally check "Force complete rebuild" for a clean build

## 📊 Build Process

The deployment workflow:

1. Sets up Java 17, Ruby/Jekyll, and Node.js 20
2. Installs FHIR packages and dependencies
3. Runs SUSHI to compile FSH files
4. Executes IG Publisher to generate the complete IG
5. Uploads build artifact to GitHub Pages
6. Deploys via official GitHub Pages deployment action

---
*Last updated: September 24, 2025*