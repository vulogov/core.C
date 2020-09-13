import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

tests_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

from coreC import *

def test_ns1():
    ns = NS()
    assert isinstance(ns, NS)

def test_ns2():
    ns = NS(answer=42)
    assert ns.get("/etc/answer") == 42