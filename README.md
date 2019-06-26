# ArcGIS Profile Tools
Manages the **ArcGIS API for Python** profile File

## The ArcGIS API for Python

ArcGIS API for Python is a Python library for working with maps and geospatial data, powered by web GIS. It 
provides simple and efficient tools for sophisticated vector and raster analysis, geocoding, map making, 
routing and directions, as well as for organizing and managing a GIS with users, groups and information 
items. In addition to working with your own data, the library enables access to ready to use maps and 
curated geographic data from Esri and other authoritative sources. It also integrates well with the 
scientific Python ecosystem and includes rich support for Pandas and Jupyter notebook.

To download or find out more, go here: https://developers.arcgis.com/python

## Usage

### Listing Profile Names

The `.arcgisprofile` file can contain multiple entries.  It is nice to know what profile names exist.

```python
from arcgisprofile import list_profiles
print(list_profiles())
```

### Listing Profile Names

The `.arcgisprofile` file can contain multiple entries.  It is nice to know what profile names exist.

```python
from arcgisprofile import list_profiles
print(list_profiles())
```

### Getting the Profile Information

The profile file provides basic information that is important.  It provides the site URL, the last 
time used, and the username.

```python
from arcgisprofile import list_profiles, profile_information
for profile in list_profiles():
	data = profile_information(profile)
	print(data)
```

The result of the `profile_information` is to provide a dictionary with the following key/value pairs:

```
{
	"date_modified" : <datime.datetime> object,
	"username" : "Username as String",
	"url" : "Login URL for the Site"
}
```

### Removing a Profile Entry

The profile file determines if a user can access that profile stored on a system.  This method will
remove the profile name from the `.arcgisprofile` file.

```python
from arcgisprofile import list_profiles, remove_profile
for profile in list_profiles():
	if profile == 'bad profile':
		data = remove_profile(profile)
print(list_profiles())
```


