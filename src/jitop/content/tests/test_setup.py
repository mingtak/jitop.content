# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from jitop.content.testing import JITOP_CONTENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that jitop.content is properly installed."""

    layer = JITOP_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if jitop.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'jitop.content'))

    def test_browserlayer(self):
        """Test that IJitopContentLayer is registered."""
        from jitop.content.interfaces import (
            IJitopContentLayer)
        from plone.browserlayer import utils
        self.assertIn(IJitopContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = JITOP_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['jitop.content'])

    def test_product_uninstalled(self):
        """Test if jitop.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'jitop.content'))

    def test_browserlayer_removed(self):
        """Test that IJitopContentLayer is removed."""
        from jitop.content.interfaces import \
            IJitopContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(IJitopContentLayer, utils.registered_layers())
