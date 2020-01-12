# todo if posting to public repo in github, remove apiKey and cx
# Google search url
baseURL = "https://www.googleapis.com/customsearch/v1?key="

# Custom search parameters
apiKey = "AIzaSyB4Qd8LnZQGMHvPbCqorO1_bMCquju2S8M"
cx = "&cx=000885305012449804475:msgywvbfrhl"

'''Instruction to create apiKey and cx
1. Create google account or use existing one
2. Create google custom search - https://cse.google.com/cse/all
3. Properties:
   - Region: Russia
   - Restrict results to region - ON
   - Sites to search: *.sledcom.ru
4. cx = Search engine ID
5. Go to https://developers.google.com/custom-search/v1/overview
   Click Get a Key
   Select previously created search
   Copy key and use it as apiKey
'''
