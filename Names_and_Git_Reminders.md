# Conventions:

## Introduction:

The following is just the tenative plan (2/1/24 at approx: 9:45 AM EST):

The general naming structure should be: {Type}_{SubTyp, optional}_{Specific_Name}_{Iteration/Edition, optional}_{Capitalized_Initials}.{Datatype}, ideally saved to whatever pertinent folders.

Ex. Data_Housing_California_I_SG.csv

Arguably, the first item, data, is superfluous. However, I'd rather every file be explicit inherently per their names so no/little confusion arises in the event of a mistake. 

Similarily, I'd think it'd be worthwhile to specify the subtype, out of anticipation that we might have multiple instances where the relevant {Specific_Name} is applicable to both - such as having both income and housing data on California.

Iteration number is somewhat broad, referring to entirely different datasets, potentially of different features, of the same type (and subtype) or even if a change was made to the original data. Ie, I'm inclined to be quite conservative with any changes and list multiple editions of the same dataframe, such as adding another 1k entries to a previously existing one, and call it a different name.

Capitalized Initials should be clear, and assumed that any questions could be asked to said person about the document.

And, datatype is datatype.

## Git Reminders:

As at least BW is new to Git, I'd figure below here would be worthwhile to right any relevant Git commands, tricks, etc. to ensure we're less likely to mess anything up. Please feel free to add and comment here!

To add comments, I'd recommend startng a new line, indenting, and starting the comment with a # (like in Python), to make the different code used in Terminal cleaerly distint from comments.

### General

git add .
    #Adds everything
git add (specific_file.type)

git comit -m "Descriptive_Message_of_Whatever_is_being_Done"

git push

git reset
    #Removes any added file
git reset (specifc_file.type)

git status

### Branching

### Github.com