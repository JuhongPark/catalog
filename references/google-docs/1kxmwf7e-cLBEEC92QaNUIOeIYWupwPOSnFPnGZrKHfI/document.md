Full data cycle - data collection, storage, processing, and consumption.

<img src="assets/media/image2.jpg" style="width:7.5in;height:4.20833in" />

**Introduction**

Welcome to the Sensemaking Problem Set, this assignment provides a comprehensive exploration of the full data cycle, from collection to consumption, focusing on a public university course catalog. You will gain hands-on experience in data acquisition, preparation, parsing, cleaning, extraction, analysis, visualization, and the creation of a clean, formatted dataset. Through a series of steps, you will work with raw HTML data, employ various programming tools and libraries, and ultimately automate the process with a data pipeline. This problem set aims to develop your skills in analytics and visualization, preparing you for real-world data handling scenarios.

**Note: *You may work individually or in pairs for this assignment.***

**Setup**

Before you start writing code, set up your development environment. See the instructions in the following video:

https://bit.ly/40etXko

<img src="assets/media/image1.png" style="width:0.81771in;height:0.82292in" />

**Objective:**

Gain hands-on experience in data collection, storage, processing, and consumption. Gain experience in analytics and visualization by working with a public university course catalog data.

**PART I**

# 1. Data Acquisition:

**Objective:** Your first task in this problem set is to collect the raw data that will form the foundation of your analysis. Specifically, you will download all the public course catalog data in raw HTML format from a university website. This step is crucial as it involves gathering the raw, unprocessed data directly from the source.

**Tools/Resources:** You are provided with a choice of three universities from which you can extract the course catalog data. Each university has its own catalog structure and content, allowing you to select the source that you find most interesting or relevant to your skills and objectives. The universities and their respective course catalog URLs are:

Harvard: https://courses.my.harvard.edu

BU: https://www.bu.edu/academics/cas/courses

NE: https://catalog.northeastern.edu/course-descriptions

**Code Submission:** Once you have successfully downloaded the data, you will need to place your code in a file named \`01_pull.py\`. This script should automate the process of accessing the website, navigating to the relevant sections if necessary, and downloading the HTML content.

# 2. Data Preparation:

**Objective**: The second question in this problem set asks you to organize and consolidate your acquired data into a more manageable form. Specifically, you are tasked with combining multiple HTML files, each containing parts of the course catalog, into a single comprehensive document. This step is to simplify the data preparation process that follows, ensuring all relevant information is in one place.

**Tools/Resources**: For this task, you may use Python or JavaScript to concatenate the HTML text from the various files. This process involves reading the contents of each HTML file and merging them into one file, preserving the integrity and structure of the data.

**Code Submission**: Your solution for this task should be placed in a file named \`02_combine.py\`. This script must automate the combination process, ensuring that the final document includes all the data needed for the next steps of parsing, cleaning, and analysis. Make sure your code is well-documented to explain your approach, including how you handle any challenges related to file reading, data concatenation, and maintaining HTML structure integrity.

# 3. Data Parsing:

**Objective**: Your objective is to parse the consolidated course data, leveraging the structure of HTML elements to extract relevant information. This step is critical for isolating specific pieces of data from the HTML document, such as course titles, descriptions, and any other relevant details provided in the course catalog.

**Tools/Resources**: You are encouraged to utilize parsing tools and libraries such as Beautiful Soup, DOMParser, or Regular Expressions to navigate and parse the HTML content efficiently. These resources are invaluable for extracting structured data from unstructured HTML, allowing you to target specific elements within the document:

**Beautiful Soup**: A Python library designed for quick turnaround projects like yours where you need to extract information from HTML pages. \[Beautiful Soup Documentation\](https://www.crummy.com/software/BeautifulSoup/)

**DOMParser**: A web API that can be used for parsing XML or HTML source code from a string into a DOM Document. \[DOMParser Documentation\](https://developer.mozilla.org/en-US/docs/Web/API/DOMParser)

**Regular Expressions (RegEx)**: A powerful language for matching text patterns. This can be particularly useful for extracting structured data from strings. \[RegEx Resources\](https://regexr.com), \[Mozilla Developer Network RegEx Guide\](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)

**Code Submission**: Your parsed data should be compiled in a script named \`03_parse.py\`. This script should automate the extraction process, ensuring that all relevant information is captured cleanly and efficiently. Ensure your code is well-commented to explain your choice of tools and methods, as well as how you navigated the challenges of parsing HTML data.

# 4. Data Cleaning:

**Objective**: This question focuses on cleaning and preprocessing the parsed data to make it suitable for analysis. The goal is to refine the extracted information by removing or correcting any data that will break the parser.

**Tools/Resources**: You are encouraged to use Regular Expressions or the string manipulation functions provided by your programming language of choice to clean the data. This might involve tasks like trimming whitespace or removing breaking data:

\- \*\*Regular Expressions:\*\* Ideal for identifying and manipulating specific patterns in text data, such as removing HTML tags or standardizing date formats.

\- \*\*String Manipulation Functions:\*\* These functions can help with trimming whitespace, splitting strings into arrays, or concatenating pieces of data for uniformity.

**Code Submission**: Your cleaned data should be compiled in a script named \`04_clean.py\`. This script should automate the cleaning process, ensuring that the dataset is polished and standardized for the upcoming stages of extraction, analysis, and visualization. Document your process clearly, explaining how you addressed various data cleaning challenges and the rationale behind your choices.

# 5. Data Extraction:

**Objective**: This task requires you to extract specific pieces of information from your cleaned dataset, focusing on course titles. The purpose is to isolate and compile a list of course titles, which are critical for understanding the range and scope of courses offered by the university.

**Example**: A typical course title might be "1.125 Architecting and Engineering Software Systems", indicating both the course code and the course name - see below. This step involves identifying and extracting such titles from the structured data you have prepared.

**Code Submission**: Place your code in a script named \`05_extract.py\`. This script should systematically go through the cleaned data, identify course titles using the criteria and methods you've developed, and extract these titles into a structured format, such as a list or a database.

Ensure your script is robust and accurately identifies course titles, avoiding any potential pitfalls such as mistaking other headings or text for a course title. Document your methodology in the script, including how you navigate the dataset and any rules or patterns you use to recognize course titles.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&lt;a name="1.125"&gt;&lt;/a&gt;</p>
<p>&lt;p&gt;&lt;h3&gt;1.125 Architecting and Engineering Software Systems</p>
<p>&lt;br&gt;&lt;img alt="______" src="/icns/hr.gif"&gt;&lt;/h3&gt;</p>
<p>&lt;img width=16 height=16 align="bottom" alt="Graduate" title="Graduate" src="/icns/grad.gif"&gt; (&lt;img width=16 height=16 align="bottom" alt="Fall" title="Fall" src="/icns/fall.gif"&gt;)</p>
<p>&lt;br&gt;Prereq: None</p>
<p>&lt;br&gt;Units: 3-0-9</p>
<p>&lt;br&gt;&lt;b&gt;Lecture:&lt;/b&gt; &lt;i&gt;TR9-10.30&lt;/i&gt; (&lt;a href="http://whereis.mit.edu/map-jpg?mapterms=1"&gt;1-390&lt;/a&gt;)&lt;!--s--&gt;</p>
<p>&lt;br&gt;&lt;img alt="______" src="/icns/hr.gif"&gt;</p>
<p>&lt;br&gt;Software architecting and design of cloud-based software-intensive systems. Targeted at future engineering managers who must understand both the business and technical issues involved in architecting enterprise-scale systems. Student teams confront technically challenging problems. Introduces modern dev-ops concepts and cloud-computing, including cloud orchestration for machine learning. Also discusses cyber-security issues of key management and use of encrypted messaging for distributed ledgers, e.g., blockchain. Students face problem solving in an active learning lab setting, completing in-class exercises and weekly assignments leading to a group project. Some programming experience preferred. Enrollment limited.</p>
<p>&lt;br&gt;&lt;I&gt;J. Williams&lt;/I&gt;&lt;br&gt;No textbook information available</p>
<p>&lt;/p&gt;&lt;!--end--&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# 6. Word Frequency Analysis:

**Objective**: This task involves performing a word frequency count on the course titles you have extracted. The goal is to analyze the most common words used in course titles, providing insights into the prevalent themes or subjects in the university's curriculum.

**Tools/Resources**: For this analysis, you may employ a "map reduce" style approach, which is effective for processing and analyzing large datasets. This method involves mapping your data into key-value pairs (in this case, words and their frequencies) and then reducing them by aggregating these values across the dataset to get the total counts for each word.

**Code Submission**: Your analysis should be encapsulated in a script named \`06_frequency.py\`. This script should read the list of course titles, perform the word count, and then output the frequency of each word encountered. Pay special attention to preprocessing steps such as lowercasing words, removing punctuation, and excluding common stopwords (e.g., "the", "and", "in") to ensure your analysis focuses on meaningful words.

Document your approach within the script, explaining how you handled the data and any specific decisions you made to refine your word frequency analysis.

# 7. Data Visualization:

**Objective**: The objective of this task is to create visual representations of the word frequencies obtained from the course titles. Visualization helps in easily identifying the most common themes and subjects within the university's course offerings, making the data more accessible and understandable.

**Tools/Resources**: You are encouraged to use any of the following visualization libraries to create your charts or graphs:

\- \*\*Chart.js:\*\* A lightweight JavaScript library for creating simple yet flexible charts, using the HTML5 canvas element. \[Chart.js Official Website\](https://www.chartjs.org/)

\- \*\*Google Charts:\*\* A tool that offers a variety of charts to be embedded in web pages. It's easy to use and provides interactive charts. \[Google Charts Official Website\](https://developers.google.com/chart/)

\- \*\*D3.js:\*\* A JavaScript library for producing dynamic, interactive data visualizations in web browsers. It's highly customizable but requires a good understanding of JavaScript. \[D3.js Official Website\](https://d3js.org/)

**Code Submission**: Your visualizations should be implemented in a script named \`07_visualization.py\`. This script should take the word frequency data and use it to generate visualizations that clearly and effectively communicate the findings. Consider creating bar charts, word clouds, or other graphical representations that best suit the data.

Ensure your code is well-documented, explaining the choice of visualization, the library used, and any customization or configuration that enhances the clarity or aesthetic appeal of the output.

# 8. Export a Clean Formatted Dataset of the Entire University Catalog:

**Objective**: The final step in your data journey involves preparing and exporting a clean, well-formatted dataset of the entire university catalog. This dataset should represent the culmination of your work, structured in a manner that is immediately usable for analysis and visualization. It should reflect the careful cleaning, consolidation, and organization of data you've performed throughout the project.

**Tools/Resources**: Utilize your programming skills to format the data in a JSON (JavaScript Object Notation) format. This process involves structuring your data with clear JSON elements consistent data formats, and documentation that outlines the dataset's structure:

**Code Submission:** Your clean and formatted dataset should be produced by a script named \`08_export.py\`. This script should automate the process of exporting the data, ensuring that it is ready for immediate use in analysis or visualization projects. Document your file's structure, including descriptions of columns, data types, and any assumptions or decisions made during the data preparation process.

# 9. Data pipeline:

Write a program that automates the sequential execution of previously created script files, ensuring that each script runs to completion before the next begins. This program aims to streamline the generation of outputs from all your previous files, consolidating the results into one sequence. This script should be designed to programmatically call and execute each of the prior scripts in the correct order:

\- Data Acquisition (01_pull.py)

\- Data Preparation (02_combine.py)

\- Data Parsing (03_parse.py)

\- Data Cleaning (04_clean.py)

\- Data Extraction (05_extract.py)

\- Word Frequency Analysis (06_frequency.py)

\- Data Visualization (07_visualization.py)

\- Export Clean Formatted Dataset (08_export.py)

Your script should handle any dependencies between scripts, ensuring that output from one step is correctly inputted into the next. It should also include error handling to manage any issues that arise during execution, ensuring the entire pipeline can run smoothly from start to finish without manual intervention.

**Code Submission::** Place your code in 09_pipeline.py

**PART II**

# 10. Extract MIT Course Catalog 1996: 

**Objective:** Extract course data from the scanned 1996 MIT course catalog. After extracting the text, create a data model and save the processed data. This task emphasizes working with raw, scanned documents and aims to teach you how to extract information from non-digitized sources.

**Tools/Resources:** You may use any Python package or software of your choice that supports PDF processing. The catalog PDF can be found at:

https://onexi.org/catalog/pdf/index.html

**Code Submission:** Save the extracted course data in a JSON file named 10_mit_1996.json and submit your extraction script in a file named 10_extract_1996.py. Ensure that your script automates the process of extracting course names and descriptions, and includes functionality to handle any inconsistencies in the scanned document.

# 11. Extract MIT Course Catalog 2024: 

**Objective:** Extract course data from the current MIT course catalog. After extracting the text, create a data model and save the processed data.

**Tools/Resources:** Use tools such as BeautifulSoup to scrape the course information from the current MIT Course Catalog. You can find the course catalog at:

https://student.mit.edu/catalog/index.cgi

**Code Submission**: Place the extracted course data in a text file named 11_mit_2024.json and submit your extraction code in a file named 11_extract_2024.py. The script should automatically scrape and save the course catalog data into a structured format.

# 12. Course Offerings Over Time: 

**Objective:** After extracting the course data from both the 1996 and present catalogs, analyze the number of courses offered in various departments. Are there any departments that have significantly expanded or reduced their course offerings? If so, identify them and discuss possible reasons for these changes.

**Code Submission:** Place your analysis and visualizations in a script named 12_course_offerings.py. Submit the code that reads the 10_mit_1996.txt and 11_mit_2024.txt files, processes the data, and outputs insights into departmental changes over time.

# 13. Title Evolution: 

**Objective:** Conduct a word frequency analysis on course titles from 1996 and 2024 to explore shifts in academic terminology and focus areas.

**Code Submission:** Submit your analysis in a script named “13_title_evolution.py”. This script should automate the word frequency analysis, comparing the most common terms in the course titles from both years and documenting your findings.

# 14. New and Discontinued Subjects: 

**Objective:** Identify subjects that were offered in 1996 but no longer exist in 2024, as well as new subjects introduced in 2024. Explore possible reasons for these changes.

**Code Submission:** Submit a script named “14_new_and_old.py” that highlights subjects that have been discontinued or newly introduced. Document any patterns or trends you observe.

# 15. Curriculum Breadth: 

**Objective:** Compare the breadth of topics in the 1996 and 2024 catalogs to assess whether the curriculum has become more interdisciplinary or specialized.

**Code Submission:** Submit your analysis in a script named “15_curriculum_breadth.py”, detailing how you classified the courses and any trends you discovered regarding curriculum diversity.

# 16. Summary and Reflection: 

**Objective**: Summarize your findings from the previous tasks, reflecting on the most significant changes in the MIT course catalog over time. Relate these changes to broader trends in education and industry.

**Code Submission:** Submit your written summary in a file named “16_summary_reflection.txt”. If applicable, include code that automatically compiles the insights from the analysis in previous scripts.
