"""
DeployWebsite.py - Build and deploy website to GitHub

Process:
1. Set dev_mode to false in config
2. Rebuild all pages
3. Convert all markdown files
4. Commit and push to GitHub
5. Restore dev_mode to true (for local development)
"""

import subprocess
import sys
from pathlib import Path
import yaml

def run_command(command, description):
    """Run a command and show output"""
    print(f"\n{'='*50}")
    print(f"📌 {description}")
    print(f"{'='*50}")
    result = subprocess.run(command, shell=True, capture_output=False)
    if result.returncode != 0:
        print(f"❌ Error: {description} failed!")
        sys.exit(1)
    print(f"✅ {description} completed!")

def update_config(dev_mode_value):
    """Update dev_mode in site_config.yaml"""
    config_path = Path('site_config.yaml')
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    config['site']['dev_mode'] = dev_mode_value
    
    with open(config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
    
    print(f"✅ Set dev_mode = {dev_mode_value}")

def deploy_website():
    """Main deployment function"""
    
    print("🚀 Starting Website Deployment Process")
    print("="*50)
    
    # Step 1: Set dev_mode to false
    print("\n📝 Step 1: Preparing for production...")
    update_config(dev_mode_value=False)
    
    # Step 2: Rebuild all pages
    print("\n🏗️  Step 2: Building website...")
    run_command(
        f"{sys.executable} render_pages.py",
        "Rendering main pages"
    )
    
    # Step 3: Convert all markdown files
    run_command(
        f"{sys.executable} convert_markdown.py",
        "Converting markdown files"
    )
    
    # Step 4: Git operations
    print("\n📦 Step 3: Committing to GitHub...")
    
    # Get commit message
    commit_message = input("\n💬 Enter commit message: ").strip()
    
    if not commit_message:
        print("❌ Commit message cannot be empty!")
        # Restore dev_mode before exiting
        update_config(dev_mode_value=True)
        sys.exit(1)
    
    # Show git status
    run_command("git status", "Checking git status")
    
    # Add all files
    run_command("git add .", "Adding files to git")
    
    # Show status again
    run_command("git status", "Verifying staged files")
    
    # Confirm deployment
    confirm = input("\n⚠️  Ready to commit and push? (yes/no): ").strip().lower()
    
    if confirm != 'yes':
        print("\n🛑 Deployment cancelled!")
        # Restore dev_mode
        update_config(dev_mode_value=True)
        sys.exit(0)
    
    # Commit
    run_command(
        f'git commit -m "{commit_message}"',
        "Committing changes"
    )
    
    # Push to GitHub
    run_command(
        "git push -u origin master",
        "Pushing to GitHub"
    )
    
    # Step 5: Restore dev_mode for local development
    print("\n🔧 Step 4: Restoring local development mode...")
    update_config(dev_mode_value=True)
    
    # Final success message
    print("\n" + "="*50)
    print("🎉 DEPLOYMENT SUCCESSFUL!")
    print("="*50)
    print("✅ Website built")
    print("✅ Changes committed to GitHub")
    print("✅ Dev mode restored")
    print("\n🌐 Your site will be live at:")
    print("   https://YOUR-USERNAME.github.io/YOUR-REPO")
    print("="*50)

if __name__ == '__main__':
    try:
        deploy_website()
    except KeyboardInterrupt:
        print("\n\n🛑 Deployment interrupted!")
        print("🔧 Restoring dev_mode...")
        update_config(dev_mode_value=True)
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Deployment failed with error: {e}")
        print("🔧 Restoring dev_mode...")
        update_config(dev_mode_value=True)
        sys.exit(1)