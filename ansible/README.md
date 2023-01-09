##Introduction to Ansible


## Confguration Management Tool
- `Confguration Management Tool 'Defination`: A mechanism for maintaining the characteristics of a system, Configuration management today is about the "tools".

## Benefits of Confguration Management Tool
- `Quickly provision infrastructure`: parallel and automated
- `No more snowflakes`: system consistency
- `Version Controlled Infrastructure`: Infrastructure as Code
- `No more snowflakes`: system consistency
- `Configuration Management Tools`: Puppet, CHEF, SALTSTACK, Ansible

## Common Info on Ansible
- `Language`: Python + YAML
- `Managed Nodes Requirements`: Agentless
- `Centralized Management`: Any Computer can be controller
- `Script Names`: Playbook / Roles

## How does Ansible work
- `Engineers deploys ansible playbooks written in YAML to a control station.(Linux Host Servers)`
- `Ansible copies modules typically written in python to remote hosts to execute task.`

## Inside the Ansible control station
- `Linux host with a python and the ansible installed`
- `Supports transport to remote hosts`: Typically SSH but could use an API
- `Ansible Components`: Ansible configuraiton file, Inventory files, Ansible modules, Playbooks

## Overview of Ansible Components
- `Ansible requires a control machine to run the Ansible tool.` 
- `By default, Ansible uses a push model to push changes to remote hosts from the Ansible control machine.` 
- `The control machine can be any Linux/Unix host with a Python interpreter that supports SSH or the required transport to devices managed by Ansible.` 
- `Here is an explanation of some of the important components of the Ansible control machine.`

- `Modules`: typically written in Python. They are typically copied to remote hosts and run by the Ansible tool. Ansible modules are referenced as tasks in Ansible playbooks or using CLI arguments in the Ansible ad-hoc CLI tool.  

- `Inventory files `: contain the hosts that are operated by Ansible. They contain group and host definitions which can be referenced by Ansible playbooks or using CLI arguments from the Ansible ad-hoc CLI tool.

- `Playbooks`: are written in YAML and contain Ansible domain-specific language (DSL). To enable reuse, playbooks can be modularized much like software. Variables containing data for playbooks can be separated into YAML files residing on the Ansible control machine.

- `Configuration files `: control how the tool runs. For example, the configuration file can change the default directories of the modules.

## Overview of Ansible Inventory Files
An Ansible control machine requires one or more files that contain an inventory of the hosts to manage. Inventory files contain two basic components; groups and hosts. Group names are enclosed in brackets. The hosts that are listed below the group name belong to that group. The following example shows a basic inventory file that contains two group definitions and three hosts in an INI format:

[sandbox-servers] # A group definition
10.10.20.20     # A host in the sandbox-servers group

[nxos-switches] # A group definition
172.16.30.101   # A host in the nxos-switches group
172.16.30.102   # A host in the nxos-switches group

To identify a host, use its IP address or a hostname that's DNS can resolve. Also, any host or group can be referenced in a playbook or from the Ansible ad-hoc CLI.
A host can belong to multiple groups. For example, the following inventory file puts the 10.10.20.20 host in two groups.

[sandbox-servers]
10.10.20.20

[nxos-switches]
172.16.30.101
172.16.30.102

[datacenter-east]
10.10.20.20


In the example shown, you could use the sandbox-servers group to interface with all servers in the infrastructure. And you could use the datacenter-east group to interface with the servers in a specific datacenter. This gives you flexibility when operating hosts in the data center infrastructure.

