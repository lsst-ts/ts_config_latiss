# ts_config_latiss
Configuration repository for the LATISS system. 

This code uses ``pre-commit`` to check yaml file syntax, maintain ``black`` formatting, and check ``flake8`` compliance.
To enable this, run the following commands once (the first removes the previous pre-commit hook)::

    git config --unset-all core.hooksPath
    pre-commit install
