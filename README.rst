Ansible pre-commit hook
#######################

Ansible `pre-commit <http://pre-commit.com/>`_ hook. The hook runs
:code:`ansible --syntax-check` against playbooks declared.

Usage
-----

Add the following to your :code:`.pre-commit-config.yaml`:

.. code:: yaml

    - repo: https://www.shore.co.il/git/ansible-pre-commit/
      sha: v0.2.0
      hooks:
      - id: ansible-pre-commit
        files: playbook.yml

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://www.shore.co.il/git/.
