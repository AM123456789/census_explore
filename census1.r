library(tidycensus)
library(tidyverse)

census_api_key("6f46a7532e0317f2318ad51b2aa17a2643edcc72")

age20 <- get_decennial(geography = "state", 
                       variables = "P13_001N", 
                       year = 2020,
                       sumfile = "dhc")

age20 %>%
  ggplot(aes(x = value, y = reorder(NAME, value))) + 
  geom_point()

v17 <- load_variables(2017, "acs5", cache = TRUE)

View(v17)

vt <- get_acs(geography = "county", 
              variables = c(medincome = "B19013_001"), 
              state = "VT", 
              year = 2021)

vt

vt %>%
  mutate(NAME = gsub(" County, Vermont", "", NAME)) %>%
  ggplot(aes(x = estimate, y = reorder(NAME, estimate))) +
  geom_errorbarh(aes(xmin = estimate - moe, xmax = estimate + moe)) +
  geom_point(color = "red", size = 3) +
  labs(title = "Household income by county in Vermont",
       subtitle = "2017-2021 American Community Survey",
       y = "",
       x = "ACS estimate (bars represent margin of error)")

