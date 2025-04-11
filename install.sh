#!bin/bash

#Install Rust binary gloablly
cargo install --path "$(pwd)" --root "$HOME/.cargo" || {
  echo "Error while installing.manual Intervention required"
  exit 1
}

#Create directory for python script
PYTHON_DEST="$HOME/.local/share/deepvibe"
mkdir -p "$PYTHON_DEST"
cp scripts/script.py "$PYTHON_DEST"

echo "Installed Python script to $PYTHON_DEST"

# Detect shell and pick correct profile
detect_shell_profile() {
  case "$SHELL" in
  */zsh) echo "$HOME/.zshrc" ;;
  */bash) echo "$HOME/.bashrc" ;;
  */fish) echo "$HOME/.config/fish/config.fish" ;; # not export compatible
  *) echo "$HOME/.profile" ;;
  esac
}
SHELL_PROFILE=$(detect_shell_profile)

#Adds binary path to Shell profile
if ! grep -q 'DEEPVIBE_SCRIPT_PATH' "$SHELL_PROFILE"; then
  echo "export DEEPVIBE_SCRIPT_PATH=\"$PYTHON_DEST/script.py\"" >>"$SHELL_PROFILE"
  echo "Added DEEPVIBE_SCRIPT_PATH to $SHELL_PROFILE"
else
  echo "DEEPVIBE_SCRIPT_PATH already set in $SHELL_PROFILE"
fi

echo "Please run: source $SHELL_PROFILE or restart your terminal"
