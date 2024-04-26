#!/usr/bin/env python3

import sqlite3

def parse_adlist(filename):
    f = open(filename)
    domains = []
    while True:
        r = f.readline()
        if r == "" or r == "\n":
            break
        else:
            domains.append(r.removesuffix("\n"))
    return(domains)


def insert_adlist(domains):
    domains = ({"address": a} for a in domains)
    with sqlite3.connect("/etc/pihole/gravity.db") as con:
        try:
            cursor = con.cursor()
            q = "INSERT OR IGNORE INTO adlist (address) VALUES (:address)"
            cursor.executemany(q, domains)
        except Exception as e:
            print(e)
            exit(1)


def main():
    filename = "pihole-adlist.txt"
    domains = parse_adlist(filename)
    insert_adlist(domains)


if __name__ == "__main__":
    main()
