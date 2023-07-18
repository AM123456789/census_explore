
library(tidycensus)
library(tidyverse)
library(ggplot2)

census_api_key("API_KEY", install = TRUE, overwrite=TRUE)


#v17 <- load_variables(2021, "acs1", cache = TRUE)


#2017-2021 State Populations
StatePopulation <- get_acs(geography ="state",variables = "B01001A_012")
View(StatePopulation)
#Plot
ggplot (StatePopulation, aes(x = estimate, y = NAME)) + geom_point()

