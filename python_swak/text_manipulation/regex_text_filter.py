import re


def filter_text(text):
    # The \b at the start and end of the pattern ensures that the match must be a whole word, not part of a larger string.
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    mentions = re.findall(r'@\w+', text)
    hashtags = re.findall(r'#\w+', text)
    links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    html_tags = re.findall(r'<[^>]+>', text)

    return {
        'emails': emails,
        'mentions': mentions,
        'hashtags': hashtags,
        'links': links,
        'html_tags': html_tags,
    }


if __name__ == "__main__":
    example_text = """
    For more information, contact <a href="support@example.com">support@example.com</a>.
    Follow us on Twitter: @example_user. Visit our website: https://www.example.com
    Join the conversation with #PythonProgramming.
    Connect with John Doe at john.doe@example.com.
    I love using Python for <b>natural language processing</b> and sentiment analysis!
    """

    filtered_info = filter_text(example_text)

    print("Emails:", filtered_info['emails'])
    print("Mentions:", filtered_info['mentions'])
    print("Hashtags:", filtered_info['hashtags'])
    print("Links:", filtered_info['links'])
    print("HTML Tags:", filtered_info['html_tags'])
