from flask import Flask
import cohere
import datetime, re, json

app = Flask(__name__)
apiKey = "WX2BauearLsTYNGnSWY8SoucprcMDBYuT4Es1ZT0"
co = cohere.Client(apiKey)
keyWords = ["Start time:", "End time:"]

dateFormatStr = "Please schedule these events with the following format: \
    Title: text format\
    Start time: YYYY-MM-DD-HH-mm format \
    End time: YYYY-MM-DD-HH-mm format"

now = datetime.datetime.now()
nowStr = "The current date is " + now.strftime("%B %d, %Y.")

@app.route('/')
# generateCalendarDates takes a prompt and returns a list of events corresponding to the prompt
def generate_calendar_dates(prompt):
    response = co.generate(
        model='command-nightly',
        prompt=prompt + nowStr + " " + dateFormatStr,
        max_tokens=2000
    )
    events = parse_calendar_dates(response[0].text)
    return generate_JSON(events)


# parseCalendarDates parses the response from the model and generates dates
def parse_calendar_dates(response):
    print(response)
    # remove all newlines
    remove = re.sub('\n', '', response)

    # remove leading and trailing text
    leading_index = remove.index('Title:')
    remove  = remove[leading_index:]

    trailing_index = remove.rfind("End time: ") + 26
    remove = remove[:trailing_index]

    print(remove)

    # replace "Start time:" and "End time:"
    remove = remove.replace("Start time:", "|")
    remove = remove.replace("End time:", "|")

    print(remove)

    # split by title
    events = remove.split("Title:")

    # remove empty string
    events = [x for x in events if x != '']

    # split events by start time and end time
    events = [event.split("|") for event in events]

    # strip leading and trailing whitespace
    events = [s.strip() for event in events for s in event]
    
    return events


def generate_JSON(events):
    events_dict = []
    for i in range(0, len(events), 3):
        ds = {
            "title": events[i],
            "start": events[i+1],
            "end": events[i+1],
        }
        events_dict.append(ds)

    events_json = json.dumps(events_dict)
    print(events_json)
    return events_json


def filter_dates (s):
    for w in keyWords:
        if s.find(w):
            return True
    return False    


generate_calendar_dates("I like to game at night. I also have a work meeting at 5pm")