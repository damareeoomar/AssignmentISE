Introduction A very brief overview of the assignment that I have
completed consist of 2 programs. One displays an image of the season
depending on the use input whereas the other program will display
messages on the screen depending on the user input or input from a file
to help the user figure out if the temperature is high or low and more.

Module description Original codes (before refactoring) For the first
program -the season program (country name and year.py) -, I have
designed and implemented 3 modules, namely Name_Month() ,season1() and
image()

Modularity (i)country_name_and_year.py Note:  1. country name and
year.py or country_name_and_year.py will need the following in the same
folder to work properly. autumn.png birak.png bunuru.png dijiba.png
djeran.png inter-monsoon.png kambarang.png makuru.png monsoon.png
northeast monsoon.png southeast monsoon.png spring.png summer.png
winter.png wrong.png

To run country_name_and_year.py, the user will have to follow the
prompts on the screen as shown below. The user has to enter the name of
the country and the number of the month in order to determine the season
If the country name is wrong or not present in our database and the
month number is right, the user will be prompted an error message. If
the country name is right but the month number is wrong, the program
will prompt the user till he enters a correct month number.

Then, as output, the picture of the season and the country name along
with the name of the season will appear as title of the picture.

Modularity concept review(before refactoring the code) ItemChecklist
question related to modularityYes/No How many times does it happens if
no and applicableDescription of the issue if No is the answer?1Is the
number of global variables zero?No 2 global variables Can cause
ambiguity and might become difficult to bring change to the program
/high coupling 2Do all our functions take parameters which do not acts
as control flags?No 3 times Causes low cohesion and high coupling3Are
all functions performing only a single distinct task? No 1 timeCause low
cohesion4are we reusing our function to do the same task? No nilDoing
redundancy 5Is there no overlapping of our code in our
modules/functions/programs?No 2Doing redundancy6Are we using all part of
our code?No1Causing ambiguity and decreasing readability. Might cause an
issue while debugging and refactoring.

Modularity concept review(After refactoring the code) ItemChecklist
question related to modularityYes/No How many times does it happens if
no and applicableDescription of the issue if No is the answer?1Is the
number of global variables zero?No 2 global variables Can cause
ambiguity and might become difficult to bring change to the program
/high coupling 2Do all our functions take parameters which do not acts
as control flags?No 7 times Causes low cohesion and high coupling3Are
all functions performing only a single distinct task? Yes nilCause low
cohesion4are we reusing our function to do the same task? No Doing
redundancy 5Is there no overlapping of our code in our
modules/functions/programs?Yes nilDoing redundancy6Are we using all part
of our code?yesnilCausing ambiguity and decreasing readability. Might
cause an issue while debugging and refactoring. Various places we have
decreased the level of redundancy, but it has increased the level of
coupling.

Black-box testing (i)country_name_and_year.py Assumption: Name_month()
module prevent any input of number of month to be out of the range of 1
and 12 Equivalence Partitioning mauritius()Category (month)Test Data
Results(season)10\< month\< 13 or 1\<= month \<= 4month = 3season =
\"Summer\"month = 5 month = 5 season = \"Autumn\"5 \< month \< 10 month
= 7season = \"Winter\"month = 10 month = 10 season = \"Spring\"
Equivalence Partitioning australia1()Category (month)Test Data
Results(season)month = 12 or 1\<= month \<= 2month = 12season =
\"Summer\"2\< month \< 6month = 5 season = \"Autumn\"5 \< month \<
9month = 7season = \"Winter\"8\< month \< 12month = 10 season =
\"Spring\" Equivalence Partitioning australia2()Category (month)Test
Data Results(season)month = 12 or month = 1 month = 1season
=\"Birak\"month = 2 or month = 3 month =2 season = \"Bunuru\"month = 4
or month = 5 month =4season = \"Djeran\"month = 6 or month = 7 month
=6season = \"Makuru\"month = 8 or month = 9 month =8season =
\"Djilba\"month = 10 or month = 11 month = 10season = \"Kambarang\"
Equivalence Partitioning spain_japan()Category (month)Test Data
Results(season)month = 12 or 1\<= month \<= 2month = 12season =
\"Winter\"2\< month \< 6month = 5 season = \"Spring\"5 \< month \<
9month = 7season = \"Summer\"8\< month \< 12month = 10 season =
\"Autumn\" Equivalence Partitioning malaysia_sri_lanka()Category
(month)Test Data Results(season)month = 12 or 1\<= month \<= 2month =
1season = \"Northeast Monsoon\"month = 3 or month =4 month = 3season
=\"Inter-monsoon\"5\<= month \<= 9month = 8season = \"Southeast
Monsoon\"month = 10 or month = 11month =10season =\"Inter-monsoon\"
Boundary value analysis malaysia_sri_lanka()boundaryvalue(month)results
(season)Boundary between \"Northeast Monsoon\" and
\"Inter-monsoon\"month = 2season = \"Northeast Monsoon\"month = 3season
= \"Inter-monsoon\"Boundary between \"Inter-monsoon\" and \"Southeast
Monsoon\"month = 4season = \"Inter-monsoon\"month = 5season= \"Southeast
Monsoon\"Boundary between \"Inter-monsoon\" and \"Southeast
Monsoon\"month = 9season= \"Southeast Monsoon\"month = 10season =
\"Inter-monsoon\"Boundary between \"Northeast Monsoon\" and
\"Inter-monsoon\"month = 11season = \"Inter-monsoon\"month = 12 season =
\"Northeast Monsoon\" (ii) mean_temperature.py Assumption: it is very
complicated to design black-box testing modules for this program and
white-box testing will be better

White-box testing (i)country_name_and_year.py Name_Month()Path Test
DataExpected Results name of country is inserted and loop is not entered
because input of date is correct line = \"Damaree\\n12\\n\"\"Enter the
country name: Enter the number of the month of the year:(1-12) DAMAREE
12\\n\"name of country is inserted and loop is entered because of wrong
input of date line = \"Dubai\\n4419\\n2\"\"Enter the country name: Enter
the number of the month of the year:(1-12) Wrong input of month number.
Try again (1 -12) DUBAI 2\\n\"

location()PathTest Data (country, month)Expected Results country is
Australia and passes through the first option of the loop country
=\"AUSTRALIA\",month = 1 , line =\"1/n\"season =\"Summer\"country is
Australia and passes through the second option of the loop country
=\"AUSTRALIA\",month = 1, line =\"2/n\"season = \"Birak\"country is
Mauritius country =\"MAURITIUS\",month = 1season =\"Summer\"country is
Spaincountry =\"SPAIN\",month = 1season = \"Winter\"country is
Japancountry = \"JAPAN\", month =3season = \"Spring\"country is sri
lankacountry = \"SRI LANKA\", month = 5season = \"Southeast
Monsoon\"country is Malaysia country = \"MALAYSIA\", month =11season
=\"Inter-monsoon\"country input is wrong country = \"ASD\",month =
4season =\"Wrong\" (ii) mean_temperature.py

choice()Category (input1,list1,error,message)Test Data Results(month
number and country name)input is in list input1 = 1 , list1 =
\[1,2,34\], error = \"error\", message = \"not in list\"input1 = 1input
is not in list input1 = 5 , list1 = \[1,2,34\], error = \"error\",
message = \"not in list\"\"error/nnot in list\" Detector()Category
(location,time,temp)Test Data Resultslocation is Perth, time morning and
temp equal to average location = \'perth\', time = \"M\", temp =
18.2\"\"The temperature is equal to the average.\\n\"location is Perth,
time morning and temp above average but less than 5.0 c
differencelocation = \'perth\', time = \"M\", temp = 20.0\"The
temperature is greater than the average this morning in
Perth.\\n\\n\"location is Perth, time morning and temp above average but
greater than 5.0 difference but less than maximum temperature location =
\'perth\', time = \"M\", temp = 28.0The temperature is greater than the
average this morning in Perth.\\n\\nThe difference from the mean
temperature is more than 5.0 C\\n\\n\\nlocation is Perth, time morning
and temp above average but greater than 5.0 difference but more than
maximum temperature location = \'perth\', time = \"M\", temp = 47.0\"The
temperature is greater than the average this morning in Perth.\\n\\nThe
difference between the mean is greater than 5.0 C and the temperature is
above the maxmimum temperature in this area.\\n\\n\\n\"location is
Perth, time morning and temp below average but less than 5.0 c
differencelocation = \'perth\', time = \"M\", temp = 16.0\"The
temperature is below average this morning in Perth.\\n\\n\"location is
Perth, time morning and temp below average but greater than 5.0
difference but greater than minimum temperature location = \'perth\',
time = \"M\", temp = 10.0\"The temperature is below average this morning
in Perth.\\n\\nThe difference from the mean temperature is above 5.0
C\\n\\n\\n\"location is Perth, time morning and temp below average but
greater than 5.0 difference but lower than minimum temperature location
= \'perth\', time = \"M\", temp = 0.0\"The temperature is below average
this morning in Perth.\\n\\nThe difference between the mean is greater
than 5.0 C and the temperature is below the minimum temperature in this
area.\\n\\n\\n\"location is Perth, time evening and temp equal to
average location = \'perth\', time = \"A\", temp = 23.0\"The temperature
is equal to the average.\\n\"location is Perth, time evening and temp
above average but less than 5.0 c differencelocation = \'perth\', time =
\"A\", temp = 25.0\"The temperature is greater than the average this
afternoon in Perth.\\n\\n\"location is Perth, time evening and temp
above average but greater than 5.0 difference but greater than maximum
temperature location = \'perth\', time = \"A\", temp = 29.0\"The
temperature is greater than the average this afternoon in
Perth.\\n\\nThe difference from the mean temperature is more than 5.0
C\\n\\n\\n\"location is Perth, time evening and temp above average but
greater than 5.0 difference but more than maximum temperature location =
\'perth\', time = \"A\", temp = 48.0\"The temperature is greater than
the average this afternoon in Perth.\\n\\nThe difference between the
mean is greater than 5.0 C and the temperature is above the maxmimum
temperature in this area.\\n\\n\\n\"location is Perth, time evening and
temp below average but less than 5.0 c differencelocation = \'perth\',
time = \"A\", temp = 22.0\"The temperature is below average this
afternoon in Perth.\\n\\n\"location is Perth, time evening and temp
below average but greater than 5.0 difference but higher than minimum
temperature location = \'perth\', time = \"A\", temp = 17.0\"The
temperature is below average this afternoon in Perth.\\n\\nThe
difference from the mean temperature is above 5.0 C\\n\\n\\n\"location
is Perth, time evening and temp below average but greater than 5.0
difference but lower than minimum temperature location = \'perth\', time
= \"A\", temp = -1\"The temperature is below average this afternoon in
Perth.\\n\\nThe difference between the mean is greater than 5.0 C and
the temperature is below the minimum temperature in this
area.\\n\\n\\n\"location is Adelaide, time morning and temp equal to
average location = \'adelaide\', time = \"M\", temp = 16.5\"\"The
temperature is equal to the average.\\n\"location is Adelaide, time
morning and temp above average but less than 5.0 c differencelocation =
\'adelaide\', time = \"M\", temp = 18.0\"The temperature is greater than
the average this morning in Adelaide.\\n\\n\"location is Adelaide, time
morning and temp above average but greater than 5.0 difference but less
than maximum temperature location = \'adelaide\', time = \"M\", temp =
22.0The temperature is greater than the average this morning in
Adelaide.\\n\\nThe difference from the mean temperature is more than 5.0
C\\n\\n\\nlocation is Adelaide, time morning and temp above average but
greater than 5.0 difference but more than maximum temperature location =
\'adelaide\', time = \"M\", temp = 50.0\"The temperature is greater than
the average this morning in Adelaide.\\n\\nThe difference between the
mean is greater than 5.0 C and the temperature is above the maxmimum
temperature in this area.\\n\\n\\n\"location is Adelaide, time morning
and temp below average but less than 5.0 c differencelocation =
\'adelaide\', time = \"M\", temp = 16.0\"The temperature is below
average this morning in Adelaide.\\n\\n\"location is Adelaide, time
morning and temp below average but greater than 5.0 difference but
higher than minimum temperature location = \'adelaide\', time = \"M\",
temp = 3.0\"The temperature is below average this morning in
Adelaide.\\n\\nThe difference from the mean temperature is above 5.0
C\\n\\n\\n\"location is Adelaide, time morning and temp below average
but greater than 5.0 difference but lower than minimum temperature
location = \'adelaide\', time = \"M\", temp = -2.0\"The temperature is
below average this morning in Adelaide.\\n\\nThe difference between the
mean is greater than 5.0 C and the temperature is below the minimum
temperature in this area.\\n\\n\\n\"location is Adelaide, time evening
and temp equal to average location = \'adelaide\', time = \"A\", temp =
21.0\"The temperature is equal to the average.\\n\"location is Adelaide,
time evening and temp above average but less than 5.0 c
differencelocation = \'adelaide\', time = \"A\", temp = 23.0\"The
temperature is greater than the average this afternoon in
Adelaide.\\n\\n\"location is Adelaide, time evening and temp above
average but greater than 5.0 difference but less than maximum
temperature location = \'adelaide\', time = \"A\", temp = 35.0\"The
temperature is greater than the average this afternoon in
Adelaide.\\n\\nThe difference from the mean temperature is more than 5.0
C\\n\\n\\n\"location is Adelaide, time evening and temp above average
but greater than 5.0 difference but more than maximum temperature
location = \'adelaide\', time = \"A\", temp = 55.0\"The temperature is
greater than the average this afternoon in Adelaide.\\n\\nThe difference
between the mean is greater than 5.0 C and the temperature is above the
maxmimum temperature in this area.\\n\\n\\n\"location is Adelaide, time
evening and temp below average but less than 5.0 c differencelocation =
\'adelaide\', time = \"A\", temp = 19.0\"The temperature is below
average this afternoon in Adelaide.\\n\\n\"location is Adelaide, time
evening and temp below average but greater than 5.0 difference but
higher than minimum temperature location = \'adelaide\', time = \"A\",
temp = 14.0\"The temperature is below average this afternoon in
Adelaide.\\n\\nThe difference from the mean temperature is above 5.0
C\\n\\n\\n\"location is Adelaide, time evening and temp below average
but greater than 5.0 difference but lower than minimum temperature
location = \'adelaide\', time = \"A\", temp = -5.0\"The temperature is
below average this afternoon in Adelaide.\\n\\nThe difference between
the mean is greater than 5.0 C and the temperature is below the minimum
temperature in this area.\\n\\n\\n\" DoneNot doneTest implementation and
execution (i)country_name_and_year.py Module name BB test design (EP)BB
test design (BVA)WB test design EP test code(implemented/run) BVA test
code(implemented/run)White-box testing (implemented
/run)Name_month()Framework used mauritius()Framework not used
spain_japan()australia_1()Framework not used australia_2()Framework used
malaysia_sri_lanka()Framework used Framework used location()Framework
usedimage() (ii) mean_temperature.py Module name BB test design (EP)BB
test design (BVA)WB test design EP test code(implemented/run) BVA test
code(implemented/run)White-box testing (implemented
/run)choice()InputFile()Detector()Framework used

Running the tests For all using modules not using frameworks:

Summary of errors: mauritius was wrongly written in the code. It was
written as mauritus Noogar seasons was assign instead of the
traditional seasons Some seasons in the mauritius() module were wrongly
assigned.

For all modules using framework: Summary of errors; The name of the
season Djilba was wrong assigned to the name of the picture causing an
error. One of the limits for malaysia_sri_lanka() module were wrongly
written After correcting the errors(both with and without framework):

Version Control This are only the commit before pushing to repositories

Commit DescriptionFirst commit Creating production code of the 2
programs Second commit Branch 1: Adding the Noogar seasons to the season
program

Branch 2: Modifying temperature program to consider max and min values
of temperature.

Branch 3: Modifying temperature program to accept input from file

Branch 4(deleted branch): Modifying temperature program to write results
to file

Branch 1, branch 2 and branch 3 are merged together to the master branch
Merge conflicts are then resolved and committed to the master branch
Third commit Trying to refactor the temperature program Adding the
picture output for the Noogar seasonFourth commit Modifying the
temperature program to accept mean values of temperature. Adding the
picture output for Malaysia/Sri Lanka in the season program. Fifth
commit Refactoring the season program only Sixth commit Designing and
implementing testing programs for the temperature and season programs
modules. Ethics and Professionalism If one day, the codes that I have
designed are used in a meteorological service station of a country and a
person working there intentionally input wrong data to the program, this
can result to faulty results, which scientist might use in turn in their
research. If their research, for instance, a device using the results
from my program is developed and it is used to predict natural
calamities, this can cause harm to people in the concerned area. The
person might be doing this in his/her personal interest, for example,
paid by the company making the devices to hide any defects.

If according to the Australian Computer Society code (ACS), the person
placed the public interest before his/her personal interest, if the
person was competent, honest and professional in his work and if he
really cared about enhancing the quality of life of those affected by
his work, he would not have done that. Discussion The codes are can be
improved in many ways such as prevent users from inputting wrong data,
making an interactive menu for the user, making the program writing the
output to a file and many other features which can be implemented.
