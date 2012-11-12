from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PolicyPlonetraining(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import policy.plonetraining
        xmlconfig.file('configure.zcml',
                       policy.plonetraining,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'policy.plonetraining:default')

POLICY_PLONETRAINING_FIXTURE = PolicyPlonetraining()
POLICY_PLONETRAINING_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(POLICY_PLONETRAINING_FIXTURE, ),
                       name="PolicyPlonetraining:Integration")