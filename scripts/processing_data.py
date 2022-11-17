import numpy as np
import pandas as pd

'''
This is used to process the calculated SPI, STI, LC, SVI, and the
other variables to make them ready for the training process.
The datasets should be saved into different folders under Data.
Pandas and Numpy are required to run this Python file.
'''

def processing_data(wdir,impacts,location,odir=None):
    '''
    wdir: the working directory where the datasets are located at
    impacts: the type of impacts to read the corresponding table
    location: state name, or climate region name, or "National"
    odir: the output directory of the processed datasets
    '''
    #read and binarize drought impacts
    if impacts in ["Agriculture", "Economy", "Fire", "Plant_Wildlife", "Relief_Response_Restriction", "Society_Public_Health", "Water_Supply_Quality"]:
        drought_impacts = pd.read_csv(wdir+"/DIR/"+impacts+".csv",index_col=[0,1])
        drought_impacts = drought_impacts.astype(bool).astype(int)
    else:
        raise ValueError('%s is not defined. The location should be in the category of drought impacts'%impacts)
    #read SPIs
    spi01 = pd.read_csv(wdir+"/SPI/CONUS_SPI01.csv",index_col=0).iloc[:,-120:] #slicing the SPIs from 2011 to 2020
    spi03 = pd.read_csv(wdir+"/SPI/CONUS_SPI03.csv",index_col=0).iloc[:,-120:]
    spi06 = pd.read_csv(wdir+"/SPI/CONUS_SPI06.csv",index_col=0).iloc[:,-120:]
    spi09 = pd.read_csv(wdir+"/SPI/CONUS_SPI09.csv",index_col=0).iloc[:,-120:]
    spi12 = pd.read_csv(wdir+"/SPI/CONUS_SPI12.csv",index_col=0).iloc[:,-120:]
    spi18 = pd.read_csv(wdir+"/SPI/CONUS_SPI18.csv",index_col=0).iloc[:,-120:]
    spi24 = pd.read_csv(wdir+"/SPI/CONUS_SPI24.csv",index_col=0).iloc[:,-120:]
    spi36 = pd.read_csv(wdir+"/SPI/CONUS_SPI36.csv",index_col=0).iloc[:,-120:]
    spi48 = pd.read_csv(wdir+"/SPI/CONUS_SPI48.csv",index_col=0).iloc[:,-120:]
    spi01 = spi01.sort_index()
    spi03 = spi03.sort_index()
    spi06 = spi06.sort_index()
    spi09 = spi09.sort_index()
    spi12 = spi12.sort_index()
    spi18 = spi18.sort_index()
    spi24 = spi24.sort_index()
    spi36 = spi36.sort_index()
    spi48 = spi48.sort_index()

    #read STIs
    sti01 = pd.read_csv(wdir+"/STI/CONUS_STI01.csv",index_col=0).iloc[:,-120:]
    sti03 = pd.read_csv(wdir+"/STI/CONUS_STI03.csv",index_col=0).iloc[:,-120:]
    sti06 = pd.read_csv(wdir+"/STI/CONUS_STI06.csv",index_col=0).iloc[:,-120:]
    sti09 = pd.read_csv(wdir+"/STI/CONUS_STI09.csv",index_col=0).iloc[:,-120:]
    sti12 = pd.read_csv(wdir+"/STI/CONUS_STI12.csv",index_col=0).iloc[:,-120:]
    sti18 = pd.read_csv(wdir+"/STI/CONUS_STI18.csv",index_col=0).iloc[:,-120:]
    sti24 = pd.read_csv(wdir+"/STI/CONUS_STI24.csv",index_col=0).iloc[:,-120:]
    sti01 = sti01.sort_index()
    sti03 = sti03.sort_index()
    sti06 = sti06.sort_index()
    sti09 = sti09.sort_index()
    sti12 = sti12.sort_index()
    sti18 = sti18.sort_index()
    sti24 = sti24.sort_index()
    
    #flatten spi and sti
    spi = np.concatenate((spi01.values.flatten().reshape(372960,1), 
                          spi03.values.flatten().reshape(372960,1), 
                          spi06.values.flatten().reshape(372960,1), 
                          spi09.values.flatten().reshape(372960,1), 
                          spi12.values.flatten().reshape(372960,1), 
                          spi18.values.flatten().reshape(372960,1), 
                          spi24.values.flatten().reshape(372960,1), 
                          spi36.values.flatten().reshape(372960,1), 
                          spi48.values.flatten().reshape(372960,1)), axis = 1)

    sti = np.concatenate((sti01.values.flatten().reshape(372960,1), 
                          sti03.values.flatten().reshape(372960,1), 
                          sti06.values.flatten().reshape(372960,1), 
                          sti09.values.flatten().reshape(372960,1), 
                          sti12.values.flatten().reshape(372960,1), 
                          sti18.values.flatten().reshape(372960,1), 
                          sti24.values.flatten().reshape(372960,1)), axis = 1)

    #read LULC category
    lulc = pd.read_csv(wdir+"/NLCD/NLCD_2016_freq.csv", index_col=0)
    lulc = lulc.sort_index()

    #read SVI
    svi = pd.read_csv(wdir+"/SVI/SVI2016_RPL.csv", index_col=0)
    svi = svi.sort_index()

    #read climate region
    cli_reg = pd.read_csv(wdir+"/Climate_Regions/Climate_Regions_County.csv",index_col=0)
    cli_reg = cli_reg.sort_index()
    climate_regions = pd.get_dummies(cli_reg.climate_regions).set_index(cli_reg.index) #one-hot encoding

    #month indicator
    month = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    months = np.tile(np.tile(month, 10),3108)
    months_dummy = pd.get_dummies(pd.DataFrame({'Month': months}).Month).reindex(columns = month) #one-hot encoding
    
    #adding the other variables to build df X
    df_X = pd.DataFrame(np.concatenate((spi,sti,np.repeat(lulc.values,120, axis = 0), 
                                        np.repeat(svi.values,120, axis = 0), 
                                        np.repeat(climate_regions.values,120, axis = 0), months_dummy),axis=1))
    df_X.columns = ['SPI01', 'SPI03','SPI06','SPI09','SPI12','SPI18','SPI24','SPI36','SPI48',\
                    'STI01','STI03','STI06','STI09','STI12','STI18','STI24']+\
                    lulc.columns.values.tolist()+svi.columns.values.tolist()+\
                    climate_regions.columns.values.tolist()+\
                    months_dummy.columns.values.tolist()
    
    #geoinfo
    geo = pd.read_csv(wdir+"/Geo_CSV/CONUS_County_wStateAbbr.csv").set_index("GEOID")
    #add the GEOID as the index of the X
    idx = np.repeat(geo.index.values,120,axis=0)
    df_X.index = idx
    
    #flatten DIR data to Y
    y = drought_impacts.values.flatten()
    df_y = pd.DataFrame({'Impacts': y}, index =idx)

    cli_reg_name = climate_regions.columns.values.tolist()
    state_name = np.unique(geo.loc[:,"State_NAME"].values)

    if location in state_name:
        geoid_series = geo.loc[geo.State_NAME.values==location,:].index.values
        df_X = df_X.loc[geoid_series,:]
        # drop climate region columns since a state is within the same climate region
        df_X = df_X.drop(cli_reg_name,axis=1)
        df_y = df_y.loc[geoid_series,:]

    elif location in cli_reg_name:
        df_X = df_X.loc[df_X.loc[:,location]==1,:]
        # drop climate region columns since the samples are from the same climate region
        df_X = df_X.drop(cli_reg_name,axis=1)
        df_y = df_y.loc[df_X.index.values,:]
        
    elif location == "National":
        pass
    
    else:
        raise ValueError('%s is not defined. The location should be either a state name (Capitalized), climate region, or "National".'%location)
    
    if odir!=None:
        df_X.to_csv(odir+"/Features.csv")
        df_y.to_csv(odir+"/Impacts.csv")
    
    return df_X, df_y
