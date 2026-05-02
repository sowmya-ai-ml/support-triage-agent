import pandas as pd

df = pd.read_csv("support_tickets.csv")

def process_ticket(issue, subject, company):

    text = str(subject) + " " + str(issue)

    text = text.lower()

    status = "replied"

    request_type = "product_issue"

    product_area = "general"

    response = "We are reviewing your request."

    if "fraud" in text or "unauthorized" in text or "charged" in text:

        status = "escalated"

        response = "This issue is escalated to support team."

    if "error" in text or "not working" in text:

        request_type = "bug"

    elif "feature" in text or "add" in text:

        request_type = "feature_request"

    if company == "Visa":

        product_area = "payments"

    elif company == "HackerRank":

        product_area = "assessments"

    elif company == "Claude":

        product_area = "ai"

    justification = "Rule-based classification"

    return [status, product_area, response, justification, request_type]

results = []

for _, row in df.iterrows():

    results.append(process_ticket(row['issue'], row['subject'], row['company']))

✅ THIS IS THE MAIN FIX

output = pd.DataFrame(results, columns=[

    "status", "product_area", "response", "justification", "request_type"

])

output.to_csv("output.csv", index=False)

print("✅ Done! Correct output.csv created")