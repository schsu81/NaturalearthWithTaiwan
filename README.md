# Natural Earth With MOI,Taiwan Boundary
資料集以內政部資料開放平臺縣市界取代原Natural Earth 10m邊界。

![OriandTW](https://github.com/schsu81/NaturalearthWithTaiwan/blob/f93c5e8e8632f5479b28b7229dbfcdd9ad08da97/OriAndTW.png)

## Requires

 * cartopy 

## Instruction
 Install:
 
    python3 INSTALL.py 
    
 Unistall:

    python3 INSTALL.py uninstall
    
 Only work with resolution='10m'. Such as:
 
    axes.coastlines(resolution='10m')
    cartopy.feature.NaturalEarthFeature('physical', 'land', '10m')
    cartopy.feature.NaturalEarthFeature('physical', 'ocean', '10m')
    cartopy.feature.NaturalEarthFeature('physical', 'coastline', '10m')
    
The follows also work when resolution='10m':
    
    cartopy.feature.LAND
    cartopy.feature.OCEAN
    cartopy.feature.COASTLINE    

## Reference dataset
 * 內政部直轄市、縣市界線：https://data.gov.tw/dataset/7442
 * 內政部鄉鎮市區界線：https://data.gov.tw/dataset/7441
