=======================================
PUMA: Python Universal Monitoring Agent
=======================================

PUMA aims to be a universal monitoring agent by wrapping several backends and allowing cross communication between them.

The goal is to have an almost agnostic monitoring tool capable of sending and receiving KPIs and alarms from any python-supported platform and/or protocol.

Some of the planned backends to be supported are:

* Paho
* gnocchi
* dweepy
* phant
* ncpa
* telegram

It's not PUMA's goal to reinvent the wheel but to wrap existing libraries into a common framework simplifying the sharing labour of merging data from different sources in your workflow.
