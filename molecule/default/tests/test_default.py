import pytest


@pytest.fixture()
def AnsibleDefaults(host):
    return host.ansible("include_vars", "defaults.yml")["ansible_facts"]


# def test_systemd_overlay_file(host):
#     f = host.file("/etc/systemd/system/cockpit.socket.d/listen.conf")
#     assert f.exists
#     assert f.is_file


def test_cockpit_client_packages(host):
    p = host.package("cockpit-storaged")
    assert p.is_installed
