#!/usr/bin/env python3

import sqlite3

def parse_adlist(filename: str)-> list[str]:
    with open(filename) as f:
        domains = [d for d in f]

    return (d.removesuffix("\n") for d in domains)


def insert_adlist(domains: list[str])->int:
    num_inserts = 0
    with sqlite3.connect("/etc/pihole/gravity.db") as con:
        try:
            for d in domains:
                cursor = con.cursor()
                q = "INSERT OR IGNORE INTO adlist (address) VALUES (:address)"
                domain = {"address": d}
                cursor.execute(q, domain)
                num_inserts += 1
        except Exception as e:
            raise e
    return num_inserts


def main():
    filename = "adlist.txt"

    try:
        domains = parse_adlist(filename)
    except FileNotFoundError as e:
        print(e)
        print(f"Could not open {filename}")
        print("Try cloning the repo again or running as root")
        exit(1)

    try:
        inserts = insert_adlist(domains)
        print(f"Inserted {inserts} domains.")
    except Exception as e:
        print(e)
        print("Unable to add domians to database. Is pihole installed? Try running as root.")
        exit(1)


if __name__ == "__main__":
    main()
