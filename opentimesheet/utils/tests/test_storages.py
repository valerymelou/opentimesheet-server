from unittest import TestCase

from ..storages import upload_to, upload_to_factory


class TestModel(object):
    class _meta:
        app_label = "test"


class StorageTest(TestCase):
    def testUploadToFactory(self):
        self.assertRegex(
            upload_to_factory("test")(object(), "test.txt"),
            r"^test/[a-zA-Z0-9\-_]{22}\.txt$",
        )

    def testUploadTo(self):
        self.assertRegex(
            upload_to(TestModel(), "test.txt"),
            r"^test/testmodel/[a-zA-Z0-9\-_]{22}\.txt$",
        )
