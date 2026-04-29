# pim - Pi IMproved

Like most other programmers, I fell in love with Mario's Pi coding agent, but as I began using it I discovered several serious security issues. Not the least of which was how it had full access to a system it was installed on. Because of this, I wanted to write a wrapper for Pi which would not only scope-limit Pi to the directory it was working on, but would flag any write/remove attempts by the agent, while still keeping that "we only ship the barebones" mentality of Pi.

The result was "pim", which totally isn't borrowed from another project...

### Installation

Pim does require an existing installation of Pi in order to work, as well as Python3:

```bash
git clone https://github.com/matthewlabrecque/pim.git $USER/bin
rm -rf $USER/bin/pim/.git
```

### Operation

By default pim will limit the write scope of Pi to the working directory, as well as Pi's local files and /tmp

```bash
pim
```

Next up is to allow Pim to talk directly with Pi and tell it when it's not in scope
