import React from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import 'react-big-calendar/lib/css/react-big-calendar.css';
import moment from 'moment';

const localizer = momentLocalizer(moment);

const events = [
  {
    title: 'Event 1',
    start: new Date(2023, 8, 20, 10, 0), // Year, Month (0-indexed), Day, Hour, Minute
    end: new Date(2023, 8, 20, 12, 0),
  },
  {
    title: 'Event 2',
    start: new Date(2023, 8, 21, 14, 0),
    end: new Date(2023, 8, 21, 16, 0),
  },
];

function App() {
  return (
    <div className="App">
      <h1>Calendar App</h1>
      <div style={{ height: '500px' }}>
        <Calendar localizer={localizer} events={events} startAccessor="start" endAccessor="end" />
      </div>
    </div>
  );
}

export default App;
