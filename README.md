# finance
Finance

# Configuring Vault

Run vault:

    vault server -config ./vault.hcl

Access from terminal:

    export VAULT_ADDR='http://127.0.0.1:8200'

Init vault (first time):

    vault init -key-threshold=1 -key-shares=1

To authenticate:

    vault unseal (enter key)
    vault auth (enter root token)

To enter secrets:

    vault write secret/foo username=foo password=-
