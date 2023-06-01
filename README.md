# Procedure

## Upload to pdisk 

1. Run ### 1_link_scrapper.py   ---------------> extrct links from webpage (links saved in links.txt) 

2. Run ### 2nd.py    --------------------------> extract video urls from the links extracted (output.txt)

3. Run ### 3_pdisk_upload.py ------------------> upload the video urls to pdisk (uploads.txt)

4. Run ### size_scanner.py --------------------> extract the size from the pdisk urls that are saved in uploads.txt (uploads.txt)

5. Run ### numbering.py -----------------------> give numbering to the urls saved in uploads.txt (uploads_num.txt)