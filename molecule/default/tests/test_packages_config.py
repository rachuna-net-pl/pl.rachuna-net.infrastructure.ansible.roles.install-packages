import pytest
import re

INSTALLED_PACKAGE_NAME = "nano"
REMOVED_PACKAGE_NAME = "vim-tiny"


def test_package_installed(host):
    package = host.package(INSTALLED_PACKAGE_NAME)
    assert package.is_installed, "Pakiet "+INSTALLED_PACKAGE_NAME+" nie jest zainstalowany!"

def test_package_removed(host):
    package = host.package(REMOVED_PACKAGE_NAME)
    assert not package.is_installed, "Pakiet "+REMOVED_PACKAGE_NAME+" jest zainstalowany!"
