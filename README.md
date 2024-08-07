<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News Article Summarizer App README</title>
</head>
<body>
    <h1>News Article Summarizer App</h1>
    <p>This project is a news article summarizer app that takes an article URL, extracts its content, and displays a summary of the news. The app uses <a href="https://python.langchain.com/en/latest/">LangChain</a> and the GROQ AI chat model.</p>
    <h2>Getting Started</h2>
    <p>Follow these instructions to set up and run the project on your local machine.</p>
    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.8 or higher</li>
        <li><a href="https://pip.pypa.io/en/stable/installation/">pip</a> package manager</li>
        <li><a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git">Git</a></li>
    </ul>
    <h3>Installation</h3>
    <p>1. Clone the repository using the following command:</p>
    <pre><code>git clone &lt;repository-url&gt;</code></pre>
    <p>Replace <code>&lt;repository-url&gt;</code> with the actual URL of the repository.</p>
    <p>2. Navigate to the project directory:</p>
    <pre><code>cd news-article-summarizer</code></pre>
    <p>3. Install the required packages using the provided requirements file:</p>
    <pre><code>pip install -r requirements.txt</code></pre>
    <h3>Running the App</h3>
    <p>Run the following command to start the Streamlit app:</p>
    <pre><code>streamlit run app.py</code></pre>
    <p>This will launch the app in your default web browser. You can then enter an article URL, adjust the temperature slider, and specify the model name to get a summary of the news article.</p>
    <h2>Project Structure</h2>
    <pre><code>
    news-article-summarizer/
    ├── app
        |──src
            |──article_retriever
            |──summarizer
        |──app.py
    ├── requirements.txt
    ├── README.md
    </code></pre>
    <h2>Usage</h2>
    <p>1. Enter the article URL in the main input field.</p>
    <p>2. Adjust the temperature slider and specify the model name in the left sidebar.</p>
    <p>3. Click the "Process" button to generate the summary of the article.</p>
    <p>The summary will be displayed on the main screen.</p>
    <h2>Contributing</h2>
    <p>We welcome contributions to improve this project. Please fork the repository and submit a pull request with your changes.</p>
    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    <h2>Acknowledgements</h2>
    <ul>
        <li><a href="https://streamlit.io/">Streamlit</a> for providing the framework to build the web app</li>
        <li><a href="https://python.langchain.com/en/latest/">LangChain</a> for the language processing library</li>
        <li><a href="https://groq.com/">GROQ AI</a> for the chat model</li>
    </ul>
</body>
</html>
