# -------------------------------------------------
# To install R for Jupyter notebooks, do NOT do this:
#   conda install -c r r-irkernel
# Instead you need to install R separately from CRAN website:
# https://cloud.r-project.org/
# (CRAN = “Comprehensive R Archive Network”)
#
# Once installed, check its location:
#   which R         # /usr/local/bin/R
#   which Rscript   # /usr/local/bin/Rscript
#   R --version
#   Rscript --version
#
# Then start R console by typing "R" command, 
# and then run two commands in an R console:
#  
# install.packages('IRkernel')
# IRkernel::installspec(user = FALSE)
#
# First command asks where to place the library
#    default user location is: 
#       ‘~/Library/R/x86_64/4.1/library’
# Then it asks to select the mirror site.
#    I selected #78
# 
# This is described here:
#   https://irkernel.github.io/installation/
#
# Then download RStudio desktop app from here:
#   https://www.rstudio.com/products/rstudio/download/
# Then run the installer.
# On Mac it will offer to copy the app into Applications folder
#
# Start the R.app
# try some simple commands:
#
#    > print("Hello")
#    [1] "Hello"
#    > a=1
#    > b=2
#    > c=a+b
#    > c
#    [1] 3
#    > 
#
# To quit R you can either use the RStudio > Quit pull-down menu
# or press ⌘ + Q (OS X) or ctrl + Q (PC).
#
# -------------------------------------------------
# For Linux you can download and install R-server.
# First install R:
#     https://cran.r-project.org/bin/linux/ubuntu/fullREADME.html
# Basically to install R you need to run one command:
#     sudo apt-get install r-base
# Then you will have:
#   /usr/bin/R
#   /usr/bin/Rscript
# Then you can get on R-prompt.
# And can run R scripts from unix prompt:  
#    Rscript test.R
# To install Rstudio server, follow instructions on this page:
#    https://www.rstudio.com/products/rstudio/download-server/debian-ubuntu/
# For example, for Ubuntu 18:
#
#    sudo apt-get install gdebi-core
#    wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-2022.07.1-554-amd64.deb
#    sudo gdebi rstudio-server-2022.07.1-554-amd64.deb
# 
# Once you install it, it will be always running.
# You can check it by using this command:
#    ps auxww | grep rstudio
# You can access it via browser on port 8787
# See also:
#    https://support.rstudio.com/hc/en-us/articles/200552306-Getting-Started
#
# Example of how to set a writable directory for your libraries:
#    mkdir /data/Rlibs
# The add to .bashrc
# 
# if [ -n $R_LIBS ]; then
#   export R_LIBS=/data/Rlibs:$R_LIBS
# else
#   export R_LIBS=/data/Rlibs
# fi
# 
# So now to install a package, use the following syntax (from R):
#   install.packages('packagename',"/data/Rlibs","http://streaming.stat.iastate.edu/CRAN")
# 
# -------------------------------------------------
# The tutorial below is mostly from this excellent video
# by Derek Banas:
#  - https://www.youtube.com/watch?v=s3FozVfd7q4
#  - http://www.newthinktank.com/2017/11/r-programming-tutorial/
# -------------------------------------------------
# Comment multiple lines in RStudio by selecting
# CMD + SHIFT + C (Mac) / CTRL + SHIFT + C Windows
# -------------------------------------------------
# getwd() returns the working directory
# setwd("working/directory") sets the working directory
# -------------------------------------------------
# You can highlight code and execute just it in the console
# -------------------------------------------------
# R-code is saved int ofiles with extention ".r"
# Usually R is used interactively from R-studio
# by opening the file, selecting the code
# (with the mous or ctrl-A)
# and pressing Ctrl-Enter
# 
# Alternatively you can run it from terminal using "Rscript"
#
#    which Rscript
#    /usr/local/bin/Rscript 
#    
#    #!/bin/bash
#    
#    Rscript myscript1.r
#    Rscript myscript2.r
#    # other bash commands
#
# -------------------------------------------------
# ----- FUN STARTING EXAMPLE -----
 
# ----- SCATTERPLOTS -----
# Use a scatterplot to see if batting average is directly
# connected to runs produced
# Load player data
mlbPlayers = read.table(file=file.choose(),
                        header=T, sep=" ",
                        na.strings="`",
                        stringsAsFactors=F)
 
# Grab just RBIs and Avg for each player
# playerData is known as a data frame (Table of Data)
# We get the stats we want by passing that list in a vector
playerData = mlbPlayers[,c("RBI","AVG")]
 
# Create the file
png(file="player_rbi_avg.png")
 
# Create the plot
plot(x=playerData$RBI, y=playerData$AVG,
     xlab="RBI", ylab="AVG", main="RBIs and Average")
 
# Create the file
dev.off()
# -------------------------------------------------
# ----- ASSIGNMENT -----
# You can assign a value using = or <-
myNum = 5
myNum
 
# ----- VARIABLES -----
# Variable names start with a letter and can contain
# numbers, underscores and dots
 
# Most languages use data types to define how much
# space to set asside in memory
# Variables in R are assigned R Objects
 
# Types are dynamic which means a variable names data
# type changes based on the data assigned to it
 
# Here are the Vector types
# numeric
print(class(4))
 
# integer
print(class(4L))
 
# logical (TRUE, FALSE, T, F)
print(class(TRUE))
 
# complex
print(class(1 + 4i))
 
# character
print(class("Sample"))
 
# raw when converted into raw bytes
print(class(charToRaw("Sample")))
 
# -------------------------------------------------
# You can check an objects class with 
# is.integer(), is.numeric(), is.matrix(), is.data.frame(),
# is.logical(), is.vector(), is.character()
 
# You can convert to different classes with
# as.integer(), as.numeric(),...
 
# ----- ARITHMETIC OPERATORS -----
sprintf("4 + 5 = %d", 4 + 5)
sprintf("4 - 5 = %d", 4 - 5)
sprintf("4 * 5 = %d", 4 * 5)
sprintf("4 / 5 = %1.3f", 4 / 5)
 
# Modulus or remainder of division
sprintf("5 %% 4 = %d", 5 %% 4)
 
# Value raised to the exponent of the next
sprintf("4^2 = %d", 4^2)
 
# ----- VECTORS -----
# Vectors store multiple values
# Create a vector
numbers = c(3, 2, 0, 1, 8)
numbers
 
# Get value by index
numbers[1]
 
# Get the number of items
length(numbers)

# Get the last value
numbers[length(numbers)]
 
# Get everything but an index
numbers[-1]
 
# Get the 1st 2 values
numbers[c(1,2)]
 
# Get the 2nd and 3rd
numbers[2:3]
 
# Replace a value
numbers[5] = 1
numbers
 
# Replace the 4th and 5th with 2
numbers[c(4,5)] = 2
numbers
 
# sort values (decreasing can be TRUE or FALSE)
sort(numbers, decreasing=TRUE)
 
# Generate a sequence from 1 to 10
oneToTen = 1:10
oneToTen
 
# Sequence from 3 to 27 adding 3 each time
add3 = seq(from=3, to=27, by=3)
add3
 
# Create 10 evens from 2
evens = seq(from=2, by=2, length.out=10)
evens
 
# Find out if a value is in vector
sprintf("4 in evens %s", 4 %in% evens)
 
# rep() repeats a value/s x, a number of times and
# each defines how many times to repeat each item
rep(x=2, times=5, each=2)
 
rep(x=c(1,2,3), times=2, each=2)
 
# ----- RELATIONAL OPERATORS -----
iAmTrue = TRUE
iAmFalse = FALSE
 
sprintf("4 == 5 : %s", 4 == 5)
sprintf("4 != 5 : %s", 4 != 5)
sprintf("4 > 5 : %s", 4 > 5)
sprintf("4 < 5 : %s", 4 < 5)
sprintf("4 >= 5 : %s", 4 >= 5)
sprintf("4 <= 5 : %s", 4 <= 5)
 
# Relational operator vector tricks
oneTo20 = c(1:20)
 
# Create vector of Ts and Fs depending on condition
isEven = oneTo20 %% 2 == 0
isEven
 
# Create array of evens
justEvens = oneTo20[oneTo20 %% 2 == 0]
justEvens
# -------------------------------------------------
# ----- LOGICAL OPERATORS -----
cat("TRUE && FALSE = ", T && F, "\n")
cat("TRUE || FALSE = ", T || F, "\n")
cat("!TRUE = ", !T, "\n")
# -------------------------------------------------
# ----- DECISION MAKING -----
age = 18
 
# if, else and else if works like other languages
if(age >= 18) {
  print("Drive and Vote")
} else if (age >= 16){
  print("Drive")
} else {
  print("Wait")
}
# -------------------------------------------------
# ----- SWITCH -----
# Used when you have a limited set of possible values
grade = "Z"
 
switch(grade,
       "A" = print("Great"),
       "B" = print("Good"),
       "C" = print("Ok"),
       "D" = print("Bad"),
       "F" = print("Terrible"),
       print("No Such Grade"))
# -------------------------------------------------
# ----- STRINGS -----
str1 = "This is a string"
 
# String length
nchar(string1)
 
# You can compare strings where later letters are considered
# greater than
sprintf("Dog > Egg : %s", "Dog" > "Egg")
sprintf("Dog == Egg : %s", "Dog" == "Egg")
 
# Combine strings and define sperator if any
str2 = paste("Owl", "Bear", sep="")
str2
 
# Remove bear from the string
substr(x=str2, start=4, stop=7)
 
# Substitute one string with another
sub(pattern="Owl", replacement="Hawk", x=str2)
 
# Substitute all matches
gsub(pattern="Egg", replacement="Chicken", x="Egg Egg")
 
# Split string into vector
strVect = strsplit("A dog ran fast", " ")
 
strVect
 
# -------------------------------------------------
# ----- FACTORS ------
# Factors are used when you have a limited number of values
# that are strings or integers
 
# Create a factor vector
direction = c("Up", "Down", "Left", "Right", "Left", "Up")
factorDir = factor(direction)
 
# Check if it's a Factor
is.factor(factorDir)
 
# A Factor object contains levels which store all possible
# values
levels(x=factorDir)
 
# You can define your levels and their orders
dow = c("Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday")
 
wDays = c("Tuesday", "Thursday", "Monday")
 
wdFact = factor(x=wDays, levels=dow, ordered=T)
 
wdFact
 
# -------------------------------------------------
# ----- DATA FRAMES -----
# A Data Frame is a table which contains any type 
# of data and an equal amount of data in each column
 
# Each row is called a record and each column a varaible
 
# Create customer data frame
custData = data.frame(name=c("Tom", "Sally", "Sue"),
                      age=c(43, 28, 35), 
                      stringsAsFactors=F)
 
custData
 
# Get data in row 1 column 1
custData[1,1]
 
# Get all data in 1st row
custData[1,1:2]
 
# Get all ages
custData[1:3, 2]
 
# Get dimensions
dim(custData)
 
# Add another record
recordMark = data.frame(name="Mark", age=33)
custData = rbind(custData, recordMark)
custData
 
# Add a column representing debt
debt = c(0, 25.50, 36, 48.19)
custData = cbind(custData, debt)
custData
 
# Check if money is owed
owesMoney = custData[custData$debt > 0,]
owesMoney
 
# ----- LOOPING -----
# Repeat until a condition is met
num = 1
repeat{
  print(num)
  num = num + 1
  if(num > 5){
    
    # Jumps out of loop
    break
  }
}
 
# Repeat while condition is true
while(num > 0){
  num = num - 1
  
  # next skips the rest of the loop and jumps
  # back to the top
  if(num %% 2 == 0){
    next
  }
  print(num)
}
 
# For can be used to cycle through a vector
# or do the same thing a specific number of times
oneTo5 = 1:5
for (i in oneTo5){
  print(i)
}
 
# -------------------------------------------------
# ----- MATRICES -----
# A Matrix stores values in rows and columns
 
# Create a Matrix with a single column
matrix1 = matrix(data=c(1,2,3,4))
matrix1
 
# Create a matrix with defined rows and columns
matrix2 = matrix(data=c(1,2,3,4), nrow=2, ncol=2)
matrix2
 
# You can also fill by row (You can use T or TRUE)
matrix3 = matrix(data=c(1,2,3,4), nrow=2, ncol=2, byrow=T)
matrix3
 
# Get a Matrix dimension
dim(matrix3)
 
# A value at row, column
matrix3[1,2]
 
# Get a whole row
matrix3[1,]
 
# Get a whole column
matrix3[,2]
 
# Combine vectors to make a Matrix
matrix4 = rbind(1:3, 4:6, 7:9)
matrix4
 
# Get 2nd and 3rd row
matrix4[2:3,]
 
# Get 2nd and 3rd row by ommitting the 1st
matrix4[-1,]
 
# Change the first value
matrix4[1,1] = 0
matrix4
 
# Change the 1st row
matrix4[1,] = c(10,11,12)
matrix4
 
# -------------------------------------------------
# ----- MULTI-DIMENSIONAL ARRAYS -----
# You can also create Matrices in layers
 
# Create a MDA with 2 rows, columns and layers
array1 = array(data=1:8, dim=c(2,2,2))
array1
 
# Get a value
array1[1,2,2]
 
# Experiment grabbing values like we did with the Matrix
# Everything is the same
 
# -------------------------------------------------
# ----- FUNCTIONS -----
# A function is R is an object that performs operations
# on passed attributes and then returns results
# or simply control back
 
getSum = function(num1, num2){
  return(num1 + num2)
}
 
sprintf("5 + 6 = %d", getSum(5,6))
 
# If there is no return the last expression is returned
# You can define default attribute values
getDifference = function(num1=1, num2=1){
  num1 - num2
}
 
sprintf("5 - 6 = %d", getDifference(5,6))
 
# Return multiple values in a list
makeList = function(theString){
  return (strsplit(theString, " "))
}
 
makeList("Random Words")
 
# Handling missing arguments
missFunc = function(x){
  if(missing(x)){
    return("Missing Argument")
  } else {
    return(x)
  }
}
 
missFunc()
 
# Excepting variable number of arguments with ellipses
getSumMore = function(...){
  numList = list(...)
  sum = 0
  for(i in numList){
    sum = sum + i
  }
  sum
}
 
getSumMore(1,2,3,4)
 
# Disposable / Anonymous Functions are great for 
# quick operations like doubling everything in a list
numList = 1:10
dblList = (function(x) x * 2)(numList)
dblList
 
# Closures are functions created by functions
# Create a function that finds x to a user defined
# power
power = function(exp){
  function(x){
    x ^ exp
  }
}
 
cubed = power(3)
cubed(2)
cubed(1:5)
 
# You can store functions in lists
addFunc = list(
  add2 = function(x) x + 2,
  add3 = function(x) x + 3
)
 
addFunc$add2(5)
 
# -------------------------------------------------
# ----- EXCEPTION HANDLING -----
# Used to gracefully handle errors
# I handle a division with string error
 
divide = function(num1, num2){
  tryCatch(
    num1 / num2,
    error = function(e) {
      if(is.character(num1) || is.character(num2)){
        print("Can't Divide with Strings")
      }
  })
}
 
divide(10,"5")
 
# -------------------------------------------------
# ----- READING WRITING FILES -----
# Create a text file with headers fname lname sex
# and the data in a txt file Use `for missing values
# Save in the same directory as your R file
 
# Supply the file to read, whether the 1st line is 
# headers, what seperates the data, what is being used
# for missing data and false because you don't want to
# convert string vectors to factors
 
# myPeople is a data frame
myPeople = read.table(file=file.choose(),
                      header=T, sep=" ",
                      na.strings="`",
                      stringsAsFactors=F)
myPeople
 
# Add another person
donnaRecord = data.frame(fname="Donna",
                         lname="Heyward",
                         sex="female")
myPeople = rbind(myPeople, donnaRecord)
 
# Update a record
myPeople[7,2] = "Smith"
 
# Update the file by supplying the data.frame,
# the file to write, seperator, na, whether to
# quote strings, whether to include row numbers
write.table(x=myPeople, file=file.choose(),
            sep=" ", na="`",
            quote=F, row.names=F)
 
# Get 1st 3 records
head(myPeople, 3)
 
# Get remaining records
tail(myPeople)
 
# -------------------------------------------------
# ----- BASIC PLOTTING -----
# R provides great plotting tools
 
# Plotting x y coordinates from a matrix
# 1st 5 are x and 2nd 5 are y
xy1 = matrix(data=c(1,2,3,4,5,
                    6,7,8,9,10), nrow=5, ncol=2)
plot(xy1)
 
# Draw a line
x2 = c(1,2,3,4,5)
y2 = c(1,2,3,4,5)
plot(x2, y2, type="l")
 
# Points and lines
plot(x2, y2, type="b")
 
# Points and lines with no space around points,
# labels, a blue line (Find more with colors())
plot(x2, y2, type="o", 
     main="My Plot", xlab="x axis", ylab="y axis",
     col="steelblue")
 
# pch (1-25) defines different points
# lty (1-6) defines different lines
# xlim defines the max and min x plotting region
# ylim defines the max and min y plotting region
plot(x2, y2, type="b", pch=2, lty=2,
     xlim=c(-8,8), ylim=c(-8,8))
 
# Multiple plots
plot(x2, y2, type="b")
 
# Adds straight lines at 2 and 4 coordinates
abline(h=c(2,4), col="red",lty=2)
 
# Draw a 2 segmented lines with starting and ending x
# and y points
segments(x0=c(2,4), y0=c(2,2), x1=c(2,4), y1=c(4,4),
         col="red",lty=2)
 
# Draw an arrow
arrows(x0=1.5, y0=4.55, x1=2.7, y1=3.3, col="blue")
 
# Print Text
text(x=1.25, y=4.75, labels="Center")
 
# Load a built in data.frame
plot(faithful)
 
# Highlight eruptions with a waiting time greater
# then 4
eruptions4 = with(faithful, faithful[eruptions > 4,])
 
# Draw specific points
points(eruptions4, col="red", pch=4)
 
 
# -------------------------------------------------
# ----- MATH FUNCTIONS -----
sqrt(x=100)
 
# Get the power you raise the base to get x
log(x=4, base=2)
 
# Euler's number 2.718 to the power of x
exp(x=2)
 
# Sum all vector values
sum(c(1,2,3))
 
# Find the mean (average)
randD1 = c(1,5,6,7,10,16)
mean(randD1)
 
# The median (Middle Number or avg of middle 2)
median(randD1)
 
# Minimum value
min(randD1)
 
# Maximum value
max(randD1)
 
# Min and max
range(randD1)
 
# Rounding
ceiling(4.5)
floor(4.5)
 
# Cumulatives
cumsum(c(1,2,3))
cumprod(c(1,2,3))
cummax(c(7:9, 4:6, 1:3))
cummin(c(4:6, 1:3, 7:9))
 
# Generating Random samples
# Flipping a coin 10 times and weigh the probability
# of the next flip based on the previous
sample(0:1,10,replace=T)
 
sample(1:20,10,replace=T)
 
# ----- PIE CHARTS -----
# List percentages
foodPref = c(15, 35, 10, 25, 15)
 
# Labels associated with percentages
foodLabels = c("Spaghetti", "Pizza", "Mac n' Cheese",
           "Chicken Nuggets", "Tacos")
 
# Where to save the image
png(file="child_food_pref.png")
 
# Colors used for each option
colors = rainbow(length(foodPref))
 
# Create the chart
pie(foodPref, foodLabels, main="Food Prefs",
    col=colors)
 
# Print legend and cex shrinks the size
legend("topright", c("Spaghetti", "Pizza", "Mac n' Cheese",
                     "Chicken", "Tacos"), cex=0.8,
       fill=colors)
 
# Save the chart
dev.off()
 
# 3D Pie Chart
# Download package in console install.packages("plotrix")
# Get the library
library(plotrix)
 
# Name the chart file
png(file="3d_child_food_pref.png")
 
# Create the chart
pie3D(foodPref, labels=foodLabels, explode=0.1,
      start=pi/2, main="Food Prefs", labelcex=0.8)
 
# Save the chart
dev.off()
 
# ----- BAR CHARTS -----
# Define the bar chart file
png(file="food_pref_bar_chart.png")
 
# Plot the chart
barplot(foodPref, names.arg=foodLabels, xlab="Votes",
        ylab="Food Options", col=colors, 
        main="Food Prefs")
 
# Save File
dev.off()
 
# ----- REGRESSION ANALYSIS -----
# Used to study a relationship between 2 separate 
# pieces of data (What is the relation between batting
# average and RBIS)
 
# Create relationship model between AVG and RBIs
relation = lm(playerData$RBI~playerData$AVG)
 
# Create file 
png(file="RBI_AVG_Regression.png")
 
# Plot the chart
plot(playerData$AVG, playerData$RBI, 
     main="AVG & RBI Regression", 
     abline(lm(playerData$RBI~playerData$AVG)),
     xlab="AVG", ylab="RBIs")
 
# Save chart
dev.off()
 
# ----- MULTIPLE REGRESSION -----
# Used to study the impact on one variable from numerous 
# others
# Estimate RBIs based on other player stats
playerData2 = mlbPlayers[,c("RBI","AVG","HR","OBP",
                            "SLG","OPS")]
 
# Create the relationship model
relation2 = lm(playerData2$RBI ~ playerData2$AVG + 
                 playerData2$HR + playerData2$OBP +
                 playerData2$SLG + playerData2$OPS)
 
sprintf("Intercept : %f1.4", coef(relation2)[1])
 
# How stats effect RBIs
sprintf("AVG : %f1.4", coef(relation2)[2])
sprintf("HR : %f1.4", coef(relation2)[3])
sprintf("OBP : %f1.4", coef(relation2)[4])
sprintf("SLG : %f1.4", coef(relation2)[5])
sprintf("OPS : %f1.4", coef(relation2)[6])
 
# Calculate expected RBIs based on stats
# Evan Longoria
# RBIs   AVG   HR   OBP   SLG   OPS
# 86     .261  20  .313  .424  .737
RBIGuess = -5.05 + (372.96 * .261) + (2.56 * 20) +
  (-5.41 * .313) + (-167.37 * .424)
RBIGuess