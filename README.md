# pandas-proje

This project is to make a cleaner, more legible dataframe from the considered worldwide shark attacks from the 1960 to today.

Three hypotheses were created to check to credibility of the data given. These were:
- Hypothesis 1 : In Australia, men are more likely to be attacked by a shark while surfing then woman.
- Hypothesis 2: In the USA, the attacks are usually unprovoked by humans.
- Hypothesis 3: Hawaii is the area in the US where most shark attacks occur

To clean this data, the following methods have been used:
- Dropping of NAN´s for useless columns
- REGEX in order to regroup Activity and Species column.
- Creation of new dataframes with the necessary information to be able to check the hypotheses
- Turning NAN´s that were in needed columns to unknowns, to be able to use the data
- Changing numeric, but considered "object" data in to its corresponding INT64/Float64 format.
- Dropping of unecessary columns where data was useless or did not add value to the dataframe.

Libraries used:
-Pandas
-Seaborn
-REDEX
-Numpy
-SRC
