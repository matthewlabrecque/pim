# pim - Pi IMproved

pim is a Python wrapper script which seeks to do one thing: Improve the security of the Pi.dev agentic coding agent.

### The problem

I love using Pi.dev for helping me write scripts and other small programming projects, but there's one massive issue with it. By default, Pi runs with the same user permissions as the calling user, which is a security nightmare as these coding agents have the potential to nuke filesystems, or even worse leak your ssh keys on the internet. I don't blame Mario for this, he made it clear that he wanted to only ship the barebones, but that's where we have to come in and create our own solutions.

### What is pim?

Pim hardens Pi by doing the following:

1) Sandboxes the agent from the kernel
2) Makes all filesystems read only by default except the working directory, Pi's own configuration directory (~/.pi), and /tmp
3) Hides .ssh from the filesystem meaning your keys are safe from being leaked in an LLM surface vector attack
4) Rejects Pi's permissions to use `sudo`
5) Performs a prompt injection into Pi's master prompt which means Pi knows its read only except the working directory, and will tell the user
6) Will ask for permission before performing any sort of `rm` operation

### How to install pim

Currently, pim is Linux only and required an existing installation of Pi as well as the `seccomp` and `bubblewrap` packages:

```bash
git clone https://github.com/matthewlabrecque/pim.git
cd pim
cp pim.py ~/.local/bin/pim
```
