install.packages("tidycensus")
install.packages("tidyverse")
install.packages("ggplot2")


library(tidycensus)
library(tidyverse)
library(ggplot2)

census_api_key("6f46a7532e0317f2318ad51b2aa17a2643edcc72", install = TRUE, overwrite=TRUE)


#v17 <- load_variables(2021, "acs1", cache = TRUE)


#2017-2021 State Populations
Statei <- get_acs(geography ="state",variables = "B01001A_012")
View(Statei)
#Plot
ggplot (Statei, aes(x = estimate, y = NAME)) + geom_point()

