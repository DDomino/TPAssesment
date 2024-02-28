from database.dbcontroller import insertOneOrMoreReview, fetchReviewById, updateReview, insertSingelReview
import pandas as pd
from datetime import datetime

csv_file_dir = 'data/dataops_tp_reviews.csv'

date = datetime.now().strftime('%y-%m-%d') #date is for demo and test purposes

# Reviews for insert Demo
new_review1 = {'Reviewer Name': 'My Man',
              'Review Title':'Great Tech Assesment', 
              'Review Rating': 5,
              'Review Content': 'This assesment was a good exercise to show my skills',
              'Email Address': 'some@email.com', 'Country':'Denmark', 'Review Date':date}
new_review2 = {'Reviewer Name': 'Micky Mouse',
              'Review Title':'Dreamworks is copying me!', 
              'Review Rating': 1,
              'Review Content': 'I feel like Dreamworks are stealing my ideas',
              'Email Address': 'Dis@email.com', 'Country':'USA', 'Review Date':date}
reviews = [new_review1, new_review2]

# Reviews for Update Demo:
original_review = {'Reviewer Name': 'Original Man',
              'Review Title':'Will this Update?', 
              'Review Rating': 5,
              'Review Content': 'I made this review to see if it would update',
              'Email Address': 'og@nal.com', 'Country':'Denmark', 'Review Date':date}
updated_review = {'id': None, 'Reviewer Name': 'Original Man',
              'Review Title':'Yes it will update', 
              'Review Rating': 3,
              'Review Content': 'This review has been updated',
              'Email Address': 'up@date.com', 'Country':'USA', 'Review Date':date}

#Populates the Database from the provided CSV file
def populateFromCSV(csv_file):
    '''
    Populate review table in database.
    Parameter:
        csv_file (file): .csv file to be processed.
    Raises:
        FileNotFoundError: If file does not exsist.
    '''
    try:
        data = pd.read_csv(csv_file)
        data_dict = data.to_dict(orient='records')
        if len(data_dict) > 1:
            insertOneOrMoreReview(data_dict)
        else:
            insertSingelReview(data_dict[0])
    except FileNotFoundError as e:
        print(f'Error: {e}')
    except:
        print(f'Something went wrong on insert')

# This function inserts new reviews into the Database
def insertReview(review):
    '''
    Inserts a single review into the review table.
    Parameters:
        data (dict): A dictonary containing the review to be processed.
                     Dictornary should have the following structure:
                                         {
                                            'Reviewer Name' : string,
                                            'Review title': string,
                                            'Review raitning' : integer
                                            ...
                                         }
    ''' 
    return insertSingelReview(review)

# This function inserts multiple reviews into the Database
def insertReviews(reviews):
    '''
    Inserts one or more reviews into the review table.
    Parameters:
        data_list (List[Dict[str,Any]]): A list containing review dictonaries to be processed.
                                         Each dictornary should have the following structure:
                                        {
                                            'Reviewer Name' : string,
                                            'Review title': string,
                                            'Review raitning' : integer
                                            ...
                                         }
    '''
    insertOneOrMoreReview(reviews)

# This function fetch review from Databse
def getReviewById(id):
    ''' 
    Get single review by reviewid.
    Parameters:
        data (Integer): An integer representing the review id.
    returns:
        data: A dictonary containing the requested data.
              Dictonary has the follwing structure:
                {
                    'id' : integer,
                    'Reviewer Name' : string,
                    'Review title': string,
                    'Review raitning' : integer
                    ...
                }              

    '''
    review = fetchReviewById(id)
    if review is not None:
        return review
    else:
        print("No records found")

# Update Databse
def update(old_review, new_review):
    '''
    Updates a review with new data.
    Parameters:
        old_review (dict): The item that is being updated.
                            Dictornary should have the following structure:
                                         {
                                            'id' : integer,
                                            'Reviewer Name' : string,
                                            'Review title': string,
                                            ...
                                         }
        new_review (dict): The item with updated data.
                            Dictornary should have the following structure:
                                         {
                                            'id' : integer,
                                            'Reviewer Name' : string,
                                            'Review title': string,
                                            ...
                                         }
    '''
    # Valuates if there are differences in the two times, and if id matches to ensure update on right review id
    if set(old_review.keys()) != set(new_review.keys()) and old_review['id'] == new_review['id']:
        updateReview(old_review, new_review)
    else:
        print('No changes has been made to the review')

# Demo code to test Update function
def updateDemo():
    id = insertReview(original_review) #Inserts the original_review to test update
    new_review = updated_review
    new_review['id']= id
    old_review = getReviewById(new_review['id']) #Gets the "original_review" with new_review id as the review to update 
    update(old_review, new_review)

populateFromCSV(csv_file_dir)
insertSingelReview(new_review1)
insertOneOrMoreReview(reviews)
updateDemo()