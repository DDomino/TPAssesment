# TPAssesment

This is my code for my Tech Assesment at Trustpilot.

The assignement is detailed in the docuements folder.

For this assignement i went with Python for my language and Postgres as a database.
Additional python packages neede for this project is the "psycopg2" package and "Pandas"

```
python -m pip install psycopg2
python -m pip install pandas
```
# Files and Functions
The code has two files:
database/dbcontroller.py and Main.py

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

