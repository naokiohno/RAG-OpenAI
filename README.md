# RAG-OpenAI
A proof of concept application of RAG using an OpenAI GPT model and langchain.

It is specifically designed to process user specified pdf files, and use them as input for the model. The model then uses the content of the files
as context, summarising the documents or answering specific questions about them. This is a very popular application of LLM, and enables organisations
to consolidate a large number of unstructured data sources, such as pdf files, Power Point presentations, and Word documents. This enables non-technical
stakeholders to derive insights without bespoke data analysis or extensive research.

The model was tested as an HR screening application that helps recruiters filter candidates based on the criteria of choice (tech stack, leadership experience, etc).
The input data in this application is a list of CVs.

# Scripts

* The script called 'single_pdf_app.py' takes only a single pdf file as input. This is an adaptation the following medium article:
https://medium.com/@infoalex1/creating-a-rag-system-with-openai-to-analyze-existing-pdf-documents-e52044f05f9c

* In the script 'multip_pdf_app' I improved upon the method of the Medium article by implementing a vectorised approach enabling users to add multiple PDF files.
This significantly improves the tool for HR screening, as multiple candidates can now be compared across a variety of criteria based on user input.

# Examples

**Query:** Who in the context is best qualified for a Java programmer role?
**Answer:** Based on the provided context, Sebastian Mercer is best qualified for a Java programmer role. He has experience as a Senior Software Engineer and Software Development Team Lead, and his skills section lists Java as one of his programming languages.

**Query:** Who in the context has the most data science experience?
**Answer** Based on the provided context, the individual with the most data science experience is Naoki Ohno. His work experience includes roles as a Data Scientist at Royal Ballet and Opera, an Interim Data Scientist, and a Junior Digital Analyst.

**Query** Who in the context has the most management experience?
**Answer** Sebastian Mercer has the most management experience in the provided context. He has worked as a Senior Software Engineer where he led a team of five developers in the implementation of a real-time chat application. He also held the position of a Software Development Team Lead.
