Ansible pre-commit hooks
########################

Ansible `pre-commit <http://pre-commit.com/>`_ hooks.

- ansible-syntax-check: The hook runs
  :code:`ansible --syntax-check` against playbooks declared.
- ansible-vault-check: The hook verifies that files that have :code:`vault` in
  the filename are indeed vaulted.

Dependencies
------------

- Ansible.
- Pre-commit.

Installation
------------

Add the following to your :code:`.pre-commit-config.yaml`:

.. code:: yaml

    - repo: https://www.shore.co.il/git/ansible-pre-commit/
      sha: v0.4.0
      hooks:
      - id: ansible-syntax-check
        # In case you want to specify other playbook files:
        files: playbook.yml
      - id: ansible-vault-check

And run :code:`pre-commit autoupdate` to update the hooks. In case your
:code:`roles` directory isn't in the same directory as the playbook you're
testing or at :code:`/etc/ansible/roles` you need to declare the roles search
path in :code:`ansible.cfg` in the root of the repo like so:

.. code:

    [defaults]
    roles_path=path/to/roles/directory:path/to/another/roles/directory

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
