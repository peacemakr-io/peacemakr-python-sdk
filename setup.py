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
import shutil
import platform

NAME = "peacemakr"
VERSION = "0.0.2"

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
    "urllib3>=1.23",
    "distro>=1.4.0",
]

CORE_CRYPTO_URL_BASE="https://github.com/peacemakr-io/peacemakr-core-crypto/releases/download/"
CORE_CRYPTO_VERSION="v0.2.0"

class InstallCoreCryptoCommand(distutils.cmd.Command):
  """A custom command to run Pylint on all Python source files."""

  description = 'run Pylint on Python source files'
  user_options = []
  def initialize_options(self):
    """Set default values for options."""
    pass

  def finalize_options(self):
    """Post-process options."""
    pass

  def _execute_command(self, command, err_msg=""):
    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT)
    except Exception as e:
        sys.exit("Running command %s failed. %s. %s" % (" ".join(command), e, err_msg))

  def _execute_shell_command(self, command, err_msg=""):
      ret_code = os.system(" ".join(command))

      if ret_code != 0:
          sys.exit("Running shell command %s failed with error code %s. %s" % (" ".join(command), ret_code, err_msg))

  def _is_pyversion_in_range(self, tuple, major_version, minor_version):
    return tuple[0] == major_version and tuple[1] == minor_version

  def _install_from_artifact(self, tar_filename, core_crypto_so_filename, core_crypto_shared_filename, core_crypto_cpp_shared_filename):
    self.announce("Installing from artifact", level=distutils.log.INFO)
    site_package_dir = next(p for p in sys.path if 'site-packages' in p)
    get_command = "wget -q " + CORE_CRYPTO_URL_BASE + CORE_CRYPTO_VERSION + "/" + tar_filename
    unzip_command = "tar -zxvf " + tar_filename

    self._execute_command(get_command.split(" "))
    self._execute_command(unzip_command.split(" "))

    # copying file
    shutil.copyfile(core_crypto_so_filename, site_package_dir+"/"+core_crypto_so_filename)
    shutil.copyfile("lib/"+core_crypto_shared_filename, "/usr/local/lib/"+core_crypto_shared_filename)
    shutil.copyfile("lib/"+core_crypto_cpp_shared_filename, "/usr/local/lib/"+core_crypto_cpp_shared_filename)

  def _virtualenv_enabled(self):
    """Checks virtualenv is enabled or not"""
    return hasattr(sys, 'real_prefix')

  def _install_from_source(self):
    site_package_dir = "none"
    if self._virtualenv_enabled():
        site_package_dir = next(p for p in sys.path if 'site-packages' in p)
    # commands to run
    git_clone_command = ["git" ,"clone", "https://github.com/peacemakr-io/peacemakr-core-crypto.git"]
    git_checkout_tag = ["cd", "peacemakr-core-crypto", "&&", "git", "checkout", "tags/"+CORE_CRYPTO_VERSION]
    rm_clone_command = ["rm", "-rf", "peacemakr-core-crypto"]
    install_command = ["cd", "peacemakr-core-crypto/bin", "&&", "./release-python.sh", "local", site_package_dir, "release"]
    check_openssl_installed = ["openssl", "version"]
    check_cmake_installed = ["cmake", "--version"]

    # clone the repo
    self.announce(
    'Cloning core-crypto @: %s' % ("https://github.com/peacemakr-io/peacemakr-core-crypto.git"),
    level=distutils.log.INFO)
    self._execute_command(git_clone_command)

    # checkout lastest stable core-crypto tag
    self.announce(
        'Checking out tag '+CORE_CRYPTO_VERSION,
        level=distutils.log.INFO)
    self._execute_shell_command(git_checkout_tag)

    # check openssl and cmake
    self.announce("Checking CMake and OpenSSL is installed", level=distutils.log.INFO)
    self._execute_shell_command(check_cmake_installed, err_msg="CMake not installed. CMake 3.15+ required for this library.\n\n\n \
        Please refer to Core-crypto for installation: https://github.com/peacemakr-io/peacemakr-core-crypto/")
    self._execute_shell_command(check_openssl_installed, err_msg="OpenSSL not installed. Openssl 1.1+ required for this library.\n\n\n \
        Please refer to Core-crypto for installation: https://github.com/peacemakr-io/peacemakr-core-crypto/")

    # running release commands
    self.announce(
    'Installing core-crytpo into %s %s' % (str(site_package_dir), " ".join(install_command)),
    level=distutils.log.INFO)
    self._execute_shell_command(install_command, err_msg="Installation from source failed. Please refer to Core-crypto for installation: https://github.com/peacemakr-io/peacemakr-core-crypto/")

    # remove peacemakr-core-crypto
    self.announce(
    'Removing core-crytpo folder',
    level=distutils.log.INFO)
    self._execute_command(rm_clone_command)

  def run(self):
    """Build core-crypto
    Two methods to build core-crypto python library
    1. From Artifact: If user is using a OS/Arch/Python version that fits the deployed artifact,
       the command simply fetch and deploy the pre-built library
    2. From Source: If the version doesn't match, but is still macos/linux. The command
       clone the core-crypto from specific tag and built from source.

    # TODO: Remind user to set LD_LIBRARY_PATH for Ubuntu in README
    """
    os_type = sys.platform
    machine_type = platform.machine()
    python_version = platform.python_version_tuple()
    tar_filename = ""
    core_crypto_so_filename = ""
    core_crypto_shared_filename = ""
    core_crypto_cpp_shared_filename = ""

    if os_type == "darwin":
        # user is using macos
        if machine_type == "x86_64" and self._is_pyversion_in_range(python_version, '3', '7'):
            # install from artifact
            tar_filename = "peacemakr-core-crypto-python-macos-x86_64.tar.gz"
            core_crypto_so_filename = "peacemakr_core_crypto_python.cpython-37m-darwin.so"
            core_crypto_shared_filename = "libpeacemakr-core-crypto.dylib"
            core_crypto_cpp_shared_filename = "libpeacemakr-core-crypto-cpp.dylib"

            self._install_from_artifact(tar_filename, core_crypto_so_filename, core_crypto_shared_filename, core_crypto_cpp_shared_filename)

        else:
            # install from src
            self.announce("Installing core-crypto from source", level=distutils.log.INFO)
            self._install_from_source()

    elif os_type == "linux":
        # user is using linux
        import distro
        linux_distribution = distro.linux_distribution(full_distribution_name=False)[0]
        
        if linux_distribution in ["debian", "ubuntu"] and machine_type == "x86_64" and self._is_pyversion_in_range(python_version, '3', '6'):
            # install from artifact
            tar_filename = "peacemakr-core-crypto-python-ubuntu-x86_64.tar.gz"
            core_crypto_so_filename = "peacemakr_core_crypto_python.cpython-36m-x86_64-linux-gnu.so"
            core_crypto_shared_filename = "libpeacemakr-core-crypto.so"
            core_crypto_cpp_shared_filename = "libpeacemakr-core-crypto-cpp.so"

            self._install_from_artifact(tar_filename, core_crypto_so_filename, core_crypto_shared_filename, core_crypto_cpp_shared_filename)

        else:
            # install from src
            self.announce("Installing in Non-Debian Linux, installing core-crypto from source", level=distutils.log.INFO)
            self._install_from_source()
    else:
        sys.exit("Error: OS not supported. We only support Ubuntu and MacOS at the moment.")

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
    python_requires='>=3.6',
    author_email="",
    url="",
    keywords=["Peacemakr"],
    install_requires=REQUIRES,
    setup_requires=['distro'],
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This API describes the Peacemakr services, which enable seamless application layer encryption and verification.  # noqa: E501
    """,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries",
    ]
)
