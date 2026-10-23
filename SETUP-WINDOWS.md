# Windows setup

Security tooling lives on Linux, so you work in **WSL2** (Ubuntu running inside Windows).
✅ = already done.

## ✅ Step 0. Install Ubuntu (PowerShell as Administrator)
```powershell
wsl --install -d Ubuntu
```

Open Ubuntu any time: Windows key, type **Ubuntu**, Enter. The prompt is green and ends in `$`.

## Step 1. Update Ubuntu and install tools (Ubuntu window)
```bash
cd ~
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv git curl
python3 --version
git --version
```

## Step 2. Git identity
```bash
git config --global user.name "Aaron F"
git config --global user.email "builtbyaaronf@gmail.com"
git config --global init.defaultBranch main
```
To hide your email, turn on GitHub Settings > Emails > "Keep my email addresses private" and use the `...@users.noreply.github.com` address above instead.

## ✅ Step 3. GitHub account: `builtbyaaronf-sif`

## Step 4. Connect this computer to GitHub
```bash
ssh-keygen -t ed25519 -C "github"
cat ~/.ssh/id_ed25519.pub
```
Press Enter 3 times at the prompts. Copy the line starting `ssh-ed25519` into GitHub > Settings > SSH and GPG keys > New SSH key.
```bash
ssh -T git@github.com
```
Type `yes` if asked. Success: "Hi builtbyaaronf-sif!"
Never share `~/.ssh/id_ed25519` (no `.pub`). That is the private key.

## Step 5. VS Code (Windows)
Open VS Code, `Ctrl+Shift+X`, install **WSL** and **Python** (both Microsoft).

## ✅ Step 6. Repo created: `ai-security-career`

## Step 7. Clone and open it (Ubuntu window)
```bash
mkdir -p ~/code && cd ~/code
git clone git@github.com:builtbyaaronf-sif/ai-security-career.git
cd ai-security-career
code .
```
Bottom left of VS Code must say **"WSL: Ubuntu"**.

## Step 8. Your first commit
```bash
cp log/TEMPLATE.md log/week-01.md
```
Fill in `log/week-01.md` in VS Code, save, then:
```bash
git add log/week-01.md
git commit -m "Week 1 log started"
git push
```

**Done when:** `ssh -T git@github.com` says "Hi" and `log/week-01.md` shows on GitHub.
