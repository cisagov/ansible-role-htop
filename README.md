# ansible-role-htop #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-htop/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-htop/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-htop/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-htop/actions/workflows/codeql-analysis.yml)

An Ansible role for installing and configuring
[`htop`](https://hisham.hm/htop/).

## Requirements ##

This role uses the `package` Ansible module, so [its
requirements](https://docs.ansible.com/ansible/latest/modules/package_module.html#requirements)
apply.

## Role Variables ##

None.

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Install and configure htop
      ansible.builtin.include_role:
        name: htop
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier <jeremy.frasier@gwe.cisa.dhs.gov>
