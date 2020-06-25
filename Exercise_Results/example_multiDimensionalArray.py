lstNextExercise = [
    ["EPA_Ecoregion3", "C:/temp/us_eco_l3.shp", "US_L3NAME"],
    ["Unified_Regions", "https://services.arcgis.com/4OV0eRKiLAYkbH2J/arcgis/rest/services/DOI_Unified_Regions/FeatureServer/0", "REG_NAME"], 
    ["Omernick3","C:/temp/NA_CEC_Eco_Level3.shp"," NA_L3NAME"],
    ["FS_Ecoregtions", "C:/Temp/eco_us.shp", "Province"]
]

for x in lstNextExercise:
    for xx in x:
        print(xx)


