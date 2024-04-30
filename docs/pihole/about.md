# About

## What is Pi-Hole

Pi-Hole is a program aims to block ads and improve privacy on a local
network. Pi-Hole runs a private DNS server and filters
requests based on a domain blacklist. Pi-Hole ships with a
database of domains that are known to serve ads or host tracking
information, these domains are on the blacklist. Any request that
matches one of these domains is dropped, meaning the requesting
device does not know the IP address of the server at that domain.
Without the IP address it is impossible to send requests to the ad
server, effectively blocking the ad and stopping the sending of any
tracking information.

## Why phm

`phm` is part of cybersecurity project with the goal of researching
security and privacy focused open-source networking tools. Pi-Hole has
great documentation and has made the installation process very easy, I
created `phm` to encapsulate the installation process and make it
easier to add domains to the blacklist.

## How pihole works

### High-Level

`pihole` is a process that listens on port 53 and answers DNS
requests. When `pihole` receives a request, it checks to see if the
domain is in the pihole database. If there is a match in the database,
and the record is on the blacklist, `pihole` does not reply to
the request. If the requested domain is not on the blacklist, `pihole`
delegates the request to another DNS server and replies with the result.

### Technical Details

#### DNS

## Why root

I recommend running pihole on a dedicated machine, primarily because
the pihole install script and pihole its self must run with root
permissions to listen on port 53, the default DNS port. `pihole` also
stores its database under `/etc/`, which requires root
permissions to write to.
