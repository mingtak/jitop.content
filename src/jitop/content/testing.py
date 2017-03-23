# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import jitop.content


class JitopContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=jitop.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'jitop.content:default')


JITOP_CONTENT_FIXTURE = JitopContentLayer()


JITOP_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(JITOP_CONTENT_FIXTURE,),
    name='JitopContentLayer:IntegrationTesting'
)


JITOP_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(JITOP_CONTENT_FIXTURE,),
    name='JitopContentLayer:FunctionalTesting'
)


JITOP_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        JITOP_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='JitopContentLayer:AcceptanceTesting'
)
