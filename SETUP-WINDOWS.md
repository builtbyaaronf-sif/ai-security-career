# Windows setup (Monday, about 2 hours)

Security tooling lives on Linux. You will work in **WSL2** (real Ubuntu inside Windows).

Open **PowerShell as Administrator**:

```powershell
wsl --install -d Ubuntu-24.04
```
Restart. Ubuntu opens; create a Linux username and password.

Back in PowerShell (normal):
```powershell
winget install -e --id Microsoft.VisualStudioCode
winget install -e --id Git.Git
```

In VS Code, install the extensions **WSL** and **Python**.

In the Ubuntu terminal:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv git curl
git config --global user.name "Aaron F"
git config --global user.email "your-public-email"
ssh-keygen -t ed25519 -C "github"
cat ~/.ssh/id_ed25519.pub
```
Paste that key into GitHub > Settings > SSH keys. Test: `ssh -T git@github.com`

Then:
```bash
mkdir -p ~/code && cd ~/code
git clone git@github.com:<you>/ai-security-journey.git
code ai-security-journey
```
Done when VS Code opens with "WSL: Ubuntu" in the bottom left corner.

Use a **new email** for the public profiles (not the FORGE sales inbox) so career and business stay separate.
