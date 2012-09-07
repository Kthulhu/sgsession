from pprint import pprint
from subprocess import call
from unittest import TestCase
import itertools

from sgfs import SGFS

from . import fixtures


def setUpModule():
    fixtures.setup_tasks()
    globals().update(fixtures.__dict__)


class TestContext(TestCase):
    
    def setUp(self):
        self.sgfs = SGFS(root=root, shotgun=sg)
        
    def test_basics(self):
        
        shots = [self.sgfs.session.merge(x) for x in fixtures.tasks]
        shots[0].pprint()
        print
        
        ctx = self.sgfs.context_from_entities([shots[0]])
        ctx.pprint()
        print
        
        ctx = self.sgfs.context_from_entities(shots)
        ctx.pprint()
        print
        
        self.assert_(False)
        