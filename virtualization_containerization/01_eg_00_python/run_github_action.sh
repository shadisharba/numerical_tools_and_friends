curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | bash
./bin/act --action-offline-mode -l
./bin/act --action-offline-mode --graph
./bin/act --action-offline-mode
# rm ~/.config/act/actrc

# act --job <name-of-your-job>
# act --env-file=my-custom.env
# act --secret-file=my-custom.secrets
# act pull_request