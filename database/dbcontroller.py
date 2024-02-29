import psycopg2
import pandas as pd


dbname = ''
user = ''
password = ''
host = ''



def getDBConnection():
    '''
    Creates a connection to database using psycopg2.
    Returns:
        psycopg2.extentions.connection: A connection to database.
    Raises:
        psycopg2.Error: If error occurs with connection 
    '''
    try:
        connection = psycopg2.connect( 
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        print("Connected to the database!")
        return connection

    except psycopg2.Error as e:
        print("Unable to connect to the database.")
        print(e)

def insertReview(review, cursor):
    '''
    Inserts a review into the Database
    Parameters:
        review (dict): A dictonary containing the review to be processed.
                     Dictornary should have the following structure:
                                         {
                                            'Reviewer Name' : string,
                                            'Review title': string,
                                            'Review raitning' : integer
                                            ...
                                         }
        cursor psycopg2.extentions.connection.cursor: Cursor provided for Query execution
    Returns:
        reviewId (Integer): Returns the reviewId for the inserted review
    Raises:
        psycopg2.Error: If error on execute
    '''
    try:
        insert_data = (review['Reviewer Name'], review['Review Title'],
                           review['Review Rating'],review['Review Content'],
                           review['Email Address'],review['Country'],review['Review Date'], )
        query = '''
                INSERT INTO dataopstpreviewtable (
                    reviewername, 
                    reviewtitle, 
                    reviewrating, 
                    reviewcontent, 
                    emailaddress, 
                    country, 
                    reviewdate)
                    VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING id
                '''
        cursor.execute(query, insert_data)
    except psycopg2.Error as e:
        print(e)
    finally:
        return cursor.fetchone()[0]  #fetches insertedIds for Updatedemopurposes

def insertSingelReview(review):
    '''
    Inserts a review into the Database
    Parameters:
        review (dict): A dictonary containing the review to be processed.
                     Dictornary should have the following structure:
                                         {
                                            'Reviewer Name' : string,
                                            'Review title': string,
                                            'Review raitning' : integer
                                            ...
                                         }
    Returns:
        reviewId (Integer): Returns the reviewId for the inserted review.
    Raises:
        psycopg2.Error: If error in insertReview(review, cursor).
    '''
    if review is not None:
        conn = getDBConnection()
        cursor = conn.cursor()
        try:
            inserted_Id = insertReview(review, cursor)
            conn.commit() #psql has an implicit .beghin() for transactions.
        except psycopg2.Error as e:
            print('Error! Performing Rollback')
            print(e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
            if inserted_Id is not None:
                return inserted_Id #Returns inserted_Id for updatedemo purposes 
            else:
                print('Review Not Inserted')
    else:
        print("Review is None") 

def insertOneOrMoreReview(reviews):
    '''
    Inserts a list of reviews into the Database
    Parameters:
        reviews (List[Dict[str,Any]]): A list containing review dictonaries to be processed.
                     Dictornary should have the following structure:
                                         {
                                            'Reviewer Name' : string,
                                            'Review title': string,
                                            'Review raitning' : integer
                                            ...
                                         }
    Returns:
        review_Ids (List): Returns a list of reviewIds for the inserted review
    Raises:
        psycopg2.Error: If error in insertReview(review, cursor)
    '''
    print(len(reviews))
    inserted_Ids = []
    try:
        conn = getDBConnection()
        cursor = conn.cursor()
        for review in reviews:
            review_Id = insertReview(review, cursor)
            inserted_Ids.append(review_Id)
        conn.commit() #psql has an implicit .beghin() for transactions.
    except psycopg2.Error as e:
        print('Error! Performing Rollback')
        print(e)
        conn.rollback()
    finally:
        cursor.close
        conn.close()
        if len(inserted_Ids) > 0:
            return inserted_Ids # Returns inserted_Ids for updateDemo purposes

def updateReview(old_review, new_review):
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
    Raises:
        psycopg2.Error: If error on execute
    '''
    conn = getDBConnection()
    cursor = conn.cursor()
    if cursor is not None:
        try:
            update_data = (new_review['Reviewer Name'],new_review['Review Title'],
                           new_review['Review Rating'],new_review['Review Content'],
                           new_review['Email Address'],new_review['Country'],new_review['Review Date'], old_review['id'])
            query = '''
            UPDATE dataopstpreviewtable SET 
                reviewername = %s, 
                reviewtitle = %s, 
                reviewrating = %s, 
                reviewcontent = %s,
                emailaddress = %s, 
                country = %s, 
                reviewdate= %s where id = %s
            '''
            cursor.execute(query,update_data)
            conn.commit() #psql has an implicit .beghin() for transactions.
        except psycopg2.Error as e:
            print('Error! Performing Rollback')
            print(e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

def fetchReviewById(id):
    ''' 
    Get single review by reviewid.
    Parameters:
        id (Integer): An integer representing the review id.
    Returns:
        Result: A dictonary containing the requested data.
              Dictonary has the follwing structure:
                {
                    'id' : integer,
                    'Reviewer Name' : string,
                    'Review title': string,
                    'Review raitning' : integer
                    ...
                }              

    '''
    result = None
    try:
        conn = getDBConnection()
        cursor = conn.cursor()
        get_data = (id,)
        query = 'SELECT * FROM dataopstpreviewtable where id = %s'
        cursor.execute(query, get_data)
        row = cursor.fetchone()
        if row is not None:
            columns = [desc[0] for desc in cursor.description]
            result = pd.DataFrame([row], columns=columns)
            result = result.to_dict(orient='records')[0]
    except psycopg2.Error as e:
        print(f'Error: {e}')
    finally:
        cursor.close()
        conn.close()
    return result