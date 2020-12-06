from setuptools import setup


setup(
    name="pre_commit_ansible_dummy_package",
    url="https://git.shore.co.il/ansible/ansible-pre-commit",
    author="Nimrod Adar",
    author_email="nimrod@shore.co.il",
    version=open("VERSION", "r").read().strip(),
    install_requires=["ansible==2.9.6"],
)
