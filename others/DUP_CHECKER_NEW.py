import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def compare_and_update_files():
    # Read the contents of dup_checked.txt
    with open('dup_checked.txt', 'r') as dup_checked_file:
        dup_checked_links = set(line.strip() for line in dup_checked_file)

    # Read the contents of all_links.txt
    with open('all_links.txt', 'r') as all_links_file:
        all_links = set(line.strip() for line in all_links_file)

    # Remove links from dup_checked_links that are present in all_links
    initial_count = len(dup_checked_links)
    dup_checked_links -= all_links
    removed_count = initial_count - len(dup_checked_links)

    # Append unique links to all_links.txt
    added_count = 0
    with open('all_links.txt', 'a') as all_links_file:
        for link in dup_checked_links:
            all_links_file.write(link + '\n')
            added_count += 1

    # Update dup_checked.txt with the modified set of links
    with open('dup_checked.txt', 'w') as dup_checked_file:
        for link in dup_checked_links:
            dup_checked_file.write(link + '\n')

    # Logging
    logging.info(f'Removed {removed_count} duplicate link(s) from dup_checked.txt')
    logging.info(f'Added {added_count} unique link(s) to all_links.txt')

# Call the function to compare and update the files
compare_and_update_files()
