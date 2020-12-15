# To convert the level2 rawdata ncdf file into the tiff file of quarter degree
# Loading required packages
library(ncdf4)
# library(akima)
# require(AtmRay)
require(raster)
# require(rgdal)
# library(rasterVis)
# library(scales)

# Read input from shell
args = commandArgs(trailingOnly=TRUE)
raw.dir <- args[1]
out.dir <- args[2]
year = args[3]
day_of_year <- args[4]

in.files <- Sys.glob(file.path(raw.dir,sprintf("*/*/*/*/%s/%s/*.nc4", year,day_of_year)))
  for (in.file  in in.files) {
  
  parameters = c('SoilMoi0_10cm_inst')#, 'SoilMoi10_40cm_inst', 'SoilMoi40_100cm_inst','SoilMoi100_200cm_inst',
                 #'SoilTMP0_10cm_inst','SoilTMP10_40cm_inst','SoilTMP40_100cm_inst','SoilTMP100_200cm_inst')
  for (parameter in parameters) {
    product = substr(parameter, 1, 7)
    if(product =="SoilMoi"){
      depth = gsub("SoilMoi", "", parameter)
      product = "sm"
    }else if (product == "SoilTMP"){
      depth = gsub("SoilTMP", "", parameter)
      product = "temp"
    }
    in.bn <- basename(in.file)
    yyyymmdd.hhmm.vvv <- substr(in.bn, 19, 35)
    yyyymmdd.hhmm.vvv <- gsub('[.]', '_', yyyymmdd.hhmm.vvv)
    out.bn <- sprintf('%s.tif', yyyymmdd.hhmm.vvv)
    
    prod.dir = sprintf("%s/%s/%s", out.dir, product,depth)
    dir.create(prod.dir,recursive = T)
    out.file = file.path(prod.dir, out.bn)
    
    if(!file.exists(out.file)){
      
      
      in.ras = raster(in.file, varname = parameter)
      writeRaster(in.ras, out.file)
    }
  }
}
