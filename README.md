# Ansible role: OpenSSH

![Molecule Tests](https://github.com/crgwilson/ansible-role-openssh/workflows/Molecule%20Test/badge.svg)

Manage SSH configuration & service

* Install SSH related packages
* Create `ssh_config` & `sshd_config` based on templates
* Manage SSH service

## Variables

TODO

## Testing

Testing for this project is setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```

