# googlebooks_search.py
# Purpose: Use the Google Books API to return info about books, based on the
# user request.
# Authors: Tanya and Isabel
# Date: 04/21/16

"""
Credits:
The Google Book API application was written by Eni Mustafaraj for the Fall 2015 
version of CS 111.
Lyn Turbak took the application and converted into a task for PS 10.
"""

import requests
import json
import jinja2, webbrowser, os
import googlebookstemplate
reload(googlebookstemplate)
from googlebookstemplate import gBooksTemplate

###############################################################################
# Provided Helper Functions

def writeJSONforExploration(jsonData, filename):
    """Write results as JSON to explore them."""
    with open(filename, 'w') as fw:
        json.dump(jsonData, fw, sort_keys= True, indent=2)
        

def fillHTMLTemplate(templateString, paramsDict):
    """Invokes the jinja2 methods to fill in the slots in the template."""
    templateObject = jinja2.Template(templateString)
    htmlContent = templateObject.render(paramsDict)
    return htmlContent


def writeHTMLFile(htmlText, filename):
    """Helper file to write the HTML file from the given text. It uses the
       codecs module, which can deal correctly with UTF8 encoding.
    """
    import codecs
    with codecs.open(filename, 'w', 'utf8') as htmlFile:
        htmlFile.write(htmlText)


def openBrowserForHTMLFile(HTMLfilename):
    '''Open a browser to display the HTML in the file named HTMLfilename'''
    URL = 'file:' + os.getcwd() + '/' + HTMLfilename
    print '\n\n\Opening web page', URL
    webbrowser.open(URL)


###############################################################################
# Flesh out the following functions

def requestBooks(titleSearchString):
    """Prepares the request for the Web API and checks the returned response.
       If the response status code is 200, prints 'We got a response from the 
       API!' and returns the content part of the response as a string. 
       Otherwise, prints the status code, reason, and text of the response, 
       returning None. 
    """
    baseURL = "https://www.googleapis.com/books/v1/volumes"
    
    httpResp = requests.get(baseURL, 
                            params={'q': 'intitle:' + titleSearchString, 'maxResults': 40, 'langRestrict': 'en'})
                                         
    if httpResp.status_code == 200:
        print "We got a response from the API!"
        return httpResp.content
    else:
        print "Request not fulfilled"
        print httpResp.status_code, httpResp.reason, httpResp.text
 

def extractBookInfo(stringResponseFromAPI):
    """Takes the string response from the API, converts it to a Python value,
       extracts the info needed for the HTML template and returns it in a 
       dictionary with keys 'totalCount' (the total number of items in the 
       Google Books database), 'displayCount' (the number of books to be 
       displayed on the HTML page), and 'booksList' (a list of dictionaries, 
       one for each book result that has a cover image). Assumes that the user 
       has already explored the data and knows what fields to extract, e.g., by 
       using writeJSONforExploration.
    """
    queryResult = json.loads(stringResponseFromAPI)
    outerDict = queryResult.get('items', [])
    total = queryResult['totalItems'] 

    booksList = []
    hugeDict = {}
    
    for books in outerDict: 
        miniDict = {} 
       
        # Adds image, if available 
        if 'imageLinks' in books['volumeInfo']:
            imgUrl = books['volumeInfo']['imageLinks']['thumbnail'] 
            miniDict['imgURL'] = imgUrl
            miniDict['title'] = books['volumeInfo']['title']
            miniDict['previewLink'] = books['volumeInfo']['previewLink']

            # Adds author, if available 
            if 'authors' in books["volumeInfo"]: 
                miniDict['author'] = ",".join(books['volumeInfo']['authors'])               
            else:
                miniDict['author'] = "Unknown"
            
            # Adds date of publication, if available 
            if 'publishedDate' in books["volumeInfo"]: 
                miniDict['publishedDate'] = books['volumeInfo']['publishedDate'].split("-")[0]
            else: 
                miniDict['publishedDate'] = "Missing"
            
            # Adds 700 words of description, if available
            if 'description' in books["volumeInfo"] and len(books['volumeInfo']['description']) <= 700 and len(books['volumeInfo']['description']) > 0: 
                miniDict['description'] = books['volumeInfo']['description']
                if len(books['volumeInfo']['description']) > 700: 
                    miniDict['description'] = books['volumeInfo']['description'][:700] + "..."
            else: 
                miniDict['description'] = "No description available."
            
            # Adds page count, if available
            if 'pageCount' in books["volumeInfo"]: 
                miniDict['pageCount'] = books['volumeInfo']['pageCount']
            else: 
                miniDict['pageCount'] =  "Not available."
                
            booksList.append(miniDict)
          
    hugeDict = {"totalCount": total, "booksList": booksList,'displayCount': len(booksList)}     
    return hugeDict
    
    
def sortByPublishedDate(listOfBookDicts):
    """Given a list of dictionaries with book information, returns a new list 
       with the same elements sorted in reverse chronological order by 
       publication year. All books with missing publication years should
       appear at the end of the sorted list. Two books with the same 
       publication year info should have the same relative order in the 
       output list that they have in the input list. 
   """
    booksList = []
    missingBooksList = []
    
    for books in listOfBookDicts:
        if books['publishedDate'] != "Missing":    
            booksList.append(books)
        else: 
            missingBooksList.append(books)
    
    results = sorted(booksList, key=lambda k: k['publishedDate'], reverse=True) 
    results.extend(missingBooksList) 
    return results     


def main():
    """Prompts the user for a search term (possibly containing multiple words
       separated by spaces), and then looks up this search term in the 
       Google Books web API. If the response status code is not 200, does
       nothing. Otherwise does the following:
     
           1. Writes a file named book4<search term>.json that contains the
              formatted JSON for the response, where <search term> is replaced
              by the actual search term, without spaces. E.g. for the search
              term 'joy luck', writes the file book4joyluck.json. Use the
              helper function writeJSONforExploration for this purpose. 

           2. Extracts relevant information from the response and uses
              this to fill the template gBooksTemplate to create the 
              HTML file named book4<search term>.html that is structured
              as specified in the PS10 problem description. E.g. for the search
              term 'joy luck', generates the file book4joyluck.html. 
              Use the helper functions fillHTMLTemplate and 
              writeHTMLFile in this step. 

           3. Opens a browser on the file generated in step 2. 
              Use the helper function openBrowserForHTMLFile in this step.
    """
    # get parameters from the user
    searchTerm = raw_input('Enter your search term/phrase: ')

    # Test:
    # searchTerm = 'summer'

    # get API data from Google using user-given parameter (searchTerm)
    stringResponseFromAPI = requestBooks(searchTerm)

    # if API works (returns 200)
    if stringResponseFromAPI:

        # generates the .json file required by the pset, names it according to instructions (eg: "book4summer.json" for searchTerm == "summer")
        jsonResponse = json.loads(stringResponseFromAPI)
        writeJSONforExploration(jsonResponse, 'book4' + "".join(searchTerm.split()) + '.json')

        # tunnels thru stringResponseFromAPI to return hugeDict (relevant info to build HTML page later)
        bookDicts = extractBookInfo(stringResponseFromAPI)
    

        # parameters to fill holes in HTML template
        paramsForTemplate = {'query1': searchTerm,
                                 'totalCount': bookDicts['totalCount'],
                                 'displayCount': bookDicts['displayCount'],
                                 'booksList': sortByPublishedDate(bookDicts['booksList'])}
        
        # actually fill the holes
        htmlText = fillHTMLTemplate(gBooksTemplate, paramsForTemplate)
        
        # generates the .html file required by the pset, names it according to instructions (eg: "book4summer.html" for searchTerm == "summer"), and pulls it up in the browser
        fileName = 'book4'+ "".join(searchTerm.split()) + ".html"
        
        writeHTMLFile(htmlText, fileName)
        openBrowserForHTMLFile(fileName)


#Uncomment the invocation of the main function below
if __name__ == '__main__':
    main()
