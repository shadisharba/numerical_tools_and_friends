curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | bash
./bin/act --action-offline-mode
# rm ~/.config/act/actrc