# coding: utf-8

"""
    Peacemakr

    This API describes the Peacemakr services, which enable seamless application layer encryption and verification.  # noqa: E501

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301
import setuptools.command.build_py
import distutils.cmd
import distutils.log
import subprocess
import setuptools
import sys
import os

NAME = "peacemakr-sdk"
VERSION = "0.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]

# subprocess.call("./scripts/install_core_crypto")

class InstallCoreCryptoCommand(distutils.cmd.Command):
  """A custom command to run Pylint on all Python source files."""

  description = 'run Pylint on Python source files'
  user_options = [
      # The format is (long option, short option, description).
      ('pylint-rcfile=', None, 'path to Pylint config file'),
  ]
  def initialize_options(self):
    """Set default values for options."""
    pass

  def finalize_options(self):
    """Post-process options."""
    pass

  def run(self):
    """Run command."""
    site_packages = next(p for p in sys.path if 'site-packages' in p)
    git_clone_command = ["git" ,"clone", "https://github.com/peacemakr-io/peacemakr-core-crypto.git"]
    rm_clone_command = ["rm", "-rf", "peacemakr-core-crypto"]
    install_command = ["cd", "peacemakr-core-crypto/bin", "&&", "./release-python.sh", "local", site_packages, "release"]
    export_env = ["export", "LD_LIBRARY_PATH=/usr/local/lib"]
    # clone the repo
    self.announce(
        'Cloning core-crypto @: %s' % ("https://github.com/peacemakr-io/peacemakr-core-crypto.git"),
        level=distutils.log.INFO)
    subprocess.run(git_clone_command)

    # check openssl and cmake

    # running release commands
    self.announce(
        'Installing core-crytpo into %s' % str(site_packages),
        level=distutils.log.INFO)
    os.system(" ".join(install_command))

    # remove peacemakr-core-crypto
    self.announce(
        'Removing core-crytpo folder',
        level=distutils.log.INFO)
    subprocess.run(rm_clone_command)

    self.announce(
        'Removing core-crytpo folder',
        level=distutils.log.INFO)
    os.system(" ".join(export_env))


class BuildPyCommand(setuptools.command.build_py.build_py):
  """Custom build command."""

  def run(self):
    self.run_command('install_core_crypto')
    setuptools.command.build_py.build_py.run(self)

setup(
    cmdclass={
        'install_core_crypto': InstallCoreCryptoCommand,
        'build_py': BuildPyCommand,
    },
    name=NAME,
    version=VERSION,
    description="Peacemakr",
    author_email="",
    url="",
    keywords=["Peacemakr"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This API describes the Peacemakr services, which enable seamless application layer encryption and verification.  # noqa: E501
    """
)
