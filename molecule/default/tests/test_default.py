import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_default_server_package(host):
    p = host.package('openssh-server')
    assert p.is_installed


def test_default_client_package(host):
    if host.system_info.distribution == 'centos':
        pkg = 'openssh-clients'
    else:
        pkg = 'openssh-client'

    p = host.package(pkg)
    assert p.is_installed


def test_default_revoked_keys_file(host):
    f = host.file('/etc/ssh/revoked_keys')
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o600


def test_default_service(host):
    if host.system_info.distribution == 'debian':
        service_name = 'ssh'
    else:
        service_name = 'sshd'

    s = host.service(service_name)
    assert s.is_running
