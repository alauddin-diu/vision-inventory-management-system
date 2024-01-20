"""This module provides template tags pertaining to SSO functionality"""

import logging

from django import template

from common.models import Vision_IMSSetting
from Vision_IMS.helpers import str2bool

register = template.Library()
logger = logging.getLogger('Vision_IMS')


@register.simple_tag()
def sso_login_enabled():
    """Return True if single-sign-on is enabled"""

    return str2bool(Vision_IMSSetting.get_setting('LOGIN_ENABLE_SSO'))


@register.simple_tag()
def sso_reg_enabled():
    """Return True if single-sign-on is enabled for self-registration"""
    return str2bool(Vision_IMSSetting.get_setting('LOGIN_ENABLE_SSO_REG'))


@register.simple_tag()
def sso_auto_enabled():
    """Return True if single-sign-on is enabled for auto-registration"""
    return str2bool(Vision_IMSSetting.get_setting('LOGIN_SIGNUP_SSO_AUTO'))


@register.simple_tag()
def sso_check_provider(provider):
    """Return True if the given provider is correctly configured"""

    import allauth.app_settings
    from allauth.socialaccount.models import SocialApp

    # First, check that the provider is enabled
    apps = SocialApp.objects.filter(provider__iexact=provider.id)

    if not apps.exists():
        logging.error(
            "SSO SocialApp %s does not exist (known providers: %s)",
            provider.id, [obj.provider for obj in SocialApp.objects.all()]
        )
        return False

    # Next, check that the provider is correctly configured
    app = apps.first()

    if allauth.app_settings.SITES_ENABLED:
        # At least one matching site must be specified
        if not app.sites.exists():
            logger.error("SocialApp %s has no sites configured", app)
            return False

    # At this point, we assume that the provider is correctly configured
    return True
