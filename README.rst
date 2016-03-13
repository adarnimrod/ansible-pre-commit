Ansible pre-commit hook
#######################

Ansible `pre-commit <http://pre-commit.com/>`_ hook. The hook runs
:code:`ansible --syntax-check` against playbooks found.

Usage
-----

Add the following to your :code:`.pre-commit-config.yaml`:

.. :code: yaml

    - repo: https://www.shore.co.il/git/ansible-pre-commit/
      sha: v0.1.0
      hooks:
      - id: ansible-pre-commit
        files: playbook.yml
