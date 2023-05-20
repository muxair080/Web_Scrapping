from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()
    # print(content) 

    soup = BeautifulSoup(content, 'lxml')
    # print html code in best formate
    # print(soup.prettify)

    # search for specific tag it return the first eleement
    # tags = soup.find('h5')
    # print(tags)
    
    # search for specific tag and return all that tags in code
    # courses_tags = soup.find_all('h5')
    # for course_tags in courses_tags:
    #     print(course_tags)

    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        # print specific elemetntns
        # print(course.a)
        # return text of specific element.
        course_name = course.h5.text
        # course_price = course.a.text
        # print just amount  
        course_price = course.a.text.split(' ')[-1]
        print(course_name)
        print(course_price)
