from ast import Lambda
from operator import index
import os
import pandas as pd
import numpy as np

IN_PATH_AUSTIN_WEATHER = os.path.join('weather','austin','2010_2020_austin.csv')
IN_PATH_DALLAS_WEATHER = os.path.join('weather','dallas','2010_2020_dallas.csv')
IN_PATH_HOUSTON_WEATHER = os.path.join('weather','houston','2010_2020_houston.csv')
IN_PATH_LOS_ANGELES_WEATHER = os.path.join('weather','los_angeles','2010_2020_los_angeles.csv')
IN_PATH_NEW_YORK_WEATHER = os.path.join('weather','new_york','2010_2020_new_york.csv')
AUSTIN_WEATHER_URL = 'https://www.ncei.noaa.gov/orders/cdo/2909277.csv'
DALLAS_WEATHER_URL = 'https://www.ncei.noaa.gov/orders/cdo/2905654.csv'
HOUSTON_WEATHER_URL = 'https://www.ncei.noaa.gov/orders/cdo/2905669.csv'
LOS_ANGELES_WEATHER_URL = 'https://www.ncei.noaa.gov/orders/cdo/2905675.csv'
NEW_YORK_WEATHER_URL = 'https://www.ncei.noaa.gov/orders/cdo/2905680.csv'
IN_PATH_AUSTIN_PM25_2020 = os.path.join('air_pollution','austin','pm25','austin_2020_pm25.csv')
IN_PATH_AUSTIN_PM25_2019 = os.path.join('air_pollution','austin','pm25','austin_2019_pm25.csv')
IN_PATH_AUSTIN_PM25_2018 = os.path.join('air_pollution','austin','pm25','austin_2018_pm25.csv')
IN_PATH_AUSTIN_PM25_2017 = os.path.join('air_pollution','austin','pm25','austin_2017_pm25.csv')
IN_PATH_AUSTIN_PM25_2016 = os.path.join('air_pollution','austin','pm25','austin_2016_pm25.csv')
IN_PATH_AUSTIN_PM25_2015 = os.path.join('air_pollution','austin','pm25','austin_2015_pm25.csv')
IN_PATH_AUSTIN_PM25_2014 = os.path.join('air_pollution','austin','pm25','austin_2014_pm25.csv')
IN_PATH_AUSTIN_PM25_2013 = os.path.join('air_pollution','austin','pm25','austin_2013_pm25.csv')
IN_PATH_AUSTIN_PM25_2012 = os.path.join('air_pollution','austin','pm25','austin_2012_pm25.csv')
IN_PATH_AUSTIN_PM25_2011 = os.path.join('air_pollution','austin','pm25','austin_2011_pm25.csv')
IN_PATH_AUSTIN_PM25_2010 = os.path.join('air_pollution','austin','pm25','austin_2010_pm25.csv')
IN_PATH_HOUSTON_PM25_2020 = os.path.join('air_pollution','houston','pm25','houston_2020_pm25.csv')
IN_PATH_HOUSTON_PM25_2019 = os.path.join('air_pollution','houston','pm25','houston_2019_pm25.csv')
IN_PATH_HOUSTON_PM25_2018 = os.path.join('air_pollution','houston','pm25','houston_2018_pm25.csv')
IN_PATH_HOUSTON_PM25_2017 = os.path.join('air_pollution','houston','pm25','houston_2017_pm25.csv')
IN_PATH_HOUSTON_PM25_2016 = os.path.join('air_pollution','houston','pm25','houston_2016_pm25.csv')
IN_PATH_HOUSTON_PM25_2015 = os.path.join('air_pollution','houston','pm25','houston_2015_pm25.csv')
IN_PATH_HOUSTON_PM25_2014 = os.path.join('air_pollution','houston','pm25','houston_2014_pm25.csv')
IN_PATH_HOUSTON_PM25_2013 = os.path.join('air_pollution','houston','pm25','houston_2013_pm25.csv')
IN_PATH_HOUSTON_PM25_2012 = os.path.join('air_pollution','houston','pm25','houston_2012_pm25.csv')
IN_PATH_HOUSTON_PM25_2011 = os.path.join('air_pollution','houston','pm25','houston_2011_pm25.csv')
IN_PATH_HOUSTON_PM25_2010 = os.path.join('air_pollution','houston','pm25','houston_2010_pm25.csv')
IN_PATH_DALLAS_PM25_2020 = os.path.join('air_pollution','dallas','pm25','dallas_2020_pm25.csv')
IN_PATH_DALLAS_PM25_2019 = os.path.join('air_pollution','dallas','pm25','dallas_2019_pm25.csv')
IN_PATH_DALLAS_PM25_2018 = os.path.join('air_pollution','dallas','pm25','dallas_2018_pm25.csv')
IN_PATH_DALLAS_PM25_2017 = os.path.join('air_pollution','dallas','pm25','dallas_2017_pm25.csv')
IN_PATH_DALLAS_PM25_2016 = os.path.join('air_pollution','dallas','pm25','dallas_2016_pm25.csv')
IN_PATH_DALLAS_PM25_2015 = os.path.join('air_pollution','dallas','pm25','dallas_2015_pm25.csv')
IN_PATH_DALLAS_PM25_2014 = os.path.join('air_pollution','dallas','pm25','dallas_2014_pm25.csv')
IN_PATH_DALLAS_PM25_2013 = os.path.join('air_pollution','dallas','pm25','dallas_2013_pm25.csv')
IN_PATH_DALLAS_PM25_2012 = os.path.join('air_pollution','dallas','pm25','dallas_2012_pm25.csv')
IN_PATH_DALLAS_PM25_2011 = os.path.join('air_pollution','dallas','pm25','dallas_2011_pm25.csv')
IN_PATH_DALLAS_PM25_2010 = os.path.join('air_pollution','dallas','pm25','dallas_2010_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2020 = os.path.join('air_pollution','los_angeles','pm25','la_2020_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2019 = os.path.join('air_pollution','los_angeles','pm25','la_2019_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2018 = os.path.join('air_pollution','los_angeles','pm25','la_2018_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2017 = os.path.join('air_pollution','los_angeles','pm25','la_2017_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2016 = os.path.join('air_pollution','los_angeles','pm25','la_2016_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2015 = os.path.join('air_pollution','los_angeles','pm25','la_2015_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2014 = os.path.join('air_pollution','los_angeles','pm25','la_2014_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2013 = os.path.join('air_pollution','los_angeles','pm25','la_2013_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2012 = os.path.join('air_pollution','los_angeles','pm25','la_2012_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2011 = os.path.join('air_pollution','los_angeles','pm25','la_2011_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2010 = os.path.join('air_pollution','los_angeles','pm25','la_2010_pm25.csv')
IN_PATH_NEW_YORK_PM25_2020 = os.path.join('air_pollution','new_york','pm25','ny_2020_pm25.csv')
IN_PATH_NEW_YORK_PM25_2019 = os.path.join('air_pollution','new_york','pm25','ny_2019_pm25.csv')
IN_PATH_NEW_YORK_PM25_2018 = os.path.join('air_pollution','new_york','pm25','ny_2018_pm25.csv')
IN_PATH_NEW_YORK_PM25_2017 = os.path.join('air_pollution','new_york','pm25','ny_2017_pm25.csv')
IN_PATH_NEW_YORK_PM25_2016 = os.path.join('air_pollution','new_york','pm25','ny_2016_pm25.csv')
IN_PATH_NEW_YORK_PM25_2015 = os.path.join('air_pollution','new_york','pm25','ny_2015_pm25.csv')
IN_PATH_NEW_YORK_PM25_2014 = os.path.join('air_pollution','new_york','pm25','ny_2014_pm25.csv')
IN_PATH_NEW_YORK_PM25_2013 = os.path.join('air_pollution','new_york','pm25','ny_2013_pm25.csv')
IN_PATH_NEW_YORK_PM25_2012 = os.path.join('air_pollution','new_york','pm25','ny_2012_pm25.csv')
IN_PATH_NEW_YORK_PM25_2011 = os.path.join('air_pollution','new_york','pm25','ny_2011_pm25.csv')
IN_PATH_NEW_YORK_PM25_2010 = os.path.join('air_pollution','new_york','pm25','ny_2010_pm25.csv')

IN_PATH_AUSTIN_PM10_2020 = os.path.join('air_pollution','austin','pm10','austin_2020_pm10.csv')
IN_PATH_AUSTIN_PM10_2019 = os.path.join('air_pollution','austin','pm10','austin_2019_pm10.csv')
IN_PATH_AUSTIN_PM10_2018 = os.path.join('air_pollution','austin','pm10','austin_2018_pm10.csv')
IN_PATH_AUSTIN_PM10_2017 = os.path.join('air_pollution','austin','pm10','austin_2017_pm10.csv')
IN_PATH_AUSTIN_PM10_2016 = os.path.join('air_pollution','austin','pm10','austin_2016_pm10.csv')
IN_PATH_AUSTIN_PM10_2015 = os.path.join('air_pollution','austin','pm10','austin_2015_pm10.csv')
IN_PATH_AUSTIN_PM10_2014 = os.path.join('air_pollution','austin','pm10','austin_2014_pm10.csv')
IN_PATH_AUSTIN_PM10_2013 = os.path.join('air_pollution','austin','pm10','austin_2013_pm10.csv')
IN_PATH_AUSTIN_PM10_2012 = os.path.join('air_pollution','austin','pm10','austin_2012_pm10.csv')
IN_PATH_AUSTIN_PM10_2011 = os.path.join('air_pollution','austin','pm10','austin_2011_pm10.csv')
IN_PATH_AUSTIN_PM10_2010 = os.path.join('air_pollution','austin','pm10','austin_2010_pm10.csv')

IN_PATH_HOUSTON_PM10_2020 = os.path.join('air_pollution','houston','pm10','houston_2020_pm10.csv')
IN_PATH_HOUSTON_PM10_2019 = os.path.join('air_pollution','houston','pm10','houston_2019_pm10.csv')
IN_PATH_HOUSTON_PM10_2018 = os.path.join('air_pollution','houston','pm10','houston_2018_pm10.csv')
IN_PATH_HOUSTON_PM10_2017 = os.path.join('air_pollution','houston','pm10','houston_2017_pm10.csv')
IN_PATH_HOUSTON_PM10_2016 = os.path.join('air_pollution','houston','pm10','houston_2016_pm10.csv')
IN_PATH_HOUSTON_PM10_2015 = os.path.join('air_pollution','houston','pm10','houston_2015_pm10.csv')
IN_PATH_HOUSTON_PM10_2014 = os.path.join('air_pollution','houston','pm10','houston_2014_pm10.csv')
IN_PATH_HOUSTON_PM10_2013 = os.path.join('air_pollution','houston','pm10','houston_2013_pm10.csv')
IN_PATH_HOUSTON_PM10_2012 = os.path.join('air_pollution','houston','pm10','houston_2012_pm10.csv')
IN_PATH_HOUSTON_PM10_2011 = os.path.join('air_pollution','houston','pm10','houston_2011_pm10.csv')
IN_PATH_HOUSTON_PM10_2010 = os.path.join('air_pollution','houston','pm10','houston_2010_pm10.csv')

IN_PATH_DALLAS_PM10_2020 = os.path.join('air_pollution','dallas','pm10','dallas_2020_pm10.csv')
IN_PATH_DALLAS_PM10_2019 = os.path.join('air_pollution','dallas','pm10','dallas_2019_pm10.csv')
IN_PATH_DALLAS_PM10_2018 = os.path.join('air_pollution','dallas','pm10','dallas_2018_pm10.csv')
IN_PATH_DALLAS_PM10_2017 = os.path.join('air_pollution','dallas','pm10','dallas_2017_pm10.csv')
IN_PATH_DALLAS_PM10_2016 = os.path.join('air_pollution','dallas','pm10','dallas_2016_pm10.csv')
IN_PATH_DALLAS_PM10_2015 = os.path.join('air_pollution','dallas','pm10','dallas_2015_pm10.csv')
IN_PATH_DALLAS_PM10_2014 = os.path.join('air_pollution','dallas','pm10','dallas_2014_pm10.csv')
IN_PATH_DALLAS_PM10_2013 = os.path.join('air_pollution','dallas','pm10','dallas_2013_pm10.csv')
IN_PATH_DALLAS_PM10_2012 = os.path.join('air_pollution','dallas','pm10','dallas_2012_pm10.csv')
IN_PATH_DALLAS_PM10_2011 = os.path.join('air_pollution','dallas','pm10','dallas_2011_pm10.csv')
IN_PATH_DALLAS_PM10_2010 = os.path.join('air_pollution','dallas','pm10','dallas_2010_pm10.csv')

IN_PATH_LOS_ANGELES_PM10_2020 = os.path.join('air_pollution','los_angeles','pm10','la_2020_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2019 = os.path.join('air_pollution','los_angeles','pm10','la_2019_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2018 = os.path.join('air_pollution','los_angeles','pm10','la_2018_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2017 = os.path.join('air_pollution','los_angeles','pm10','la_2017_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2016 = os.path.join('air_pollution','los_angeles','pm10','la_2016_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2015 = os.path.join('air_pollution','los_angeles','pm10','la_2015_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2014 = os.path.join('air_pollution','los_angeles','pm10','la_2014_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2013 = os.path.join('air_pollution','los_angeles','pm10','la_2013_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2012 = os.path.join('air_pollution','los_angeles','pm10','la_2012_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2011 = os.path.join('air_pollution','los_angeles','pm10','la_2011_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2010 = os.path.join('air_pollution','los_angeles','pm10','la_2010_pm10.csv')

IN_PATH_NEW_YORK_PM10_2020 = os.path.join('air_pollution','new_york','pm10','ny_2020_pm10.csv')
IN_PATH_NEW_YORK_PM10_2019 = os.path.join('air_pollution','new_york','pm10','ny_2019_pm10.csv')
IN_PATH_NEW_YORK_PM10_2018 = os.path.join('air_pollution','new_york','pm10','ny_2018_pm10.csv')
IN_PATH_NEW_YORK_PM10_2017 = os.path.join('air_pollution','new_york','pm10','ny_2017_pm10.csv')
IN_PATH_NEW_YORK_PM10_2016 = os.path.join('air_pollution','new_york','pm10','ny_2016_pm10.csv')
IN_PATH_NEW_YORK_PM10_2015 = os.path.join('air_pollution','new_york','pm10','ny_2015_pm10.csv')
IN_PATH_NEW_YORK_PM10_2014 = os.path.join('air_pollution','new_york','pm10','ny_2014_pm10.csv')
IN_PATH_NEW_YORK_PM10_2013 = os.path.join('air_pollution','new_york','pm10','ny_2013_pm10.csv')
IN_PATH_NEW_YORK_PM10_2012 = os.path.join('air_pollution','new_york','pm10','ny_2012_pm10.csv')
IN_PATH_NEW_YORK_PM10_2011 = os.path.join('air_pollution','new_york','pm10','ny_2011_pm10.csv')
IN_PATH_NEW_YORK_PM10_2010 = os.path.join('air_pollution','new_york','pm10','ny_2010_pm10.csv')

IN_PATH_AUSTIN_NO2_2020 = os.path.join('air_pollution','austin','no2','austin_2020_no2.csv')
IN_PATH_AUSTIN_NO2_2019 = os.path.join('air_pollution','austin','no2','austin_2019_no2.csv')
IN_PATH_AUSTIN_NO2_2018 = os.path.join('air_pollution','austin','no2','austin_2018_no2.csv')
IN_PATH_AUSTIN_NO2_2017 = os.path.join('air_pollution','austin','no2','austin_2017_no2.csv')
IN_PATH_AUSTIN_NO2_2016 = os.path.join('air_pollution','austin','no2','austin_2016_no2.csv')
IN_PATH_AUSTIN_NO2_2015 = os.path.join('air_pollution','austin','no2','austin_2015_no2.csv')
IN_PATH_AUSTIN_NO2_2014 = os.path.join('air_pollution','austin','no2','austin_2014_no2.csv')
IN_PATH_AUSTIN_NO2_2013 = os.path.join('air_pollution','austin','no2','austin_2013_no2.csv')
IN_PATH_AUSTIN_NO2_2012 = os.path.join('air_pollution','austin','no2','austin_2012_no2.csv')
IN_PATH_AUSTIN_NO2_2011 = os.path.join('air_pollution','austin','no2','austin_2011_no2.csv')
IN_PATH_AUSTIN_NO2_2010 = os.path.join('air_pollution','austin','no2','austin_2010_no2.csv')

IN_PATH_DALLAS_NO2_2020 = os.path.join('air_pollution','dallas','no2','dallas_2020_no2.csv')
IN_PATH_DALLAS_NO2_2019 = os.path.join('air_pollution','dallas','no2','dallas_2019_no2.csv')
IN_PATH_DALLAS_NO2_2018 = os.path.join('air_pollution','dallas','no2','dallas_2018_no2.csv')
IN_PATH_DALLAS_NO2_2017 = os.path.join('air_pollution','dallas','no2','dallas_2017_no2.csv')
IN_PATH_DALLAS_NO2_2016 = os.path.join('air_pollution','dallas','no2','dallas_2016_no2.csv')
IN_PATH_DALLAS_NO2_2015 = os.path.join('air_pollution','dallas','no2','dallas_2015_no2.csv')
IN_PATH_DALLAS_NO2_2014 = os.path.join('air_pollution','dallas','no2','dallas_2014_no2.csv')
IN_PATH_DALLAS_NO2_2013 = os.path.join('air_pollution','dallas','no2','dallas_2013_no2.csv')
IN_PATH_DALLAS_NO2_2012 = os.path.join('air_pollution','dallas','no2','dallas_2012_no2.csv')
IN_PATH_DALLAS_NO2_2011 = os.path.join('air_pollution','dallas','no2','dallas_2011_no2.csv')
IN_PATH_DALLAS_NO2_2010 = os.path.join('air_pollution','dallas','no2','dallas_2010_no2.csv')

IN_PATH_HOUSTON_NO2_2020 = os.path.join('air_pollution','houston','no2','houston_2020_no2.csv')
IN_PATH_HOUSTON_NO2_2019 = os.path.join('air_pollution','houston','no2','houston_2019_no2.csv')
IN_PATH_HOUSTON_NO2_2018 = os.path.join('air_pollution','houston','no2','houston_2018_no2.csv')
IN_PATH_HOUSTON_NO2_2017 = os.path.join('air_pollution','houston','no2','houston_2017_no2.csv')
IN_PATH_HOUSTON_NO2_2016 = os.path.join('air_pollution','houston','no2','houston_2016_no2.csv')
IN_PATH_HOUSTON_NO2_2015 = os.path.join('air_pollution','houston','no2','houston_2015_no2.csv')
IN_PATH_HOUSTON_NO2_2014 = os.path.join('air_pollution','houston','no2','houston_2014_no2.csv')
IN_PATH_HOUSTON_NO2_2013 = os.path.join('air_pollution','houston','no2','houston_2013_no2.csv')
IN_PATH_HOUSTON_NO2_2012 = os.path.join('air_pollution','houston','no2','houston_2012_no2.csv')
IN_PATH_HOUSTON_NO2_2011 = os.path.join('air_pollution','houston','no2','houston_2011_no2.csv')
IN_PATH_HOUSTON_NO2_2010 = os.path.join('air_pollution','houston','no2','houston_2010_no2.csv')

IN_PATH_LOS_ANGELES_NO2_2020 = os.path.join('air_pollution','los_angeles','no2','la_2020_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2019 = os.path.join('air_pollution','los_angeles','no2','la_2019_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2018 = os.path.join('air_pollution','los_angeles','no2','la_2018_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2017 = os.path.join('air_pollution','los_angeles','no2','la_2017_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2016 = os.path.join('air_pollution','los_angeles','no2','la_2016_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2015 = os.path.join('air_pollution','los_angeles','no2','la_2015_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2014 = os.path.join('air_pollution','los_angeles','no2','la_2014_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2013 = os.path.join('air_pollution','los_angeles','no2','la_2013_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2012 = os.path.join('air_pollution','los_angeles','no2','la_2012_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2011 = os.path.join('air_pollution','los_angeles','no2','la_2011_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2010 = os.path.join('air_pollution','los_angeles','no2','la_2010_no2.csv')

IN_PATH_NEW_YORK_NO2_2020 = os.path.join('air_pollution','new_york','no2','ny_2020_no2.csv')
IN_PATH_NEW_YORK_NO2_2019 = os.path.join('air_pollution','new_york','no2','ny_2019_no2.csv')
IN_PATH_NEW_YORK_NO2_2018 = os.path.join('air_pollution','new_york','no2','ny_2018_no2.csv')
IN_PATH_NEW_YORK_NO2_2017 = os.path.join('air_pollution','new_york','no2','ny_2017_no2.csv')
IN_PATH_NEW_YORK_NO2_2016 = os.path.join('air_pollution','new_york','no2','ny_2016_no2.csv')
IN_PATH_NEW_YORK_NO2_2015 = os.path.join('air_pollution','new_york','no2','ny_2015_no2.csv')
IN_PATH_NEW_YORK_NO2_2014 = os.path.join('air_pollution','new_york','no2','ny_2014_no2.csv')
IN_PATH_NEW_YORK_NO2_2013 = os.path.join('air_pollution','new_york','no2','ny_2013_no2.csv')
IN_PATH_NEW_YORK_NO2_2012 = os.path.join('air_pollution','new_york','no2','ny_2012_no2.csv')
IN_PATH_NEW_YORK_NO2_2011 = os.path.join('air_pollution','new_york','no2','ny_2011_no2.csv')
IN_PATH_NEW_YORK_NO2_2010 = os.path.join('air_pollution','new_york','no2','ny_2010_no2.csv')

#put all air pollution read csv here
austin_pm25_2020 = pd.read_csv(IN_PATH_AUSTIN_PM25_2020)
austin_pm25_2019 = pd.read_csv(IN_PATH_AUSTIN_PM25_2019)
austin_pm25_2018 = pd.read_csv(IN_PATH_AUSTIN_PM25_2018)
austin_pm25_2017 = pd.read_csv(IN_PATH_AUSTIN_PM25_2017)
austin_pm25_2016 = pd.read_csv(IN_PATH_AUSTIN_PM25_2016)
austin_pm25_2015 = pd.read_csv(IN_PATH_AUSTIN_PM25_2015)
austin_pm25_2014 = pd.read_csv(IN_PATH_AUSTIN_PM25_2014)
austin_pm25_2013 = pd.read_csv(IN_PATH_AUSTIN_PM25_2013)
austin_pm25_2012 = pd.read_csv(IN_PATH_AUSTIN_PM25_2012)
austin_pm25_2011 = pd.read_csv(IN_PATH_AUSTIN_PM25_2011)
austin_pm25_2010 = pd.read_csv(IN_PATH_AUSTIN_PM25_2010)

 
austin_pm10_2020 = pd.read_csv(IN_PATH_AUSTIN_PM10_2020)
austin_pm10_2019 = pd.read_csv(IN_PATH_AUSTIN_PM10_2019)
austin_pm10_2018 = pd.read_csv(IN_PATH_AUSTIN_PM10_2018)
austin_pm10_2017 = pd.read_csv(IN_PATH_AUSTIN_PM10_2017)
austin_pm10_2016 = pd.read_csv(IN_PATH_AUSTIN_PM10_2016)
austin_pm10_2015 = pd.read_csv(IN_PATH_AUSTIN_PM10_2015)
austin_pm10_2014 = pd.read_csv(IN_PATH_AUSTIN_PM10_2014)
austin_pm10_2013 = pd.read_csv(IN_PATH_AUSTIN_PM10_2013)
austin_pm10_2012 = pd.read_csv(IN_PATH_AUSTIN_PM10_2012)
austin_pm10_2011 = pd.read_csv(IN_PATH_AUSTIN_PM10_2011)
austin_pm10_2010 = pd.read_csv(IN_PATH_AUSTIN_PM10_2010)


austin_no2_2020 = pd.read_csv(IN_PATH_AUSTIN_NO2_2020)
austin_no2_2019 = pd.read_csv(IN_PATH_AUSTIN_NO2_2019)
austin_no2_2018 = pd.read_csv(IN_PATH_AUSTIN_NO2_2018)
austin_no2_2017 = pd.read_csv(IN_PATH_AUSTIN_NO2_2017)
austin_no2_2016 = pd.read_csv(IN_PATH_AUSTIN_NO2_2016)
austin_no2_2015 = pd.read_csv(IN_PATH_AUSTIN_NO2_2015)
austin_no2_2014 = pd.read_csv(IN_PATH_AUSTIN_NO2_2014)
austin_no2_2013 = pd.read_csv(IN_PATH_AUSTIN_NO2_2013)
austin_no2_2012 = pd.read_csv(IN_PATH_AUSTIN_NO2_2012)
austin_no2_2011 = pd.read_csv(IN_PATH_AUSTIN_NO2_2011)
austin_no2_2010 = pd.read_csv(IN_PATH_AUSTIN_NO2_2010)


houston_pm25_2020 = pd.read_csv(IN_PATH_HOUSTON_PM25_2020)
houston_pm25_2019 = pd.read_csv(IN_PATH_HOUSTON_PM25_2019)
houston_pm25_2018 = pd.read_csv(IN_PATH_HOUSTON_PM25_2018)
houston_pm25_2017 = pd.read_csv(IN_PATH_HOUSTON_PM25_2017)
houston_pm25_2016 = pd.read_csv(IN_PATH_HOUSTON_PM25_2016)
houston_pm25_2015 = pd.read_csv(IN_PATH_HOUSTON_PM25_2015)
houston_pm25_2014 = pd.read_csv(IN_PATH_HOUSTON_PM25_2014)
houston_pm25_2013 = pd.read_csv(IN_PATH_HOUSTON_PM25_2013)
houston_pm25_2012 = pd.read_csv(IN_PATH_HOUSTON_PM25_2012)
houston_pm25_2011 = pd.read_csv(IN_PATH_HOUSTON_PM25_2011)
houston_pm25_2010 = pd.read_csv(IN_PATH_HOUSTON_PM25_2010)


houston_pm10_2020 = pd.read_csv(IN_PATH_HOUSTON_PM10_2020)
houston_pm10_2019 = pd.read_csv(IN_PATH_HOUSTON_PM10_2019)
houston_pm10_2018 = pd.read_csv(IN_PATH_HOUSTON_PM10_2018)
houston_pm10_2017 = pd.read_csv(IN_PATH_HOUSTON_PM10_2017)
houston_pm10_2016 = pd.read_csv(IN_PATH_HOUSTON_PM10_2016)
houston_pm10_2015 = pd.read_csv(IN_PATH_HOUSTON_PM10_2015)
houston_pm10_2014 = pd.read_csv(IN_PATH_HOUSTON_PM10_2014)
houston_pm10_2013 = pd.read_csv(IN_PATH_HOUSTON_PM10_2013)
houston_pm10_2012 = pd.read_csv(IN_PATH_HOUSTON_PM10_2012)
houston_pm10_2011 = pd.read_csv(IN_PATH_HOUSTON_PM10_2011)
houston_pm10_2010 = pd.read_csv(IN_PATH_HOUSTON_PM10_2010)

houston_no2_2020 = pd.read_csv(IN_PATH_HOUSTON_NO2_2020)
houston_no2_2019 = pd.read_csv(IN_PATH_HOUSTON_NO2_2019)
houston_no2_2018 = pd.read_csv(IN_PATH_HOUSTON_NO2_2018)
houston_no2_2017 = pd.read_csv(IN_PATH_HOUSTON_NO2_2017)
houston_no2_2016 = pd.read_csv(IN_PATH_HOUSTON_NO2_2016)
houston_no2_2015 = pd.read_csv(IN_PATH_HOUSTON_NO2_2015)
houston_no2_2014 = pd.read_csv(IN_PATH_HOUSTON_NO2_2014)
houston_no2_2013 = pd.read_csv(IN_PATH_HOUSTON_NO2_2013)
houston_no2_2012 = pd.read_csv(IN_PATH_HOUSTON_NO2_2012)
houston_no2_2011 = pd.read_csv(IN_PATH_HOUSTON_NO2_2011)
houston_no2_2010 = pd.read_csv(IN_PATH_HOUSTON_NO2_2010)


dallas_pm25_2020 = pd.read_csv(IN_PATH_DALLAS_PM25_2020)
dallas_pm25_2019 = pd.read_csv(IN_PATH_DALLAS_PM25_2019)
dallas_pm25_2018 = pd.read_csv(IN_PATH_DALLAS_PM25_2018)
dallas_pm25_2017 = pd.read_csv(IN_PATH_DALLAS_PM25_2017)
dallas_pm25_2016 = pd.read_csv(IN_PATH_DALLAS_PM25_2016)
dallas_pm25_2015 = pd.read_csv(IN_PATH_DALLAS_PM25_2015)
dallas_pm25_2014 = pd.read_csv(IN_PATH_DALLAS_PM25_2014)
dallas_pm25_2013 = pd.read_csv(IN_PATH_DALLAS_PM25_2013)
dallas_pm25_2012 = pd.read_csv(IN_PATH_DALLAS_PM25_2012)
dallas_pm25_2011 = pd.read_csv(IN_PATH_DALLAS_PM25_2011)
dallas_pm25_2010 = pd.read_csv(IN_PATH_DALLAS_PM25_2010)


dallas_pm10_2020 = pd.read_csv(IN_PATH_DALLAS_PM10_2020)
dallas_pm10_2019 = pd.read_csv(IN_PATH_DALLAS_PM10_2019)
dallas_pm10_2018 = pd.read_csv(IN_PATH_DALLAS_PM10_2018)
dallas_pm10_2017 = pd.read_csv(IN_PATH_DALLAS_PM10_2017)
dallas_pm10_2016 = pd.read_csv(IN_PATH_DALLAS_PM10_2016)
dallas_pm10_2015 = pd.read_csv(IN_PATH_DALLAS_PM10_2015)
dallas_pm10_2014 = pd.read_csv(IN_PATH_DALLAS_PM10_2014)
dallas_pm10_2013 = pd.read_csv(IN_PATH_DALLAS_PM10_2013)
dallas_pm10_2012 = pd.read_csv(IN_PATH_DALLAS_PM10_2012)
dallas_pm10_2011 = pd.read_csv(IN_PATH_DALLAS_PM10_2011)
dallas_pm10_2010 = pd.read_csv(IN_PATH_DALLAS_PM10_2010)


dallas_no2_2020 = pd.read_csv(IN_PATH_DALLAS_NO2_2020)
dallas_no2_2019 = pd.read_csv(IN_PATH_DALLAS_NO2_2019)
dallas_no2_2018 = pd.read_csv(IN_PATH_DALLAS_NO2_2018)
dallas_no2_2017 = pd.read_csv(IN_PATH_DALLAS_NO2_2017)
dallas_no2_2016 = pd.read_csv(IN_PATH_DALLAS_NO2_2016)
dallas_no2_2015 = pd.read_csv(IN_PATH_DALLAS_NO2_2015)
dallas_no2_2014 = pd.read_csv(IN_PATH_DALLAS_NO2_2014)
dallas_no2_2013 = pd.read_csv(IN_PATH_DALLAS_NO2_2013)
dallas_no2_2012 = pd.read_csv(IN_PATH_DALLAS_NO2_2012)
dallas_no2_2011 = pd.read_csv(IN_PATH_DALLAS_NO2_2011)
dallas_no2_2010 = pd.read_csv(IN_PATH_DALLAS_NO2_2010)


los_angeles_pm25_2020 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2020)
los_angeles_pm25_2019 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2019)
los_angeles_pm25_2018 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2018)
los_angeles_pm25_2017 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2017)
los_angeles_pm25_2016 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2016)
los_angeles_pm25_2015 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2015)
los_angeles_pm25_2014 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2014)
los_angeles_pm25_2013 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2013)
los_angeles_pm25_2012 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2012)
los_angeles_pm25_2011 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2011)
los_angeles_pm25_2010 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2010)


los_angeles_pm10_2020 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2020)
los_angeles_pm10_2019 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2019)
los_angeles_pm10_2018 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2018)
los_angeles_pm10_2017 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2017)
los_angeles_pm10_2016 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2016)
los_angeles_pm10_2015 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2015)
los_angeles_pm10_2014 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2014)
los_angeles_pm10_2013 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2013)
los_angeles_pm10_2012 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2012)
los_angeles_pm10_2011 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2011)
los_angeles_pm10_2010 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2010)


los_angeles_no2_2020 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2020)
los_angeles_no2_2019 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2019)
los_angeles_no2_2018 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2018)
los_angeles_no2_2017 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2017)
los_angeles_no2_2016 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2016)
los_angeles_no2_2015 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2015)
los_angeles_no2_2014 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2014)
los_angeles_no2_2013 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2013)
los_angeles_no2_2012 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2012)
los_angeles_no2_2011 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2011)
los_angeles_no2_2010 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2010)


new_york_pm25_2020 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2020)
new_york_pm25_2019 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2019)
new_york_pm25_2018 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2018)
new_york_pm25_2017 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2017)
new_york_pm25_2016 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2016)
new_york_pm25_2015 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2015)
new_york_pm25_2014 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2014)
new_york_pm25_2013 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2013)
new_york_pm25_2012 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2012)
new_york_pm25_2011 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2011)
new_york_pm25_2010 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2010)


new_york_pm10_2020 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2020)
new_york_pm10_2019 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2019)
new_york_pm10_2018 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2018)
new_york_pm10_2017 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2017)
new_york_pm10_2016 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2016)
new_york_pm10_2015 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2015)
new_york_pm10_2014 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2014)
new_york_pm10_2013 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2013)
new_york_pm10_2012 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2012)
new_york_pm10_2011 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2011)
new_york_pm10_2010 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2010)

new_york_no2_2020 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2020)
new_york_no2_2019 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2019)
new_york_no2_2018 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2018)
new_york_no2_2017 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2017)
new_york_no2_2016 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2016)
new_york_no2_2015 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2015)
new_york_no2_2014 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2014)
new_york_no2_2013 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2013)
new_york_no2_2012 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2012)
new_york_no2_2011 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2011)
new_york_no2_2010 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2010)


def cleanweatherdataaustin(IN_PATH):
    weatherdata = (pd.read_csv(IN_PATH))
    weatherdata.set_index(pd.DatetimeIndex(weatherdata['DATE']),inplace=True)   
    weatherdata.drop(['DATE','STATION','NAME'],axis=1,inplace=True)
    weatherdata.fillna(0,inplace = True)
    #weatherdata['CITY']='AUSTIN'
    return weatherdata

#read from url
austin_weather = cleanweatherdataaustin(AUSTIN_WEATHER_URL)
dallas_weather = cleanweatherdataaustin(DALLAS_WEATHER_URL)
houston_weather = cleanweatherdataaustin(HOUSTON_WEATHER_URL)
los_angeles_weather = cleanweatherdataaustin(LOS_ANGELES_WEATHER_URL)
new_york_weather = cleanweatherdataaustin(NEW_YORK_WEATHER_URL)

#read from csv
# austin_weather = cleanweatherdataaustin(IN_PATH_AUSTIN_WEATHER)
# dallas_weather = cleanweatherdataaustin(IN_PATH_DALLAS_WEATHER)
# houston_weather = cleanweatherdataaustin(IN_PATH_HOUSTON_WEATHER)
# los_angeles_weather = cleanweatherdataaustin(IN_PATH_LOS_ANGELES_WEATHER)
# new_york_weather = cleanweatherdataaustin(IN_PATH_NEW_YORK_WEATHER)


def citypm25(city_pm25_data):
    city_pm25_data['Date']=pd.to_datetime(city_pm25_data['Date'])
    
    pm25stationdatemean=city_pm25_data.groupby(['Date','Site ID'])['Daily Mean PM2.5 Concentration'].mean()
    pm25datemean=pm25stationdatemean.groupby('Date').mean().to_frame()
    pm25aqistationdatemean=city_pm25_data.groupby(['Date','Site ID'])['DAILY_AQI_VALUE'].mean()
    pm25aqidatemean=pm25aqistationdatemean.groupby('Date').mean().to_frame()
    
    citypm25data=pd.merge(pm25datemean,pm25aqidatemean,how='outer', left_index=True, right_index=True)
    citypm25data.columns = ['Daily Mean PM2.5 Concentration', 'DAILY AQI VALUE PM25']
    return citypm25data

austin2020pm25 = citypm25(austin_pm25_2020)
austin2019pm25 = citypm25(austin_pm25_2019)
austin2018pm25 = citypm25(austin_pm25_2018)
austin2017pm25 = citypm25(austin_pm25_2017)
austin2016pm25 = citypm25(austin_pm25_2016)
austin2015pm25 = citypm25(austin_pm25_2015)
austin2014pm25 = citypm25(austin_pm25_2014)
austin2013pm25 = citypm25(austin_pm25_2013)
austin2012pm25 = citypm25(austin_pm25_2012)
austin2011pm25 = citypm25(austin_pm25_2011)
austin2010pm25 = citypm25(austin_pm25_2010)
frames_austin_pm25=[austin2010pm25,austin2011pm25,austin2012pm25,austin2013pm25,austin2014pm25,austin2015pm25,austin2016pm25,austin2017pm25,austin2018pm25,austin2019pm25,austin2020pm25]
austinpm25=pd.concat(frames_austin_pm25,join='outer')
# print("Austin PM2.5 2010-2020")
# print(austinpm25)


houston2020pm25 = citypm25(houston_pm25_2020)
houston2019pm25 = citypm25(houston_pm25_2019)
houston2018pm25 = citypm25(houston_pm25_2018)
houston2017pm25 = citypm25(houston_pm25_2017)
houston2016pm25 = citypm25(houston_pm25_2016)
houston2015pm25 = citypm25(houston_pm25_2015)
houston2014pm25 = citypm25(houston_pm25_2014)
houston2013pm25 = citypm25(houston_pm25_2013)
houston2012pm25 = citypm25(houston_pm25_2012)
houston2011pm25 = citypm25(houston_pm25_2011)
houston2010pm25 = citypm25(houston_pm25_2010)
frames_houston_pm25=[houston2010pm25,houston2011pm25,houston2012pm25,houston2013pm25,houston2014pm25,houston2015pm25,houston2016pm25,houston2017pm25,houston2018pm25,houston2019pm25,houston2020pm25]
houstonpm25=pd.concat(frames_houston_pm25,join='outer')
# print("Houston PM2.5 2010-2020")
# print(houstonpm25)



dallas2020pm25 = citypm25(dallas_pm25_2020)
dallas2019pm25 = citypm25(dallas_pm25_2019)
dallas2018pm25 = citypm25(dallas_pm25_2018)
dallas2017pm25 = citypm25(dallas_pm25_2017)
dallas2016pm25 = citypm25(dallas_pm25_2016)
dallas2015pm25 = citypm25(dallas_pm25_2015)
dallas2014pm25 = citypm25(dallas_pm25_2014)
dallas2013pm25 = citypm25(dallas_pm25_2013)
dallas2012pm25 = citypm25(dallas_pm25_2012)
dallas2011pm25 = citypm25(dallas_pm25_2011)
dallas2010pm25 = citypm25(dallas_pm25_2010)
frames_dallas_pm25=[dallas2010pm25,dallas2011pm25,dallas2012pm25,dallas2013pm25,dallas2014pm25,dallas2015pm25,dallas2016pm25,dallas2017pm25,dallas2018pm25,dallas2019pm25,dallas2020pm25]
dallaspm25=pd.concat(frames_dallas_pm25,join='outer')
# print("Dallas PM2.5 2010-2020")
# print(dallaspm25)


los_angeles_2020pm25 = citypm25(los_angeles_pm25_2020)
los_angeles_2019pm25 = citypm25(los_angeles_pm25_2019)
los_angeles_2018pm25 = citypm25(los_angeles_pm25_2018)
los_angeles_2017pm25 = citypm25(los_angeles_pm25_2017)
los_angeles_2016pm25 = citypm25(los_angeles_pm25_2016)
los_angeles_2015pm25 = citypm25(los_angeles_pm25_2015)
los_angeles_2014pm25 = citypm25(los_angeles_pm25_2014)
los_angeles_2013pm25 = citypm25(los_angeles_pm25_2013)
los_angeles_2012pm25 = citypm25(los_angeles_pm25_2012)
los_angeles_2011pm25 = citypm25(los_angeles_pm25_2011)
los_angeles_2010pm25 = citypm25(los_angeles_pm25_2010)
frames_los_angeles_pm25=[los_angeles_2010pm25,los_angeles_2011pm25,los_angeles_2012pm25,los_angeles_2013pm25,los_angeles_2014pm25,los_angeles_2015pm25,los_angeles_2016pm25,los_angeles_2017pm25,los_angeles_2018pm25,los_angeles_2019pm25,los_angeles_2020pm25]
los_angelespm25=pd.concat(frames_los_angeles_pm25,join='outer')
# print("Los Angeles PM2.5 2010-2020")
# print(los_angelespm25)





new_york_2020pm25 = citypm25(new_york_pm25_2020)
new_york_2019pm25 = citypm25(new_york_pm25_2019)
new_york_2018pm25 = citypm25(new_york_pm25_2018)
new_york_2017pm25 = citypm25(new_york_pm25_2017)
new_york_2016pm25 = citypm25(new_york_pm25_2016)
new_york_2015pm25 = citypm25(new_york_pm25_2015)
new_york_2014pm25 = citypm25(new_york_pm25_2014)
new_york_2013pm25 = citypm25(new_york_pm25_2013)
new_york_2012pm25 = citypm25(new_york_pm25_2012)
new_york_2011pm25 = citypm25(new_york_pm25_2011)
new_york_2010pm25 = citypm25(new_york_pm25_2010)
frames_new_york_pm25=[new_york_2010pm25,new_york_2011pm25,new_york_2012pm25,new_york_2013pm25,new_york_2014pm25,new_york_2015pm25,new_york_2016pm25,new_york_2017pm25,new_york_2018pm25,new_york_2019pm25,new_york_2020pm25]
new_yorkpm25=pd.concat(frames_new_york_pm25,join='outer')
# print("New York PM2.5 2010-2020")
# print(new_yorkpm25)



def citypm10(city_pm10_data):
    city_pm10_data['Date']=pd.to_datetime(city_pm10_data['Date'])
    
    pm10stationdatemean=city_pm10_data.groupby(['Date','Site ID'])['Daily Mean PM10 Concentration'].mean()
    pm10datemean=pm10stationdatemean.groupby('Date').mean().to_frame()
    
    pm10aqistationdatemean=city_pm10_data.groupby(['Date','Site ID'])['DAILY_AQI_VALUE'].mean()
    pm10aqidatemean=pm10aqistationdatemean.groupby('Date').mean().to_frame()
    
    citypm10data=pd.merge(pm10datemean,pm10aqidatemean,how='outer', left_index=True, right_index=True)
    citypm10data.columns = ['Daily Mean PM10 Concentration', 'DAILY AQI VALUE PM10']
    return citypm10data


austin2020pm10 = citypm10(austin_pm10_2020)
austin2019pm10 = citypm10(austin_pm10_2019)
austin2018pm10 = citypm10(austin_pm10_2018)
austin2017pm10 = citypm10(austin_pm10_2017)
austin2016pm10 = citypm10(austin_pm10_2016)
austin2015pm10 = citypm10(austin_pm10_2015)
austin2014pm10 = citypm10(austin_pm10_2014)
austin2013pm10 = citypm10(austin_pm10_2013)
austin2012pm10 = citypm10(austin_pm10_2012)
austin2011pm10 = citypm10(austin_pm10_2011)
austin2010pm10 = citypm10(austin_pm10_2010)
frames_austin_pm10=[austin2010pm10,austin2011pm10,austin2012pm10,austin2013pm10,austin2014pm10,austin2015pm10,austin2016pm10,austin2017pm10,austin2018pm10,austin2019pm10,austin2020pm10]
austinpm10=pd.concat(frames_austin_pm10,join='outer')
# print("Austin PM10 2010-2020")
# print(austinpm10)



houston2020pm10 = citypm10(houston_pm10_2020)
houston2019pm10 = citypm10(houston_pm10_2019)
houston2018pm10 = citypm10(houston_pm10_2018)
houston2017pm10 = citypm10(houston_pm10_2017)
houston2016pm10 = citypm10(houston_pm10_2016)
houston2015pm10 = citypm10(houston_pm10_2015)
houston2014pm10 = citypm10(houston_pm10_2014)
houston2013pm10 = citypm10(houston_pm10_2013)
houston2012pm10 = citypm10(houston_pm10_2012)
houston2011pm10 = citypm10(houston_pm10_2011)
houston2010pm10 = citypm10(houston_pm10_2010)
frames_houston_pm10=[houston2010pm10,houston2011pm10,houston2012pm10,houston2013pm10,houston2014pm10,houston2015pm10,houston2016pm10,houston2017pm10,houston2018pm10,houston2019pm10,houston2020pm10]
houstonpm10=pd.concat(frames_houston_pm10,join='outer')
# print("Houston PM10 2010-2020")
# print(houstonpm10)


dallas2020pm10 = citypm10(dallas_pm10_2020)
dallas2019pm10 = citypm10(dallas_pm10_2019)
dallas2018pm10 = citypm10(dallas_pm10_2018)
dallas2017pm10 = citypm10(dallas_pm10_2017)
dallas2016pm10 = citypm10(dallas_pm10_2016)
dallas2015pm10 = citypm10(dallas_pm10_2015)
dallas2014pm10 = citypm10(dallas_pm10_2014)
dallas2013pm10 = citypm10(dallas_pm10_2013)
dallas2012pm10 = citypm10(dallas_pm10_2012)
dallas2011pm10 = citypm10(dallas_pm10_2011)
dallas2010pm10 = citypm10(dallas_pm10_2010)
frames_dallas_pm10=[dallas2010pm10,dallas2011pm10,dallas2012pm10,dallas2013pm10,dallas2014pm10,dallas2015pm10,dallas2016pm10,dallas2017pm10,dallas2018pm10,dallas2019pm10,dallas2020pm10]
dallaspm10=pd.concat(frames_dallas_pm10,join='outer')
# print("Dallas PM10 2010-2020")
# print(dallaspm10)




los_angeles_2020pm10 = citypm10(los_angeles_pm10_2020)
los_angeles_2019pm10 = citypm10(los_angeles_pm10_2019)
los_angeles_2018pm10 = citypm10(los_angeles_pm10_2018)
los_angeles_2017pm10 = citypm10(los_angeles_pm10_2017)
los_angeles_2016pm10 = citypm10(los_angeles_pm10_2016)
los_angeles_2015pm10 = citypm10(los_angeles_pm10_2015)
los_angeles_2014pm10 = citypm10(los_angeles_pm10_2014)
los_angeles_2013pm10 = citypm10(los_angeles_pm10_2013)
los_angeles_2012pm10 = citypm10(los_angeles_pm10_2012)
los_angeles_2011pm10 = citypm10(los_angeles_pm10_2011)
los_angeles_2010pm10 = citypm10(los_angeles_pm10_2010)
frames_los_angeles_pm10=[los_angeles_2010pm10,los_angeles_2011pm10,los_angeles_2012pm10,los_angeles_2013pm10,los_angeles_2014pm10,los_angeles_2015pm10,los_angeles_2016pm10,los_angeles_2017pm10,los_angeles_2018pm10,los_angeles_2019pm10,los_angeles_2020pm10]
los_angelespm10=pd.concat(frames_los_angeles_pm10,join='outer')
# print("Los Angeles PM10 2010-2020")
# print(los_angelespm10)




new_york_2020pm10 = citypm10(new_york_pm10_2020)
new_york_2019pm10 = citypm10(new_york_pm10_2019)
new_york_2018pm10 = citypm10(new_york_pm10_2018)
new_york_2017pm10 = citypm10(new_york_pm10_2017)
new_york_2016pm10 = citypm10(new_york_pm10_2016)
new_york_2015pm10 = citypm10(new_york_pm10_2015)
new_york_2014pm10 = citypm10(new_york_pm10_2014)
new_york_2013pm10 = citypm10(new_york_pm10_2013)
new_york_2012pm10 = citypm10(new_york_pm10_2012)
new_york_2011pm10 = citypm10(new_york_pm10_2011)
new_york_2010pm10 = citypm10(new_york_pm10_2010)
frames_new_york_pm10=[new_york_2010pm10,new_york_2011pm10,new_york_2012pm10,new_york_2013pm10,new_york_2014pm10,new_york_2015pm10,new_york_2016pm10,new_york_2017pm10,new_york_2018pm10,new_york_2019pm10,new_york_2020pm10]
new_yorkpm10=pd.concat(frames_new_york_pm10,join='outer')
# print("New York PM10 2010-2020")
# print(new_yorkpm10)




def cityno2(city_no2_data):
    city_no2_data['Date']=pd.to_datetime(city_no2_data['Date'])
    
    no2stationdatemean=city_no2_data.groupby(['Date','Site ID'])['Daily Max 1-hour NO2 Concentration'].mean()
    no2datemean=no2stationdatemean.groupby('Date').mean().to_frame()
    
    no2aqistationdatemean=city_no2_data.groupby(['Date','Site ID'])['DAILY_AQI_VALUE'].mean()
    no2aqidatemean=no2aqistationdatemean.groupby('Date').mean().to_frame()
    
    cityno2data=pd.merge(no2datemean,no2aqidatemean,how='outer', left_index=True, right_index=True)
    cityno2data.columns = ['Daily Mean NO2 Concentration', 'DAILY AQI VALUE NO2']
    return cityno2data

austin2020no2 = cityno2(austin_no2_2020)
austin2019no2 = cityno2(austin_no2_2019)
austin2018no2 = cityno2(austin_no2_2018)
austin2017no2 = cityno2(austin_no2_2017)
austin2016no2 = cityno2(austin_no2_2016)
austin2015no2 = cityno2(austin_no2_2015)
austin2014no2 = cityno2(austin_no2_2014)
austin2013no2 = cityno2(austin_no2_2013)
austin2012no2 = cityno2(austin_no2_2012)
austin2011no2 = cityno2(austin_no2_2011)
austin2010no2 = cityno2(austin_no2_2010)
frames_austin_no2=[austin2010no2,austin2011no2,austin2012no2,austin2013no2,austin2014no2,austin2015no2,austin2016no2,austin2017no2,austin2018no2,austin2019no2,austin2020no2]
austinno2=pd.concat(frames_austin_no2,join='outer')
# print("Austin NO2 2010-2020")
# print(austinno2)

dallas2020no2 = cityno2(dallas_no2_2020)
dallas2019no2 = cityno2(dallas_no2_2019)
dallas2018no2 = cityno2(dallas_no2_2018)
dallas2017no2 = cityno2(dallas_no2_2017)
dallas2016no2 = cityno2(dallas_no2_2016)
dallas2015no2 = cityno2(dallas_no2_2015)
dallas2014no2 = cityno2(dallas_no2_2014)
dallas2013no2 = cityno2(dallas_no2_2013)
dallas2012no2 = cityno2(dallas_no2_2012)
dallas2011no2 = cityno2(dallas_no2_2011)
dallas2010no2 = cityno2(dallas_no2_2010)
frames_dallasno2=[dallas2010no2,dallas2011no2,dallas2012no2,dallas2013no2,dallas2014no2,dallas2015no2,dallas2016no2,dallas2017no2,dallas2018no2,dallas2019no2,dallas2020no2]
dallasno2=pd.concat(frames_dallasno2,join='outer')
# print("Dallas NO2 2010-2020")
# print(dallasno2)

houston2020no2 = cityno2(houston_no2_2020)
houston2019no2 = cityno2(houston_no2_2019)
houston2018no2 = cityno2(houston_no2_2018)
houston2017no2 = cityno2(houston_no2_2017)
houston2016no2 = cityno2(houston_no2_2016)
houston2015no2 = cityno2(houston_no2_2015)
houston2014no2 = cityno2(houston_no2_2014)
houston2013no2 = cityno2(houston_no2_2013)
houston2012no2 = cityno2(houston_no2_2012)
houston2011no2 = cityno2(houston_no2_2011)
houston2010no2 = cityno2(houston_no2_2010)
frames_houstonno2=[houston2010no2,houston2011no2,houston2012no2,houston2013no2,houston2014no2,houston2015no2,houston2016no2,houston2017no2,houston2018no2,houston2019no2,houston2020no2]
houstonno2=pd.concat(frames_houstonno2,join='outer')
# print("Houston NO2 2010-2020")
# print(houstonno2)

los_angeles_2020no2 = cityno2(los_angeles_no2_2020)
los_angeles_2019no2 = cityno2(los_angeles_no2_2019)
los_angeles_2018no2 = cityno2(los_angeles_no2_2018)
los_angeles_2017no2 = cityno2(los_angeles_no2_2017)
los_angeles_2016no2 = cityno2(los_angeles_no2_2016)
los_angeles_2015no2 = cityno2(los_angeles_no2_2015)
los_angeles_2014no2 = cityno2(los_angeles_no2_2014)
los_angeles_2013no2 = cityno2(los_angeles_no2_2013)
los_angeles_2012no2 = cityno2(los_angeles_no2_2012)
los_angeles_2011no2 = cityno2(los_angeles_no2_2011)
los_angeles_2010no2 = cityno2(los_angeles_no2_2010)
frames_los_angeles_no2=[los_angeles_2010no2,los_angeles_2011no2,los_angeles_2012no2,los_angeles_2013no2,los_angeles_2014no2,los_angeles_2015no2,los_angeles_2016no2,los_angeles_2017no2,los_angeles_2018no2,los_angeles_2019no2,los_angeles_2020no2]
los_angelesno2=pd.concat(frames_los_angeles_no2,join='outer')
#print("Los Angeles NO2 2010-2020")
#print(los_angelesno2)


new_york_2020no2 = cityno2(new_york_no2_2020)
new_york_2019no2 = cityno2(new_york_no2_2019)
new_york_2018no2 = cityno2(new_york_no2_2018)
new_york_2017no2 = cityno2(new_york_no2_2017)
new_york_2016no2 = cityno2(new_york_no2_2016)
new_york_2015no2 = cityno2(new_york_no2_2015)
new_york_2014no2 = cityno2(new_york_no2_2014)
new_york_2013no2 = cityno2(new_york_no2_2013)
new_york_2012no2 = cityno2(new_york_no2_2012)
new_york_2011no2 = cityno2(new_york_no2_2011)
new_york_2010no2 = cityno2(new_york_no2_2010)
frames_new_york_no2=[new_york_2010no2,new_york_2011no2,new_york_2012no2,new_york_2013no2,new_york_2014no2,new_york_2015no2,new_york_2016no2,new_york_2017no2,new_york_2018no2,new_york_2019no2,new_york_2020no2]
new_yorkno2=pd.concat(frames_new_york_no2,join='outer')
#print("New York NO2 2010-2020")
#print(new_yorkno2)


def citymergeairpollution(pm25data, pm10data, no2data):
    cityairpollution = pd.merge(pm25data, pm10data, how='outer', left_index=True, right_index=True)
    cityairpollution = pd.merge(cityairpollution, no2data, how='outer', left_index=True, right_index=True)
    return cityairpollution

austin_air_pollution = citymergeairpollution(austinpm25, austinpm10, austinno2)
dallas_air_pollution = citymergeairpollution(dallaspm25, dallaspm10, dallasno2)
houston_air_pollution = citymergeairpollution(houstonpm25, houstonpm10, houstonno2)
los_angeles_air_pollution = citymergeairpollution(los_angelespm25, los_angelespm10, los_angelesno2)
new_york_air_pollution = citymergeairpollution(new_yorkpm25, new_yorkpm10, new_yorkno2)


def citymergeweatherpollution(city_weather_data, city_air_pollution_data):
    city_merge = pd.merge(city_weather_data, city_air_pollution_data, how = 'outer', left_index = True, right_index= True )
    return city_merge

austin = citymergeweatherpollution(austin_weather, austin_air_pollution)
dallas = citymergeweatherpollution(dallas_weather, dallas_air_pollution)
houston = citymergeweatherpollution(houston_weather, houston_air_pollution)
los_angeles = citymergeweatherpollution(los_angeles_weather, los_angeles_air_pollution)
new_york = citymergeweatherpollution(new_york_weather, new_york_air_pollution)

##这后面的注释就不用看了，一些小草稿，我要是还要改的话还需要用到一下，所以暂时不删,以上城市名字是对应的城市的数据（其中包括天气数据和污染数据）我将天气数据和污染数据一一整合了，所以目前只有城市是分开的,共五个dataframe


# austin['CITY'] = 'AUSTIN'
# dallas['CITY'] = 'DALLAS'
# houston['CITY'] = 'HOUSTON'
# los_angeles['CITY'] = 'LOS_ANGELES'
# new_york['CITY'] = 'NEW_YORK'
# city_frame = [austin, dallas, houston, los_angeles, new_york]
# data_five_cities = pd.concat(city_frame,join='outer')
# print("laji")
# print(data_five_cities.info())
# print(data_five_cities.iloc[-1])


# print(austin_air_pollution.head())
# print('haha')
# print(len(austin_air_pollution))
# print(len(austin_weather))
# print(len(dallas_weather))
# print(len(houston_weather))
# print(len(los_angeles_weather))
# print(len(new_york_weather))
# print(len(austin))
# print(austin_air_pollution.iloc[-1])
# print(austin.iloc[-1])

# dicttemp = dict(tuple(austin_pm25_2020.groupby(austin_pm25_2020['Site Name'])))
# austin_2020_station1 = pd.DataFrame.from_dict(dicttemp['Austin North Hills Drive'])
# austin_2020_station1.set_index(pd.DatetimeIndex(austin_2020_station1['Date']), inplace=True)
# austin_2020_station1_aqi=austin_2020_station1.loc[austin_2020_station1['POC']==3,'DAILY_AQI_VALUE'].to_frame().rename(columns={'DAILY_AQI_VALUE':'AQI1'})
# print(austin_2020_station1_aqi)
# austin_2020_station2 = pd.DataFrame.from_dict(dicttemp['Austin Webberville Rd'])
# austin_2020_station2.set_index(pd.DatetimeIndex(austin_2020_station2['Date']), inplace=True)
# austin_2020_station2_aqi=austin_2020_station2.loc[austin_2020_station2['POC']==3,'DAILY_AQI_VALUE'].to_frame().rename(columns={'DAILY_AQI_VALUE':'AQI2'})
# print(austin_2020_station2_aqi)
# austin_2020_station3 = pd.DataFrame.from_dict(dicttemp['Austin North Interstate 35'])
# austin_2020_station3.set_index(pd.DatetimeIndex(austin_2020_station3['Date']), inplace=True)
# austin_2020_station3_aqi=austin_2020_station3.loc[austin_2020_station3['POC']==2,'DAILY_AQI_VALUE'].to_frame().rename(columns={'DAILY_AQI_VALUE':'AQI3'})
# print(austin_2020_station3_aqi)
# austin_2020_merge=pd.merge(austin_2020_station3_aqi, austin_2020_station2_aqi, how='outer', left_index=True, right_index=True)
# austin_2020_merge=pd.merge(austin_2020_merge,austin_2020_station1_aqi,how='outer', left_index=True, right_index=True)
# means = austin_2020_merge.mean(axis=1,skipna=True)
# print(means)

