import html
import re


# Normally i would sanitize on input from frontend or earlier in the process
def sanitize(text):
    '''
    Sanitizes a provided text for emojies, and possible XSS.
    parameters:
        text (String): The text or string to be sanitized.
    returns:
        text (String): The sanitized text or string.
    '''
    text = html.escape(re.sub(r'[^\w\s,]', '', text))
    return text #Escaped to remove possible XSS and removes emojies
    #I have chosen to remove emojies as this is for data analysis purposes.


def validateEmail(email):
    '''
    Validates if a provided email matches general Email composition.
    Parameters:
            email (String): The text to be processed
    Returns:
            boolean True: If the email fulfill general email composition
                          Must match pattern: \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b
            
            boolean False: If email does not fulfill general email composition. 
    '''
    #Regular Email expression
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pattern, email):
        return True
    else:
        print(email)
        return False

