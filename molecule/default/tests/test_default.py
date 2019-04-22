import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["htop"])
def test_packages(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize("file", ["/etc/htoprc"])
def test_files(host, file):
    f = host.file(file)

    assert f.exists
