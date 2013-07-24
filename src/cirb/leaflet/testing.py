from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CirbleafletLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import cirb.leaflet
        xmlconfig.file(
            'configure.zcml',
            cirb.leaflet,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'cirb.leaflet:default')

CIRB_LEAFLET_FIXTURE = CirbleafletLayer()
CIRB_LEAFLET_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CIRB_LEAFLET_FIXTURE,),
    name="CirbleafletLayer:Integration"
)
CIRB_LEAFLET_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CIRB_LEAFLET_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CirbleafletLayer:Functional"
)
