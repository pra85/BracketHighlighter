"""
BracketHighlighter.

Copyright (c) 2013 - 2015 Isaac Muse <isaacmuse@gmail.com>
License: MIT
"""
from BracketHighlighter.bh_plugin import import_module
lowercase = import_module("bh_modules.lowercase")


def validate(*args):
    """Check if bracket is lowercase."""
    return lowercase.validate(*args)


def compare(name, first, second, bfr):
    """Ensure correct open is paired with correct close."""

    o = bfr[first.begin:first.end]
    c = bfr[second.begin:second.end]

    match = False
    if o == "if" and c == "fi":
        match = True
    elif o in ["select", "for", "while", "until"] and c == "done":
        match = True
    elif o == "case" and c == "esac":
        match = True
    return match
