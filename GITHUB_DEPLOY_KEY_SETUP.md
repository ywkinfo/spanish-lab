# GitHub Deploy Key Setup for Hermes

Use this when Hermes should push content branches to a single repository without using the operator's personal GitHub login.

## Recommended use

- Hermes may push only to staging/content branches
- `main` remains protected
- Human review still gates merge into `main`
- Best for a single repository with repeatable branch pushes

## Security model

- Use one SSH keypair per repo or per deployment target
- Store private keys in persistent secret storage, not in the repo
- Restrict permissions on secret files to the owner only
- Prefer branch push access over full account access

## 1) Generate a keypair

If this is a Hermes VM or container with persistent storage, create the key under a secret directory outside the repo.

Preferred path when `ssh-keygen` is available:

```sh
mkdir -p /opt/data/secrets/github
chmod 700 /opt/data/secrets /opt/data/secrets/github
ssh-keygen -t ed25519 \
  -C "hermes-espanol-studio-deploy" \
  -f /opt/data/secrets/github/hermes_espanol_deploy \
  -N ""
chmod 600 /opt/data/secrets/github/hermes_espanol_deploy
```

Fallback when `ssh-keygen` is not installed in this environment:

```sh
openssl genrsa -out /opt/data/secrets/github/hermes_espanol_deploy_rsa.pem 4096
chmod 600 /opt/data/secrets/github/hermes_espanol_deploy_rsa.pem
```

Print the public key for GitHub:

```sh
cat /opt/data/secrets/github/hermes_espanol_deploy.pub
# or, with the RSA fallback, use the generated .pub file next to the private key
```

## 2) Register the public key on GitHub

Repository settings:

- Settings
- Deploy keys
- Add deploy key
- Title: something like `hermes-espanol-studio-vps`
- Paste the public key
- If you want Hermes to push branches, enable write access

## 3) Create a dedicated SSH config entry

```sh
cat > /opt/data/secrets/github/ssh_config <<'EOF'
Host github-hermes
  HostName github.com
  User git
  IdentityFile /opt/data/secrets/github/hermes_espanol_deploy
  IdentitiesOnly yes
  StrictHostKeyChecking accept-new
EOF
chmod 600 /opt/data/secrets/github/ssh_config
```

## 4) Test the connection

```sh
GIT_SSH_COMMAND="ssh -F /opt/data/secrets/github/ssh_config" \
ssh -T git@github.com
```

A successful test should identify the key or at least stop asking for password auth.

## 5) Clone or repoint the repo

Clone using the SSH alias:

```sh
GIT_SSH_COMMAND="ssh -F /opt/data/secrets/github/ssh_config" \
git clone git@github-hermes:OWNER/REPO.git /opt/data/repos/spanish-lab
```

Or repoint an existing clone:

```sh
cd /opt/data/repos/spanish-lab
git remote set-url origin git@github-hermes:OWNER/REPO.git
```

## 6) Configure git identity

```sh
cd /opt/data/repos/spanish-lab
git config user.name "Hermes Agent"
git config user.email "hermes-agent@users.noreply.github.com"
```

## 7) Content branch workflow

```sh
cd /opt/data/repos/spanish-lab
git fetch origin
git switch main
git pull --ff-only

BRANCH="hermes/content-a1-$(date +%Y%m%d-%H%M)"
git switch -c "$BRANCH"
# generate package files here

git status --short
git diff --check
git add .
git commit -m "Add A1 content package"
GIT_SSH_COMMAND="ssh -F /opt/data/secrets/github/ssh_config" git push -u origin "$BRANCH"
```

## 8) Review gate

After push:

- send the branch name to the human reviewer
- include the checklist
- do not merge to `main` until approved

## Common problems

- Permission denied: check that the deploy key has write access
- Host key prompt: confirm the SSH config file is being used
- Push rejected: verify you are pushing a branch, not `main`
- Repo not found: confirm OWNER/REPO and the deploy key is added to that exact repository
