# Pagination

## Learning Objectives
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Setup - Popular_Baby_Names.csv
use [this data file](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20251201%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20251201T091312Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=985ab5187747a0f3cbae2a5dd01c569f6e1c1f2059e67e5251a3ac40eb03f993) for your project

## Tasks
0. Write a function named index_range that takes two integer arguments page and page_size.
The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

1. Implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.

2. Implement a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:

- page_size: the length of the returned dataset page
- page: the current page number
- data: the dataset page (equivalent to return from previous task)
- next_page: number of the next page, None if no next page
- prev_page: number of the previous page, None if no previous page
- total_pages: the total number of pages in the dataset as an integer
- Make sure to reuse get_page in your implementation.

3. The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.
