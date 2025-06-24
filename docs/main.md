## Przykładowe użycie
```yml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: install-packages
      vars:
        input_debug: true
        input_ubuntu_repositories:
          - repo: "deb [arch=amd64 signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com {{ ansible_distribution_release }} main"
            filename: "hashicorp"
            self_signed_repository_key: https://apt.releases.hashicorp.com/gpg
            self_signed_repository_key_dest: /usr/share/keyrings/hashicorp-archive-keyring.gpg
            state: present
        input_packages_to_install:
          - "nano"
        input_packages_to_remove:
          - "vim-tiny"
      when: ansible_os_family == "Debian"

    - role: install-packages
      vars:
        input_debug: true
        input_packages_to_install:
          - "nano"
        input_packages_to_remove:
          - "vim-tiny"
      when: ansible_os_family == "Alpine"

    - role: install-packages
      vars:
        input_debug: true
        input_redhat_repositories: []
        input_packages_to_install:
          - "epel-release"
          # - "nano"
        input_packages_to_remove:
          - "vim-tiny"
      when: ansible_os_family == "RedHat"
```
## Testy molecule

```bash
python3 -m venv ~/.venvs/molecule
source ~/.venvs/molecule/bin/activate
pip install --upgrade pip

pip3 install ansible-core molecule molecule-proxmox pytest-testinfra ansible-lint molecule-plugins requests testinfra

export TEST_PROXMOX_DEBUG=
export TEST_PROXMOX_HOST=
export TEST_PROXMOX_PORT=
export TEST_PROXMOX_USER=
export TEST_PROXMOX_PASSWORD=
export TEST_PROXMOX_NODE=

molecule test

# molecule create
# molecule converge
# molecule verify
# molecule destroy
 ```