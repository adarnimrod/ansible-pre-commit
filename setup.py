from setuptools import setup


setup(
        name='pre_commit_ansible_dummy_package',
        url='https://www.shore.co.il/git/ansible-pre-commit',
        author='Nimrod Adar',
        author_email='nimrod@shore.co.il',
        version=open('VERSION', 'r').read().strip(),
        install_requires=['ansible==2.6.18'],
)
