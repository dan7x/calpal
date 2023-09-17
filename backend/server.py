from flask import Flask, request
from db3 import add_event_to_table
import cohere
import datetime, re, json

app = Flask(__name__)
apiKey = "WX2BauearLsTYNGnSWY8SoucprcMDBYuT4Es1ZT0"
co = cohere.Client(apiKey)
keyWords = ["Start time:", "End time:"]

# dateFormatStr = "Please schedule these events with the following format: \
#     Title: text format\
#     Start time: YYYY-MM-DD-HH-mm format \
#     End time: YYYY-MM-DD-HH-mm format"

dateFormatStr = "Please schedule these events in an array. Each element should have the following JSON format: \
    title: text format\
    start: YYYY-MM-DD HH:mm format \
    end: YYYY-MM-DD HH:mm format."

now = datetime.datetime.now()
nowStr = "The current date is " + now.strftime("%B %d, %Y.")

# generateCalendarDates takes a prompt and returns a list of events corresponding to the prompt
def generate_calendar_dates(prompt):
    response = co.generate(
        model='command-nightly',
        prompt=prompt + nowStr + " " + dateFormatStr,
        max_tokens=2000
    )
    return parse_calendar_dates(response[0].text)


# parseCalendarDates parses the response from the model and generates dates
def parse_calendar_dates(response):
    print(response)
    # remove all newlines
    # remove = re.sub('\n', '', response)

    # remove leading and trailing text
    leading_index = response.index('[')
    json_string  = response[leading_index:]

    trailing_index = json_string.rfind("]") + 1
    json_string = json_string[:trailing_index]

    # replace "Start time:" and "End time:"
    # remove = remove.replace("Start time:", "|")
    # remove = remove.replace("End time:", "|")

    # split by title
    # events = remove.split("Title:")

    # remove empty string
    # events = [x for x in events if x != '']

    # split events by start time and end time
    # events = [event.split("|") for event in events]

    # strip leading and trailing whitespace
    # events = [s.strip() for event in events for s in event]

    print(json_string)

    json_object = json.loads(json_string)

    for ob in json_object:
        add_event_to_table(ob["title"], ob["start"], ob["end"])

    return json_object
  

@app.route('/new', methods=['POST'])
def endpoint_post():
    prompt = request.form.get('prompt')
    n_prompt = request.form.get('negative')

    res = generate_calendar_dates(prompt + " " + n_prompt)

    return res

@app.route('/get', methods=['GET'])
def endpoint_get():
    res = generate_calendar_dates(prompt + " " + n_prompt)

    return res


if __name__ == "__main__":
    app.run(debug=True, port=5001)
