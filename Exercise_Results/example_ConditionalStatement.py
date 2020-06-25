strSource = "https://services.arcgis.com/4OV0eRKiLAYkbH2J/arcgis/rest/services/DOI_Unified_Regions/FeatureServer/0"
iIndex = strSource.find("http")

if (iIndex >= 0):
    print("this could be a valid URL")
else:
    print("it’s not likely this is a URL")
