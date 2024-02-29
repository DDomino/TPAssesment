# TPAssesment

This is my code for my Tech Assesment at Trustpilot.

The assignement is detailed in the docuements folder.

For this assignement i went with Python for my language and Postgres as a database.
Additional python packages needed for this project is "psycopg2" and "Pandas"

```
python -m pip install psycopg2
python -m pip install pandas
```
# Files and Functions
The code consist of three files:
database/dbcontroller.py, Main.py and utility.py 

## dbcontroller.py
This file contains the connector to the database aswell as the requested CRUD operation
At delivery the following CRUD operations are available:

```
insertReview(review, cursor)
```
This function accepts a review as a dictonary, and a cursor from a connection. 
This function takes a cursor to make the insertReview function usable in both single insert and multiple insert
and avoid opening additional cursors for each object in a multiple insert

```
insertOneOrMoreReviews(reviews) 
```
Takes a list of review dictonaries and inserts them to the database. I called this "oneOrMore" as it also handles lists of one dictonaries.
Inserts all or none, if error occures during insert of dictonaries no commit will happen and the system makes a rollback.

```
insertSingleReview(review)
```
Same as above, just with a single review dictornary

```
updateReview(new_review, old_review)
```
This function updates an already exsisting review. All or nothing, if an error occures the system makes a rollback.

```
fetchReviewById(id)
```
Fetch a requested review from the database based on id and returns it as dictonary

NOTE: I have decided to go with pythons dictonary as it gives better readability of the code eg. review['Reviewer Name'] instead of review[1], especially when it comes to the data objects for the queries. Another option would be to make a Review entity with constructor, setter and getters and use functions like "review.reviewerName"

Additional Extensions would be:
- Delete review function
- Delete multiple function
- Update multiple function
- Get on additional parameters
- Archive architecture 
- UpdateDate field

## Main.py
This file function as a facade for the dbcontroller.py. The file has the required data objects and functions to run and test against the dbcontroller.py 

## utility.py
This file contains more general functions. 
```
validateEmail(email)
sanitize(text)
```
Each are used to clean the data: 
- validateEmail ensures that emails confine to a specific composition.
- sanitize ensures no XSS in the content or title, aswell as removes Emojies.

NOTE: I have chosen to remove emojies as this assignment is for a position as Data Engineer. I therefore make the asumption that 
the data is to be used for Data analysis purposes. If emojies would be important for analysis i recommend an emoji count field in the database.
If an application fetches and display the reviews, I would keep the emojies in the content


# How would I run in a production environment?
I would make an application and run it with either flask or django, that i would host on Azure Cloud platform.
Postgres database i would aswell host on Azure Cloud platform, probably in a container.
Addtionally i would make a CI/CD pipline connected between Azure and Github. 

