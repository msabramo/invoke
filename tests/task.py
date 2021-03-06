from spec import Spec, skip, eq_, raises

from invoke.task import task
from invoke.loader import Loader

from _utils import support


class _Dummy(object):
    pass


class task_(Spec):
    "@task"

    def allows_access_to_wrapped_object(self):
        dummy = _Dummy()
        eq_(task(dummy).body, dummy)

    def allows_alias_specification(self):
        c = Loader(root=support).load_collection('decorator')
        eq_(c.get('foo'), c.get('bar'))

    def allows_default_specification(self):
        c = Loader(root=support).load_collection('decorator')
        eq_(c.get(), c.get('biz'))

    @raises(ValueError)
    def raises_ValueError_on_multiple_defaults(self):
        c = Loader(root=support).load_collection('decorator_multi_default')
