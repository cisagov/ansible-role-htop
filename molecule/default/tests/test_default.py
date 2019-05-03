"""Module containing the tests for the default scenario."""

import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["htop"])
def test_packages(host, pkg):
    """Test that the appropriate packages were installed."""
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize("file", ["/etc/htoprc"])
def test_files(host, file):
    """Test that config files were copied over as expected."""
    f = host.file(file)

    assert f.exists
