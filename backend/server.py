from flask import Flask, request
from flask_cors import CORS, cross_origin
from db3 import add_event_to_table, get_events_from_table
import cohere
import datetime, re, json

app = Flask(__name__)
apiKey = "WX2BauearLsTYNGnSWY8SoucprcMDBYuT4Es1ZT0"
co = cohere.Client(apiKey)
keyWords = ["Start time:", "End time:"]

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


dateFormatStr = "Schedule these events in an array. Elements should have the following JSON format: \
    title: text format\
    start: YYYY-MM-DD HH:mm format \
    end: YYYY-MM-DD HH:mm format."

now = datetime.datetime.now()
nowStr = "The current date is " + now.strftime("%A %B %d, %Y.")

# generateCalendarDates takes a prompt and returns a list of events corresponding to the prompt
def generate_calendar_dates(prompt):
    current_events = json.dumps(get_events_from_table())
    avoid_conflicts = "I already have the following events: " + current_events + " \
        Please avoid scheduling conflicts."
    response = co.generate(
        model='command-nightly',
        prompt=prompt + nowStr + " " + dateFormatStr + "\n" + avoid_conflicts,
        max_tokens=2000
    )
    return parse_calendar_dates(response[0].text)


# parseCalendarDates parses the response from the model and generates dates
def parse_calendar_dates(response):
    # print(response)

    # remove leading and trailing text
    leading_index = response.index('[')
    json_string  = response[leading_index:]

    trailing_index = json_string.rfind("]") + 1
    json_string = json_string[:trailing_index]

    print(json_string)

    json_object = json.loads(json_string)

    for ob in json_object:
        add_event_to_table(ob["title"], ob["start"], ob["end"])

    return json_object
  

@app.route('/new', methods=['POST'])
@cross_origin()
def endpoint_post():
    # print("im here")
    prompt = request.json['prompt']
    n_prompt = request.json['negative']
    # breakpoint()

    # print(prompt)
    # print(n_prompt)

    res = generate_calendar_dates(prompt + " " + n_prompt)

    return res


@app.route('/get', methods=['GET'])
@cross_origin()
def endpoint_get():
    events = get_events_from_table()
    print(events)
    return json.dumps(events)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
