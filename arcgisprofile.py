"""
Manages and Assists Users to understand what is in their .arcgisprofile file.
"""
import os
import configparser
from pathlib import Path
__version__ = "1.0.0"
#--------------------------------------------------------------------------
def list_profiles():
    """
    Lists the names of all the profiles on the system
    
    :returns: List
    
    """
    home_dir = str(Path.home())
    profile_file = os.path.join(home_dir, ".arcgisprofile")
    if os.path.isfile(profile_file):
        config = configparser.ConfigParser()
        config.read(profile_file)
        return config.sections()
    return []
#--------------------------------------------------------------------------
def profile_information(profile):
    """
    Returns the profile information about a given connection
    
    =====================================================================     ====================================================================
    **Parameter**                                                             **Description**
    ---------------------------------------------------------------------     --------------------------------------------------------------------           
    profile                                                                   Required String. The name of the profile to get the information about.
    =====================================================================     ====================================================================
    
    :returns: Dict
    
    """
    home_dir = str(Path.home())
    profile_file = os.path.join(home_dir, ".arcgisprofile")
    if os.path.isfile(profile_file):
        config = configparser.ConfigParser()
        config.read(profile_file)
        keys = config.options(profile)
        values = {}
        for key in keys:
            try:
                if key == 'date_modified':
                    import datetime as _datetime
                    values[key] = _datetime.datetime.strptime(
                        config.get(
                            profile, 
                            key), 
                        "%Y-%m-%d %H:%M:%S.%f")
                else:
                    values[key] = config.get(profile, key)
            except:
                values[key] = None
        return values
    return None  
#--------------------------------------------------------------------------
def remove_profile(profile):
    """
    Deletes a profile from the .arcgisprofile file

    =====================================================================     ====================================================================
    **Parameter**                                                             **Description**
    ---------------------------------------------------------------------     --------------------------------------------------------------------           
    profile                                                                   Required String. The name of the profile to delete.
    =====================================================================     ====================================================================
    
    :returns: Boolean
    """
    home_dir = str(Path.home())
    profile_file = os.path.join(home_dir, ".arcgisprofile")
    if os.path.isfile(profile_file):    
        profiles = list_profiles()
        if profile in profiles:
            config = configparser.ConfigParser()
            with open(profile_file, 'r') as reader:
                config.readfp(reader)            
            config.remove_section(section=profile)
            with open(profile_file, "w") as f:
                config.write(f)            
            return True
        else:
            raise ValueError("Profile not found.")
    return False