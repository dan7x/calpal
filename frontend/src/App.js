import React from 'react';
import { useState } from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar';
import 'react-big-calendar/lib/css/react-big-calendar.css';
import PromptForm from './components/Prompt';
import moment from 'moment';
import {
  StyleSheet,
  Button,
  View,
  SafeAreaView,
  Text,
  Alert,
} from 'react-native';

const localizer = momentLocalizer(moment);

function App() {
    const [events, setEvents] = useState([
        // {
        //   title: 'Event 1',
        //   start: new Date(2023, 8, 20, 10, 0), // Year, Month (0-indexed), Day, Hour, Minute
        //   end: new Date(2023, 8, 20, 12, 0),
        // },
        // {
        //   title: 'gtbtgtgb 2',
        //   start: new Date(2023, 8, 21, 14, 0),
        //   end: new Date(2023, 8, 21, 16, 0),
        // },
    ]);
    
    return (
        <div className="App">
            <div style={{ padding: '20px' }}>
                <h1>Calendar App</h1>
                <PromptForm setEvents={setEvents} />
                <div style={{ height: '500px' }}>
                    <Calendar localizer={localizer} events={events} startAccessor="start" endAccessor="end" />
                </div>
            </div>
        </div>
    );
}

export default App;
