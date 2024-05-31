import re                                      # import regular expression (it will search the pattern)

def extract_yt_term(command):
    '''Using re extracts search terms from user's command & return it 
    if not found returns None'''
    
    # Define an regular expression pattern to capture the song name (dynamic terms/constant terms/searched tearms)
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command parameter
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None 
    return match.group(1) if match else None

# 6. Make Helper Function to remove unwanted words from query

def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string

# 7. Example of Helper Function

#Example usage
# input_string = "make a phone call to pappa"
# words_to_remove = ['make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', '']

# result = remove_words(input_string, words_to_remove)
# print(result)

