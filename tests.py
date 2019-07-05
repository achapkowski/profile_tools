"""
This is the test suite to test the `arcgisprofile` methods.

To run this suite, update the `USERNAME` and `PASSWORD` 
variable to test against ArcGIS Online.
If you want to test against a Portal, update the `URL`
variable.

"""

import unittest
import pytest

USERNAME = None
PASSWORD = None
URL = None

import uuid
from arcgis.gis import GIS
import arcgisprofile


class TestProfileTools(unittest.TestCase):
    """Tests the Profile Tool Methods"""
    #----------------------------------------------------------------------
    @pytest.mark.skipif((USERNAME is None or PASSWORD is None), 
                        reason="requires a USERNAME and PASSWORD to be provided.")    
    def test_list_profile(self):
        """tests listing a system profiles"""
        profiles_old = arcgisprofile.list_profiles()
        assert isinstance(arcgisprofile.list_profiles(), list)
        assert len(profiles_old) >= 0
        profile = uuid.uuid4().hex
        GIS(url=URL, 
            username=USERNAME, password=PASSWORD, 
            verify_cert=False, profile=profile)
        assert isinstance(arcgisprofile.list_profiles(), list)
        profiles = arcgisprofile.list_profiles()
        assert len(profiles) >= len(profiles_old)
        arcgisprofile.remove_profile(profile=profile)
        profiles = arcgisprofile.list_profiles()
        assert len(profiles) == len(profiles_old)
    #----------------------------------------------------------------------
    @pytest.mark.skipif((USERNAME is None or PASSWORD is None), 
                        reason="requires a USERNAME and PASSWORD to be provided.")    
    def test_profile_information(self):
        """tests the profile information method"""
        profiles = arcgisprofile.list_profiles()
        created = False
        if len(profiles) > 0:
            profile = profiles[0]
        else:
            created = True
            profile = uuid.uuid4().hex
            GIS(url=URL, 
                username=USERNAME, password=PASSWORD, 
                verify_cert=False, profile=profile)
        assert arcgisprofile.profile_information(profile=profile)
        assert len(arcgisprofile.profile_information(profile=profile).keys()) >= 2
        if created:
            arcgisprofile.remove_profile(profile=profile)
    #----------------------------------------------------------------------
    @pytest.mark.skipif((USERNAME is None or PASSWORD is None), 
                        reason="requires a USERNAME and PASSWORD to be provided.")    
    def test_remove_profile(self):
        """tests the profile removal method"""
            
        profile = uuid.uuid4().hex
        GIS(url=URL, username=USERNAME, 
            password=PASSWORD, 
            verify_cert=False, profile=profile)
        assert profile in arcgisprofile.list_profiles()
        assert arcgisprofile.remove_profile(profile)
        assert not profile in arcgisprofile.list_profiles()
    