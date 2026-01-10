# emails.py
# Functions for extracting data from a raw email using regular expressions

import re

def email_sender(content):
    pattern = r"From: .*<(.*)>"
    match = re.search(pattern, content)
    return match.group(1) if match else None


def email_recipient(content):
    pattern = r"To: .*<(.*)>"
    match = re.search(pattern, content)
    return match.group(1) if match else None


def email_subject(content):
    pattern = r"Subject: (.+)"
    match = re.search(pattern, content)
    return match.group(1) if match else None


def email_body(content):
    # Email body starts after the first empty line
    pattern = r"\n\n([\s\S]*)"
    match = re.search(pattern, content)
    return match.group(1).strip() if match else None
