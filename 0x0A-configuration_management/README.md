#An Introduction to Configuration Management
CM (configration manegement) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time.
There are a number of configuration management tools available in the market. Puppet, Ansible, Chef and Salt are popular choices. And they are all driven by the same purpose: to make sure the system’s state matches the state described by your provisioning scripts.

## Benefits of Configuration Management for Servers
Quick Provisioning of New Servers.
Quick Recovery from Critical Events.
No More Snowflake Servers: Manual hotfixes, configuration tweaks, and software updates can turn servers into unique snowflakes, hard to manage and even harder to replicate. By using CM tool, the procedure necessary for bringing up a new server or updating will be all documented in the provisioning scripts.
Version Control for the Server Environment.
Replicated Environments

## Overview of Configuration Management Tools

### Automation Framework
Each CM tool provides a specific syntax and a set of features that you can use to write provisioning scripts.

### Idempotent Behavior
Configuration management tools keep track of the state of resources in order to avoid repeating tasks that were executed before.

### System Facts
Configuration management tools usually provide detailed information about the system being provisioned. 

### Templating System
Most CM tools will provide a built-in templating system that can be used to facilitate setting up configuration files and services.

### Extensibility
it can be extended by using third party extions and modules.

#Conclusion
Configuration management can drastically improve the integrity of servers over time by providing a framework for automating processes and keeping track of changes made to the system environment.
Configuration management
