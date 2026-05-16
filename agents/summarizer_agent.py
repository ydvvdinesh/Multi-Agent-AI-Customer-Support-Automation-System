import re

def summarize_ticket(ticket_text):

    # Remove extra spaces
    ticket_text = re.sub(r"\s+", " ", ticket_text)

    # Split into sentences
    sentences = ticket_text.split(".")

    # Keep first 2 meaningful sentences
    summary = " ".join(sentences[:2])

    return summary.strip()


if __name__ == "__main__":

    sample_ticket = """
    Customer says the software installation
    keeps failing at 75 percent on Windows 11.
    Antivirus conflict detected during setup.
    Installation stops unexpectedly.
    """

    result = summarize_ticket(sample_ticket)

    print("\nTicket Summary:\n")

    print(result)